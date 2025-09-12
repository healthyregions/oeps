def test_build_docs(runner):
    result = runner.invoke(
        args=[
            "build-explorer",
            "--explorer-path",
            runner.app.config["TEST_OUTPUT_DIR"],
            "--registry-path",
            runner.app.config["TEST_REGISTRY_DIR"],
            "--docs-only"
        ]
    )
    assert result.exit_code == 0


def test_build_map(runner):
    result = runner.invoke(
        args=[
            "build-explorer",
            "--explorer-path",
            runner.app.config["TEST_OUTPUT_DIR"],
            "--registry-path",
            runner.app.config["TEST_REGISTRY_DIR"],
            "--map-only"
        ]
    )
    assert result.exit_code == 0
