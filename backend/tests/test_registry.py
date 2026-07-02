import json
from pathlib import Path

import pytest

from oeps.registry_validation import RegistryValidationError


def test_validate(runner):
    result = runner.invoke(
        args=[
            "validate-registry",
            "--registry-path",
            runner.app.config["TEST_REGISTRY_DIR"],
        ]
    )
    assert result.exit_code == 0


def test_validate_fails_on_invalid_metadata(runner, tmp_path):
    registry_path = Path(runner.app.config["TEST_REGISTRY_DIR"])
    bad_var = registry_path / "variables" / "BadVar.json"
    bad_var.write_text(
        json.dumps(
            {
                "name": "BadVar",
                "title": "Bad variable",
                "type": "number",
                "example": "1",
                "description": "test",
                "longitudinal": False,
                "analysis": False,
                "metadata": "Not_A_Real_Metadata",
                "table_sources": ["t-latest"],
            }
        ),
        encoding="utf-8",
    )
    try:
        result = runner.invoke(
            args=[
                "validate-registry",
                "--registry-path",
                str(registry_path),
            ]
        )
        assert result.exit_code != 0
        assert "registry validation failed" in result.output.lower()
    finally:
        bad_var.unlink(missing_ok=True)


def test_validate_geography_rules_point_tmdr(runner, tmp_path):
    registry_path = Path(runner.app.config["TEST_REGISTRY_DIR"])
    met = registry_path / "variables" / "MetTmDr.json"
    original = met.read_text(encoding="utf-8")
    data = json.loads(original)
    data["table_sources"] = list(data["table_sources"]) + ["c-2010"]
    met.write_text(json.dumps(data, indent=2), encoding="utf-8")
    try:
        result = runner.invoke(
            args=[
                "validate-registry",
                "--registry-path",
                str(registry_path),
                "--check-geography-rules",
            ]
        )
        assert result.exit_code != 0
    finally:
        met.write_text(original, encoding="utf-8")


def test_validate_fails_on_missing_csv_column(runner):
    registry_path = Path(runner.app.config["TEST_REGISTRY_DIR"])
    bad_var = registry_path / "variables" / "BadColVar.json"
    bad_var.write_text(
        json.dumps(
            {
                "name": "BadColVar",
                "title": "Bad column variable",
                "type": "number",
                "example": "1",
                "description": "test",
                "longitudinal": False,
                "analysis": False,
                "metadata": "Demographic_Characteristics",
                "table_sources": ["t-latest"],
            }
        ),
        encoding="utf-8",
    )
    try:
        result = runner.invoke(
            args=[
                "validate-registry",
                "--registry-path",
                str(registry_path),
                "--check-columns",
            ]
        )
        assert result.exit_code != 0
        assert "badcolvar" in result.output.lower()
    finally:
        bad_var.unlink(missing_ok=True)


def test_registry_validation_error_is_raised():
    from oeps.handlers import Registry

    registry = Registry.create_from_directory(
        Path(__file__).parent / "test_registry"
    )
    registry.variables["TotPop"].metadata = "missing"
    with pytest.raises(RegistryValidationError):
        registry.validate()
