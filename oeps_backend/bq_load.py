import io
import os
import json
import argparse
import numpy
import pandas as pd
import geopandas as gpd
from glob import glob
from datetime import datetime
from google.cloud.bigquery import (
    Table,
    SchemaField,
    LoadJobConfig,
)

from oeps_backend.utils import get_client

def create_table(schema, overwrite=False):

    project_id = os.getenv("BQ_PROJECT_ID")

    #create big query client
    client = get_client()

    # make sure the dataset exists
    client.create_dataset(schema['bq_dataset_name'], exists_ok=True)

    field_list = []
    for f in schema["fields"]:
        max_length = f.get('max_length')
        field_list.append(
            SchemaField(
                name=f["name"],
                field_type=f["bq_data_type"],
                max_length=max_length,
            )
        )

    full_table_id = f"{project_id}.{schema['bq_dataset_name']}.{schema['bq_table_name']}"
    if overwrite is True:
        client.delete_table(full_table_id, not_found_ok=True)
    table = client.create_table(
        Table(full_table_id, schema=field_list),
    )
    return table

def load_rows_from_file(schema):
    """Loads all data from the file indicated in the provided schema, and
    performs some data validation and cleaning along the way.

    Returns a list of serialized JSON strings, and a list of error messages"""

    rows, errors = [], []

    dataset_path = schema['data_source']

    try:
        if dataset_path.endswith('.shp'):
            df = gpd.read_file(dataset_path)
        elif dataset_path.endswith('.csv'):
            # set all columns as object type
            df = pd.read_csv(dataset_path, dtype='object')
        else:
            print(f"Invalid dataset: {dataset_path}")
            return
    except Exception as e:
        errors.append(str(e))
        return rows, errors

    # use any src_name properties to rename columns where needed
    field_mapping = {}
    for f in schema['fields']:
        src_name = f.get('src_name')
        if src_name:
             field_mapping[src_name] = f['name']
        else:
            errors.append(f"warning: {f['name']} missing required src_name attribute")
    if field_mapping:
        df.rename(columns=field_mapping, inplace=True)

    # remove any input columns that are not in the schema
    drop_columns = [i for i in df.columns if not i in field_mapping.values()]
    if drop_columns:
        errors.append(f"{len(drop_columns)} source columns missing from schema: " + \
                      ", ".join(drop_columns))
    df.drop(columns=drop_columns, inplace=True)

    # check for schema columns that are not found in the source data
    missing_columns = [i for i in field_mapping.values() if not i in df.columns]
    if missing_columns:
        errors.append(f"{len(missing_columns)} schema fields missing from source: " +\
                      ", ".join(missing_columns))

    # iterate fields and zfill columns where needed
    for f in schema['fields']:
        if f.get('zfill', False) is True:
            df[f['name']] = df[f['name']].apply(lambda x: str(x).zfill(f['max_length']))

    field_types = {f['name']: f['type'] for f in schema['fields']}

    # iterate the dataframe and turn each row into a dict that gets appened to rows.
    # this list is later loaded as if it were a newline-delimited JSON file.
    rows = []
    for i in df.index:
        row = {col: df.at[i, col] for col in df.columns if not col == "geom"}

        # cast all values to strings for string fields. necessary because some
        # NULL shapefile attribute values were interpreted as float('nan'), which
        # breaks json parsing
        for k in row:
            val_str = str(row[k])
            # test for float('nan') type, set to None
            if val_str == 'nan':
                row[k] = None
            if "NA" in val_str:
                row[k] = None
            # handle some infinite number variations
            if 'inf' in val_str.lower():
                row[k] = None
            if row[k]:
                if field_types[k] == "string":
                    row[k] = val_str
                if field_types[k] == "integer":
                    try:
                        row[k] = int(row[k])
                    except ValueError:
                        # special handle string values like '23493.3434'
                        row[k] = int(round(float(row[k])))
                if field_types[k] == "number":
                    row[k] = float(row[k])
                if field_types[k] == "boolean":
                    if row[k] in [1, "1", "Yes", "YES", "yes", True, 'True', 'TRUE', 'true']:
                        row[k] = True
                    elif row[k] in [0, "0", "No", "NO", "no", False, 'False', 'FALSE', 'false']:
                        row[k] = False
                    else:
                        row[k] = None

        # handle geometry column by dumping it to GeoJSON string. this fixes
        # some Polygon format errors that occurred with the default WKT that
        # GeoPandas returns for shapes. geom.__geo_interface__ is a shapely thing.
        if 'geom' in df.columns:
            row['geom'] = json.dumps(df.at[i, 'geom'].__geo_interface__)
        try:
            rows.append(json.dumps(row))
        except Exception as e:
            for k, v in row.items():
                print(field_types[k])
                print(k, v, type(v))
                print(isinstance(v, numpy.int64))
            raise(e)

    return rows, errors

def load_table(rows, dataset_name, table_name):
    """
    Takes an input list of serialized json strings, each representing a table
    row, and loads them into the provided table name and dataset.

    The schema for the rows must match the table schema, and the datset and
    table must both already exist.
    """

    client = get_client()

    print(f"Input rows: {len(rows)}")

    str_data = "\n".join(rows)
    data_as_file = io.StringIO(str_data)

    project_id = os.getenv("BQ_PROJECT_ID")
    full_table_id = f"{project_id}.{dataset_name}.{table_name}"
    table = client.get_table(full_table_id)

    load_job_config = LoadJobConfig(
        source_format="NEWLINE_DELIMITED_JSON"
    )
    load_job = client.load_table_from_file(
        file_obj=data_as_file,
        destination=table,
        job_config=load_job_config
    )
    print("Running job now...")
    try:
        load_job.result()
    except Exception as e:
        print(f"Errors encountered: {len(load_job.errors)}")
        for error in load_job.errors:
            print(error)
        raise e
    print(f"Output rows: {load_job.output_rows}")
    if load_job.errors:
        print(f"Errors encountered: {len(load_job.errors)}")
    return load_job

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--table-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        paths = glob(os.path.join(args.path, "*.json"))
    elif os.path.isfile(args.path):
        paths = [args.path]
    else:
        print('invalid path input')
        exit()

    all_errors = []
    for path in paths:
        with open(path, "r") as o:
            schema = json.load(o)

        if args.table_only:
            table = create_table(schema, overwrite=args.overwrite)
            print(table)
            exit()

        else:
            start = datetime.now()
            print(f"\nVALIDATE INPUT SOURCE: {schema['data_source']}")
            rows, errors = load_rows_from_file(schema)
            all_errors += errors
            print(f"WARNINGS ENCOUNTERED: {len(errors)}")
            for e in errors:
                print("  " + e)

            if not args.dry_run:
                print(f"\nBEGIN LOAD: {path}")
                table = create_table(schema, overwrite=args.overwrite)
                print(f"TABLE CREATED: {table}")
                load_job = load_table(rows, schema['bq_dataset_name'], schema['bq_table_name'])
                print(f"TIME ELAPSED: {datetime.now()-start}")
