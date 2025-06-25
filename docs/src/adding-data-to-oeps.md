# Adding Data to OEPS

Because the OEPS backend must export the same data to many different formats, we have a [registry](./registry.md) that configures and manages all of the data within the system. The data itself is stored across many different CSV files, while a set of JSON files hold descriptive information about these CSV files and how they relate. Finally, a set of a "geodata sources" provide base geometries to which any of the data CSVs can be joined. With these pieces in mind, adding new data to OEPS has a few steps, and the first is preparation.

## Data preparation

Incoming data must:

1. Be stored CSV format
2. Contain values for only one year and only one geography level
    - For example, state-level population data for 1980, or tract-level housing data for 2018
4. Have proper column names (see below)
3. Include an appropriate join column (see below)

### Naming columns

If you are adding values for a variable that already exists in the registry, say, "Total Population", then your column must have the exact name that we already use for that variable, `TotPop`.

If you are adding values for a new variable, then your columns must follow our existing naming conventions, and you'll need to [supply extra information](#defining-new-variables) about that variable separately

### Configuring a join column

A join column serves as the linkage between the non-spatial CSV data and geographic data like county boundaries. To facilitate this linkage, any incoming CSV must have one of these columns:

- `GEOID`
    - For state, county, and tract data the `GEOID` is equivalent to the `FIPS` id. For ZCTA data, `GEOID` can match the zip code for each ZCTA.
- `FIPS` (for state, county, or tract data)
    - `FIPS` ids are nested such that, for example, the 5-digit `FIPS` for a county includes the 2-digit `FIPS` for its state.
- `ZCTA5` (for zip-code tabulation area (ZCTA) data)
    - A `ZCTA5` field is (essentially) the same as normal zip codes.
- `HEROP_ID`
    - A `HEROP_ID` is our version of `GEOID`, which also includes a "summary-level" code on the front of it, indicating what geography level the id refers to.

## Registry preparation

After the data has been prepared, the registry must also be prepared. The best way to do this is by asking these questions:

### 1. Is there a geodata target for this data already in the registry?

If the new data must be joined to 2020 county boundaries, for example, is there already a `geodata-source` for that geography and vintage?

- If yes, great! Proceed to next step.
- If not, you need to [create a new geodata source](#create-a-new-geodata-source) before continuing.

### 2. Is there an existing table source that matches the year and geography of the incoming data?

If the new CSV contains county-level data for 2021, then is there already a `county-2021` table source in the registry?

- If yes, great! Proceed to next step.
- If not, you need to [create a new table-source](#create-a-new-table source) before continuing.

### 3. Are all columns in the incoming data already defined in the OEPS registry?

You can check this with the following command:

```
flask inspect-csv -s path/to/MyNewCountyData2021.csv
```

> **Note:** You can run this command on a directory as well, and every CSV within it will be inspected.

- If yes, great! You are ready to [merge data into OEPS](#merge-data-into-oeps).
- If no, you need to [create a new variable entry](#create-a-new-variable-entry) for every new incoming variable.

## Registry operations

Presented in logical order, though often only the later steps will be needed.

- [Create a new geodata source](#create-a-new-geodata-source)
- [Create a new table source](#create-a-new-table-source)
- [Create a new variable entry](#create-a-new-variable-entry)
- [Create a new construct](#create-a-new-construct)
- [Merge data into OEPS](#merge-data-into-oeps)

### Create a new geodata source

A geodata-source is a JSON file that points to one of the shapefiles we have in our [geodata.healthyregions.org](https://geodata.healthyregions.org) storage system. If you need a new geography level and/or vintage that is not already in the 

To create a new geodata-source, add a new JSON file named `<summary level>-<year>.json`. Using 2010 county boundaries as an example, name the file `counties-2010.json` and its content will look like this:

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

> **Note:** Currently, we use plurals in geodata-source names, "counties", instead of "county" which we use elsewhere. In the future, geodata source definitions will not use plural.

> **Note:** The bq* attributes are used for Google BigQuery, and are likely to be removed in the future.

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

> **Note:** Currently, we use plurals in geodata-source names, "counties", instead of "county" which we use elsewhere. In the future, geodata source definitions will not use plural.

### Create a new variable entry

In `registry/variables.json` there is a single entry for each variable that has values for any geography level or any year within OEPS. Currently, adding new variables is a manual process, just directly edit the content of that file. A full variable definition looks like this:

```
"TotPop": {
    "title": "Total Population",
    "name": "TotPop",
    "type": "integer",
    "example": "1632480",
    "description": "Total population",
    "constraints": "1980-2000 historic data was acquired from NHGIS and then interpolated to modern county boundaries through a population weighted interpolation using the tidycensus `interpolate_pw` function. For 1980, the underlying population weighting was county subdivisions, while for 1990 and 200 the underlying population weighting was tracts.",
    "construct": "Population",
    "source": "ACS 2018, 5-Year; Census 2010; IPUMS NHGIS",
    "source_long": "American Community Survey 2014-2018 5 Year Estimate; 2010 Decennial Census; Integrated Public Use Microdata Series National Historic Geographic Information System",
    "comments": "",
    "metadata_doc_url": "https://github.com/GeoDaCenter/opioid-policy-scan/blob/main/data_final/metadata/Age_2018.md",
    "table_sources": []
}
```

Some notes on a few of these properties:

- The top-level key and `name` for this variable must be identical, and must follow these rules:
    - Follow abbreviation patterns we already use
    - Follow [PascalCase](https://www.techopedia.com/definition/pascal-case): Use `TotPop`, don't use `tot_pop` or `totPop` or `tot-pop`
- `type` must be one of:
    - `number` for any decimal number values
    - `integer` for any integer values
    - `string` for text values, for example a coded entry
    - `boolean` for true/false or yes/no values
    - `date` for date values
    - see [Frictionless field data types](https://specs.frictionlessdata.io/table-schema/#types-and-formats) for more info
- `construct` must match the name of a construct in the `themes.json` file. If you are adding a variable that part of a new construct, then you must also [create a new construct](#create-a-new-theme-or-construct).
- `table_sources` must start as an empty list, and will fill up with the names of table sources that hold values for this variable, as more and more data is merged into the system.

### Create a new theme or construct

OEPS is built on a conceptual framework that places different measures (or, "variables") into different themes and constructs. This grouping is defined in the `registry/themes.json` file, which lists "themes" at the top-level and then nests one or more constructs within each theme.

To add a new construct or theme, just edit that file directly. Once you are finished, you'll need to regenerate the docs content for the OEPS explorer.

```
flask build-explorer-docs
```

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

Once you have completed this operation for one or more CSVs, you will (eventually) need to regenerate the many various data outputs needed to push these updates to all OEPS venues.

You can read more about this in [Exporting Data from OEPS](./exporting-data-from-oeps.md).