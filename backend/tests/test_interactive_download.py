"""Unit tests for constrained interactive download SQL planning."""

import os

import pytest

from oeps.clients.interactive_download import (
    InteractiveDownloadError,
    build_download_plan,
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
