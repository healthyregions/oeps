from oeps.commands import explorer_grp


def test_build_docs(runner):
    result = runner.invoke(explorer_grp, ["build-docs"])
    assert result.exit_code == 0


def test_build_map(runner):
    result = runner.invoke(explorer_grp, ["build-map"])
    assert result.exit_code == 0
