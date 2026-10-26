"""Unit tests for constrained interactive download SQL planning."""

import pandas as pd
import pytest

import io
import zipfile

from google.api_core.exceptions import NotFound

from oeps.clients.interactive_download import (
    MAX_ROWS,
    DownloadPlan,
    InteractiveDownloadError,
    _build_join_sql,
    build_download_plan,
    code_from_herop_id,
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


def test_missing_table_returns_clear_error_without_raw_details(monkeypatch):
    class _MissingTableClient:
        def query(self, sql, job_config=None):
            raise NotFound(
                "404 Not found: Table oeps-391119:tabular.county-2023 was not found "
                "in location US\nJob ID: 2e1eb33d-ce05-4c8a-84f0-6cef50c1e7e7"
            )

    monkeypatch.setattr(
        "oeps.clients.interactive_download.get_client",
        lambda: _MissingTableClient(),
    )
    plan = DownloadPlan(
        years=["2023"],
        scales=["County"],
        variable_names=["MedInc"],
        tables={"county-2023": ["MedInc"]},
        sql="SELECT 1",
    )
    with pytest.raises(InteractiveDownloadError, match="no file was created") as exc:
        run_download_query(plan)
    assert exc.value.status_code == 404
    message = exc.value.message
    assert "2023 County" in message
    assert "Data Access" in message
    assert "oeps-391119" not in message
    assert "2e1eb33d" not in message
    assert "location US" not in message


def test_under_row_limit_still_returns_csv(monkeypatch):
    frame = pd.DataFrame({"HEROP_ID": ["14017001", "14017002"], "MedInc": [1, 2]})
    monkeypatch.setattr(
        "oeps.clients.interactive_download.get_client",
        lambda: _FakeClient(frame),
    )
    csv_text, row_count = run_download_query(_plan())
    assert row_count == 2
    assert csv_text.startswith("HEROP_ID,FIPS,MedInc")
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


def test_county_sql_adds_fips_beside_herop_id():
    sql = _build_join_sql("oeps-test", {"county-2023": ["MedInc"]})
    assert sql.startswith("SELECT `HEROP_ID`, SUBSTR(`HEROP_ID`, 6) AS `FIPS`, `MedInc`")
    assert "ZCTA5" not in sql


def test_zcta_sql_adds_zip_column_instead_of_fips():
    sql = _build_join_sql("oeps-test", {"zcta-2023": ["MedInc"]})
    assert "SUBSTR(`HEROP_ID`, 6) AS `ZCTA5`" in sql
    assert "`FIPS`" not in sql


def test_state_and_tract_sql_add_fips():
    state_sql = _build_join_sql("oeps-test", {"state-2023": ["Pop"]})
    tract_sql = _build_join_sql("oeps-test", {"tract-2020": ["MedInc"]})
    assert "AS `FIPS`" in state_sql
    assert "AS `FIPS`" in tract_sql


def test_joined_tables_add_one_geography_code():
    sql = _build_join_sql(
        "oeps-test",
        {"county-2023": ["MedInc"], "county-2018": ["Pop"]},
    )
    assert sql.count("AS `FIPS`") == 1
    assert "SUBSTR(COALESCE(t0.HEROP_ID, t1.HEROP_ID), 6) AS `FIPS`" in sql
    assert "JOIN" in sql


def test_code_from_herop_id_keeps_leading_zero():
    assert code_from_herop_id("050US01001") == "01001"
    assert code_from_herop_id("040US17") == "17"
    assert code_from_herop_id("140US17019005900") == "17019005900"
    assert code_from_herop_id("860US00601") == "00601"


def test_csv_writes_fips_with_leading_zero(monkeypatch):
    frame = pd.DataFrame({"HEROP_ID": ["050US01001"], "MedInc": [34898]})
    monkeypatch.setattr(
        "oeps.clients.interactive_download.get_client",
        lambda: _FakeClient(frame),
    )
    plan = DownloadPlan(
        years=["2023"],
        scales=["County"],
        variable_names=["MedInc"],
        tables={"county-2023": ["MedInc"]},
        sql="SELECT 1",
    )
    csv_text, row_count = run_download_query(plan)
    assert row_count == 1
    assert csv_text.splitlines()[0] == "HEROP_ID,FIPS,MedInc"
    assert "050US01001,01001,34898" in csv_text


def test_csv_writes_zcta_zip(monkeypatch):
    frame = pd.DataFrame({"HEROP_ID": ["860US00601"], "MedInc": [1]})
    monkeypatch.setattr(
        "oeps.clients.interactive_download.get_client",
        lambda: _FakeClient(frame),
    )
    plan = DownloadPlan(
        years=["2023"],
        scales=["ZCTA"],
        variable_names=["MedInc"],
        tables={"zcta-2023": ["MedInc"]},
        sql="SELECT 1",
    )
    csv_text, _row_count = run_download_query(plan)
    assert csv_text.splitlines()[0] == "HEROP_ID,ZCTA5,MedInc"
    assert "860US00601,00601,1" in csv_text
