from pathlib import Path

import click

from ..clients.s3 import clear_s3_bucket
from ..utils import load_json
from ._common_opts import (
    add_common_opts,
    explorer_opt,
)


@click.command()
@click.option(
    "--non-interactive",
    is_flag=True,
    default=False,
    help="Fail immediately if explorer/config/sources.json is missing (for CI). "
    "Without this flag, a missing file triggers an interactive confirmation.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Print S3 keys that would be deleted without deleting them.",
)
@add_common_opts(explorer_opt)
def clean_explorer_bucket(
    explorer_path: Path,
    non_interactive: bool,
    dry_run: bool,
):
    """Deletes all files from the S3 bucket which are not mentioned in the local
    explorer/config/sources.json file. If no sources.json file exists, optionally
    deletes all uploaded files (interactive only).
    """
    config_dir = Path(explorer_path, "config")
    sources_path = Path(config_dir, "sources.json")
    objs_in_use = []

    # command is highly destructive if sources.json is missing
    # so prompt user in that case (unless --non-interactive)
    try:
        sources = load_json(sources_path)["sources"]
        tables = [source["tables"] for source in sources]

        # grab all filenames nested in the sources.json
        objs_in_use = [
            value["file"].split("/")[-1]
            for table in tables
            for value in table.values()
        ]

    except FileNotFoundError:
        msg = (
            f"{sources_path} not found; continuing would delete all files under "
            "`explorer/csv` except an explicit keep list."
        )
        if non_interactive:
            raise click.ClickException(
                f"{msg} Refusing in --non-interactive mode (e.g. CI). "
                "Commit sources.json or run locally without --non-interactive."
            )
        print(msg)
        resp = input("Would you like to continue with deletion? (y/N)")
        if resp.lower() != "y":
            print("Exiting without deleting files.")
            return

    objs_in_use = objs_in_use + ["counties.csv", "states.csv"]

    if dry_run:
        print("Dry run: no objects will be deleted.")

    clear_s3_bucket(
        prefix="explorer/csv",
        objs_to_keep=objs_in_use,
        dry_run=dry_run,
    )
