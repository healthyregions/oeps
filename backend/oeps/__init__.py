from flask import Flask

from oeps.commands import (
    frictionless_grp,
    census_grp,
    bigquery_grp,
    overture_grp,
)
from oeps.routes import api

def create_app():

    # create app instance
    app = Flask(__name__)

    # configure from config.py file
    app.config.from_object('oeps.config')

    # add all cli commands
    app.cli.add_command(frictionless_grp)
    app.cli.add_command(census_grp)
    app.cli.add_command(bigquery_grp)
    app.cli.add_command(overture_grp)

    # register routes via blueprints
    app.register_blueprint(api)

    return app

