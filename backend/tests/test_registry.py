from oeps.commands import registry_grp


def test_validate(runner):
    result = runner.invoke(
        registry_grp,
        ["validate", "--registry-path", runner.app.config["TEST_REGISTRY_DIR"]],
    )
    assert result.exit_code == 0


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
