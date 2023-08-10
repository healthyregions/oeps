# Table Schemas

*this is a work-in-progress*

The structure of these schema files is based on the [table schema](https://specs.frictionlessdata.io/table-schema) specification, published by [Frictionless Standards](https://specs.frictionlessdata.io), with a few additions aimed at use in Google BigQuery.

For example, per table-schema, the `type` and `format` properties must follow the [table schema](https://specs.frictionlessdata.io/table-schema/#types-and-formats) spec, but a different set of data type values must be used for BigQuery, and these will be stored in `bg_data_type`.

Note on spatial data: `table schema` only has `geojson` or `geopoint` as valid types. This means the spec doesn't really work for many common spatial formats (CSV with the geometries stored as WKT, for example).

```
{
    "bq_dataset_name": "the name of the dataset in BigQuery to hold this table",
    "bq_table_name": "this table's name as it will appeard in BigQuery",
    "data_source": "relative path from data_local directory to CSV or SHP for this table",
    "fields": [
        {
            "name": "name of field (e.g. column name)",
            "title": "A nicer human readable label or title for the field",
            "type": "A string specifying the type",
            "format": "A string specifying a format",
            "example": "An example value for the field",
            "description": "A description for the field",
            "constraints": {
                // a constraints-descriptor
            }
            "bq_data_type": "a datatype string for use in BigQuery"
        }
    ]
}
```
