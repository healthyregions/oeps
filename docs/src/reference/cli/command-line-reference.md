# Command Line Reference
## merge-csv

Merge data from an external CSV into the canonical CSVs in OEPS.

    ARGUMENTS:

    -s / --source: Path to CSV to be merged in.

    -t / --table-source: name of table_source to merge this CSV into. Table source
    must already exist in the registry.

    --dry-run: load and stage the CSV but alter no files.
    

###### Usage

```
Usage: merge-csv [OPTIONS]
```

###### Arguments


###### Options

* `source`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--source
-s`

    Path to CSV that will be merged into the data registry.



* `table_source`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--table-source
-t`

    Name of the table source this input will be joined to.



* `dry_run`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--dry-run`

    Stage and prepare the import but alter no registry or data files.



* `registry_path`:
    * Type: <click.types.Path object at 0x7fe64be59d50>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: merge-csv [OPTIONS]

  Merge data from an external CSV into the canonical CSVs in OEPS.

  ARGUMENTS:

  -s / --source: Path to CSV to be merged in.

  -t / --table-source: name of table_source to merge this CSV into. Table
  source must already exist in the registry.

  --dry-run: load and stage the CSV but alter no files.

Options:
  -s, --source TEXT        Path to CSV that will be merged into the data
                           registry.
  -t, --table-source TEXT  Name of the table source this input will be joined
                           to.
  --dry-run                Stage and prepare the import but alter no registry
                           or data files.
  --registry-path PATH     Optional override for the registry directory.
  --help                   Show this message and exit.
```


## validate-registry

Runs a series of validation processes against the current registry content.

###### Usage

```
Usage: validate-registry [OPTIONS]
```

###### Arguments


###### Options

* `registry_path`:
    * Type: <click.types.Path object at 0x7fa38e062110>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `sync_table_sources`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--sync-table-sources`

    Updates all variable table_sources values directly from CSV data.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: validate-registry [OPTIONS]

  Runs a series of validation processes against the current registry content.

Options:
  --registry-path PATH  Optional override for the registry directory.
  --sync-table-sources  Updates all variable table_sources values directly
                        from CSV data.
  --help                Show this message and exit.
```


## bigquery-export

Runs a SQL statement, which must be provided in a .sql file, and the results are printed to the console
    or saved to a CSV or SHP output file, based on the destination argument.

###### Usage

```
Usage: bigquery-export [OPTIONS]
```

###### Arguments


###### Options

* `output`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--output
-o`

    Output file for export. Must end with .csv for CSV or .shp for ESRI Shapefile.



* `sql_file`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--sql-file`

    Path to file with SQL SELECT statement to run.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: bigquery-export [OPTIONS]

  Runs a SQL statement, which must be provided in a .sql file, and the results
  are printed to the console or saved to a CSV or SHP output file, based on
  the destination argument.

Options:
  -o, --output TEXT  Output file for export. Must end with .csv for CSV or
                     .shp for ESRI Shapefile.
  --sql-file TEXT    Path to file with SQL SELECT statement to run.
  --help             Show this message and exit.
```


## create-table-source

Creates a new blank table source and generates an accompanying
    CSV with only relevant keys.
    

###### Usage

```
Usage: create-table-source [OPTIONS]
```

###### Arguments


###### Options

* `name`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--name
-n`

    Name (id) of new table source. This will be used for the CSV file name.



* `data_year`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--data-year
-y`

    Year of data that this table source will hold.



* `geodata_source`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--geodata-source
-g`

    Name of the geodata source that this table source will be joined to.



* `dry_run`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--dry-run`

    Stage and prepare new table source but don't save.



* `registry_path`:
    * Type: <click.types.Path object at 0x7fbdcb8560d0>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: create-table-source [OPTIONS]

  Creates a new blank table source and generates an accompanying CSV with only
  relevant keys.

Options:
  -n, --name TEXT            Name (id) of new table source. This will be used
                             for the CSV file name.
  -y, --data-year TEXT       Year of data that this table source will hold.
  -g, --geodata-source TEXT  Name of the geodata source that this table source
                             will be joined to.
  --dry-run                  Stage and prepare new table source but don't
                             save.
  --registry-path PATH       Optional override for the registry directory.
  --help                     Show this message and exit.
```


## remove-variable

Remove variable(s) from the registry and all of their columns from table source CSVs.
    Optionally remove variables only from one table source.
    
    Can remove multiple variables at once by providing comma-separated names.
    Example (single): flask remove-variable -n Var1 -t county-2025
    Example (multiple): flask remove-variable -n "Var1,Var2,Var3" -t county-2025 --yes
    

###### Usage

```
Usage: remove-variable [OPTIONS]
```

###### Arguments


###### Options

* `name`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--name
-n`

    Name of variable(s) to remove. For multiple variables, use comma-separated values (e.g., -n 'Var1,Var2,Var3').



* `table_source`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--table-source
-t`

    Name of single table source from which the variable will be removed.



