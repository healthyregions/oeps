# Geodata Sources

!!! tip
    For a list of all geodata sources currently in the registry, see [geodata_sources.csv](https://github.com/healthyregions/oeps/blob/main/docs/src/reference/registry/geodata_sources.csv) on Github.

This directory holds Frictionless [Data Resource](https://specs.frictionlessdata.io/data-resource/) definitions of shapefiles, that are used as base data for all joins. There are 4 different geographies--States, Counties, Tracts, and Zip Code Tabulation Areas (ZCTAs)--and (currently) all but the ZCTAs have data for both 2010 and 2018.

Each shapefile must have, at least, a `HEROP_ID` field which will be used by all CSV files for joins.
