
# bigquery-upload

Load a data resource to a big query table. The data resource schema should provide all field
    and table configuration information that is needed to create the table and load data into it.

## Usage

```
Usage: bigquery-upload [OPTIONS]
```

## Arguments


## Options

* `name`:
    * Type: STRING
    * Default: `None`
    * Usage: `--name
-n`

    Name can be provided to load a single Data Resource to Big Query (instead of everything in the registry)



* `table_only`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--table-only`

    Only create the new table, don't load data into it.



* `dry_run`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--dry-run`

    Mock operation and perform no create/delete actions.



* `check_credentials`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--check-credentials`

    Checks local credentials and exits.



* `overwrite`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--overwrite`

    Overwrite output content if it already exists.



* `registry_path`:
    * Type: <click.types.Path object at 0x740f2064e980>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



## CLI Help

```
Usage: bigquery-upload [OPTIONS]

  Load a data resource to a big query table. The data resource schema should
  provide all field and table configuration information that is needed to
  create the table and load data into it.

Options:
  -n, --name TEXT       Name can be provided to load a single Data Resource to
                        Big Query (instead of everything in the registry)
  --table-only          Only create the new table, don't load data into it.
  --dry-run             Mock operation and perform no create/delete actions.
  --check-credentials   Checks local credentials and exits.
  --overwrite           Overwrite output content if it already exists.
  --registry-path PATH  Optional override for the registry directory.
  --help                Show this message and exit.
```

!!! note
    _This documentation is automatically generated. Do not edit this file directly._
