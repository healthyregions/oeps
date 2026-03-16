from datetime import datetime

import click

from ..clients.bigquery import BigQuery, get_client
from ..handlers import Registry

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

    messages = []

    # Get table sources from registry
    if name:
        if name not in registry.table_sources:
            print(f"ERROR: No table source found with name '{name}' in registry.")
            exit(1)
        to_load = [registry.table_sources[name]]
    else:
        to_load = list(registry.table_sources.values())

    for table_source in to_load:
        if name and table_source.name != name:
            continue

        # Convert TableSource to format expected by BigQuery methods
        # Use default dataset name "tabular" (as per old structure)
        # HEROP_ID is the primary key and must be included in schema (first)
        schema_fields = [
            {
                "name": "HEROP_ID",
                "type": "string",
                "max_length": None,
            }
        ]
        # Add all variable fields (skip HEROP_ID if it's already in variables to avoid duplicate)
        for var in table_source.variables:
            if var.name == "HEROP_ID":
                continue  # Already added above
            schema_fields.append({
                "name": var.name,
                "type": var.type,
                "max_length": getattr(var, "max_length", None),
            })
        
        resource = {
            "name": table_source.name,
            "path": table_source.full_path,
            "format": "csv",  # Table sources are always CSV
            "bq_dataset_name": "tabular",  # Default dataset name
            "bq_table_name": table_source.name,  # Use table source name as table name
            "schema": {
                "fields": schema_fields
            }
        }

        if table_only:
            table = bq.create_table(resource, overwrite=overwrite)
            print(table)
            if name:
                exit(0)
            continue

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
        else:
            print(f"\nDRY RUN: Would load {len(rows)} rows to {resource['bq_dataset_name']}.{resource['bq_table_name']}")

    print(f"\nTOTAL ERRORS/WARNINGS ENCOUNTERED: {len(messages)}")
