from flask import Flask

from oeps.commands import (
    make_cli_docs,
    make_registry_summary,
    bigquery_grp,
    explorer_grp,
    frictionless_grp,
    registry_grp,
)
from oeps.routes import api


def create_app():
    # create app instance
    app = Flask(__name__)

    # configure from config.py file
    app.config.from_object("oeps.config")

    # add all cli commands
    app.cli.add_command(make_cli_docs)
    app.cli.add_command(make_registry_summary)
    app.cli.add_command(bigquery_grp)
    app.cli.add_command(explorer_grp)
    app.cli.add_command(frictionless_grp)
    app.cli.add_command(registry_grp)

    # register routes via blueprints
    app.register_blueprint(api)

    return app
