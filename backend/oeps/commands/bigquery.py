import os
import json
from datetime import datetime
from glob import glob
from pathlib import Path
from argparse import Namespace

import click
from flask import current_app
from flask.cli import AppGroup

from oeps.clients.bigquery import BigQuery, get_client
from oeps.clients.frictionless import DataResource
from oeps.config import (
    EXPLORER_ROOT_DIR,
    RESOURCES_DIR,
    CACHE_DIR,
)

# Make relative paths for directory configs so they can properly be used as default values for 
# CLI arguments. Using absolute paths (e.g. those in the config) would result in absolute paths
# in the generated docs... this would be incorrect on every system besides the one that had 
# generated the docs.
EXPLORER_ROOT_DIR_rel = os.path.relpath(EXPLORER_ROOT_DIR, start=Path(__file__).parent)
RESOURCES_DIR_rel = os.path.relpath(RESOURCES_DIR, start=Path(__file__).parent.parent)
CACHE_DIR_rel = os.path.relpath(CACHE_DIR, start=Path(__file__).parent.parent)

## Group of commands for Google Big Query operations
bigquery_grp = AppGroup('bigquery',
    help="A group of operations for loading, querying, and exporting data to Google Big Query."
)

@bigquery_grp.command()
def check_credentials():
    """Check provided credentials for BigQuery client."""
    get_client()
    print('ok')

@bigquery_grp.command()
@click.option("--source", "-s",
    default=RESOURCES_DIR_rel,
    help="Data resource JSON file to load, or directory with multiple files to load. If no source "\
        "is provided, will process all files in the data/resources directory.",
)
@click.option("--overwrite",
    is_flag=True,
    default=False,
    help="Overwrite BQ table if it already exists."
)
@click.option("--table-only",
    is_flag=True,
    default=False,
    help="Only create the new table, don't load data into it."
)
@click.option("--dry-run",
    is_flag=True,
    default=False,
    help="Mock operation and perform no create/delete actions."
)
def load(**kwargs):
    """Load a data resource to a big query table. The data resource schema should provide all field
and table configuration information that is needed to create the table and load data into it."""

    args = Namespace(**kwargs)
    client = BigQuery()

    source = Path(args.source)
    if source.isdir():
        paths = source.glob("*.json")
    elif source.isfile():
        paths = [source]
    else:
        print('invalid path input')
        exit()

    all_errors = []
    
    for path in paths:
        
        dr = DataResource(path)

        if args.table_only:
            table = client.create_table(dr.schema, overwrite=args.overwrite)
            print(table)
            exit()

        else:
            start = datetime.now()
            print(f"\nVALIDATE INPUT SOURCE: {dr.schema['path']}")
            rows, errors = dr.load_rows_from_file()
            all_errors += errors
            print(f"WARNINGS ENCOUNTERED: {len(errors)}")
            for e in errors:
                print("  " + e)

            if not args.dry_run:
                print(f"\nBEGIN LOAD: {path}")
                table = client.create_table(dr.schema, overwrite=args.overwrite)
                print(f"TABLE CREATED: {table}")
                load_job = client.load_table(rows, dr.schema['bq_dataset_name'], dr.schema['bq_table_name'])
                print(F"JOB COMPLETE: {load_job}")
                print(f"TIME ELAPSED: {datetime.now()-start}")

@bigquery_grp.command()
@click.option('--output', "-o",
    help="Output file for export. Must end with .csv for CSV or .shp for ESRI Shapefile."
)
@click.option('--sql-file',
    help="Path to file with SQL SELECT statement to run."
)
def export(**kwargs):
    """ Runs a SQL statement, which must be provided in a .sql file, and the results are printed to the console
or saved to a CSV or SHP output file, based on the destination argument."""

    args = Namespace(**kwargs)

    client = BigQuery()

    if args.sql_file:
        client.run_query_from_file(args.sql_file)

    if args.destination:
        client.export_results(args.destination)

    else:
        client.print_results()


@bigquery_grp.command()
def generate_reference_md():
    """Generates a reference document for the BigQuery project schema, based on the
locally stored resource JSON schema files. """

    project_id = os.getenv("BQ_PROJECT_ID")

    datasets = {}

    files = glob(os.path.join(current_app.config['RESOURCES_DIR'], "*.json"))

    for f in files:
        with open(f, "r") as openf:
            d = json.load(openf)

        ds_name = d['bq_dataset_name']
        t_name = d['bq_table_name']

        if ds_name not in datasets:
            datasets[ds_name] = {}

        if t_name not in datasets[ds_name]:
            datasets[ds_name][t_name] = []

        for f in d['schema']['fields']:
            datasets[ds_name][t_name].append({
                'name': f.get('name'),
                'data_type': f.get('bq_data_type'),
                'description': f.get('description'),
                'source': f.get('source')
            })

    out_path = Path(Path(__file__).resolve()).parent.parent / "BQ-Reference.md"
    with open(out_path, 'w') as openf:

        ds_ct = len(datasets)
        openf.write(f"""# Project Id: {project_id}

{ds_ct} dataset{'s' if ds_ct != 1 else ''} in this project: {', '.join(datasets.keys())}

""")
        for ds in datasets:
            t_ct = len(datasets[ds])
            openf.write(f"""## {ds}

{t_ct} table{'s' if t_ct != 1 else ''} in this dataset.

""")

            for t in datasets[ds]:

                c_ct = len(datasets[ds][t])
                openf.write(f"""### {t}

ID: `{project_id}.{ds}.{t}`

{c_ct} column{'s' if c_ct != 1 else ''} in this table.

Name|Data Type|Description|Source
-|-|-|-
""")

                for c in datasets[ds][t]:
                    openf.write(f"{c['name']}|{c['data_type']}|{c['description']}|{c['source']}\n")

                openf.write("\n")
