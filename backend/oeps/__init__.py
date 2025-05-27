from flask import Flask

# from oeps.commands2 import (
#     make_cli_docs,
#     make_registry_summary,
#     bigquery_grp,
#     explorer_grp,
#     frictionless_grp,
#     registry_grp,
# )
from oeps.commands.bigquery_export import bigquery_export
from oeps.commands.bigquery_upload import bigquery_upload
from oeps.commands.build_docs import build_docs
from oeps.commands.build_explorer_docs import build_explorer_docs
from oeps.commands.build_explorer_map import build_explorer_map
from oeps.commands.create_data_package import create_data_package
from oeps.commands.create_data_dictionaries import create_data_dictionaries
from oeps.commands.merge_data_table import merge_data_table
from oeps.commands.validate_registry import validate_registry
from oeps.commands.inspect_csv import inspect_csv
from oeps.routes import api


def create_app():
    # create app instance
    app = Flask(__name__)

    # configure from config.py file
    app.config.from_object("oeps.config")

    # add all cli commands
    app.cli.add_command(bigquery_export)
    app.cli.add_command(bigquery_upload)
    app.cli.add_command(build_docs)
    app.cli.add_command(build_explorer_docs)
    app.cli.add_command(build_explorer_map)
    app.cli.add_command(create_data_dictionaries)
    app.cli.add_command(create_data_package)
    app.cli.add_command(merge_data_table)
    app.cli.add_command(validate_registry)
    app.cli.add_command(inspect_csv)

    # register routes via blueprints
    app.register_blueprint(api)

    return app
