# Generating Derived Documentation

A variety of informational content can be automatically derived from the registry and backend code by running this CLI command:

```shell
flask build-docs
```

Four different sets of content are created with this command. You can create only one type of content (useful during development) using a specific flag in the command.

- [Command Line Reference](#command-line-reference), isolation flag: `--cli-only`
- [Data Dictionaries](#data-dictionaries), isolation flag: `--data-dictionaries-only`
- [BigQuery Table Schemas](#bigquery-table-schemas), isolation flag: `--bq-only`
- [Registry Summary](#registry-summary), isolation flag: `--registry-only`

## Command Line Reference

The command line reference documentation for each command is automatically generated from comments and docstrings directly within the code.

!!! message ""
    Output location: [/docs/src/reference/cli](https://github.com/healthyregions/oeps/tree/main/docs/src/reference/cli)

## Data Dictionaries

Data dictionaries can be generated in MS Excel format for easy-to-access, human readable distribution. These data dictionaries are split by geography--state, county, tract, or zcta--and list all variables with data at that geography and the for which years we have data for that variable.

Use the following command to generate updated data dictionaries:

```shell
flask create-data-dictionaries
```



These files are directly linked for download within the OEPS Explorer (/docs page) and are also referenced within the oepsData R package.

!!! message ""
    Output location: [/docs/src/reference/data-dictionaries](https://github.com/healthyregions/oeps/tree/main/docs/src/reference/data-dictionaries)


## Registry Summary

While the registry content is stored in JSON files, it can be easier to quickly search and digest that information in CSV format. The following command will generate a full set of CSV files from the registry.

These are the files linked in the [current registry content](../registry/current-content.md) section.

!!! message ""
    Output location: [/docs/src/reference/registry](https://github.com/healthyregions/oeps/tree/main/docs/src/reference/registry)

## BigQuery Table Schemas

To help researchers use the BigQuery tables to which we upload OEPS data, a reference document can be generated that describes the full shape of the content in BigQuery:

```shell
flask build-docs bq-reference
```

!!! warning
    The document describes the **anticipated** shape of these tables, even if they have not actually been updated recently, so extra care must be taken to keep these things in sync.

!!! message ""
    [/docs/src/reference/bigquery](https://github.com/healthyregions/oeps/tree/main/docs/src/reference/bigquery)