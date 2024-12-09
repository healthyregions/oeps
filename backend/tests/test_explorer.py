from oeps.commands import explorer_grp


def test_build_docs(runner):
    result = runner.invoke(
        explorer_grp,
        [
            "build-docs",
            "--explorer-path",
            runner.app.config["TEST_OUTPUT_DIR"],
            "--registry-path",
            runner.app.config["TEST_REGISTRY_DIR"],
        ],
    )
    assert result.exit_code == 0


def test_build_map(runner):
    result = runner.invoke(
        explorer_grp,
        [
            "build-map",
            "--make-csvs",
            "--explorer-path",
            runner.app.config["TEST_OUTPUT_DIR"],
            "--registry-path",
            runner.app.config["TEST_REGISTRY_DIR"],
        ],
    )
    assert result.exit_code == 0
