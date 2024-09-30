# Data registry

The files in this directory are the overall schema definitions for all data within the OEPS warehouse. The structure of this content is largely inspired by [Frictionless](https://frictionlessdata.io/) data specs, which are used to generate [Data Packages](https://specs.frictionlessdata.io/data-package/), [Data Resources](https://specs.frictionlessdata.io/data-resource/), and other forms of data dictionaries and downloadable content.

The registry is broken into three parts:

- [geodata](#geodata)
- [sources.json](#sourcesjson)
- [variables.json](#variablesjson)

## `geodata (directory)`

This directory holds Frictionless [Data Resource](https://specs.frictionlessdata.io/data-resource/) definitions of shapefiles, that are used as base data for all joins. There are 4 different geographies--States, Counties, Tracts, and Zip Code Tabulation Areas (ZCTAs)--and (currently) all but the ZCTAs have data for both 2010 and 2018.

Each shapefile must have, at least, a `HEROP_ID` field which will be used by all CSV files for joins.

## `sources.json`

A keyed set of references to individual CSV files with actual data in them, one entry per CSV. An example entry is show below. A few important things to keep in mind about data sources.

1. A data source must have a `HEROP_ID` column that joins each row to a geography.
3. A data source must only have data for a single geography category within it.
2. A data source should only have variables in it that correspond to a single publication year.

### Example

```json
"c-1980": {
    "name": "c-1980",
    "path": "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/full_tables/C_1980.csv",
    "title": "OEPS Data Aggregated by Census Tract (1980)",
    "description": "This CSV aggregates all 1980 data variables from the OEPS v2 release at the Census Tract level.",
    "year": "1980",
    "geography": "county",
    "bq_dataset_name": "tabular",
    "bq_table_name": "C_1980",
}
```

- `c-1980` - This is the identifier for the source, and is referenced in the variables file below. It can be any string value (no spaces though!)
- `name` - Name of the source. Same as identifier above.
- `path` - URL to publicly hosted CSV file.
- `title` - Human reaadable title of this source.
- `description` - A short, informative description of the data source.
- `year`- The year of the data variables in this source (ideally they are all the same year).
- `geography` - The geography that these variable values correspond to.
- `bq_dataset_name` - The "dataset" (i.e. database) name in BigQuery that this source will be loaded into.
- `bq_table_name` - The table name that this dataset will be loaded into.

## `variables.json`

This is a master list of _all_ variables that are present within any of the data sources. The reason for this sort of a "central registry" is that we now have variables exist across multiple time periods and multiple geographies. For example, `TopPop` is **Total Population** and it appears in 16 different data sources. We need to store a number of meta properties about this variable that are identical across all CSV files, so having a single place to do so makes this easier to achieve.

### Example

```json
"TotPop": {
    "name": "TotPop",
    "title": "Total Population",
    "src_name": "TotPop",
    "type": "number",
    "example": "1632480",
    "description": "Total population",
    "constraints": "1980-2000 historic data was acquired from NHGIS and then interpolated to modern county boundaries through a population weighted interpolation using the tidycensus `interpolate_pw` function. For 1980, the underlying population weighting was county subdivisions, while for 1990 and 200 the underlying population weighting was tracts.",
    "theme": "Social",
    "source": "ACS 2018, 5-Year; Census 2010; IPUMS NHGIS",
    "source_long": "American Community Survey 2014-2018 5 Year Estimate; 2010 Decennial Census; Integrated Public Use Microdata Series National Historic Geographic Information System",
    "oeps_v1_table": null,
    "comments": "For more information about how these data have been used in homelessness and housing stability research, please refer to https://www.census.gov/newsroom/press-releases/2020/special-operations-homelessness.html or https://www.americanprogress.org/issues/poverty/reports/2020/10/05/491122/count-people-where-they-are/.",
    "bq_data_type": "FLOAT",
    "metadata_doc_url": "https://github.com/GeoDaCenter/opioid-policy-scan/blob/main/data_final/metadata/Age_2018.md",
    "longitudinal": true,
    "analysis": false,
    "data_sources": [
      "c-1980",
      "s-latest",
      "t-2010",
      "t-latest",
      "s-2000",
      "t-2000",
      "c-1990",
      "z-latest",
      "t-1990",
      "s-1980",
      "c-latest",
      "s-1990",
      "s-2010",
      "t-1980",
      "c-2010",
      "c-2000"
  ]
},
```

These properties are meant to facilitate compliance with Frictionless [Field Descriptors](https://specs.frictionlessdata.io/table-schema/#field-descriptors), so that spec will provide guidance for any properties marked with an *.

- `TotPop` - Main identifier for this variable. It must be in CamelCase format, and under 10 characters long.
- `name` - Canonical name of the variable. Same as identifier above.
- `title` * - Human-readable title.
- `type` * - The type of data in this column, must be one of Frictionless [field types](https://specs.frictionlessdata.io/table-schema/#types-and-formats).
- `example` * - An example value in this field.
- `description` * - A one or two sentence description.
- `constraints` * - Any data usage constraints that are relevant for this variable.
- `comments` - Any extra comments about this variable's creation that don't fit into other properties.
- `src_name` - The name of this column in its data sources (this _should_ be the same as name above anyway).
- `bq_data_type` - The type of column that this variable will be placed into in BigQuery, must be one of [these types](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types).
- `theme` - One of: _Social_, _Economic_, _Policy_, _Physical Environment_, _Outcome_
- `source` - Creator of this variable, abbreviations ok.
- `source_long` - Long-form version of source
- `oeps_v1_table` - If applicable, the name of the data table that this variable was stored in in OEPS v1.
- `metadata_doc_url` - URL to raw content for a Markdown-formatted metadata document (this content is read and loaded directly into the explorer webpages).
- `longitudinal` - `true`/`false`, appropriate for longitudinal comparison.
- `analysis` - `true`/`false`
- `data_sources` - A list of data_source identifiers, must match identiers in the `sources.json` file. 