# Preparing CSV Data

## Requirements

To add new data to OEPS, you must prepare a CSV file. Ultimately this CSV will be merged into existing files, and information about its content will be added to the [registry](../registry/index.md). Before any of that happens though, the CSV data must be prepared with a few things in mind.

- **MUST** Use empty cells for "no data" values
    - Do not use `NA`
    - Keep in mind, a "no data" value is very different from `0`!
- **MUST** Have column names in `CamelCase`
    - If the data already exists in OEPS (for a different year or geography) your column name must exactly match the name for that variable
    - Ideally, names will be 10 characters or less
    - If the data is completely new to OEPS, you will also need to create the variable
- **MUST** Include an appropriate join column for spatial joins
    - `HEROP_ID`, `GEOID`, and `FIPS` codes are all acceptable, see below for more info
- **MUST** contain values for **only one year** and only **one geography level**
- **MAY** contain values for multiple variables (i.e. a CSV can has as many columns as you need)

## Configuring a join column

A join column serves as the linkage between the non-spatial CSV data and geographic data like county boundaries. To facilitate this linkage, any incoming CSV must have one of these columns:

Name|Geography|Description
-|-|-
`HEROP_ID`|all|A `HEROP_ID` is our version of `GEOID`, which also includes a "summary-level" code on the front of it, indicating what geography level the id refers to.
`GEOID`|all|For state, county, and tract data the `GEOID` is equivalent to the `FIPS` id. For ZCTA data, `GEOID` can match the zip code or `ZCTA5` for each ZCTA.
`FIPS`|state, county, tract|`FIPS` ids are nested such that, for example, the 5-digit `FIPS` for a county includes the 2-digit `FIPS` for its state.
`ZCTA5`|zcta|5-digit zip code that corresponds with the zip code tabulation area.
