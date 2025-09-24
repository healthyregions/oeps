import click

from ..registry.handlers import Registry
from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@click.option(
    "--name",
    "-n",
    help="Name (id) of new table source. This will be used for the CSV file name.",
)
@click.option(
    "--data-year",
    "-y",
    help="Year of data that this table source will hold.",
)
@click.option(
    "--geodata-source",
    "-g",
    help="Name of the geodata source that this table source will be joined to.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Stage and prepare new table source but don't save.",
)
@add_common_opts(registry_opt)
def create_table_source(name, data_year, geodata_source, dry_run, registry_path):
    """Creates a new blank table source and generates an accompanying
    CSV with only relevant keys.
    """

    if not name or not data_year or not geodata_source:
        print("ERROR: You must provide -n/--name, -y/--data-year, and -g/--geodata-source")
        exit()

    registry = Registry.create_from_directory(registry_path)

    if name in registry.table_sources:
        print("ERROR: A table source with this name already exists.")
        exit()

    if geodata_source not in registry.geodata_sources:
        print(f"ERROR: Invalid geodata source: {geodata_source}")
        exit()


    registry.create_table_source(name, data_year, geodata_source, dry_run=dry_run)
