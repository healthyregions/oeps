
# frictionless create-data-package

None

## Usage

```
Usage: frictionless create-data-package [OPTIONS]
```

## Options
* `destination`: 
  * Type: STRING 
  * Default: `none`
  * Usage: `--destination
-d`

  Output path for export. Must end with .csv for CSV or .shp for shapefile.


* `source`: 
  * Type: STRING 
  * Default: `none`
  * Usage: `--source
-s`

  Data Resource JSON file to export, or directory with multiple files.


* `zip_`: 
  * Type: BOOL 
  * Default: `false`
  * Usage: `--zip`

  Zip the output directory.


* `upload`: 
  * Type: BOOL 
  * Default: `false`
  * Usage: `--upload`

  Upload the processed files to S3.


* `no_cache`: 
  * Type: BOOL 
  * Default: `false`
  * Usage: `--no-cache`

  Force re-download of any remote files.


* `skip_foreign_keys`: 
  * Type: BOOL 
  * Default: `false`
  * Usage: `--skip-foreign-keys`

  Don't define foreign keys in the output data package.


* `overwrite`: 
  * Type: BOOL 
  * Default: `false`
  * Usage: `--overwrite`

  Overwrite data packages with the same name.


* `help`: 
  * Type: BOOL 
  * Default: `false`
  * Usage: `--help`

  Show this message and exit.



## CLI Help

```
Usage: frictionless create-data-package [OPTIONS]

Options:
  -d, --destination TEXT  Output path for export. Must end with .csv for CSV
                          or .shp for shapefile.

  -s, --source TEXT       Data Resource JSON file to export, or directory with
                          multiple files.

  --zip                   Zip the output directory.
  --upload                Upload the processed files to S3.
  --no-cache              Force re-download of any remote files.
  --skip-foreign-keys     Don't define foreign keys in the output data
                          package.

  --overwrite             Overwrite data packages with the same name.
  --help                  Show this message and exit.
```

