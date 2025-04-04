"""## OEPS Backend

These pages document the backend of the OEPS package, which is a Flask app
that holds a suite of command line tools for various OEPS data-related operations.


### Getting started

To install this backend, follow these steps:

```
# create and activate Python 3.8+ virtual environment
python3 -m venv env && source ./env/bin/activate

# clone the source repo
git clone https://github.com/healthyregions/oeps

# enter the backend directory
cd oeps/backend

pip install -e .
```
"""

from flask import Flask

from oeps.commands import (
    make_cli_docs,
    make_registry_summary,
    bigquery_grp,
    census_grp,
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
    app.cli.add_command(census_grp)
    app.cli.add_command(explorer_grp)
    app.cli.add_command(frictionless_grp)
    app.cli.add_command(registry_grp)

    # register routes via blueprints
    app.register_blueprint(api)

    return app
