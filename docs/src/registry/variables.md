# Variables

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
`source`|Abbreviated data source|This information appears in OEPS Explorer interfaces
`source_long`|Long-form data source info|
`longitudinal`|N/A|N/A
`analysis`|N/A|N/A
`table_sources`|List of all [table sources](./table-sources.md) this variable appears in|Table source names are in this list

## Example `variable` entry

```
"TotPop": {
    "title": "Total Population",
    "name": "TotPop",
    "type": "integer",
    "example": "1632480",
    "description": "Total population",
    "metadata": "Demographic_Characteristics",
    "source": "ACS 2018, 5-Year; Census 2010; IPUMS NHGIS",
    "source_long": "American Community Survey 2014-2018 5 Year Estimate; 2010 Decennial Census; Integrated Public Use Microdata Series National Historic Geographic Information System",
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
