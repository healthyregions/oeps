# Exporting Data from OEPS

The data stored within OEPS is distributed through a number of different channels, and extraction methods have been built to transform the content as needed. For example, OEPS data is restructured in a specific way to populate the [interactive web map](https://oeps.healthyregions.org/map), but the same data must also be configured into a [Frictionless Data Package](https://https://specs.frictionlessdata.io) for integration into the JCOIN Data Commons, a data sharing and analysis portal based on the Gen3 platform.

The rest of this page describes the various commands available and the export content they will create.

## Data Package (Frictionless Data spec v1)

To generate a data package, run the following:

```
flask create-data-package
```

Run on its own, this command will end in a `row_stream` error. This is because a validation check is attempted that doesn't support foreign keys to shapefiles, which is how we have the package configured. You can avoid this by using either the `--skip-foreign-keys` or `--skip-validation` flags as described in the full docs.

[[see full docs]](./reference/commands/create-data-package.md)

## Data Dictionaries

A suite of data dictionaries, one per geography level, can be generated with the following command:

```
flask create-data-dictionaries
```

These files compile all information available for each variable into a human readable, easy-to-distribute MS Excel spreadsheet.

## Documentation

A number of files within this set of docs are also generated from the registry content and placed within the docs/references directory, by using this command:

```
flask build-docs [category]
```

Categories are:

- `bq-reference`: Generates a markdown reference file for all content in BigQuery
- `cli`: Generates the detailed command documentation (for every command described here!)
- `registry-summary`: Generates the summary CSV files that list all registry content, and are easy to search through in Github.
