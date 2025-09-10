from pathlib import Path

import click

from ..clients.data_dictionary import create_data_dictionary
from ..registry.handlers import Registry

from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@click.option(
    "--destination",
    "-d",
    default="../docs/src/reference/data-dictionaries/",
    help="Output directory for new dictionaries, if not supplied will be placed within data dir.",
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
@add_common_opts(registry_opt)
def create_data_dictionaries(destination, registry_path):
    """Create the human readable, MS Excel data dictionaries based on registry content."""

    registry = Registry.create_from_directory(registry_path)
    outdir = Path(destination).absolute().resolve()

    create_data_dictionary(registry, "state", outdir)
    create_data_dictionary(registry, "county", outdir)
    create_data_dictionary(registry, "tract", outdir)
    create_data_dictionary(registry, "zcta", outdir)
