# OEPS Backend

This project builds from the Opioid Environment Policy Scan (OEPS) data warehouse stored in [github.com/GeoDaCenter/opioid-policy-scan](https://github.com/GeoDaCenter/opioid-policy-scan), and published on Zenodo at [doi.org/10.5281/zenodo.5842465](https://doi.org/10.5281/zenodo.5842465).

The backend includes [commands](./reference/commands/README.md) for managing data transformation to and from to different destinations, as well as a [registry](./registry.md) to define all aspects of the data within OEPS.

## Getting Started

### Install the backend Python Package

1. Clone this repo

        git clone https://github.com/healthyregions/oeps
        cd oeps/backend

2. Create and activate a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) with [venv](https://docs.python.org/3/library/venv.html), [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), or your other tool of choice.

    For example, using the `venv` module that is included in Python 3, the commands will be:

        python3 -m venv env
        source ./env/bin/activate

    This will create a new directory `env/`, and when properly activated your command prompt will have a `(env)` prefix.

3. Install this package and its dependencies

        pip install -e .

4. Create a `.env` file from the provided template (no need to update any values right now)

        cp .env.example .env

5. You can now run any commands with

        flask [command]

    To see what commands are available, run

        flask --help

    You should see a printout that lists about 10 commands.

    > If you only see three commands (`routes`, `run`, and `shell`): These are default flask commands and you either need to activate your virtual environment or make sure you have a `.env` file with `FLASK_APP=oeps` in it.

6. (for development only)

        pip install -e .[dev]
        pip install md-click@git+https://github.com/kid-116/md-click@support-arguments

    The `md-click` library is used to generate documentation of the CLI commands, and the
    particular branch is needed to handle Arguments on the commands that are being documented.
    Hopefull, this PR will be merged at some point and this install process could be updated:
    https://github.com/RiveryIO/md-click/pull/12.

    There is a dependency resolution bug (or something) when putting that github reference 
    directly in the `pyproject.toml` file, so it needs to be run separately after everything
    else is installed.

## JCOIN

*section in progress*

## Google BigQuery

### Setup BigQuery Credentials

To use the BigQuery script (`scripts/bq.py`) you will need to add access credentials as environment variables using the `.env` file. This file must always stay out of version control.

- Make a copy of `.env.example` and name it `.env`. Any variables defined in this file will now be available via `os.getenv('VARIABLE_NAME')`

- Obtain a set of JSON credentials for the project, and store the file anywhere on your computer (but outside of this repository).

- In your `.env` file, update the `BQ_CREDENTIALS_FILE_PATH` variable with the full path to this file. For example:

    ```
    BQ_CREDENTIALS_FILE_PATH="/home/my_username/bq_credentials/oeps-391119-5783b2b59b83.json"
    ```

- It is also possible to set BigQuery credentials without storing a local JSON file. More info on this is in the `.env.example` file.

Once you have setup these credentials, you can test them with

    python ./scripts/bq.py check-credentials

If all is well, the command will print `ok`.

## BigQuery Import/Export

The `bq.py` script can perform import and export operations on our BigQuery database.

### Importing Data

Use the following command to load a new table into BigQuery:

    python ./scripts/bq.py load --source ./resources

Where `--source` is the path to a Data Resource schema (stored as JSON file), or a directory containing multiple Data Resource schemas. Optional flags on this command are:

- `--table-only` will create the BigQuery dataset and table based on the schema, but will not attempt to load data into it.
- `--dry-run` will validate the input dataset against the schema, but not attempt to load it.
- `--overwrite` will drop and recreate the BigQuery table if it already exists in the dataset.

### Exporting Data

Use the following command to query the OEPS BigQuery tables:

    python scripts/bq.py export --sql sql/states.sql --output states.shp

Where `states.sql` is an example of a file that holds the SQL query to perform against one or more tables. In the SQL, `PROJECT_ID` is a placeholder (it will be replaced with the actual project identifier before the query is performed), such that table references look like `PROJECT_ID.dataset_name.table_name`, or `PROJECT_ID.spatial.states2018` for the table that holds state boundaries.

- `--sql-file` path to a file whose contents is a complete SQL query. 
- `--output` is the name of a file to which the query results will be written. Either .csv or .shp files can be specified, and if a spatial result is written to CSV the geometries will be in WKT format. If this argument is omitted, the query results will be printed to the console (helpful for testing queries).

You can write your own SQL into a file and use the same command to perform your query and export the results.

Use the [big-query-tables](./reference/big-query-tables.md) page for quick access to all table and column names.

### Table Definitions

A **table definition** is a JSON file that specifies

1. The location of a source dataset to load
2. The Google BigQuery project and table name to load into
3. A thorough schema defining all fields from the source dataset and how they will be stored in BigQuery

This information is used in various contexts to

1. Create (or re-create) table schemas in BigQuery
2. Load data into these tables
3. Export data from BigQuery into various formats and file types

The structure of a table definition is inspired by the [Table Schema](https://specs.frictionlessdata.io/table-schema) specification published by [Frictionless Standards](https://specs.frictionlessdata.io), with a few additions for our own use case.

#### Structure

The top-level properties of a table definition are:

Property|Format|Description
-|-|-
`path`|String|Path or URL for CSV or SHP dataset to load
`bq_table_name`|String|Target table in BigQuery
`bq_dataset_name`|String|Target dataset in BigQuery
`fields`|List|List of definitions for all table fields

Note that in BigQuery, a `dataset` is akin to a database in other RDBS implementations, such that a dataset holds one or more tables. Often, tables are identified by their fully-qualified identifier: `project_id.dataset_name.table_name`.

The `fields` property is a list of one or more field objects, as described below. The only requirement of the `fields` list is that **must** contain an entry for a [`HEROP_ID`](#herop_id-field) field. This is our unique GIS join field.

#### Field Descriptors

Fields are defined by a JSON object that adheres to the [field descriptors](https://specs.frictionlessdata.io/table-schema/#field-descriptors) portion of the table schema standard, though not all possible attributes are required or implemented.

Property|Format|Description|OEPS Use
-|-|-|-
`name`|String|Canonical name for this column (used in BigQuery)|Required
`title`|String|A nicer human readable label or title for the field|Required
`type`|String|A string specifying the type. See [types](https://specs.frictionlessdata.io/table-schema/#types-and-formats).|Required
`format`|String|A string specifying a format|Not Implemented
`example`|String|An example value for the field|Optional
`description`|String|A description for the field|Optional
`constraints`|JSON|A [constraints descriptor](https://specs.frictionlessdata.io/table-schema/#constraints)|Not Implemented

The following additional attributes are also supported and in some cases required:

Property|Format|Description|OEPS Use
-|-|-|-
`theme`|String|One of `Social`, `Environment`, `Economic`, `Policy`, `Outcome`, or `Geography`. See [OEPS docs](https://oeps.healthyregions.org/docs).|Optional
`comment`|String|Additional information about the data in this field|Optional
`source`|String|Source of the data in this field|Optional
`max_length`|Integer|Max length of field (used in BigQuery schema)|Optional

#### HEROP_ID Field

For now, please see [this comment](https://github.com/GeoDaCenter/opioid-policy-scan/issues/68#issuecomment-1701863572) for a detailed description of how `HEROP_ID` values are constructed.

A field descriptor for this field will look something like this:

```
{
    "name": "HEROP_ID",
    "type": "string",
    "example": "040US01-2018",
    "description": "A derived unique id corresponding to the relevant geographic unit.",
    "theme": "Geography",
}
```

#### Geometry Fields

To load a shapefile you must include the following field descriptor in your `fields` list:

```
{
    "name": "geom",
    "title": "Geom",
    "type": "string"
}
```

Note that for spatial data Table Schema only allows `geojson` or `geopoint` as valid geographic types, while Google BigQuery uses `GEOGRAPHY`. For now, we'll just use the above configuration, and more nuances can be pursued down the road. 

#### Example

The following is a truncated version of a table definition for the 2010 State-level data published in OEPS v2.0. This defines a table `project_id.tabular.S_2010` with two fields, `HEROP_ID` and `TotPop`. Note also the direct URL to the raw `path` on GitHub.

```
{
    "bq_dataset_name": "tabular",
    "bq_table_name": "S_2010",
    "path": "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/full_tables/S_2010.csv",
    "fields": [
        {
            "name": "HEROP_ID"
            "type": "string",
            "description": "A derived unique id corresponding to the relevant geographic unit.",
            "constraints": null,
            "theme": "Geography"
        },
        {
            "name": "TotPop"
            "type": "integer",
            "example": "7294336",
            "description": "Estimated total population",
            "constraints": null,
            "theme": "Social",
            "source": "American Community Survey 2014-2018 5 Year Estimates; 2010 Decennial Census; Integrated Public Use Microdata Service National Historic Geographic Information Systems",
            "comments": "1980, 1990, and 2000 data from respective decennial censuses downloaded from IPUMS NHGIS and aggregated upwards."
        }
    ]
}
```
