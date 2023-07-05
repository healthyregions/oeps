#the modules you will use
from google.cloud import bigquery
from google.auth import impersonated_credentials
from google.auth.transport.requests import Request
from google.oauth2 import service_account
#set up project
project_id = 'your-project-id'
#set up crendentials
# (developer): Set key_path to the path to the service account key file.
# key_path = "path/to/service_account.json"
credentials_path = "key_path"
credentials = service_account.Credentials.from_service_account_file(
    credentials_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
if credentials.expired and credentials.refresh_token:
    credentials.refresh(Request())
#impersonating a target service account
target_principal = 'your-email-address-with-service-account'
target_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
impersonated_creds = impersonated_credentials.Credentials(
    source_credentials=credentials,
    target_principal=target_principal,
    target_scopes=target_scopes,
)
#create big query client
client = bigquery.Client(project=project_id, credentials=impersonated_creds)
#set schema(including columns and type of data)
schema = [
    bigquery.SchemaField('colunm-name-1', 'type1'),
    bigquery.SchemaField('colunm-name-2', 'type2'),
    bigquery.SchemaField('colunm-name-3', 'type3')
]
#create your table in your bigquery
table_options = bigquery.BigtableOptions()
dataset_ref = client.dataset('your-dataset-name')
table_ref = dataset_ref.table('your-table-name')
table = bigquery.Table(table_ref)
table.schema = schema
table = client.create_table(table)

print('Table created: {}'.format(table.table_id))

