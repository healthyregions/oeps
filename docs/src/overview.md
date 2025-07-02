
# OEPS Overview

A number of components work together to create a data ecosystem from which data can be accessed and analyzed in many different ways. The following is a brief description of each component, with links to topics of interest for each one.

- [OEPS Explorer](#oeps-explorer)
- [OEPS Backend](#oeps-backend)
- [OEPS Documentation](#oeps-documentation)
- [oepsData (R package)](#oepsdata)

## OEPS Explorer

The [OEPS Explorer](https://oeps.healthyregions.org) is a NextJS app built from [WebGeoDa Scaffolding](https://docs.webgeoda.org/), a configurable web map application that implements [jsGeoDa](https://jsgeoda.libgeoda.org/) for geospatial interactivity. It is deployed through Netlify.

- [Install the OEPS Explorer for local development](guides/install.md#oeps-explorer)
- [Provision static assets for the OEPS Explorer (using the backend app)](guides/provisioning-oeps-explorer.md)

## OEPS Backend

The OEPS Backend is a [Flask](https://flask.palletsprojects.com/en/stable/) application that holds a relational database-style JSON file registry based on [Frictionless Data](https://specs.frictionlessdata.io) standards and all OEPS data in CSV format, as well as a suite of management commands that perform various data-related actions.

- [Install the OEPS Backend](guides/install.md#oeps-backend)
- [Get started with CLI commands](./guides/getting-started-with-cli.md)
- [Learn about the registry and what's in it](./registry/index.md)

!!! note
    In the future, Flask's URL routing could be used to expose registry-related operations to HTTP endpoints, but for now everything is handling via the CLI.

## OEPS Documentation

The OEPS Documentation is a static site build with [MkDocs](https://www.mkdocs.org/) and hosted on Github pages at [healthyregions.github.io/oeps](https://healthyregions.github.io/oeps).

- [Install the documentation for local development](./guides/install.md#oeps-documentation)

## oepsData

We also manage an R data package called `oepsData` that makes it especially easy to download and analyze datasets from OEPS in an R environment.

- <a href="https://oepsdata.healthyregions.org" target="_blank">Go to full `oepsData` Documentation &nearr;</a>
