import click
from pathlib import Path

from ..handlers import Registry
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

    registry = Registry.create_from_directory(registry_path)
    print(f"variables: {len(registry.variables)}")
    print(f"table sources: {len(registry.table_sources)}")
    print(f"geodata sources: {len(registry.geodata_sources)}")
    print(f"metadata entries: {len(registry.metadata)}")

    registry.validate()

    if sync_table_sources:
        registry.update_variable_table_sources()
