
# create-data-dictionaries

Create the human readable, MS Excel data dictionaries based on registry content.

## Usage

```
Usage: create-data-dictionaries [OPTIONS]
```

## Arguments


## Options

* `destination`:
    * Type: <click.types.Path object at 0x7a49b26d2740>
    * Default: `None`
    * Usage: `--destination
-d`

    Output directory for new dictionaries, if not supplied will be placed within data dir.



* `registry_path`:
    * Type: <click.types.Path object at 0x7a49b269d9f0>
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


_This documentation is automatically generated by [md-click](https://github.com/RiveryIo/md-click). Do not edit this file directly._
