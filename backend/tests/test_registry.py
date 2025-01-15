from pathlib import Path

from oeps.clients.registry import Registry
from oeps.commands import registry_grp
from oeps.utils import load_json


def test_validate(runner):
    result = runner.invoke(
        registry_grp,
        ["validate", "--registry-path", runner.app.config["TEST_REGISTRY_DIR"]],
    )
    assert result.exit_code == 0


def test_init(runner):
    """Test initialization of the Registry."""

    registry = Registry(runner.app.config["TEST_REGISTRY_DIR"])
    src = load_json(Path(runner.app.config["TEST_REGISTRY_DIR"], "variables.json"))
    for k, v in src.items():
        reg_var = registry.variables[k]
        ## delete "years" which are added during registry init process and not in source JSON
        del reg_var["years"]
        assert reg_var == v

    table_sources = list(
        Path(runner.app.config["TEST_REGISTRY_DIR"], "table_sources").glob("*.json")
    )
    assert len(registry.table_sources) == len(table_sources)
    for ts_path in table_sources:
        ## delete "schema" which is created during load and not in source JSON
        del registry.table_sources[ts_path.stem]["schema"]
        assert registry.table_sources[ts_path.stem] == load_json(ts_path)

    geodata_sources = list(
        Path(runner.app.config["TEST_REGISTRY_DIR"], "geodata_sources").glob("*.json")
    )
    assert len(registry.geodata_sources) == len(geodata_sources)
    for gs_path in geodata_sources:
        ## "csv_abbrev "is a deriv"  key/value that is added on load, and isn't present in the source JSON
        del registry.geodata_sources[gs_path.stem]["csv_abbrev"]
        assert registry.geodata_sources[gs_path.stem] == load_json(gs_path)


def test_create_oeps_dicts(runner):
    result = runner.invoke(
        registry_grp,
        [
            "create-data-dictionaries",
            "--destination",
            runner.app.config["TEST_OUTPUT_DIR"],
            "--registry-path",
            runner.app.config["TEST_REGISTRY_DIR"],
        ],
    )
    assert result.exit_code == 0

    xlsx_output = list(Path(runner.app.config["TEST_OUTPUT_DIR"]).glob("*.xlsx"))
    assert len(xlsx_output) == 3
