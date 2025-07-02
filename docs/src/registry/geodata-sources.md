# Geodata Sources

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
    Geodata sources are very similar to [table sources](./table-sources.md) (based on Frictionless [Data Resources](https://specs.frictionlessdata.io/data-resource/)) but instead of referencing CSV files they reference zipped ESRI Shapfiles, and they do include the `schema` property.

## Example `geodata_source`

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
