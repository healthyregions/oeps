# Table Sources

!!! tip
    For a list of all table sources currently in the registry, see [table_sources.csv](https://github.com/healthyregions/oeps/blob/main/docs/src/reference/registry/table_sources.csv) on Github.

**Table sources** are a JSON representations of each CSV dataset within OEPS--one JSON file per CSV. The structure is based on the [Tabular Data Resource](https://specs.frictionlessdata.io/tabular-data-resource/) from Frictionless Data. However, where a `schema` property would typically define a primary key, foreign key (for joins), and a list of all fields, all of this information is inferred or standardized elsewhere and need not be stored in these files.

Characteristics of table source CSVs:

- Only have data for **one** geography level (state, county, tract, or zcta)
- Only have data for **one** year
- Named with the format `{geography}-{year}`, for example, `county-2020`
- Has a `HEROP_ID` column as primary key that joins each row to a geography unit.
- Has column names that match (exactly) with [variable](./variables.md) names already defined in the registry.

Each table source is defined by the following attributes:

Property|Description|Comment
-|-|-
`name`|ID of table source|Will always be in `{geography}-{year}` format
`title`|Human-readable title|Currently not used anywhere, and set to match `name`
`description`|Short description|Will always be "This CSV aggregates all OEPS data values from {year} at the {geography} level.
`path`|Path to CSV|Relative to data directory, this path will always be `tables/{name}.csv`, i.e. `tables/{geography}-{year}.csv`
`format`|Will always be `csv`|
`mediatype`|Will always be `text/csv`|
`year`|Year of the data in this CSV|
`bq_dataset_name`|Target dataset during BigQuery upload|To be deprecated.
`bq_table_name`|Target table during BigQuery upload|To be deprecated.
`geodata_source`|Name of geodata source this CSV will join to|Geodata source must already exist in the registry. Importantly, the year of the CSV data may not match the geodata source, as 2015 data should be joined to 2010 geographies (for example).

!!! warning "Future simplification"
    Much of the content stored in the attributes described above can be inferred from other information, or is always the same across all table sources, so it's possible that some of these will be removed in the future.

## Example `table_source`

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
