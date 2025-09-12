from pathlib import Path


def test_validate(runner):
    result = runner.invoke(
        args=[
            "validate-registry",
            "--registry-path",
            runner.app.config["TEST_REGISTRY_DIR"],
        ]
    )
    assert result.exit_code == 0

def test_create_oeps_dicts(runner):
    result = runner.invoke(
        args=[
            "create-data-dictionaries",
            "--destination",
            runner.app.config["TEST_OUTPUT_DIR"],
            "--registry-path",
            runner.app.config["TEST_REGISTRY_DIR"],
        ]
    )
    assert result.exit_code == 0

    xlsx_output = list(Path(runner.app.config["TEST_OUTPUT_DIR"]).glob("*.xlsx"))
    assert len(xlsx_output) == 4
