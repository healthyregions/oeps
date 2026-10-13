"""Unit tests for constrained interactive download SQL planning."""

import pandas as pd
import pytest

import io
import zipfile

from oeps.clients.interactive_download import (
    MAX_ROWS,
    DownloadPlan,
    InteractiveDownloadError,
    build_download_plan,
    csv_text_as_zip,
    row_limit_error_message,
    run_download_query,
)
from oeps.config import REGISTRY_DIR
from oeps.handlers import Registry


@pytest.fixture(scope="module")
def registry():
    return Registry.create_from_directory(REGISTRY_DIR)


def test_plan_single_variable_single_table(registry, monkeypatch):
    monkeypatch.setenv("BQ_PROJECT_ID", "oeps-test")
    plan = build_download_plan(
        years=["2023"],
        scales=["County"],
        variables=["MedInc"],
        registry=registry,
        project_id="oeps-test",
    )
    assert plan.years == ["2023"]
    assert plan.scales == ["County"]
    assert plan.variable_names == ["MedInc"]
    assert "county-2023" in plan.tables
    assert "MedInc" in plan.tables["county-2023"]
    assert "HEROP_ID" in plan.sql
    assert "`oeps-test.tabular.county-2023`" in plan.sql
    assert "MedInc" in plan.sql
    # No free-form injection surface: only allowlisted identifiers
    assert ";" not in plan.sql


def test_rejects_multiple_years(registry, monkeypatch):
    monkeypatch.setenv("BQ_PROJECT_ID", "oeps-test")
    with pytest.raises(InteractiveDownloadError, match="exactly one year"):
        build_download_plan(
            years=["2022", "2023"],
            scales=["County"],
            variables=["MedInc"],
            registry=registry,
            project_id="oeps-test",
        )


def test_rejects_unknown_variable(registry, monkeypatch):
    monkeypatch.setenv("BQ_PROJECT_ID", "oeps-test")
    with pytest.raises(InteractiveDownloadError, match="Unknown variable"):
        build_download_plan(
            years=["2023"],
            scales=["County"],
            variables=["NotARealVar"],
            registry=registry,
            project_id="oeps-test",
        )


def test_theme_skips_unavailable_variables(registry, monkeypatch):
    monkeypatch.setenv("BQ_PROJECT_ID", "oeps-test")
    plan = build_download_plan(
        years=["2023"],
        scales=["County"],
        themes=["Economic"],
        registry=registry,
        project_id="oeps-test",
    )
    assert "MedInc" in plan.variable_names
    assert "EssnWrkE" not in plan.variable_names
    assert any("Skipped" in n for n in plan.notes)


def test_explicit_missing_variable_still_errors(registry, monkeypatch):
    monkeypatch.setenv("BQ_PROJECT_ID", "oeps-test")
    with pytest.raises(InteractiveDownloadError, match="No 2023 County data"):
        build_download_plan(
            years=["2023"],
            scales=["County"],
            variables=["EssnWrkE"],
            registry=registry,
            project_id="oeps-test",
        )


class _FakeResult:
    def __init__(self, frame):
        self._frame = frame

    def to_dataframe(self):
        return self._frame


class _FakeJob:
    def __init__(self, frame):
        self._frame = frame

    def result(self, timeout=None):
        return _FakeResult(self._frame)


class _FakeClient:
    def __init__(self, frame):
        self._frame = frame

    def query(self, sql, job_config=None):
        return _FakeJob(self._frame)


def _plan():
    return DownloadPlan(
        years=["2020"],
        scales=["Tract"],
        variable_names=["MedInc"],
        tables={"tract-2020": ["MedInc"]},
        sql="SELECT 1",
    )


def test_over_row_limit_returns_error_and_no_csv(monkeypatch):
    frame = pd.DataFrame({"HEROP_ID": range(MAX_ROWS + 1), "MedInc": 1})
    monkeypatch.setattr(
        "oeps.clients.interactive_download.get_client",
        lambda: _FakeClient(frame),
    )
    with pytest.raises(InteractiveDownloadError, match="no file was created") as exc:
        run_download_query(_plan())
    assert exc.value.status_code == 413
    message = exc.value.message.lower()
    assert "select a state" in message
    assert "per-scale zip" in message


def test_under_row_limit_still_returns_csv(monkeypatch):
    frame = pd.DataFrame({"HEROP_ID": ["14017001", "14017002"], "MedInc": [1, 2]})
    monkeypatch.setattr(
        "oeps.clients.interactive_download.get_client",
        lambda: _FakeClient(frame),
    )
    csv_text, row_count = run_download_query(_plan())
    assert row_count == 2
    assert csv_text.startswith("HEROP_ID,MedInc")
    assert "14017001" in csv_text


def test_csv_is_wrapped_in_one_zip_entry():
    csv_text = "HEROP_ID,MedInc\n05017001,42000\n"
    payload = csv_text_as_zip(csv_text, "oeps-county-2023-subset.csv")
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        assert archive.namelist() == ["oeps-county-2023-subset.csv"]
        assert archive.read("oeps-county-2023-subset.csv").decode("utf-8") == csv_text


def test_download_route_returns_zip_and_keeps_row_count(monkeypatch):
    from oeps import create_app

    monkeypatch.setenv("BQ_PROJECT_ID", "oeps-test")
    monkeypatch.setattr(
        "oeps.api.interactive_download.run_download_query",
        lambda plan: ("HEROP_ID,MedInc\n05017001,42000\n", 1),
    )
    client = create_app().test_client()
    response = client.post(
        "/api/interactive-download",
        json={"years": ["2023"], "scales": ["County"], "variables": ["MedInc"]},
    )
    assert response.status_code == 200
    assert response.mimetype == "application/zip"
    assert response.headers["X-OEPS-Row-Count"] == "1"
    assert 'filename="oeps-county-2023-subset.zip"' in response.headers["Content-Disposition"]
    with zipfile.ZipFile(io.BytesIO(response.data)) as archive:
        assert archive.namelist() == ["oeps-county-2023-subset.csv"]
        assert b"05017001,42000" in archive.read("oeps-county-2023-subset.csv")


def test_dry_run_stays_json(monkeypatch):
    from oeps import create_app

    monkeypatch.setenv("BQ_PROJECT_ID", "oeps-test")
    client = create_app().test_client()
    response = client.post(
        "/api/interactive-download",
        json={
            "years": ["2023"],
            "scales": ["County"],
            "variables": ["MedInc"],
            "dry_run": True,
        },
    )
    assert response.status_code == 200
    assert response.is_json
    assert "sql" in response.get_json()


def test_over_row_limit_route_returns_json_error(monkeypatch):
    from oeps import create_app

    monkeypatch.setenv("BQ_PROJECT_ID", "oeps-test")

    def _too_big(plan):
        raise InteractiveDownloadError(row_limit_error_message(), status_code=413)

    monkeypatch.setattr("oeps.api.interactive_download.run_download_query", _too_big)
    client = create_app().test_client()
    response = client.post(
        "/api/interactive-download",
        json={"years": ["2020"], "scales": ["Tract"], "variables": ["MedInc"]},
    )
    assert response.status_code == 413
    assert response.is_json
    assert "no file was created" in response.get_json()["error"]
