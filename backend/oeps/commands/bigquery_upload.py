from datetime import datetime

import click

from oeps.clients.bigquery import BigQuery, get_client
from ..registry.handlers import Registry

from ._common_opts import (
    add_common_opts,
    overwrite_opt,
    registry_opt,
)


@click.command()
@click.option(
    "--name",
    "-n",
    help="Name can be provided to load a single Data Resource to Big Query (instead of everything in the registry)",
)
@click.option(
    "--table-only",
    is_flag=True,
    default=False,
    help="Only create the new table, don't load data into it.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Mock operation and perform no create/delete actions.",
)
@click.option(
    "--check-credentials",
    is_flag=True,
    default=False,
    help="Checks local credentials and exits.",
)
@add_common_opts(overwrite_opt, registry_opt)
def bigquery_upload(
    name, table_only, dry_run, overwrite, registry_path, check_credentials
):
    """Load a data resource to a big query table. The data resource schema should provide all field
    and table configuration information that is needed to create the table and load data into it."""

    if check_credentials:
        get_client()
        print("ok")
        exit()

    bq = BigQuery()
    registry = Registry.create_from_directory(registry_path)

    print("WARNING: This command still needs to be updated to use the new Registry model.")
    print("  --cancelling operation")
    exit()

    messages = []

    data_resources = registry.get_all_sources()

    if name:
        to_load = [i for i in data_resources if i["name"] == name]
        if len(to_load) == 0:
            print("no resource by that name in registry. cancelling load.")
            exit()
    else:
        to_load = data_resources

    for resource in to_load:
        if name and resource["name"] != name:
            continue

        if table_only:
            table = bq.create_table(resource, overwrite=overwrite)
            print(table)
            exit()

        else:
            start = datetime.now()
            print(f"\nVALIDATE INPUT SOURCE: {resource['path']}")
            rows, errors = bq.load_rows_from_resource(resource)
            messages += errors
            print(f"WARNINGS ENCOUNTERED: {len(errors)}")
            for e in errors:
                print("  " + e)

            if not dry_run:
                print(f"\nBEGIN LOAD: {resource['name']}")
                table = bq.create_table(resource, overwrite=overwrite)
                print(f"TABLE CREATED: {table}")
                load_job = bq.load_table(
                    rows, resource["bq_dataset_name"], resource["bq_table_name"]
                )
                print(f"JOB COMPLETE: {load_job}")
                print(f"TIME ELAPSED: {datetime.now()-start}")

    print(f"ERRORS/WARNINGS ENCOUNTERED: {len(messages)}")
