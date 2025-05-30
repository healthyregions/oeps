import click

from oeps.clients.registry import Registry

from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@click.option(
    "--name",
    "-n",
    help="Name of new table source, must be constructed like: {summary level}-{year}",
)
@click.option(
    "--geodata-source",
    "-g",
    help="Name of the geodata source for new table source.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Stage and prepare the import but alter no registry or data files.",
)
@add_common_opts(registry_opt)
def create_table_source(name, geodata_source, dry_run, registry_path):
    """Creates a new blank table source and generates an accompanying
    CSV with only HEROP_IDs.
    """

    registry = Registry(registry_path)

    if geodata_source not in registry.geodata_sources:
        print(f"Invalid geodata source: {geodata_source}")
        exit()
    if name in registry.table_sources:
        print(f"This table source already exists: {name}")
        exit()

    registry.create_table_source(name, geodata_source, dry_run=dry_run)
