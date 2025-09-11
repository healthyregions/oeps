import click

from ..registry.handlers import Registry
from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@click.option(
    "--year",
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
def create_table_source(year, geodata_source, dry_run, registry_path):
    """Creates a new blank table source and generates an accompanying
    CSV with only relevant keys.
    """

    registry = Registry.create_from_directory(registry_path)

    if geodata_source not in registry.geodata_sources:
        print(f"ERROR: Invalid geodata source: {geodata_source}")
        exit()

    for ts in registry.table_sources.values():
        if ts.year == year and ts.geodata_source == geodata_source:
            print(f"ERROR: This table source already exists: {ts.name}")
            exit()

    registry.create_table_source(year, geodata_source, dry_run=dry_run)
