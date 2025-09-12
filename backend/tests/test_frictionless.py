def test_create_data_package(runner):

    ## TODO need to update this test
    return
    result = runner.invoke(
        args=[
            "create-data-package",
            "--destination",
            runner.app.config["TEST_OUTPUT_DIR"],
            "--registry-path",
            runner.app.config["TEST_REGISTRY_DIR"],
            "--no-cache",
        ]
    )
    assert result.exit_code == 0
