import click

from oeps.clients.registry import Registry
from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@add_common_opts(registry_opt)
def validate_registry(registry_path):
    """Create the human readable, MS Excel data dictionaries based on registry content."""

    registry = Registry(registry_path)
    registry.validate()
