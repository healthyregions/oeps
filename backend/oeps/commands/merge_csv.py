import click

import pandas as pd

from ..registry.handlers import Registry

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

    registry = Registry.create_from_directory(registry_path)

    ts = registry.table_sources.get(table_source)
    if not ts:
        print(f"Invalid table source name: {table_source}")
        exit()

    df = pd.read_csv(source)
    staged_df = registry.prepare_incoming_df(df, ts)
    if not dry_run:
        ts.merge_df(staged_df)
        registry.update_variable_table_sources(ts)
