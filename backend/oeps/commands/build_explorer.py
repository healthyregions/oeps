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
    "--map-only",
    is_flag=True,
    default=False,
    help="Only build static content to drive the map.",
)
@click.option(
    "--docs-only",
    is_flag=True,
    default=False,
    help="Only build static content to drive the docs page.",
)
@click.option(
    "--upload-map-data",
    is_flag=True,
    default=False,
    help="Upload the output map data CSV files to S3 bucket.",
)
def build_explorer(map_only: bool, docs_only: bool, upload_map_data: bool, registry_path: Path, explorer_path: Path):
    """Builds all static data content needed to power the frontend OEPS Explorer application.
    
    Optionally only build data for the map, or for the /docs page (theme, construct, and source data)
    
    Use --upload-map-data to make a production update for the map. Without this argument, CSV data
    files for the map will just be stored locally in .cache/explorer/csvs and the frontend running locally
    will read them from there.
    """

    registry = Registry(registry_path)
    ex = Explorer(registry=registry, root_dir=explorer_path)

    ops = {
        "docs": not map_only,
        "map": not docs_only,
    }

    if ops["docs"]:
        ex.build_docs_config()

    if ops["map"]:
        ex.build_map_config(upload=upload_map_data)
