# Interacting with OEPS Data in BigQuery

## Project Access

The OEPS BigQuery project is hosted at:
- **Project ID**: `oeps-391119`
- **Dashboard**: [https://console.cloud.google.com/welcome?project=oeps-391119](https://console.cloud.google.com/welcome?project=oeps-391119)

Team members with Owner access can manage the project, view datasets, and access all resources. To request access, contact the project administrators.

## Project Structure

All OEPS data tables are stored in the `tabular` dataset within the BigQuery project. Each table corresponds to a table source in the OEPS registry and is named after the table source name. All tables include `HEROP_ID` as the primary key field (first column), which uniquely identifies each geographic unit.

## Setting up Credentials

To load OEPS data to BigQuery you will need to add access credentials as environment variables using the `.env` file. This file must always stay out of version control.

### Method 1: Using a Service Account JSON File (Recommended for Local Development)

1. Make a copy of `backend/.env.example` and name it `backend/.env`. Any variables defined in this file will now be available via `os.getenv('VARIABLE_NAME')`

2. Obtain a set of JSON credentials for the project (service account key file), and store the file anywhere on your computer (but outside of this repository).

3. In your `backend/.env` file, set the following variables:
   ```
   BQ_PROJECT_ID="oeps-391119"
   BQ_CREDENTIALS_FILE_PATH="/path/to/your/service-account-key.json"
   ```

   For example:
   ```
   BQ_CREDENTIALS_FILE_PATH="/home/my_username/bq_credentials/oeps-391119-xxxxxxxxxxxx.json"
   ```
   
   **Note**: Replace `xxxxxxxxxxxx` with your actual service account key filename. The filename typically follows the pattern `oeps-391119-<key-id>.json`.

   On Windows, use forward slashes or escaped backslashes:
   ```
   BQ_CREDENTIALS_FILE_PATH="C:/Users/username/bq_credentials/oeps-391119-xxxxxxxxxxxx.json"
   ```

### Method 2: Using Environment Variables (For CI/CD or GitHub Actions)

If you don't have a local JSON file (e.g., during CI or GitHub Actions), you can set all credential information as environment variables. In this case, set `BQ_CREDENTIALS_FILE_PATH` to an empty string and provide all of the following variables:

```
BQ_PROJECT_ID="oeps-391119"
BQ_CREDENTIALS_FILE_PATH=""
BQ_CREDENTIALS_PRIVATE_KEY_ID="..."
BQ_CREDENTIALS_PRIVATE_KEY="..."
BQ_CREDENTIALS_CLIENT_EMAIL="..."
BQ_CREDENTIALS_CLIENT_ID="..."
BQ_CREDENTIALS_AUTH_URI="https://accounts.google.com/o/oauth2/auth"
BQ_CREDENTIALS_TOKEN_URI="https://oauth2.googleapis.com/token"
BQ_CREDENTIALS_AUTH_PROVIDER_X509_CERT_URL="https://www.googleapis.com/oauth2/v1/certs"
BQ_CREDENTIALS_CLIENT_X509_CERT_URL="..."
BQ_CREDENTIALS_UNIVERSE_DOMAIN="googleapis.com"
```

The credential system will automatically:
- Prefer the JSON file path if `BQ_CREDENTIALS_FILE_PATH` is set and non-empty
- Fall back to environment variables if no file path is provided
- Automatically refresh expired credentials if a refresh token is available

### Testing Credentials

Once you have setup these credentials, you can test them with:

```shell
flask bigquery-upload --check-credentials
```

If all is well, the command will print `ok`. If there are issues, you'll see an error message describing what went wrong.

## Data Type Mapping

The OEPS backend automatically maps data types from the registry schema to BigQuery data types:

| Registry Type | BigQuery Type | Notes |
|---------------|---------------|-------|
| `string` | `STRING` | Text data, can specify `max_length` |
| `boolean` | `BOOLEAN` | True/false values |
| `integer` | `INTEGER` | Whole numbers |
| `number` | `NUMERIC` | Decimal numbers |
| `date` | `DATE` | Date values (formatted as YYYY-MM-DD) |

For shapefiles, an additional `geom` field of type `GEOGRAPHY` is automatically added to store the geometric data.

## Uploading Tables

The `flask bigquery-upload` command loads data from the OEPS registry into BigQuery tables. The command reads table sources from the registry and creates corresponding BigQuery tables.

### Basic Usage

To upload all tables from the registry:

```shell
flask bigquery-upload
```

To upload a specific table by name:

```shell
flask bigquery-upload --name <table_name>
```

For example:
```shell
flask bigquery-upload --name states2023
```

### Command Options

- `--name` / `-n`: Load only a specific table source by name (instead of all tables in the registry)
- `--table-only`: Create the BigQuery dataset and table based on the schema, but don't load data into it. Useful for testing schema creation.
- `--dry-run`: Validate the input dataset against the schema and show what would be loaded, but don't actually create tables or load data. Useful for testing before actual uploads.
- `--overwrite`: Drop and recreate the BigQuery table if it already exists in the dataset. **Use with caution** as this will delete existing data.
- `--registry-path`: Specify a custom path to the registry (defaults to `backend/oeps/registry`)

### Upload Process

The upload process performs the following steps:

1. **Schema Validation**: Reads the table source from the registry and validates the schema
2. **Data Loading**: Loads the CSV data file specified in the table source
3. **Data Cleaning**: 
   - Removes columns not in the schema
   - Handles missing columns (reports as warnings)
   - Applies `zfill` padding where specified in the schema
   - Converts data types according to the schema
   - Handles special values (NaN, NA, infinity) by converting to NULL
   - Converts boolean values from various formats (1/0, Yes/No, True/False, etc.)
   - Formats dates from MM/DD/YYYY to YYYY-MM-DD format
4. **Table Creation**: Creates the BigQuery dataset (if it doesn't exist) and table with the appropriate schema
5. **Data Upload**: Loads the cleaned data rows into BigQuery using newline-delimited JSON format

### Table Structure

Each uploaded table:
- Is stored in the `tabular` dataset
- Uses the table source name as the table name
- Includes `HEROP_ID` as the first column (primary key)
- Contains all variables defined in the table source schema
- For shapefiles, includes a `geom` column with GEOGRAPHY type

### Example Output

When running the upload, you'll see output like:

```
VALIDATE INPUT SOURCE: backend/oeps/data/states2023.csv
WARNINGS ENCOUNTERED: 0

BEGIN LOAD: states2023
TABLE CREATED: <google.cloud.bigquery.table.Table object>
Input rows: 52
Running job now...
Output rows: 52
JOB COMPLETE: <google.cloud.bigquery.job.load.LoadJob object>
TIME ELAPSED: 0:00:15.234567
```

## Extracting Data from BigQuery

The `flask bigquery-export` command allows you to run SQL queries against BigQuery tables and export the results.

### Basic Usage

```shell
flask bigquery-export --sql-file path/to/query.sql --output results.csv
```

### Command Options

- `--sql-file`: Path to a file containing a complete SQL SELECT statement
- `--output` / `-o`: Output file path. Must end with:
  - `.csv` for CSV format (geometries will be in WKT format if present)
  - `.shp` for ESRI Shapefile format (for spatial queries)
  
If `--output` is omitted, the query results will be printed to the console (useful for testing queries).

### SQL Query Format

In your SQL file, use `PROJECT_ID` as a placeholder for the project ID. It will be automatically replaced with `oeps-391119` before the query is executed.

Example SQL file (`query_states.sql`):
```sql
SELECT 
  HEROP_ID,
  state_name,
  population_2020
FROM `PROJECT_ID.tabular.states2023`
WHERE population_2020 > 1000000
ORDER BY population_2020 DESC
```

### Exporting Results

**To CSV:**
```shell
flask bigquery-export --sql-file query_states.sql --output states_large.csv
```

**To Shapefile:**
```shell
flask bigquery-export --sql-file query_states.sql --output states_large.shp
```

**To Console (for testing):**
```shell
flask bigquery-export --sql-file query_states.sql
```

### Querying with Geometry

When querying tables that include geometry data, you can export to shapefile format:

```sql
SELECT 
  HEROP_ID,
  state_name,
  geom
FROM `PROJECT_ID.tabular.states2023`
WHERE state_name IN ('Illinois', 'California', 'Texas')
```

Then export:
```shell
flask bigquery-export --sql-file query_with_geom.sql --output selected_states.shp
```

### Reference Documentation

- Use the [big-query-tables](../reference/bigquery/tables.md) page for quick access to all table and column names
- See [example SQL queries](https://github.com/healthyregions/oeps/tree/main/docs/src/reference/bigquery/example_sql) for sample queries you can adapt

## Automated Documentation Generation

The BigQuery table reference documentation is automatically generated from the registry and does not require BigQuery credentials. This documentation describes the **anticipated** shape of tables based on the registry schemas.

### Generating Documentation

The documentation is automatically generated as part of the `flask build-docs` command:

```shell
flask build-docs --bq-only
```

Or generate all documentation types:

```shell
flask build-docs
```

### Documentation Location

The generated BigQuery reference documentation is located at:
- **File**: `docs/src/reference/bigquery/tables.md`
- **Online**: [BigQuery Tables Reference](../reference/bigquery/tables.md)

### Automated Generation in CI/CD

The BigQuery documentation is automatically regenerated in the GitHub Actions workflow (`.github/workflows/generate_derived_data.yml`) whenever:
- Changes are pushed to `backend/oeps/registry/**` or `backend/oeps/data/**`
- The workflow is manually triggered

The workflow runs:
```yaml
- name: Run build-docs (BigQuery)
  working-directory: backend
  run: flask build-docs --bq-only
```

This ensures the documentation stays in sync with the registry without requiring BigQuery credentials in the CI environment.

## Implementation Details

### Credential Handling

The BigQuery client (`backend/oeps/clients/bigquery.py`) handles credentials through the `get_credentials()` function:

1. **Priority 1**: If `BQ_CREDENTIALS_FILE_PATH` is set, loads credentials from the JSON file
2. **Priority 2**: If no file path, constructs credentials from individual environment variables
3. **Auto-refresh**: Automatically refreshes expired credentials if a refresh token is available

The client uses the `https://www.googleapis.com/auth/cloud-platform` scope for full BigQuery access.

### Data Loading Process

The `load_rows_from_resource()` method performs extensive data cleaning:
- Type conversion and validation
- Handling of NULL/NaN/infinity values
- Boolean value normalization
- Date format conversion (MM/DD/YYYY → YYYY-MM-DD)
- Geometry serialization to GeoJSON for shapefiles
- Column validation against schema

Data is loaded using BigQuery's `NEWLINE_DELIMITED_JSON` format for efficient bulk loading.

### Dependencies

The BigQuery functionality requires:
- `google-cloud-bigquery==3.11.3` (specified in `backend/pyproject.toml`)
- `google-auth` (for authentication)
- `pandas` and `geopandas` (for data processing)
- `db-dtypes` (for BigQuery data type support)
