# Adding Data to OEPS

Because the OEPS backend must export the same data to many different formats, we have a [registry](./registry.md) that configures and manages all of the data within the system.

## Overview

It is important to understand how a few terms are used:

term|definition
---|---
variable|A definition of a data point that is stored in OEPS. A variable can have values at different geographic scales (state, county, etc.) as well as different years (2010, 2020, etc.).
table source|A structured description of a CSV that holds data values for one or more variables. Each table source must hold data for only one year, and only one geography.

For a detailed description of how the entire data registry is put together, see [registry.md](./registry.md).

With this in mind, the most first consideration to begin with is:

### Am I adding data for new or existing variables?

You can see a full list of all variables that are already in the system here: [all-content.md](./reference/registry/all-content.md)

_If you are adding data for existing variables, the variable names in your CSV (column headers) must exactly match the existing variable names in registry._

#### Scenario 1:

> I am adding historical data for 1970, for standard variables like "Total Population" that already exist in the system.

If your data only contains new values for variables that are already in OEPS, then the process will look like this:

- Create a new **table source** that references your CSV
  - [Create a table source &rarr;](#create-a-table-source)
- Add that new table source to the `table_sources` field for the existing Total Population **variable**
  - [Add a table source to a variable &rarr;](#add-a-table-source-to-a-variable)

#### Scenario 2

> I have a CSV with a new variable, "English Proficiency" in 2018 at the county level.

In this case, the new variable "English Proficiency" must be defined in the registry before we can add the new data to it.

- Define a new **variable** called "English Proficiency" in the variables list
  - [Define a new variable &rarr;](#define-a-new-variable)

After the new variable is defined, you can head up to the steps in [Scenario 1](#scenario-1).

Keep in mind, you can will most likely be adding multiple new variable values at once, and they can all live in the same CSV. You can also add a CSV that has values for new variables _as well as_ existing variables. A scenario in which this could happen is as follows:

> I have created a new CSV for county level in 2017. This CSV includes values for a number of standard variables, like "Total Population", but also has a few new variables that now only exist for 2017.

In this scenario, just add all of the new variables first before heading back up to [Scenario 1](#scenario-1).

---

The rest of this document has more information on how to carry out each step.

## Create a table source

Every table source is defined through its own JSON file in the registry. A table source:

- References a single CSV
- Must only contain data for a single year
- Must only contain data for a single geography (state, county, tract, ZCTA)
- Must have a `HEROP_ID` field, this is how its data gets connected to spatial data

Steps to cover while creating a table source.

### Create a HEROP_ID field

`HEROP_ID` is basically just a FIPS or GEOID with a prefix, different prefixes correspond to different geographies. See the [Geographic Boundaries metadata document](https://github.com/GeoDaCenter/opioid-policy-scan/blob/main/data_final/metadata/GeographicBoundaries.md) for a full explanation.

### Upload to web accessible location

Upload the CSV to something like GitHub or even Google Drive. Get the publicly accessible URL for it.

### Define properties

_We don't have a formal way of submitting this information yet, but the first thing to do is collect it..._

- `name`: A lower-case name without spaces that is unique across all table sources (this will be the JSON file name as well)
- `summary_level`: Geography to join to, this must be `state`, `county`, `tract`, or `zcta`
- `geodata_source`: The name of the **geodata_source** to join to
  - Generally speaking this, matches with the `summary_level` but we do have two different vintages you can choose from. Use 2010 for any pre-2018 data, and 2018 for table sources from 2018 and later
- `path`: Publicly accessible URL for the CSV dataset

There are more properties, but these can be derived down the road.

<details>
  <summary>Show full example</summary>
  <pre>
  {
    "bq_dataset_name": "tabular",
    "bq_table_name": "C_1980",
    "name": "c-1980",
    "path": "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/full_tables/C_1980.csv",
    "format": "csv",
    "mediatype": "text/csv",
    "title": "OEPS Data Aggregated by County (1980)",
    "description": "This CSV aggregates all 1980 data variables from the OEPS v2 release at the Census Tract level.",
    "year": "1980",
    "geodata_source": "counties-2010"
}
</pre>
</details>

## Define a new variable

All variables are defined in a single file, `backend/oeps/registry/variables.json` so adding a new variable to the system requires a new entry in that file.

### Create a metadata document

One thing each variable should have is a metadata file in Github. Here are [all our existing metdata files](https://github.com/GeoDaCenter/opioid-policy-scan/tree/main/data_final/metadata) for context. A metadata file should describe the process through which a variable was acquired, as well as the original source. Some notes on the metadata documents:

- Some of this info will also be stored in the variable properties described below, but it the metadata document offers a lot of flexibility and narration that the properties do not.
- One metadata file must suffice for **every year or geography** of a variable.

### Define properties

_We don't have a formal way of submitting this information yet, but the first thing to do is collect it..._

- `name`: A name that 
- `summary_level`: Geography to join to, this must be `state`, `county`, `tract`, or `zcta`
- `geodata_source`: The name of the **geodata_source** to join to
  - Generally speaking this, matches with the `summary_level` but we do have two different vintages you can choose from. Use 2010 for any pre-2018 data, and 2018 for table sources from 2018 and later
- `path`: Publicly accessible URL for the CSV dataset
- `construct`: What construct (a subset of "theme") that this variable fits into
  - You may need to update the proxy for the construct now that you've added a new variable to it)

<details>
  <summary>Show full example</summary>
  <pre>
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
    "table_sources": ["c-1980", "s-latest", "t-2010", "t-latest", "s-2000", "t-2000"]
  }
</pre>
</details>

## Add a table source to a variable

### Update the `table_sources` field

- Find the table source `name` that you are adding for a variable. This will be a lower-case, no spaces, identifier like `c-1980`.
- Find the variable entry, say `TotPop` in `variables.json` and add the table source `name` to the `table_sources` property of the entry.

This process tells the system: There is a set of values for `TotPop` (Total Population) in the `c-1980` table source.

### Update the `source` and/or `source_long` properties

If you used a new source that is not already listed within this variable, update these properties accordingly.

### Update the existing metadata document

There should already be a metadata document for this variable (if not, please make one!), but even so you still may need to update it with new information to reflect the provenance of the data values you have added.