* `yes`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--yes
-y`

    Skip confirmation prompts. Useful for batch operations.



* `registry_path`:
    * Type: <click.types.Path object at 0x7f6196c69ed0>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: remove-variable [OPTIONS]

  Remove variable(s) from the registry and all of their columns from table
  source CSVs. Optionally remove variables only from one table source.

  Can remove multiple variables at once by providing comma-separated names.
  Example (single): flask remove-variable -n Var1 -t county-2025 Example
  (multiple): flask remove-variable -n "Var1,Var2,Var3" -t county-2025 --yes

Options:
  -n, --name TEXT          Name of variable(s) to remove. For multiple
                           variables, use comma-separated values (e.g., -n
                           'Var1,Var2,Var3').
  -t, --table-source TEXT  Name of single table source from which the variable
                           will be removed.
  -y, --yes                Skip confirmation prompts. Useful for batch
                           operations.
  --registry-path PATH     Optional override for the registry directory.
  --help                   Show this message and exit.
```


## move-variable

Move a variable from one table to another. This command is primarily meant to
    be a corrective tool to help move a set of values for a variable to a different year,
    after being initially placed in the wrong year.
    

###### Usage

```
Usage: move-variable [OPTIONS]
```

###### Arguments


###### Options

* `name`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--name
-n`

    Name of variable to move.



* `source`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--source
-s`

    Name of table source from which the variable will be moved.



* `target`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--target
-t`

    Name of table source to which this variable will be moved.



* `overwrite`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--overwrite`

    Overwrite output content if it already exists.



* `registry_path`:
    * Type: <click.types.Path object at 0x7fa6e5e5e090>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: move-variable [OPTIONS]

  Move a variable from one table to another. This command is primarily meant
  to be a corrective tool to help move a set of values for a variable to a
  different year, after being initially placed in the wrong year.

Options:
  -n, --name TEXT       Name of variable to move.
  -s, --source TEXT     Name of table source from which the variable will be
                        moved.
  -t, --target TEXT     Name of table source to which this variable will be
                        moved.
  --overwrite           Overwrite output content if it already exists.
  --registry-path PATH  Optional override for the registry directory.
  --help                Show this message and exit.
```


## create-data-package

Generates a Frictionless data package from the Data Resource definitions in this backend. This export
    process was developed specifically to support integration of the OEPS data warehouse into the JCOIN commons.

    The resulting package will be validated against the `frictionless` standard using that Python library.

    `--skip-foreign-keys` to skip the creation of foreign keys--useful because foreign keys to shapefiles break
    validation.

    `--skip-validation` to skip the final step of running validation on the output package.
    

###### Usage

```
Usage: create-data-package [OPTIONS]
```

###### Arguments


###### Options

* `destination`:
    * Type: <click.types.Path object at 0x7fb270bd2e90>
    * Default: `.temp/data-packages`
    * Usage: `--destination
-d`

    Output location for export directory. The package will be placed within this directory and given a name generated from the current date and time.



* `config`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
    * Usage: `--config
-c`

    Name of folder in data/package_rules that holds configs for the export.



* `zip_`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--zip`

    Zip the output data package.



* `upload`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--upload`

    Upload the zipped data package to S3. Bucket is determined by `AWS_BUCKET_NAME` environment variable.



* `no_cache`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--no-cache`

    Force re-download of any remote files.



* `check_rules`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--check-rules`

    Only check the rules file, don't create any dataframes or output files.



* `skip_foreign_keys`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--skip-foreign-keys`

    Don't define foreign keys in the output data package. This is needed to avoid validation errors that occur when Shapefiles are used in foreign keys.



* `skip_validation`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--skip-validation`

    Don't run data package validation on the final output.



* `overwrite`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--overwrite`

    Overwrite output content if it already exists.



* `registry_path`:
    * Type: <click.types.Path object at 0x7fb27167e0d0>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `data_dir_path`:
    * Type: <click.types.Path object at 0x7fb27167de90>
    * Default: `oeps/data`
    * Usage: `--data-dir-path`

    Optional override for the data directory path.



* `verbose`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--verbose`

    Enable verbose logging.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: create-data-package [OPTIONS]

  Generates a Frictionless data package from the Data Resource definitions in
  this backend. This export process was developed specifically to support
  integration of the OEPS data warehouse into the JCOIN commons.

  The resulting package will be validated against the `frictionless` standard
  using that Python library.

  `--skip-foreign-keys` to skip the creation of foreign keys--useful because
  foreign keys to shapefiles break validation.

  `--skip-validation` to skip the final step of running validation on the
  output package.

Options:
  -d, --destination PATH  Output location for export directory. The package
                          will be placed within this directory and given a
                          name generated from the current date and time.
  -c, --config TEXT       Name of folder in data/package_rules that holds
                          configs for the export.
  --zip                   Zip the output data package.
  --upload                Upload the zipped data package to S3. Bucket is
                          determined by `AWS_BUCKET_NAME` environment
                          variable.
  --no-cache              Force re-download of any remote files.
  --check-rules           Only check the rules file, don't create any
                          dataframes or output files.
  --skip-foreign-keys     Don't define foreign keys in the output data
                          package. This is needed to avoid validation errors
                          that occur when Shapefiles are used in foreign keys.
  --skip-validation       Don't run data package validation on the final
                          output.
  --overwrite             Overwrite output content if it already exists.
  --registry-path PATH    Optional override for the registry directory.
  --data-dir-path PATH    Optional override for the data directory path.
  --verbose               Enable verbose logging.
  --help                  Show this message and exit.
```


