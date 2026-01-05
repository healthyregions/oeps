import io
import os
import json
from datetime import datetime
from pathlib import Path

import pandas as pd
import geopandas as gpd
import numpy

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.cloud.bigquery import (
    Client,
    Table,
    SchemaField,
    LoadJobConfig,
)

from ..handlers import TableSource

BQ_TYPE_LOOKUP = {
    "string": "STRING",
    "boolean": "BOOLEAN",
    "integer": "INTEGER",
    "date": "DATE",
    "number": "NUMERIC",
}

def get_client():
    """Creates a BigQuery Client object and returns it, acquires credentials
    through get_credentials()."""

    project_id = os.getenv("BQ_PROJECT_ID")
    credentials = get_credentials()
    client = Client(project=project_id, credentials=credentials)
    return client


def get_credentials():
    """Creates and returns a credentials object to be used in a BigQuery Client.

    If BQ_CREDENTIALS_FILE_PATH is present, that path is used to create the creds.

    If not, the following suite of environment variables must all be present and
    they will be used in place of the file:

        BQ_PROJECT_ID
        BQ_CREDENTIALS_PRIVATE_KEY_ID
        BQ_CREDENTIALS_PRIVATE_KEY
        BQ_CREDENTIALS_CLIENT_EMAIL
        BQ_CREDENTIALS_CLIENT_ID
        BQ_CREDENTIALS_AUTH_URI
        BQ_CREDENTIALS_TOKEN_URI
        BQ_CREDENTIALS_AUTH_PROVIDER_X509_CERT_URL
        BQ_CREDENTIALS_CLIENT_X509_CERT_URL
        BQ_CREDENTIALS_UNIVERSE_DOMAIN

    These variables are all acquired through the get_credentials_info() helper function."""

    credentials = None

    # prefer a local path to JSON credentials file.
    json_crendentials_path = os.getenv("BQ_CREDENTIALS_FILE_PATH")
    if json_crendentials_path:
        credentials = service_account.Credentials.from_service_account_file(
            json_crendentials_path,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

    # if no local file, attempt to get all credential info from environment
    else:
        json_crendentials = {
            "type": "service_account",
            "project_id": os.getenv("BQ_PROJECT_ID"),
            "private_key_id": os.getenv("BQ_CREDENTIALS_PRIVATE_KEY_ID"),
            "private_key": os.getenv("BQ_CREDENTIALS_PRIVATE_KEY"),
            "client_email": os.getenv("BQ_CREDENTIALS_CLIENT_EMAIL"),
            "client_id": os.getenv("BQ_CREDENTIALS_CLIENT_ID"),
            "auth_uri": os.getenv("BQ_CREDENTIALS_AUTH_URI"),
            "token_uri": os.getenv("BQ_CREDENTIALS_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv(
                "BQ_CREDENTIALS_AUTH_PROVIDER_X509_CERT_URL"
            ),
            "client_x509_cert_url": os.getenv("BQ_CREDENTIALS_CLIENT_X509_CERT_URL"),
            "universe_domain": os.getenv("BQ_CREDENTIALS_UNIVERSE_DOMAIN"),
        }
        credentials = service_account.Credentials.from_service_account_info(
            json_crendentials,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

    return credentials


class BigQuery:
    def __init__(self, project_id=os.getenv("BQ_PROJECT_ID")):
        if not project_id:
            raise Exception(
                "project_id must be provided or present as env var BQ_PROJECT_ID"
            )

        self.project_id = project_id
        self.client = get_client()
        self.job_result = None

    def create_table(self, schema, overwrite=False):
        # make sure the dataset exists
        self.client.create_dataset(schema["bq_dataset_name"], exists_ok=True)

        field_list = []
        for f in schema["schema"]["fields"]:
            max_length = f.get("max_length")
            field_list.append(
                SchemaField(
                    name=f["name"],
                    field_type=BQ_TYPE_LOOKUP[f["type"]],
                    max_length=max_length,
                )
            )

        # if loading a shapefile, create and extra field for the geometry
        if schema["format"] == "shp":
            field_list.append(
                SchemaField(
                    name="geom",
                    field_type="GEOGRAPHY",
                )
            )

        full_table_id = (
            f"{self.project_id}.{schema['bq_dataset_name']}.{schema['bq_table_name']}"
        )
        if overwrite is True:
            self.client.delete_table(full_table_id, not_found_ok=True)
        table = self.client.create_table(
            Table(full_table_id, schema=field_list),
        )
        return table

    def load_rows_from_resource(self, data_resource):
        """Loads all data from the file indicated in the provided schema, and
        performs some data validation and cleaning along the way.

        Returns a list of serialized JSON strings, and a list of error messages"""

        rows, errors = [], []

        dataset_path = data_resource["path"]

        # get the format, assume CSV if not present
        format = data_resource.get("format", "csv")

        if format not in ["csv", "shp"]:
            errors.append(f"Invalid dataset format: {format}")
            return rows, errors

        try:
            if format == "shp":
                if isinstance(dataset_path, list):
                    dataset_path = [i for i in dataset_path if i.endswith(".shp")][0]
                    df = gpd.read_file(dataset_path)
                elif dataset_path.endswith(".zip"):
                    df = gpd.read_file(f"/vsizip/vsicurl/{dataset_path}")
            elif format == "csv":
                df = pd.read_csv(dataset_path, dtype="object")

        except Exception as e:
            errors.append(f"error reading file: {str(e)}")
            return rows, errors

        field_names = [i["name"] for i in data_resource["schema"]["fields"]]

        # remove any input columns that are not in the schema
        drop_columns = [i for i in df.columns if i not in field_names]
        if drop_columns:
            errors.append(
                f"{len(drop_columns)} source columns missing from schema: "
                + ", ".join(drop_columns)
            )
        df.drop(columns=drop_columns, inplace=True)

        # check for schema columns that are not found in the source data
        missing_columns = [i for i in field_names if i not in df.columns]
        if missing_columns:
            errors.append(
                f"{len(missing_columns)} schema fields missing from source: "
                + ", ".join(missing_columns)
            )

        # iterate fields and zfill columns where needed
        for f in data_resource["schema"]["fields"]:
            if f.get("zfill", False) is True:
                df[f["name"]] = df[f["name"]].apply(
                    lambda x: str(x).zfill(f["max_length"])
                )

        field_types = {f["name"]: f["type"] for f in data_resource["schema"]["fields"]}
        bq_field_types = {
            f["name"]: BQ_TYPE_LOOKUP[f["type"]]
            for f in data_resource["schema"]["fields"]
        }

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
                if val_str == "nan":
                    row[k] = None
                if "NA" in val_str:
                    row[k] = None
                # handle some infinite number variations
                if "inf" in val_str.lower():
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
                        if row[k] in [
                            1,
                            "1",
                            "Yes",
                            "YES",
                            "yes",
                            True,
                            "True",
                            "TRUE",
                            "true",
                        ]:
                            row[k] = True
                        elif row[k] in [
                            0,
                            "0",
                            "No",
                            "NO",
                            "no",
                            False,
                            "False",
                            "FALSE",
                            "false",
                        ]:
                            row[k] = False
                        else:
                            row[k] = None
                    if bq_field_types[k] == "DATE":
                        try:
                            val = datetime.strptime(row[k], "%m/%d/%Y").strftime(
                                "%Y-%m-%d"
                            )
                            row[k] = val
                        except Exception as e:
                            raise e

            # handle geometry column by dumping it to GeoJSON string. this fixes
            # some Polygon format errors that occurred with the default WKT that
            # GeoPandas returns for shapes. geom.__geo_interface__ is a shapely thing.
            if "geom" in df.columns:
                row["geom"] = json.dumps(df.at[i, "geom"].__geo_interface__)
            try:
                rows.append(json.dumps(row))
            except Exception as e:
                for k, v in row.items():
                    print(field_types[k])
                    print(k, v, type(v))
                    print(isinstance(v, numpy.int64))
                raise (e)

        return rows, errors

    def load_table(self, rows, dataset_name, table_name):
        """
        Takes an input list of serialized json strings, each representing a table
        row, and loads them into the provided table name and dataset.

        The schema for the rows must match the table schema, and the dataset and
        table must both already exist.
        """

        print(f"Input rows: {len(rows)}")

        str_data = "\n".join(rows)
        data_as_file = io.StringIO(str_data)

        full_table_id = f"{self.project_id}.{dataset_name}.{table_name}"
        table = self.client.get_table(full_table_id)

        load_job_config = LoadJobConfig(source_format="NEWLINE_DELIMITED_JSON")
        load_job = self.client.load_table_from_file(
            file_obj=data_as_file, destination=table, job_config=load_job_config
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

    def run_query_from_file(self, path, dry_run=False):
        """Reads a query statement from a .sql file and performs the query on BQ.
        If dry_run is true, just print the query and don't perform it.
        """

        with open(path, "r") as o:
            content = o.read()
        sql = content.replace("PROJECT_ID", self.project_id)
        print(sql)

        if dry_run:
            return

        query_job = self.client.query(sql)
        result = query_job.result()

        self.job_result = result

        return result

    def export_results(self, path):
        """Exports the latest results from a query job."""

        if not self.job_result:
            print("No results to export")

        if path.endswith(".csv"):
            df = self.job_result.to_dataframe()
            print(df.columns)
            df.to_csv(path, index=False)

        elif path.endswith(".shp"):
            df = self.job_result.to_geodataframe()
            df.to_file(path)

        else:
            print("Invalid output type. Must be file ending in .csv or .shp.")

    def print_results(self):
        """Prints the latest results from a query job."""

        if not self.job_result:
            print("No results")
            return

        for n, row in enumerate(self.job_result):
            if n == 0:
                print(list(row.keys()))
            clean_row = []
            for k, v in row.items():
                if k == "geom":
                    v = v.split("(")[0]
                clean_row.append(v)
            print(clean_row)

    def generate_reference_doc(self, table_sources: list[TableSource], outfile: Path):
        project_id = os.getenv("BQ_PROJECT_ID")

        datasets = {}

        for d in table_sources:
            ds_name = "tabular"
            t_name = d.name

            if ds_name not in datasets:
                datasets[ds_name] = {}

            if t_name not in datasets[ds_name]:
                datasets[ds_name][t_name] = []

            for f in d.variables:
                datasets[ds_name][t_name].append(
                    {
                        "name": f.name,
                        "data_type": BQ_TYPE_LOOKUP[f.type],
                        "description": f.description,
                    }
                )
        # fmt: off
        with open(outfile, "w") as openf:
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

Name|Data Type|Description
-|-|-|-
""")

                    for c in datasets[ds][t]:
                        openf.write(
f"{c['name']}|{c['data_type']}|{c['description']}\n"
                        )

                    openf.write("\n")


# fmt: on
