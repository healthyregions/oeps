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
def clean_explorer_bucket(
    registry_path: Path,
    explorer_path: Path
):
    """Deletes all files from the S3 bucket which are not mentioned in the local
    explorer/configs/sources.json file. If no sources.json file exists, optionally
    deletes all uploaded files.
    """

    registry = Registry(registry_path)
    ex = Explorer(registry=registry, root_dir=explorer_path)
    ex.clean_explorer_bucket()
