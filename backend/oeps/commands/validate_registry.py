import click

from oeps.clients.registry import Registry
from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@add_common_opts(registry_opt)
def validate_registry(registry_path):
    """Runs a series of validation processes against the current registry content."""

    registry = Registry(registry_path)
    registry.validate()
