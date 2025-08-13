# Adding Data to OEPS

Because the OEPS backend must export the same data to many different formats, we have a [registry](../registry/index.md) that configures and manages all of the data within the system. The data itself is stored across many different CSV files, while a set of JSON files hold descriptive information about these CSV files and how they relate. Finally, a set of a "geodata sources" provide base geometries to which any of the data CSVs can be joined.

With these pieces in mind, adding new data to OEPS is a multi-step process.

[TOC]

## Data preparation

Incoming data:

1. MUST be stored CSV format
2. MUST contain values for only one year and only one geography level
3. MUST have proper column names (see below)
4. MUST include an appropriate join column (see below)
5. MAY have data for as many different variables as needed

### Naming columns

If you are adding values for a variable that already exists in the registry, say, "Total Population", then your column must have the exact name that we already use for that variable, `TotPop`.

If you are adding values for a new variable, then your columns must follow our existing naming conventions, and you'll need to [create a new entry for that variable](#create-a-new-variable-entry) as described below.

### Configuring a join column

A join column serves as the linkage between the non-spatial CSV data and geographic data like county boundaries. To facilitate this linkage, any incoming CSV must have one of these columns:

Name|Geography|Description
-|-|-
`GEOID`|all|For state, county, and tract data the `GEOID` is equivalent to the `FIPS` id. For ZCTA data, `GEOID` can match the zip code or `ZCTA5` for each ZCTA.
`FIPS`|state, county, tract|`FIPS` ids are nested such that, for example, the 5-digit `FIPS` for a county includes the 2-digit `FIPS` for its state.
`ZCTA5`|zcta|5-digit zip code that corresponds with the zip code tabulation area.
`HEROP_ID`|all|A `HEROP_ID` is our version of `GEOID`, which also includes a "summary-level" code on the front of it, indicating what geography level the id refers to.


## Registry preparation

After the data has been prepared, the registry must also be prepared. The best way to do this is by asking these questions:

### Is there a geodata target for this data already in the registry?

If the new data must be joined to 2020 county boundaries, for example, is there already a `geodata-source` for that geography and vintage?

