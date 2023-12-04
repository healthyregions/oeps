import os
import dotenv
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.cloud.bigquery import (
    Client,
)

dotenv.load_dotenv()

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
        json_crendentials = get_credentials_info()
        credentials = service_account.Credentials.from_service_account_info(
            json_crendentials,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

    return credentials

def get_credentials_info():
    """ Helper function to aggregate all BiqQuery credential info stored in environment
    variables and return them in single dict. """

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
