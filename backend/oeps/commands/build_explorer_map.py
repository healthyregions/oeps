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
    upload: bool = False,
):
    """Builds configuration files for the frontend OEPS Explorer application,
    and ptionally upload them to S3 bucket for direct access from the frontend.

    If not uploaded, they will be in .cache/explorer/csvs and the frontend will
    read them from there.
    """

    registry = Registry(registry_path)
    ex = Explorer(registry=registry, root_dir=explorer_path)
    ex.build_map_config(upload=upload)
