import click
from pathlib import Path

from oeps.clients.registry import Registry, TableSource
from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@add_common_opts(registry_opt)
@click.option(
    "--sync-table-sources",
    is_flag=True,
    default=False,
    help="Updates all variable table_sources values directly from CSV data.",
)
def validate_registry(registry_path: Path, sync_table_sources: bool):
    """Runs a series of validation processes against the current registry content."""

    registry = Registry(registry_path)
    registry.validate()
    if sync_table_sources:
        for ts in registry.table_sources.keys():
            table_source = TableSource(ts, with_data=True)
            registry.sync_variable_table_sources(table_source)
