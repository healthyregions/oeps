import click

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
def merge_data_table(source, table_source, registry_path, dry_run):
    """Merge data from an external CSV into the canonical CSVs in OEPS.

    ARGUMENTS:

    TABLE_SOURCE: name of table_source to merge this CSV into. Table source
    must already exist in the registry.
    """

    registry = Registry(registry_path)

    ts = TableSource(table_source, registry=registry, with_data=True)

    ts.stage_incoming_csv(source)
    ts.validate_incoming_csv()
    ts.merge_incoming_csv(dry_run=dry_run)
