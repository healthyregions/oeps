# Variables

!!! tip
    For a list of all variables currently in the registry, see [variables.csv](https://github.com/healthyregions/oeps/blob/main/docs/reference/variables.csv) on Github.

A single file, `variable.json`, serves as a central lookup for all variables, each one being defined as a Frictionless [Field Descriptor](https://specs.frictionlessdata.io/table-schema/#field-descriptors), with some extra properties that we have added for our own needs. The key for each item in the lookup must be the same as its `name` property.


Fields are defined by a JSON object that adheres to the [field descriptors](https://specs.frictionlessdata.io/table-schema/#field-descriptors) portion of the table schema standard, though not all possible attributes are required or implemented.



The following additional attributes are also supported and in some cases required:


Property|Format|Description|OEPS Use
-|-|-|-
`name`|String|Canonical name for this column (used in BigQuery)|Required
`title`|String|A nicer human readable label or title for the field|Required
`type`|String|A string specifying the type. See [types](https://specs.frictionlessdata.io/table-schema/#types-and-formats).|Required
`format`|String|A string specifying a format|Not Implemented
`example`|String|An example value for the field|Optional
`description`|String|A description for the field|Optional
`constraints`|JSON|A [constraints descriptor](https://specs.frictionlessdata.io/table-schema/#constraints)|Not Implemented

- `name` - Canonical name of the variable, same as key for this item, must be CamelCase and &lt;= 10 characters long.
- `title` - Human-readable title.
- `type` - The type of data in this column, must be one of Frictionless [field types](https://specs.frictionlessdata.io/table-schema/#types-and-formats).
- `example` - An example value in this field.
- `description` - A one or two sentence description.
- `constraints` - Any data usage constraints that are relevant for this variable.
- `comments` - Any extra comments about this variable's creation that don't fit into other properties.
- `construct` - A "construct" string that is present within the `themes.json` file (see above)
- `source` - Creator of this variable, abbreviations ok.
- `source_long` - Long-form version of source
- `oeps_v1_table` - If applicable, the name of the data table that this variable was stored in in OEPS v1.
- `metadata_doc_url` - URL to raw content for a Markdown-formatted metadata document (this content is read and loaded directly into the explorer webpages).
- `longitudinal` - `true`/`false`, appropriate for longitudinal comparison.
- `analysis` - `true`/`false`
- `table_sources` - A list of data_source identifiers, must match identiers in the `sources.json` file.

Property|Format|Description|OEPS Use
-|-|-|-
`theme`|String|One of `Social`, `Environment`, `Economic`, `Policy`, `Outcome`, or `Geography`. See [OEPS docs](https://oeps.healthyregions.org/docs).|Optional
`comment`|String|Additional information about the data in this field|Optional
`source`|String|Source of the data in this field|Optional
`max_length`|Integer|Max length of field (used in BigQuery schema)|Optional


```
"TotPop": {
    "name": "TotPop",
    "title": "Total Population",
    "type": "number",
    "example": "1632480",
    "description": "Total population",
    "constraints": "1980-2000 historic data was acquired from NHGIS and then interpolated to modern county boundaries through a population weighted interpolation using the tidycensus `interpolate_pw` function. For 1980, the underlying population weighting was county subdivisions, while for 1990 and 200 the underlying population weighting was tracts.",
    "construct": "Population",
    "source": "ACS 2018, 5-Year; Census 2010; IPUMS NHGIS",
    "source_long": "American Community Survey 2014-2018 5 Year Estimate; 2010 Decennial Census; Integrated Public Use Microdata Series National Historic Geographic Information System",
    "oeps_v1_table": null,
    "comments": "For more information about how these data have been used in homelessness and housing stability research, please refer to https://www.census.gov/newsroom/press-releases/2020/special-operations-homelessness.html or https://www.americanprogress.org/issues/poverty/reports/2020/10/05/491122/count-people-where-they-are/.",
    "metadata_doc_url": "https://github.com/GeoDaCenter/opioid-policy-scan/blob/main/data_final/metadata/Age_2018.md",
    "longitudinal": true,
    "analysis": false,
    "table_sources": [
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
}
```
