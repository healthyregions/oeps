import click

import pandas as pd

from oeps.clients.registry import Registry, TableSource

from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@click.option(
    "--source",
    "-s",
    help="Path to CSV that will be merged into the data registry.",
)
@click.option(
    "--table-source",
    "-t",
    help="Name of the table source this input will be joined to.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Stage and prepare the import but alter no registry or data files.",
)
@add_common_opts(registry_opt)
def merge_csv(source, table_source, registry_path, dry_run):
    """Merge data from an external CSV into the canonical CSVs in OEPS.

    ARGUMENTS:

    -s / --source: Path to CSV to be merged in.

    -t / --table-source: name of table_source to merge this CSV into. Table source
    must already exist in the registry.

    --dry-run: load and stage the CSV but alter no files.
    """

    registry = Registry(registry_path)

    ts = TableSource(table_source, registry=registry, with_data=True)

    df = pd.read_csv(source)
    staged_df = ts.stage_incoming_df(df)
    if not dry_run:
        ts.merge_df(staged_df)
