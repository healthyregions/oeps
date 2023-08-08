import os
import json

from google.cloud import bigquery

from oeps_backend.utils import make_credentials, LOCAL_DATA_DIR

#set up project
project_id = os.getenv("BQ_PROJECT_ID")

credentials = make_credentials()

#create big query client
client = bigquery.Client(project=project_id, credentials=credentials)

#get the path of JSON file
json_path = os.path.join(LOCAL_DATA_DIR, 'JSON_example')
#read and open json file
with open(json_path) as json_file:
    file = json.load(json_file)
#set schema(including columns and type of data)

"""
in JSON file example, there are label, names, and data type in json to descibe each field,
and the data types of them are string, integer, boolean, respectively
"""

#set an empty schema
schema = []
schema = []
for item in file["table_name"]["field_name"]:
    schema.append(bigquery.SchemaField(item["column_name"],item["data_type"]))
    
#create your table in your bigquery
table_options = bigquery.BigtableOptions()

#dataset name should not include project_name, or the name will be invalid
dataset_ref = client.dataset('ac_dataset')
table_ref = dataset_ref.table('ac_table')
table = bigquery.Table(table_ref)
table.schema = schema
table = client.create_table(table)

print('Table created: {}'.format(table.table_id))

