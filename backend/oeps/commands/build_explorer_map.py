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
@click.option(
    "--upload",
    is_flag=True,
    default=False,
    help="Upload the output data CSV files to S3 bucket",
)
def build_explorer_map(
    registry_path: Path,
    explorer_path: Path,
    skip_upload: bool = False,
):
    """Builds configuration files for the frontend OEPS Explorer application,
    and uploads them to S3 bucket for direct access from the frontend.

    Optionally skip the upload step if you just want to inspect the output files
    locally. They will be in .cache/explorer/csvs.
    """

    registry = Registry(registry_path)
    ex = Explorer(registry=registry, root_dir=explorer_path)
    ex.build_map_config(upload=not skip_upload)
