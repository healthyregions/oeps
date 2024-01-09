import os
import json
import dotenv
import argparse
from datetime import datetime
from glob import glob
from pathlib import Path

from oeps_backend.src.bigquery import BigQuery, get_client
from oeps_backend.src.data_resource import DataResource

dotenv.load_dotenv()

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), 'resources')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("operation",
                        choices=[
                            "check-credentials",
                            "load",
                            "export",
                            "generate-reference-md"
                        ],
                        help="operation to run")
    parser.add_argument("--sql-file",
                        help="Path to file with SQL statement to run.")
    parser.add_argument("--destination", "-d",
                        help="Full path for export. Must end with .csv for CSV or .shp for shapefile.")
    parser.add_argument("--source", "-s",
                        help="Data Resource JSON file to load, or directory with multiple files.")
    parser.add_argument("--overwrite",
                        action="store_true",
                        help="Overwrite BQ table if it already exists.")
    parser.add_argument("--table-only",
                        action="store_true",
                        help="Only create the new table, don't load data into it.")
    parser.add_argument("--dry-run",
                        action="store_true",
                        help="Mock operation and perform no create/delete actions.")
    args = parser.parse_args()

    if args.operation == "check-credentials":
        client = get_client()
        print('ok')
        exit()

    bq = BigQuery()
    if args.operation == "load":

        if os.path.isdir(args.source):
            paths = glob(os.path.join(args.source, "*.json"))
        elif os.path.isfile(args.source):
            paths = [args.source]
        else:
            print('invalid path input')
            exit()

        all_errors = []
        
        for path in paths:
            
            dr = DataResource(path)

            if args.table_only:
                table = bq.create_table(dr.schema, overwrite=args.overwrite)
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
                    table = bq.create_table(dr.schema, overwrite=args.overwrite)
                    print(f"TABLE CREATED: {table}")
                    load_job = bq.load_table(rows, dr.schema['bq_dataset_name'], dr.schema['bq_table_name'])
                    print(f"TIME ELAPSED: {datetime.now()-start}")

    if args.operation == "export":
        if args.sql_file:
            bq.run_query_from_file(args.sql_file)

        if args.destination:
            bq.export_results(args.destination)

        else:
            bq.print_results()

    if args.operation == "generate-reference-md":

        project_id = os.getenv("BQ_PROJECT_ID")

        datasets = {}

        files = glob(os.path.join(RESOURCES_DIR, "*.json"))

        for f in files:
            with open(f, "r") as openf:
                d = json.load(openf)

            ds_name = d['bq_dataset_name']
            t_name = d['bq_table_name']

            if not ds_name in datasets:
                datasets[ds_name] = {}

            if not t_name in datasets[ds_name]:
                datasets[ds_name][t_name] = []

            for f in d['fields']:
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
