# OEPS Backend -- CLI Commands

The core of the OEPS backend is this suite of CLI commands, which handle data operations
within a variety of different contexts.

- [OEPS Explorer](#exlorer)
- [BigQuery](#bigquery)
- [Frcitionless Data](#frictionless)
- [Overture](#overture)
- [US Census Data](#census)

## bigquery

Usage: `flask bigquery [SUBCOMMAND]`

_documentation needed_

### Subcommands

#### bigquery check-credentials

Usage: `flask bigquery check-credentials [OPTS]`

 Check the credentials for Bsssig Query client. 

#### bigquery export

Usage: `flask bigquery export [OPTS]`

_documentation needed_

#### bigquery generate-reference-md

Usage: `flask bigquery generate-reference-md [OPTS]`

_documentation needed_

#### bigquery load

Usage: `flask bigquery load [OPTS]`

 Load a source to a big query table. 

## explorer

Usage: `flask explorer [SUBCOMMAND]`

Commands for configuring the [OEPS Explorer](https://oeps.healthyregions.org) web
application. The explorer is a NextJS app and can be found in the `explorer` directory of
the [OEPS repo](https://github.com/healthyregions/oeps).

### Subcommands

#### explorer build-config

Usage: `flask explorer build-config [OPTS]`

Build configs for the frontend OEPS Explorer application.

## frictionless

Usage: `flask frictionless [SUBCOMMAND]`

_documentation needed_

### Subcommands

#### frictionless create-data-package

Usage: `flask frictionless create-data-package [OPTS]`

_documentation needed_

#### frictionless create-oeps-dicts

Usage: `flask frictionless create-oeps-dicts [OPTS]`

_documentation needed_

#### frictionless generate-resources-from-oeps-dicts

Usage: `flask frictionless generate-resources-from-oeps-dicts [OPTS]`

_documentation needed_

#### frictionless list-resources

Usage: `flask frictionless list-resources [OPTS]`

_documentation needed_

## overture

Usage: `flask overture [SUBCOMMAND]`

_documentation needed_

### Subcommands

#### overture get-pois

Usage: `flask overture get-pois [OPTS]`

_documentation needed_

## census

Usage: `flask census [SUBCOMMAND]`

_documentation needed_

### Subcommands

#### census get-geodata

Usage: `flask census get-geodata [OPTS]`

_documentation needed_

