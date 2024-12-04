from oeps.commands import frictionless_grp


def test_create_data_package(runner):
    result = runner.invoke(
        frictionless_grp,
        ["create-data-package", "-d", ".cache/data-packages/.test-packages"],
    )
    assert result.exit_code == 0