- If yes, great! Proceed to next question.
- If not, you need to [create a new geodata source](#create-a-new-geodata-source) before continuing.

### Is there an existing table source that matches the year and geography of the incoming data?

If the new CSV contains county-level data for 2021, then is there already a `county-2021` table source in the registry?

- If yes, great! Proceed to next question.
- If not, you need to [create a new table-source](#create-a-new-table-source) before continuing.

### Are all columns in the incoming data already defined in the OEPS registry?

You can check this with the following command:

```
flask inspect-csv -s path/to/MyNewCountyData2021.csv
```

!!! note
    You can run this command on a directory as well, and every CSV within it will be inspected.

- If yes, great! You are ready to [merge data into OEPS](#merge-data-into-oeps).
- If no, you need to [create a new variable entry](#create-a-new-variable-entry) for every new incoming variable.

## Workflow

Listed here in logical order, though often only the later steps will be needed.

- [Create a new geodata source](#create-a-new-geodata-source)
- [Create a new table source](#create-a-new-table-source)
- [Create a new variable entry](#create-a-new-variable-entry)
- [Create a new theme or construct](#create-a-new-theme-or-construct)
- [Merge data into OEPS](#merge-data-into-oeps)

### Create a new geodata source

A [geodata source](../registry/geodata-sources.md) is a JSON file that points to one of the zipped shapefiles we have in our [geodata.healthyregions.org](https://geodata.healthyregions.org) S3 storage system. If you need a new geography level and/or vintage that is not already in S3, see [github.com/healthyregions/geodata](https://github.com/healthyregions/geodata) to learn how to add it.

To create a new geodata source, add a new JSON file named `<summary level>-<year>.json`. Using 2010 county boundaries as an example, name the file `counties-2010.json` and its content will look like this:

```
{
    "bq_dataset_name": "spatial",
    "bq_table_name": "counties2010",
    "name": "counties-2010",
    "title": "County Boundaries, 2010",
    "description": "Shapefile of county boundaries from the US Census Bureau, 2010.",
    "path": "https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2010-500k-shp.zip",
    "format": "shp",
    "mediatype": "application/vnd.shp",
    "summary_level": "county",
    "schema": {
        "primaryKey": "HEROP_ID",
        "fields": [
            {
                "name": "HEROP_ID",
                "title": "HEROP_ID",
                "type": "string"
            }
        ]
    }
}
```

!!! note
    Currently, we use plurals in geodata-source names, "counties", instead of "county" which we use elsewhere. In the future, geodata source definitions will not use plural.

!!! note
    The bq* attributes are used for Google BigQuery, and are likely to be removed in the future.

!!! tip
    See [geodata sources](../registry/geodata-sources.md) for a full explanation of geodata sources.

### Create a new table source

The following command can be used to create a new table source:

```
flask create-table-source -n <name> -g <geodata-source>
```

For example, to add a new table source to hold county-level data for the year 2021 (which will join to 2020 geometries) use this command:

```
flask create-table-source -n county-2021 -g counties-2020
```

This command will do two things:

1. Using the specified geodata-source, create a "dummy" CSV in `data/tables` named `county-2021.csv` that only contains join columns--essentially a placeholder file into which new data can be merged
2. Create a new JSON file for this table-source, `registry/table-sources/county-2021.json` that adds the new CSV to the registry.

!!! tip
    See [table sources](../registry/table-sources.md) for a full explanation of table sources.

### Getting started with PagesCMS

Some elements of the registry can be directly edited through an online interface called PagesCMS. Here's how you can get started with this.

1. Go to [app.pagescms.org/healthyregions/oeps/main](https://app.pagescms.org/healthyregions/oeps/main)
2. Sign in with GitHub if needed
3. Once logged in, you'll see `oeps` and `main` in the left-hand menu
    - Click this button and go to > "Manage branches"
4. Create a new branch with a descriptive name, `add_my_new_variable`
    - You'll now see `oeps` and `add_my_new_variable` in the left-hand menu
5. Perform the edits you need to do
    - All work will be committed directly to your new branch.
6. When you are ready, go to the actual GitHub repo, https://github.com/healthyregions/oeps/pulls, and create a new pull request into main from your branch.

### Create a new variable entry

In `registry/variables` there are individual files for each variable with data in OEPS. Instead of editing these files directly, we can edit them through PagesCMS.

See [getting started with PagesCMS](#getting-started-with-pagescms) to continue.

Some data entry notes:

- `name` must follow these rules:
    - Follow abbreviation patterns we already use
    - Follow [PascalCase](https://pascal-case.com/)
        - For example, use `TotPop`, not `tot_pop` or `totPop` or `tot-pop`
- `type` must be one of:
    - `number` for any decimal number values
    - `integer` for any integer values
    - `string` for text values, for example a coded entry
    - `boolean` for true/false or yes/no values
    - `date` for date values
    - see [Frictionless field data types](https://specs.frictionlessdata.io/table-schema/#types-and-formats) for more info
- `table_sources` leave this blank, it should not be edited in PagesCMS.

!!! tip
    See [variables](../registry/variables.md) for a full explanation of variables.

### Create a new metadata entry

In `registry/metadata` there are individual files for each metadata entry. Instead of editing these files directly, we can edit them through PagesCMS.

!!! note
    The actual metadata markdown files themselves are stored at the top of the main repo, in `/metadata`. In the future, we could further integrate them with the registry so that these files are also edited directly in PagesCMS.


To add a new metadata entry, you should begin the process in GitHub by creating a new branch and added a new markdown file to in this directory: https://github.com/healthyregions/oeps/tree/main/metadata. Create your file based on https://github.com/healthyregions/oeps/tree/main/metadata/metadata-template.md.

With your markdown file complete, you need to create an entry for it in PagesCMS. See [getting started with PagesCMS](#getting-started-with-pagescms), and be sure to use the branch you have already created (no need to make a new one).

Once the new metadata entry has been created, you can also attach new variables to it if needed.

After a pull request has been merged into the main branch, this command will need to be run to update the docs page in the OEPS Explorer:

```
flask build-explorer-docs
```

!!! tip
    See [metadata](../registry/metadata.md) for a full explanation of metadata entries.

### Merge data into OEPS

Once both the incoming data and the registry have been prepared, you can merge in an external CSV with this command, using a new set of county-level 2021 data as an example.

```
flask merge-data-table -s path/to/MyNewCountyData2021.csv -t county-2021 --dry-run
```

It is wise to use the `--dry-run` flag to test the merge before actually altering any data.

What this command will do:

1. Load the incoming CSV data, and check for a join field (`GEOID`, `FIPS`, `ZCTA5`, or `HEROP_ID`)
    - If one of these is present, it will be used to generate a `HEROP_ID` which is the actual join field that will be used during the process
2. Load the specified table source CSV in the registry and merge these two data frames
3. Write out the merged data frame into the existing table source
4. Update the `table_sources` attribute in `varibles.json` for variable in the incoming CSV

Once you have completed this operation for one or more CSVs, you will need to perform some or all of these actions to make sure the derived output from OEPS is up-to-date:

- [Re-provision the OEPS Explorer](./provisioning-oeps-explorer.md)
- [Re-create any output data packages](./creating-data-packages.md)
- [Regenerate data dictionaries](./generating-derived-documentation.md#data-dictionaries)
- [Regenerate the registry summary](./generating-derived-documentation.md#registry-summary)
- [Sync data to BigQuery](./interacting-with-bigquery.md#uploading-tables)
- [Regenerate the BigQuery reference table](./generating-derived-documentation.md#bigquery-table-schemas)