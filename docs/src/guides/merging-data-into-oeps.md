# Merging Data into OEPS

Once a CSV has been prepared and its metadata updated, then it is time to merge it into the OEPS data ecosyetem. This process does two things:

1. Merges columns from the incoming CSV into the specified matched CSV (i.e. table_source)
2. Updates the JSON registry content to record the fact that new data has been added to the system

The best way to prepare for this action, is run the merge command with the dry-run option.

```shell
flask merge-csv -s path/to/incoming.csv -t target-table-source --dry-run
```

This command will output a summary of what will happen through the merge process, and a list of columns that will be incorporated into OEPS. If columns are marked to be skipped that should be added, this means there is no variable in the registry for that column, and one must be added before moving on.

!!! tip "What table source should I target?"
    The target "table source" is the meta-identifier for the existing CSV that the incoming data will be merged into. Find a table source that matches these aspects of the incoming CSV:

    - `data_year`: The year of the incoming CSV data must match the `data_year` of the table source
    - `geodata_source`: What vintage and geography of census data should the incoming data be joined to? There must be an appropirate geodata source to match with.

## Registry preparation

After the data has been prepared, the registry must also be prepared. The best way to do this is by asking these questions:

### Is there a geodata target for this data already in the registry?

If the new data must be joined to 2020 county boundaries, for example, is there already a `geodata-source` for that geography and vintage? Check [current content](../registry/current-content.md) to see what is already registered.

- If yes, great! Proceed to next question.
- If not, you need to [create a new geodata source](#create-a-new-geodata-source) before continuing.

### Is there an existing table source that matches the year and geography of the incoming data?

If the new CSV contains county-level data for 2021, then is there already a table source with `data_year: 2021` and the proper vintage of county-level geodata in the registry?

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
- If no, you need to [create a new variable entry](creating-metadata-and-variables.md#creating-a-new-variable-entry) for every new incoming variable.

## Workflow

Listed here in logical order, though often only the later steps will be needed.

- [Create a new geodata source](#create-a-new-geodata-source)
- [Create a new table source](#create-a-new-table-source)
- [Merge data into OEPS](#merge-data-into-oeps)
- [Next steps](#next-steps)

### Create a new geodata source

A [geodata source](../registry/data-model.md#geodata-sources) is a JSON file that points to one of the zipped shapefiles we have in our [geodata.healthyregions.org](https://geodata.healthyregions.org) S3 storage system. If you need a new geography level and/or vintage that is not already in S3, see [github.com/healthyregions/geodata](https://github.com/healthyregions/geodata) to learn how to create and add it to the bucket.

To create a new geodata source in the registry, add a new JSON file named `<summary level>-<year>.json`. Using 2010 county boundaries as an example, name the file `counties-2010.json` and its content will look like this:

```
{
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

!!! tip
    See [geodata sources](../registry/data-model.md#geodata-sources) for a full explanation of geodata sources.

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
    See [table sources](../registry/data-model.md#table-sources) for a full explanation of table sources.

### Merge data into OEPS

Once both the incoming data and the registry have been prepared, you can merge in an external CSV with this command, using a new set of county-level 2021 data as an example.

```
flask merge-csv -s path/to/MyNewCountyData2021.csv -t county-2021 --dry-run
```

It is wise to use the `--dry-run` flag to test the merge before actually altering any data.

What this command will do:

1. Load the incoming CSV data, and check for a join field (`GEOID`, `FIPS`, `ZCTA5`, or `HEROP_ID`)
    - If one of these is present, it will be used to generate a `HEROP_ID` which is the actual join field that will be used during the process
2. Load the specified table source CSV in the registry and merge these two data frames
3. Write out the merged data frame into the existing table source
4. Update the `table_sources` attribute in `varibles.json` for variable in the incoming CSV

## Next steps...

Once you have completed this operation for one or more CSVs, you will need to perform some or all of these actions to make sure the derived output from OEPS is up-to-date.

Update content in the OEPS Explorer

- [Re-provision the OEPS Explorer](./provisioning-oeps-explorer.md)

Because changes have been made to data and the registry:

- [Regenerate documentation derived from content](./generating-derived-documentation.md)

Google BigQuery tables should be updated:

- [Sync data to BigQuery](./interacting-with-bigquery.md#uploading-tables)

!!! warning
    The Google BigQuery process has not been updated since recent data model changes and may not be fully functional.

If data has been added that needs to be included in existing data packages:

- [Re-create data packages](./creating-data-packages.md)

