import io
import os
import json
import argparse
import pandas as pd
import geopandas as gpd

from shapely import make_valid, is_valid, normalize, to_geojson
from shapely.geometry import Polygon, MultiPolygon

from google.cloud.bigquery import (
    Table,
    SchemaField,
    LoadJobConfig,
)

from oeps_backend.utils import get_client, LOCAL_DATA_DIR

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
    print(f'Table created: {table.full_table_id}')
    return table

def load_table(schema):
    """
    Takes an input table_definition and loads the specified data source into
    Google BigQuery, using the schema supplied. For spatial data, the BigQuery
    GEOGRAPHY column must be named 'geom'.

    The load mechanism used here is BQ's load_data_from_file, with a StringIO
    object taking the place of an opened file. The StringIO object must contain
    newline-delimited, stringified JSON objects. It took a long time to reach
    that configuration successfully, because load_data_from_dataframe failed on
    certain geometries without providing any way to debug which ones.
    """

    project_id = os.getenv("BQ_PROJECT_ID")

    dataset_path = os.path.join(LOCAL_DATA_DIR, schema['data_source'])

    client = get_client()

    df = gpd.read_file(dataset_path)
    print(df.head())

    print("Preparing data frame...")
    # use any src_name properties to rename columns where needed
    field_mapping = {}
    for f in schema['fields']:
        src_name = f.get('src_name')
        if src_name:
             field_mapping[src_name] = f['name']
    if field_mapping:
        df.rename(columns=field_mapping, inplace=True)

    # remove any input columns that are not in the schema
    drop_columns = [i for i in df.columns if not i in field_mapping.values()]
    df.drop(columns=drop_columns, inplace=True)

    # iterate fields and zfill columns where needed
    for f in schema['fields']:
        if f.get('zfill', False) is True:
            if df.dtypes[f['name']] == 'float64':
                df[f['name']] = df[f['name']].apply(lambda x: str(int(x)).zfill(f['max_length']))
            else:
                df[f['name']] = df[f['name']].apply(lambda x: str(x).zfill(f['max_length']))

    print(df.head())

    field_types = {f['name']: f['type'] for f in schema['fields']}

    rows = []
    for i in df.index:
        row = {col: df.at[i, col] for col in df.columns if not col == "geom"}

        # cast all values to strings for string fields. necessary because some
        # NULL shapefile attribute values were interpreted as float('nan'), which
        # breaks json parsing
        for k in row:
            if field_types[k] == "string":
                row[k] = str(row[k])

        # handle geometry column by dumping it to GeoJSON string. this fixes
        # some Polygon format errors that occurred with the default WKT that
        # GeoPandas returns for shapes. geom.__geo_interface__ is a shapely thing.
        if 'geom' in df.columns:
            row['geom'] = json.dumps(df.at[i, 'geom'].__geo_interface__)
        rows.append(json.dumps(row))

    print(f"Input rows: {len(rows)}")

    str_data = "\n".join(rows)
    data_as_file = io.StringIO(str_data)

    full_table_id = f"{project_id}.{schema['bq_dataset_name']}.{schema['bq_table_name']}"
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
    parser.add_argument("file_path")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--table-only", action="store_true")
    args = parser.parse_args()

    with open(args.file_path, "r") as o:
        schema = json.load(o)

    table = create_table(schema, overwrite=args.overwrite)

    if not args.table_only:
        load_job = load_table(schema)

