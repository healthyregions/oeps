
# create-data-dictionaries

Create the human readable, MS Excel data dictionaries based on registry content.

## Usage

```
Usage: create-data-dictionaries [OPTIONS]
```

## Arguments


## Options

* `destination`:
    * Type: <click.types.Path object at 0x74981a022e00>
    * Default: `../docs/src/reference/data-dictionaries/`
    * Usage: `--destination
-d`

    Output directory for new dictionaries, if not supplied will be placed within data dir.



* `registry_path`:
    * Type: <click.types.Path object at 0x74981a472b00>
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
Usage: create-data-dictionaries [OPTIONS]

  Create the human readable, MS Excel data dictionaries based on registry
  content.

Options:
  -d, --destination PATH  Output directory for new dictionaries, if not
                          supplied will be placed within data dir.
  --registry-path PATH    Optional override for the registry directory.
  --help                  Show this message and exit.
```

!!! note
    _This documentation is automatically generated. Do not edit this file directly._
