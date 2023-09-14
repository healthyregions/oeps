# oeps-backend

Data migration and management code for the transition of the OEPS data into Google BigQuery.

## how this fits into existing work

This project builds from the Opioid Environment Policy Scan (OEPS) data warehouse stored in [github.com/GeoDaCenter/opioid-policy-scan](https://github.com/GeoDaCenter/opioid-policy-scan), and published on Zenodo at [doi.org/10.5281/zenodo.5842465](https://doi.org/10.5281/zenodo.5842465). This repo allows us to pull the final data from the latest OEPS release and push it into Google BigQuery, which will enable new ways of accessing and analyzing that data.

Keep in mind, some details of this implementation may change over the course of the summer, so we will update this document as needed.

## getting started

0. Create and activate a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) with [venv](https://docs.python.org/3/library/venv.html), [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), or your other tool of choice.

1. Clone this repo

        git clone https://github.com/healthyregions/oeps-backend
        cd oeps-backend

2. Install this package and its dependencies

        pip install -e .

3. Enter the `oeps_backend` directory, this is where you'll run scripts from.

        cd oeps_backend

### Setup BigQuery Credentials

Enviroment variables allow us to keep BigQuery credentials outside of version control.

- Make a copy of `.env.example` and name it `.env`. Any variables defined in this file will now be available via `os.getenv('VARIABLE_NAME')`

- Obtain a set of JSON credentials for the project, and store the file anywhere on your computer (but outside of this repository).

- In your `.env` file, update the `BQ_CREDENTIALS_FILE_PATH` variable with the full path to this file.

    ```
    BQ_CREDENTIALS_FILE_PATH="/home/my_username/bq_credentials/oeps-391119-5783b2b59b83.json"
    ```

## Loading CSVs and Shapefiles

Use the following command to load a new table into BigQuery:

    python oeps_backend/bq_load.py oeps_backend/table_definitions/table.json

Where `table.json` is a table definition file as described in [table_definitions/README.md](oeps_backend/table_definitions/README.md).

- `--table-only` will create the dataset and table, but will not attempt to load data into it.
- `--overwrite` will drop the table if it already exists in the dataset.

## Running Queries

Use the following command to query the OEPS BigQuery tables:

    python oeps_backend/bq_query.py --sql-file oeps_backend/example_queries/states.sql --output states.shp

Where `states.sql` is an example of a file that holds the SQL query to perform against one or more tables. In the SQL, `PROJECT_ID` is a placeholder (it will be replaced with the actual project identifier before the query is performed), such that table references look like `PROJECT_ID.dataset_name.table_name`, or `PROJECT_ID.spatial.states2018` for the table that holds state boundaries.

- `--sql-file` path to a file whose contents is a complete SQL query. 
- `--output` is the name of a file to which the query results will be written. Either .csv or .shp files can be specified, and if a spatial result is written to CSV the geometries will be in WKT format. If this argument is omitted, the query results will be printed to the console (helpful for testing queries).

## contribution workflow

For contributions we'll use a standard branching pattern--make a new branch from `main`, add commits to it, and then create a pull request to get those changes merged back into `main`.

In the command line, this would look like the following steps. (VSCode and other editors have great git integrations as well, but the steps are generally the same):

1. Make sure you are on the main branch locally

        git branch

2. Create a new branch from `main`

        git checkout -b your_new_branch_name

    You will now be on a new branch, as `git branch` will show you.

3. Change code, add commits

        git add path/to/your/new_file
        git commit -m "short description of the change you made"

    If you are addressing an open ticket with your commit, say ticket number 10, you should add `#10` to your commit message, like

        git commit -m "update file list for initialization #10"

4. Push your branch to the GitHub repo

        git push --set-upstream origin your_new_branch_name

5. Create the [Pull Request](https://github.com/healthyregions/pulls) in GitHub, including a description of the changes your branch contains.