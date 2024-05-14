from flask import Flask

from oeps.commands import (
    create_data_package,
    schema,
    bq,
    census_grp,
)
from oeps.routes import api

# create app instance
app = Flask(__name__)

app.config.from_object('oeps.config')

# add all cli commands
app.cli.add_command(create_data_package)
app.cli.add_command(schema)
app.cli.add_command(bq)
app.cli.add_command(census_grp)

# register routes via blueprints
app.register_blueprint(api)