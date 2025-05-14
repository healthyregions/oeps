from pathlib import Path

import click

from oeps.clients.explorer import Explorer
from oeps.clients.registry import Registry

from ._common_opts import (
    add_common_opts,
    registry_opt,
    explorer_opt,
)


@click.command()
@add_common_opts(registry_opt, explorer_opt)
def build_explorer_docs(registry_path: Path, explorer_path: Path):
    """Builds configuration files for the frontend OEPS Explorer application."""

    registry = Registry(registry_path)
    ex = Explorer(registry=registry, root_dir=explorer_path)
    ex.build_docs_config()
