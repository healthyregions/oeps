from pathlib import Path

import click
from oeps.clients.registry import Registry

from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@click.option(
    "--destination",
    "-d",
    default=None,
    help="Output directory for new dictionaries, if not supplied will be placed within data dir.",
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
@add_common_opts(registry_opt)
def create_data_dictionaries(destination, registry_path):
    """Create the human readable, MS Excel data dictionaries based on registry content."""

    registry = Registry(registry_path)
    registry.create_data_dictionaries(destination)
