# OEPS Data Ecosystem

This documentation aims to be a comprehensive explantation of how the Opioid Policy Environment Scan (OEPS, or "oh-eeps") data ecosystem is put together, and a technical resource for developers working on the code base. It also contains information for analysts preparing and adding new data, and guides for researchers looking to download or otherwise access OEPS data.

## How does this work?

There are two primary codebases within OEPS, the **frontend web explorer**, a NextJS application published at [oeps.healthyregions.org](https://oeps.healthyregions.org), and the **OEPS backend**, a Flask app. The backend app has three pieces:

1. The actual data stored static CSV files, in `data/`
2. A "registry" constructed of static JSON files, in `registry`
3. A suite of command line tools for both the registry and the data, in `cli/`

To understand how these pieces fit together, consider the following example operation from the OEPS Backend:

```shell
flask build-explorer --map-only
```

This command will provision the interactive web map in the OEPS Explorer with the latest data content that is currently in the ecosystem. It does so through the following general steps:

1. Initialize the registry, i.e. load all the JSON files into memory
2. Reads registry to find the latest year of all data values
3. Iterates identified CSV files, pulling specific columns from each one
4. Writes to new CSV files and JSON config files into the OEPS Explorer directory

This illustrates the general idea of how the ecosystem is setup: **Static content within the backend (registry and data files) are manipulated by CLI commands to perform certain transformations.** While this example wrote new content to the frontend app, other commands will export the data into different formats, or manage the import of new data.

## Where to go from here?

This documentation provides a set of guides that can be used to complete specific tasks, as well as reference material for details about all parts of the system. Some selected guides are linked below.

### Looking to use OEPS data?

Data can be exported from OEPS in a few different ways.

- [Download data directly from the website](https://oeps.healthyregions.org/download)
- [Creating data packages from the registry](guides/creating-data-packages.md)

We also manage an R data package called `oepsData` that makes it especially easy to download and analyze datasets from OEPS in an R environment.

- <a href="https://oepsdata.healthyregions.org" target="_blank">Using OEPS data with R &nearr;</a>

### Adding data to OEPS?

- [How to prepare a CSV for inclusion in the system](guides/preparing-csv-data.md)

### Working with the OEPS Expleror?

The [OEPS Explorer](https://oeps.healthyregions.org) is a NextJS app built from [WebGeoDa Scaffolding](https://docs.webgeoda.org/), a configurable web map application that implements [jsGeoDa](https://jsgeoda.libgeoda.org/) for geospatial interactivity. It is deployed through Netlify.

- [Install the OEPS Explorer for local development](guides/install-explorer.md)
- [Provision static assets for the OEPS Explorer (using the backend app)](guides/provisioning-oeps-explorer.md)

### Getting started with the OEPS Backend?

The OEPS Backend is a [Flask](https://flask.palletsprojects.com/en/stable/) application that holds a relational database-style JSON file registry based on [Frictionless Data](https://specs.frictionlessdata.io) standards and all OEPS data in CSV format, as well as a suite of management commands that perform various data-related actions.

- [Install the OEPS Backend](guides/install-backend.md)
- [Get started with CLI commands](./guides/getting-started-with-cli.md)
- [Learn about the registry and what's in it](./registry/index.md)

!!! note
    In the future, Flask's URL routing could be used to expose registry-related operations to HTTP endpoints, but for now everything is handling via the CLI.

### Updating this documentation?

The OEPS Documentation is a static site build with [MkDocs](https://www.mkdocs.org/) and hosted on Github pages at [healthyregions.github.io/oeps](https://healthyregions.github.io/oeps).

- [Install the documentation for local development](./guides/writing-documentation.md)
