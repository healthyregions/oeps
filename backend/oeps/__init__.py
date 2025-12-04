from flask import Flask

from oeps.commands.bigquery_export import bigquery_export
from oeps.commands.bigquery_upload import bigquery_upload
from oeps.commands.build_docs import build_docs
from oeps.commands.build_explorer import build_explorer
from oeps.commands.clean_explorer_bucket import clean_explorer_bucket
from oeps.commands.create_data_package import create_data_package
from oeps.commands.create_table_source import create_table_source
from oeps.commands.validate_registry import validate_registry
from oeps.commands.merge_csv import merge_csv
from oeps.commands.move_variable import move_variable
from oeps.commands.remove_variable import remove_variable


def create_app():
    # create app instance
    app = Flask(__name__)

    # configure from config.py file
    app.config.from_object("oeps.config")

    # add all cli commands
    app.cli.add_command(bigquery_export)
    app.cli.add_command(bigquery_upload)
    app.cli.add_command(build_docs)
    app.cli.add_command(build_explorer)
    app.cli.add_command(clean_explorer_bucket)
    app.cli.add_command(create_table_source)
    app.cli.add_command(create_data_package)
    app.cli.add_command(merge_csv)
    app.cli.add_command(validate_registry)
    app.cli.add_command(move_variable)
    app.cli.add_command(remove_variable)

    return app
