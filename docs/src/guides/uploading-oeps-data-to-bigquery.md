# Uploading OEPS Data to BigQuery

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