# Overview

This documentation aims to be a comprehensive overview of how the Opioid Policy Environment Scan (OEPS, or "oh-eeps") data ecosystem is put together. Primarily, it is a technical resource for developers working on the code base, but also contains information for analysts preparing and adding new data, and information for researchers looking to download or otherwise access OEPS data.


This project builds from the original data warehouse stored in [github.com/GeoDaCenter/opioid-policy-scan](https://github.com/GeoDaCenter/opioid-policy-scan), and published on Zenodo at [doi.org/10.5281/zenodo.5842465](https://doi.org/10.5281/zenodo.5842465).

A number of components work together to create a data ecosystem from which data can be accessed and analyzed in many different ways. The following is a brief description of each component, with links to topics of interest for each one.

## OEPS Explorer

The [OEPS Explorer](https://oeps.healthyregions.org) is a NextJS app that is built from [WebGeoDa Scaffolding](https://docs.webgeoda.org/), a configurable web map application that implements [jsGeoDa](https://jsgeoda.libgeoda.org/) for geospatial interactivity. It is deployed through Netlify.

- [How to install the OEPS Explorer for local development](guides/install.md#oeps-explorer)
- [How to provision static assets for the OEPS Explorer from the backend app](guides/provisioning-oeps-explorer.md)

## OEPS Backend

The OEPS Backend is a [Flask](https://flask.palletsprojects.com/en/stable/) application that 1) holds all source data and data definitions in a "registry", and 2) provides a suite of management commands that interact with the registry to perform various data-related actions. These commands are built with [Click](https://click.palletsprojects.com/en/stable/), the CLI framework that Flask uses.

!!! note
    In the future, Flask's URL routing could be used to expose registry-related operations to HTTP endpoints, but for now everything is handling via the CLI.

- [How to install the OEPS Backend](guides/install.md#oeps-backend)

### Registry

The registry holds all data for OEPS (as CSV files), as well as linkage information for how those CSVs can be joined to the appropriate geometry Shapefiles for each year and geography (state, county, tract, or zcta). More importantly, it holds a suite of JSON files that define structured metadata about all of the data content.

### Management Commands

The backend provides management commands that can be used to perform many different data-related operations.

- [How to get started with backend management commands](guides/getting-started-with-commands.md)

## Documentation Site

todo

## oepsData - R package

We also manage an R data package, which makes it especially easy to download and analyze OEPS data in an R environment.

- [Go to full `oepsData` Documentation](https://oepsdata.healthyregions.org)
