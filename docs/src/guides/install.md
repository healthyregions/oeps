# Installation

The OEPS Explorer, OEPS Backend (which contains the registry), and this set of documentation each live in different directories of the same repository: [github.com/healthyregions/oeps](https://github.com/healthyregions/oeps). Each component operates independently, so there is no need to install them all at once.


To begin, clone the repo locally,

```shell
git clone https://github.com/healthyregions/oeps
```

then you can install any of the following components:

- [OEPS Explorer](#oeps-explorer)
- [OEPS Backend](#oeps-backend)
- [Documentation Site](#documentation-site)

## OEPS Explorer

To get started locally with the explorer:

```

cd oeps/explorer
yarn install
cp .env.example .env
```

Some environment variable values will already be set in `.env`, but you'll need to add a Mapbox token. Then run

```
yarn dev
```

and open `http://localhost:3000`

### More about Mapbox dependencies

Two Mapbox Tilesets must be configured externally and linked within this app, one for Zip Code Tabulation Areas (ZCTAs) and one for Census Tracts. These geometries are joined with CSV tables to drive map visualizations.

Additionally, a basemap style must be provided, as well as a Mapbox access token. All of these elements are (currently) provided through environment variables, so make sure your `.env` file has the following:

```
NEXT_PUBLIC_MAPBOX_TOKEN=<your token>
NEXT_PUBLIC_MAPBOX_STYLE="mapbox://styles/<account id>/<style id>'
```

## OEPS Backend

### Install Python dependencies

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

Success! To test your install, run:

```shell
flask --help
```

You should see a printout that lists about 10 commands.

!!! note
    If you only see three commands (`routes`, `run`, and `shell`), then you either need to activate your virtual environment or make sure you have a `.env` file with `FLASK_APP=oeps` in it. (These three are default Flask commands.)

You can now head to [Getting Started with the CLI](./getting-started-with-cli.md) to learn more about using these commands.

### Dev dependencies

If you are contributing code or otherwise developing on this code base, use the following commands to install dev dependencies

```shell
pip install -e .[dev]
pip install md-click@git+https://github.com/kid-116/md-click@support-arguments
```

!!! warning
    The `md-click` library is used to generate documentation of the CLI commands, and the particular branch is needed to handle Arguments on the commands that are being documented. Hopefully, this PR will be merged at some point and this install process could be updated: https://github.com/RiveryIO/md-click/pull/12.<br/><br/>There is a dependency resolution bug (or something) when putting that github reference directly in the `pyproject.toml` file, so it needs to be run separately after everything else is installed.

### Docs dependencies

The [documentation site](#documentation-site) (which you are reading right now!) is built with dependencies that are best installed directly into the backend virtual environment, so may as well install them now:

```shell
pip install -e .[docs]
```

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

## Documentation Site

This documentation content is built with [mkdocs](https://www.mkdocs.org/) and hosted on Github pages. It is easiest to install the documentation dependencies directly into the backend's Python virtual environment, as [described above](#docs-dependencies). Once that is completed, enter the docs directory and run mkdocs commands from there.

To view the docs locally:

```shell
cd oeps/docs
mkdocs serve
```

Visit http://localhost:8000 for a live preview of the docs content, and make changes to Markdown files in `/docs/src`.

!!! tip
    Keep in mind that _some_ documentation content, like the command specs reference, is autogenerated by backend commands so those files should not be edited directly.

To build and publish the docs:

```shell
mkdocs build
```

Updated content is now in `/docs/output`. Commit these changes and push to Github to rebuild the public site.
