
# frictionless create-data-package

Generates a Frictionless data package from the Data Resource definitions in this backend. This export
process was developed specifically to support integration of the OEPS data warehouse into the JCOIN commons.

The resulting package will be validated against the `frictionless` standard using that Python library. Use
`--no-foreign-keys` to allow validation to pass when shapefiles are involved in join fields.


## Usage

```
Usage: frictionless create-data-package [OPTIONS]
```

## Arguments


## Options

* `destination`:
    * Type: STRING
    * Default: `../.cache`
    * Usage: `--destination
-d`

    Output location for export directory. The package will be placed within this directory and given a name generated from the current date and time.



* `source`:
    * Type: STRING
    * Default: `data/resources`
    * Usage: `--source
-s`

    Path to a data resource JSON file to export, or a directory containing multiple data resources.



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



* `skip_foreign_keys`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--skip-foreign-keys`

    Don't define foreign keys in the output data package. This is needed to avoid validation errors that occur when Shapefiles are used in foreign keys.



* `overwrite`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--overwrite`

    Overwrite existing data package with the same name.



* `help`:
    * Type: BOOL
    * Default: `False`
    * Usage: `--help`

    Show this message and exit.



## CLI Help

```
Usage: frictionless create-data-package [OPTIONS]

  Generates a Frictionless data package from the Data Resource definitions in
  this backend. This export process was developed specifically to support
  integration of the OEPS data warehouse into the JCOIN commons.

  The resulting package will be validated against the `frictionless` standard
  using that Python library. Use `--no-foreign-keys` to allow validation to
  pass when shapefiles are involved in join fields.

Options:
  -d, --destination TEXT  Output location for export directory. The package
                          will be placed within this directory and given a
                          name generated from the current date and time.
  -s, --source TEXT       Path to a data resource JSON file to export, or a
                          directory containing multiple data resources.
  --zip                   Zip the output data package.
  --upload                Upload the zipped data package to S3. Bucket is
                          determined by `AWS_BUCKET_NAME` environment
                          variable.
  --no-cache              Force re-download of any remote files.
  --skip-foreign-keys     Don't define foreign keys in the output data
                          package. This is needed to avoid validation errors
                          that occur when Shapefiles are used in foreign keys.
  --overwrite             Overwrite existing data package with the same name.
  --help                  Show this message and exit.
```


_This documentation is automatically generated by [md-click](https://github.com/RiveryIo/md-click). Do not edit this file directly._