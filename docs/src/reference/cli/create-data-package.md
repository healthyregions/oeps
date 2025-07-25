
# create-data-package

Generates a Frictionless data package from the Data Resource definitions in this backend. This export
    process was developed specifically to support integration of the OEPS data warehouse into the JCOIN commons.

    The resulting package will be validated against the `frictionless` standard using that Python library.

    `--skip-foreign-keys` to skip the creation of foreign keys--useful because foreign keys to shapefiles break
    validation.

    `--skip-validation` to skip the final step of running validation on the output package.
    

## Usage

```
Usage: create-data-package [OPTIONS]
```

## Arguments


## Options

* `destination`:
    * Type: <click.types.Path object at 0x7f6e3ff36290>
    * Default: `.temp/data-packages`
    * Usage: `--destination
-d`

    Output location for export directory. The package will be placed within this directory and given a name generated from the current date and time.



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
    * Type: <click.types.Path object at 0x7f6e40452b00>
    * Default: `oeps/registry`
    * Usage: `--registry-path`

    Optional override for the registry directory.



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



## CLI Help

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
  --zip                   Zip the output data package.
  --upload                Upload the zipped data package to S3. Bucket is
                          determined by `AWS_BUCKET_NAME` environment
                          variable.
  --no-cache              Force re-download of any remote files.
  --skip-foreign-keys     Don't define foreign keys in the output data
                          package. This is needed to avoid validation errors
                          that occur when Shapefiles are used in foreign keys.
  --skip-validation       Don't run data package validation on the final
                          output.
  --overwrite             Overwrite output content if it already exists.
  --registry-path PATH    Optional override for the registry directory.
  --verbose               Enable verbose logging.
  --help                  Show this message and exit.
```

!!! note
    _This documentation is automatically generated. Do not edit this file directly._
