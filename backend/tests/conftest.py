from pathlib import Path

import pytest

from oeps import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "TEST_OUTPUT_DIR": str(Path(Path(__file__).parent, "test_output")),
            "TEST_REGISTRY_DIR": str(Path(Path(__file__).parent, "test_registry")),
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
