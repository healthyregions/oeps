# Data Model

## Variables

!!! tip
    For a list of all variables currently in the registry, see [variables.csv](https://github.com/healthyregions/oeps/blob/main/docs/src/reference/registry/variables.csv) on Github.

A single file, `variable.json`, serves as a central lookup for all variables, each one being defined as a Frictionless [Field Descriptor](https://specs.frictionlessdata.io/table-schema/#field-descriptors), with some extra properties that we have added for our own needs. The key for each item in the lookup must be the same as its `name` property.

Fields are defined by a JSON object that adheres to the [field descriptors](https://specs.frictionlessdata.io/table-schema/#field-descriptors) portion of the table schema standard, though not all possible attributes are required or implemented.

The following additional attributes are also supported and in some cases required:

Property|Format|Description|Comment
-|-|-|-
`name`|Primary identifier|Same as key for this item, must be CamelCase and &lt;= 10 characters long.
`title`|Human-readable title|Appears in data dictionaries and OEPS Explorer interfaces
`type`|Datatype of this variable|See [Frictionless Data field descriptor types](https://specs.frictionlessdata.io/table-schema/#types-and-formats)
`example`|Varies|An example value for the field|
`description`|A description for the field|
`longitudinal`|N/A|N/A
`analysis`|N/A|N/A
`table_sources`|List of all [table sources](#table-sources) this variable appears in|Table source names are in this list

### Example `variable` entry

```
"TotPop": {
    "title": "Total Population",
    "name": "TotPop",
    "type": "integer",
    "example": "1632480",
    "description": "Total population",
    "metadata": "Demographic_Characteristics",
    "longitudinal": true,
    "analysis": false,
    "table_sources": [
      "county-1980",
      "county-1990",
      "county-2000",
      "county-2010",
      "county-2018",
      "county-2020",
      "county-2023",
      "state-1980",
      "state-1990",
      "state-2010",
      "state-2000",
      "state-2018",
      "tract-1980",
      "tract-1990",
      "tract-2010",
      "tract-2000",
      "tract-2020",
      "tract-2018",
      "tract-2023",
      "zcta-2018",
      "zcta-2020",
      "zcta-2023"
    ]
  },
}
```


## Table Sources

!!! tip
    For a list of all table sources currently in the registry, see [table_sources.csv](https://github.com/healthyregions/oeps/blob/main/docs/src/reference/registry/table_sources.csv) on Github.

**Table sources** are a JSON representations of each CSV dataset within OEPS--one JSON file per CSV. The structure is based on the [Tabular Data Resource](https://specs.frictionlessdata.io/tabular-data-resource/) from Frictionless Data. However, where a `schema` property would typically define a primary key, foreign key (for joins), and a list of all fields, all of this information is inferred or standardized elsewhere and need not be stored in these files.

Characteristics of table source CSVs:

- Only have data for **one** geography level (state, county, tract, or zcta)
- Only have data for **one** year
- Named with the format `{geography}-{year}`, for example, `county-2020`
- Has a `HEROP_ID` column as primary key that joins each row to a geography unit.
- Has column names that match (exactly) with [variable](#variables) names already defined in the registry.

Each table source is defined by the following attributes:

Property|Description|Comment
-|-|-
`name`|ID of table source|Will always be in `{geography}-{year}` format
`title`|Human-readable title|Currently not used anywhere, and set to match `name`
`description`|Short description|Will always be "This CSV aggregates all OEPS data values from {year} at the {geography} level.
`path`|Path to CSV|Relative to data directory, this path will always be `tables/{name}.csv`, i.e. `tables/{geography}-{year}.csv`
`format`|Will always be `csv`|
`mediatype`|Will always be `text/csv`|
`data_year`|Year of the data in this CSV|
`geodata_source`|Name of geodata source this CSV will join to|Geodata source must already exist in the registry. Importantly, the year of the CSV data may not match the geodata source, as 2015 data should be joined to 2010 geographies (for example).

!!! warning "Future simplification"
    Much of the content stored in the attributes described above can be inferred from other information, or is always the same across all table sources, so it's possible that some of these will be removed in the future.

### Example `table_source`

```
{
  "bq_dataset_name": "tabular",
  "bq_table_name": "county-2020",
  "name": "county-2020",
  "path": "tables/county-2020.csv",
  "format": "csv",
  "mediatype": "text/csv",
  "title": "county-2020",
  "description": "This CSV aggregates all OEPS data values from 2020 at the county level.",
  "year": "2020",
  "geodata_source": "counties-2018"
}
```


## Metadata

!!! tip
    For a list of all metadata documents currently in the registry (and links to the markdown files), see [metadata.csv](https://github.com/healthyregions/oeps/blob/main/docs/src/reference/registry/metadata.csv) on Github.

The registry contains JSON references to metadata documents, which are ultimately stored as Markdown files on Github. Each reference defines a theme, construct, and proxy to be attached to the document, as well as the URL to the file.

Within OEPS, themes, constructs, and proxies create a hierarchical conceptual framework through which each variable can be interpreted. Metadata documents are created one-per-proxy, a proxy being a grouping of variables that (typically) have been created or extracted from the same source.

An example metadata entry looks like this:

```json
{
  "id": "Access_MOUDs",
  "theme": "Environment",
  "construct": "Spatial Access to MOUDs",
  "proxy": "Spatial access metrics... (this is a description of the variables themselves)",
  "url": "https://github.com/healthyregions/oeps/blob/main/metadata/Access_MOUDs.md",
  "source": "SAMSHA 2019, 2021; Vivitrol 2020; OSRM 2020;",
  "source_long": "U.S. Substance Abuse and Mental Health Services Administration, Treatment Locator Tool, 2019; Vivitrol, 2020; Open Source Routing Machine, 2020"
}
```

Each [variable entry](#variables) must reference a metadata entry, making a linkage to the document that describes its provenance. Typically, multiple variables are described in the same metadata document, so their `metadata` value will all be the same.


## Geodata Sources

!!! tip
    For a list of all geodata sources currently in the registry, see [geodata_sources.csv](https://github.com/healthyregions/oeps/blob/main/docs/src/reference/registry/geodata_sources.csv) on Github.

Geodata sources define the base geospatial data that can be joined to CSV data. There are 4 different geography levels (referred to as "summary levels" in the code baes): States, Counties, Tracts, and Zip Code Tabulation Areas (ZCTAs). Because we have many different years of data in the CSVs, we also need to include different years of spatial data, as boundaries and geographic unit ids change over time.

Characteristics of geodata source shapefiles:

- Has a `HEROP_ID` field which will be used by all CSV files for joins.
- Stored as zip file in AWS S3, not locally in the repository.

Each geodata source is defined by the following attributes:

Property|Description|Comment
-|-|-
`name`|ID of geodata source|Will always be in `{geography (plural)}-{year}` format.
`title`|Human-readable title|
`description`|Short description|Will always be "Shapefile of {geography} boundaries from the US Census Bureau, {year}".
`path`|Path to zipped shapefile|This is a full URL to the zipped file in AWS S3.
`format`|Will always be `shp`|
`mediatype`|Will always be `application/vnd.shp`|
`summary_level`|Type of geography|Will be one of: state, county, tract, or zcta.
`bq_dataset_name`|Target dataset during BigQuery upload|To be deprecated.
`bq_table_name`|Target table during BigQuery upload|To be deprecated.
`schema`|A nested JSON schema object|The schema defines `primaryKey` (always "HEROP_ID"), and `fields`, which will include, at least an entry for `HEROP_ID`.

!!! note
    Geodata sources are very similar to [table sources](#table-sources) (based on Frictionless [Data Resources](https://specs.frictionlessdata.io/data-resource/)) but instead of referencing CSV files they reference zipped ESRI Shapfiles, and they do include the `schema` property.

### Example `geodata_source`

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
            },
            {
                "name": "name",
                "title": "Name",
                "type": "string"
            }
        ]
    }
}
```
