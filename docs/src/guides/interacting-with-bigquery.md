# Interacting with OEPS Data in BigQuery

## Setting up Credentials

To load OEPS data to BigQuery you will need to add access credentials as environment variables using the `.env` file. This file must always stay out of version control.

- Make a copy of `.env.example` and name it `.env`. Any variables defined in this file will now be available via `os.getenv('VARIABLE_NAME')`

- Obtain a set of JSON credentials for the project, and store the file anywhere on your computer (but outside of this repository).

- In your `.env` file, update the `BQ_CREDENTIALS_FILE_PATH` variable with the full path to this file. For example:

    ```
    BQ_CREDENTIALS_FILE_PATH="/home/my_username/bq_credentials/oeps-391119-5783b2b59b83.json"
    ```

- It is also possible to set BigQuery credentials without storing a local JSON file. More info on this is in the `.env.example` file.

Once you have setup these credentials, you can test them with

    flask bigquery-upload --check-credentials

If all is well, the command will print `ok`.

## Uploading Tables

Use the following command to load a new table into BigQuery:

```shell
flask bigquery-upload
```

TODO: Need to finish this section.

Where `--source` is the path to a Data Resource schema (stored as JSON file), or a directory containing multiple Data Resource schemas. Optional flags on this command are:

- `--table-only` will create the BigQuery dataset and table based on the schema, but will not attempt to load data into it.
- `--dry-run` will validate the input dataset against the schema, but not attempt to load it.
- `--overwrite` will drop and recreate the BigQuery table if it already exists in the dataset.

## Extracting Data from BigQuery

!!! warning
    This section is outdated.

Use the following command to query the OEPS BigQuery tables:

    python scripts/bq.py export --sql sql/states.sql --output states.shp

Where `states.sql` is an example of a file that holds the SQL query to perform against one or more tables. In the SQL, `PROJECT_ID` is a placeholder (it will be replaced with the actual project identifier before the query is performed), such that table references look like `PROJECT_ID.dataset_name.table_name`, or `PROJECT_ID.spatial.states2018` for the table that holds state boundaries.

- `--sql-file` path to a file whose contents is a complete SQL query. 
- `--output` is the name of a file to which the query results will be written. Either .csv or .shp files can be specified, and if a spatial result is written to CSV the geometries will be in WKT format. If this argument is omitted, the query results will be printed to the console (helpful for testing queries).

You can write your own SQL into a file and use the same command to perform your query and export the results.

Use the [big-query-tables](../reference/bigquery/tables.md) page for quick access to all table and column names.