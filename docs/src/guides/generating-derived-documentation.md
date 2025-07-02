# Generating Derived Documentation

A variety of informational content can be automatically derived from the registry and backend code through a few different CLI commands.

[TOC]

## Data Dictionaries

Data dictionaries can be generated in MS Excel format for easy-to-access, human readable distribution. These data dictionaries are split by geography--state, county, tract, or zcta--and list all variables with data at that geography and the for which years we have data for that variable.

Use the following command to generate updated data dictionaries:

```shell
flask create-data-dictionaries
```

!!! tip ""
    [view in cli reference &rarr;](../reference/cli/create-data-dictionaries.md)

These files are directly linked for download within the OEPS Explorer (/docs page) and are also referenced within the oepsData R package.

!!! message ""
    Output location: `/docs/src/reference/data-dictionaries`

## CLI Documentation

The CLI reference documentation for each command is automatically generated from code comments and docstrings directly within those commands.

Use the following command to regenerate this content:

```shell
flask build-docs cli
```

!!! tip ""
    [view in cli reference &rarr;](../reference/cli/build-docs.md)

To properly document a newly created CLI command, make sure that

- it is listed in the code for the `build-docs` command
- the newly generated `.md` file is added to `mkdocs.yml`
- rebuild and publish these docs as described in the [OEPS Documentation installation notes](./install.md#oeps-documentation)

!!! message ""
    Output location: `/docs/src/reference/cli`

## Registry Summary

While the registry content is stored in JSON files, it can be easier to quickly search and digest that information in CSV format. The following command will generate a full set of CSV files from the registry:

```shell
flask build-docs registry-summary
```

!!! tip ""
    [view in cli reference &rarr;](../reference/cli/build-docs.md)

These are the files linked from the [What's in the Registry?](../registry/index.md#whats-in-the-registry) section.

!!! message ""
    Output location: `/docs/src/reference/registry`

## BigQuery Table Schemas

To help researchers use the BigQuery tables to which we upload OEPS data, a reference document can be generated that describes the full shape of the content in BigQuery:

```shell
flask build-docs bq-reference
```

!!! tip ""
    [view in cli reference &rarr;](../reference/cli/build-docs.md)

!!! warning
    The document describes the **anticipated** shape of these tables, even if they have not actually been updated recently, so extra care must be taken to keep these things in sync.

!!! message ""
    Output location: `/docs/src/reference/bigquery`