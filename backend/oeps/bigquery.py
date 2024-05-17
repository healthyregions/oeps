import io
import os

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.cloud.bigquery import (
    Client,
    Table,
    SchemaField,
    LoadJobConfig,
)

def get_client():
    """ Creates a BigQuery Client object and returns it, acquires credentials
    through get_credentials(). """

    project_id = os.getenv("BQ_PROJECT_ID")
    credentials = get_credentials()
    client = Client(project=project_id, credentials=credentials)
    return client

def get_credentials():
    """ Creates and returns a credentials object to be used in a BigQuery Client.

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
    json_crendentials_path = os.getenv('BQ_CREDENTIALS_FILE_PATH')
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
            "auth_provider_x509_cert_url": os.getenv("BQ_CREDENTIALS_AUTH_PROVIDER_X509_CERT_URL"),
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


class BigQuery():

    def __init__(self, project_id=os.getenv('BQ_PROJECT_ID')):

        if not project_id:
            raise Exception("project_id must be provided or present as env var BQ_PROJECT_ID")

        self.project_id = project_id
        self.client = get_client()
        self.job_result = None

    def create_table(self, schema, overwrite=False):

        # make sure the dataset exists
        self.client.create_dataset(schema['bq_dataset_name'], exists_ok=True)

        field_list = []
        for f in schema["schema"]["fields"]:
            max_length = f.get('max_length')
            field_list.append(
                SchemaField(
                    name=f["name"],
                    field_type=f["bq_data_type"],
                    max_length=max_length,
                )
            )

        full_table_id = f"{self.project_id}.{schema['bq_dataset_name']}.{schema['bq_table_name']}"
        if overwrite is True:
            self.client.delete_table(full_table_id, not_found_ok=True)
        table = self.client.create_table(
            Table(full_table_id, schema=field_list),
        )
        return table

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

        load_job_config = LoadJobConfig(
            source_format="NEWLINE_DELIMITED_JSON"
        )
        load_job = self.client.load_table_from_file(
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

    def run_query_from_file(self, path, dry_run=False):
        """ Reads a query statement from a .sql file and performs the query on BQ. 
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
        """ Exports the latest results from a query job. """

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
        """ Prints the latest results from a query job. """

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

