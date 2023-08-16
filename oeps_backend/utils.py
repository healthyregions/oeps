import os
from google.auth import impersonated_credentials
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.cloud.bigquery import (
    Client,
    Table,
    SchemaField
)

import dotenv

dotenv.load_dotenv()

LOCAL_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data_local')
TABLE_DEF_DIR = os.path.join(os.path.dirname(__file__), 'table_definitions')


def get_client():

    project_id = os.getenv("BQ_PROJECT_ID")

    credentials = get_credentials()

    #create big query client
    client = Client(project=project_id, credentials=credentials)

    return client

def get_credentials():

    # prefer a local path to JSON credentials file.
    json_crendentials_path = os.getenv('BQ_CREDENTIALS_FILE_PATH')
    if json_crendentials_path:
        credentials = service_account.Credentials.from_service_account_file(
            json_crendentials_path,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

    # if no local file, attempt to get all credential info from environment
    else:
        json_crendentials = get_credentials_info()
        credentials = service_account.Credentials.from_service_account_info(
            json_crendentials,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

    return credentials

def get_credentials_info():

    return {
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