## build-docs

Generates various documentation pages based on the data content.

    Optionally only generate one of the types of docs.
    

###### Usage

```
Usage: build-docs [OPTIONS]
```

###### Arguments


###### Options

* `bq_only`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--bq-only`

    Only build the BigQuery reference docs.



* `cli_only`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--cli-only`

    Only build the CLI docs.



* `registry_only`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--registry-only`

    Only build the registry summary docs.



* `data_dictionaries_only`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--data-dictionaries-only`

    Only build the data dictionaries.



* `registry_path`:
    * Type: <click.types.Path object at 0x7feb9a5764d0>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: build-docs [OPTIONS]

  Generates various documentation pages based on the data content.

  Optionally only generate one of the types of docs.

Options:
  --bq-only                 Only build the BigQuery reference docs.
  --cli-only                Only build the CLI docs.
  --registry-only           Only build the registry summary docs.
  --data-dictionaries-only  Only build the data dictionaries.
  --registry-path PATH      Optional override for the registry directory.
  --help                    Show this message and exit.
```


## bigquery-upload

Load a data resource to a big query table. The data resource schema should provide all field
    and table configuration information that is needed to create the table and load data into it.

###### Usage

```
Usage: bigquery-upload [OPTIONS]
```

###### Arguments


###### Options

* `name`:
    * Type: STRING
    * Default: `Sentinel.UNSET`
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
    * Type: <click.types.Path object at 0x7f4430f7e290>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

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


## clean-explorer-bucket

Deletes all files from the S3 bucket which are not mentioned in the local
    explorer/configs/sources.json file. If no sources.json file exists, optionally
    deletes all uploaded files.
    

###### Usage

```
Usage: clean-explorer-bucket [OPTIONS]
```

###### Arguments


###### Options

* `explorer_path`:
    * Type: <click.types.Path object at 0x7ff8c7a69e90>
    * Default: `../explorer`
    * Usage: `--explorer-path`

    Optional override for the root directory of the explorer.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: clean-explorer-bucket [OPTIONS]

  Deletes all files from the S3 bucket which are not mentioned in the local
  explorer/configs/sources.json file. If no sources.json file exists,
  optionally deletes all uploaded files.

Options:
  --explorer-path PATH  Optional override for the root directory of the
                        explorer.
  --help                Show this message and exit.
```


## build-explorer

Builds all static data content needed to power the frontend OEPS Explorer application.
    
    Optionally only build data for the map, or for the /docs page (theme, construct, and source data)
    
    Use --upload-map-data to make a production update for the map. Without this argument, CSV data
    files for the map will just be stored locally in .cache/explorer/csvs and the frontend running locally
    will read them from there.
    

###### Usage

```
Usage: build-explorer [OPTIONS]
```

###### Arguments


###### Options

* `registry_path`:
    * Type: <click.types.Path object at 0x7f3267e621d0>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



* `explorer_path`:
    * Type: <click.types.Path object at 0x7f3267e61e10>
    * Default: `../explorer`
    * Usage: `--explorer-path`

    Optional override for the root directory of the explorer.



* `map_only`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--map-only`

    Only build static content to drive the map.



* `docs_only`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--docs-only`

    Only build static content to drive the docs page.



* `upload_map_data`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--upload-map-data`

    Upload the output map data CSV files to S3 bucket.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



###### CLI Help

```
Usage: build-explorer [OPTIONS]

  Builds all static data content needed to power the frontend OEPS Explorer
  application.

  Optionally only build data for the map, or for the /docs page (theme,
  construct, and source data)

  Use --upload-map-data to make a production update for the map. Without this
  argument, CSV data files for the map will just be stored locally in
  .cache/explorer/csvs and the frontend running locally will read them from
  there.

Options:
  --registry-path PATH  Optional override for the registry directory.
  --explorer-path PATH  Optional override for the root directory of the
                        explorer.
  --map-only            Only build static content to drive the map.
  --docs-only           Only build static content to drive the docs page.
  --upload-map-data     Upload the output map data CSV files to S3 bucket.
  --help                Show this message and exit.
```

!!! note
    _This documentatioeen is automatically generated. Do not edit this file directly._
