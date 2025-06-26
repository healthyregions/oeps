# Table Sources

!!! tip
    For a list of all table sources currently in the registry, see [table_sources.csv](https://github.com/healthyregions/oeps/blob/main/docs/reference/table_sources.csv) on Github.

Each table source file is essentially a [Tabular Data Resource](https://specs.frictionlessdata.io/tabular-data-resource/) that links to a single data table (CSV), but without a `schema` property. Where the `schema` typically defines a primary key, foreign key (for joins), and a list of all fields, all of this information is inferred or standardized elsewhere and need not be stored in these files.

There are a few rules for how a CSV can be constructed:

1. It must have a `HEROP_ID` column that joins each row to a geography unit.
2. It must only have data for a single geography category within it.
3. *Ideally* it will only have values for a single publication year (though we don't yet have this enforced).

```json
{
    "name": "c-1980",
    "path": "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/full_tables/C_1980.csv",
    "title": "OEPS Data Aggregated by Census Tract (1980)",
    "description": "This CSV aggregates all 1980 data variables from the OEPS v2 release at the Census Tract level.",
    "bq_dataset_name": "tabular",
    "bq_table_name": "C_1980",
}
```

- `name` - Identifier for this table source. This ID is referenced by entries in the variables file.
- `path` - URL to publicly hosted CSV file.
- `title` - Human reaadable title of this source.
- `description` - A short, informative description of the data source.
- `bq_dataset_name` - The "dataset" (i.e. database) name in BigQuery that this source will be loaded into.
- `bq_table_name` - The table name that this dataset will be loaded into.