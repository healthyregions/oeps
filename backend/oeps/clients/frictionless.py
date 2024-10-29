import os
import json
import numpy
import shutil
from datetime import datetime
import pandas as pd
import geopandas as gpd
from pathlib import Path

from frictionless import validate

from oeps.config import DATA_DIR
from oeps.utils import fetch_files, upload_to_s3, load_json, write_json, BQ_TYPE_LOOKUP
from oeps.clients.registry import Registry


class DataPackage():

    def create(self,
            destination,
            zip_output: bool=False,
            upload: bool=False,
            no_cache: bool=False,
            skip_foreign_keys: bool=False,
            run_validation: bool=True,
        ):
        """ Single command to generate an output data package. Should probably be
        refactored to more modular methods on this class."""

        registry = Registry()

        dest = Path(destination)
        dest.mkdir(exist_ok=True, parents=True)
        s_path = Path(dest, "schemas")
        s_path.mkdir(exist_ok=True)
        d_path = Path(dest, "data")
        d_path.mkdir(exist_ok=True)

        data_package = {
            "profile": "data-package",
            "name": "oeps",
            "title": "Opioid Environment Policy Scan (OEPS) v2",
            "homepage": "https://oeps.healthyregions.org",
            "licenses": [{
                "name": "ODC-PDDL-1.0",
                "path": "http://opendatacommons.org/licenses/pddl/",
                "title": "Open Data Commons Public Domain Dedication and License v1.0"
            }],
            "resources": []
        }

        resources = registry.get_all_geodata_resources(trim_props=True) + registry.get_all_table_resources(trim_props=True)
        for res in resources:

            # remove foreignKeys from schema if needed
            if skip_foreign_keys:
                res["schema"].pop("foreignKeys", None)

            # write the schema out to its own file in the schemas dir
            schema = res.pop("schema")
            schema_filename = f"{res['name']}.json"

            write_json(schema, Path(s_path, schema_filename))

            # copy the data files and generate the list of local paths
            local_paths = fetch_files(res.pop("path"), d_path, no_cache=no_cache)

            res["path"] = [f"data/{i.name}" for i in local_paths]
            res["schema"] = f"schemas/{schema_filename}"

            data_package["resources"].append(res)

        package_json_path = Path(dest, "data-package.json")
        write_json(data_package, package_json_path)

        self.clean_datasets(package_json_path)

        if run_validation:
            print("\nvalidating output data package...")
            report = validate(package_json_path, skip_errors=['type-error'])

            print("VALIDATION REPORT SUMMARY:")
            for t in report.tasks:
                print(t.name, t.stats['errors'])
            
            print(f"Totals: {report.stats}")

            report.to_json(Path(dest, "error-report.json"))
        
        else:
            print("skipping data package validation...")

        if zip_output or upload:
            print("zipping output...")
            shutil.make_archive(f"{Path(dest.parent, dest.name)}", 'zip', dest)

            zip_path = dest.with_suffix(".zip")

            if upload:
                print("uploading zip to S3...")
                upload_to_s3([zip_path], prefix='oeps', progress_bar=True)

            if not zip_output:
                print('deleting local copy of zipped output...')
                os.remove(zip_path)

        print("done.")

    def clean_datasets(self, package_json_path):

        pkg = load_json(package_json_path)

        for res in pkg['resources']:
            # only run this on resources with single file paths (i.e. skip shapefiles)
            if len(res['path']) > 1:
                continue

            print(f"cleaning data for {res['name']}")

            data_path = package_json_path.parent / res['path'][0]
            schema_path = package_json_path.parent / res['schema']

            schema = load_json(schema_path)
            fields = {i["name"]: i for i in schema["fields"]}

            df = pd.read_csv(data_path)

            # create new dataframe with only fields as defined in the schema
            # (this takes care of ordering the fields properly as well)
            clean_df = df[fields.keys()]

            # set all dtypes to generic "object" so they can hold "NA"
            clean_df = clean_df.astype(object)

            # convert all NaN to NA, use this context and infer_objects to avoid a warning
            # see: https://stackoverflow.com/a/78066237/3873885
            with pd.option_context("future.no_silent_downcasting", True):
                clean_df = clean_df.fillna("NA").infer_objects(copy=False)

            # iterate all fields and if integer, cast to int to remove .0
            for k, v in fields.items():
                if v["type"] == "integer":
                    clean_df[k] = clean_df[k].apply(lambda x: int(x) if x != "NA" else "NA")

            clean_df.to_csv(data_path, index=False)

class DataResource():

    def __init__(self, resource_file=None, json_definition=None):

        if resource_file:
            with open(resource_file, "r") as o:
                data = json.load(o)
            self.schema = data
        elif json_definition:
            self.schema = json_definition
        else:
            self.schema = None
        self.variable_extras = self._load_variable_extras()

    def _load_variable_extras(self):
        data = {}
        with open(DATA_DIR / "registry" / "variables.json", "r") as o:
            data = json.load(o)
        return data

    def oeps_type_to_schema_type(self, s):
        """ Convert the type stored in the data dictionary to one that aligns
        with the table schema. """

        if s == "Integer":
            return 'integer'
        elif s in ['Date', 'String', 'Character / Factor', 'String / Factor']:
            return 'string'
        elif s == 'Boolean':
            return 'boolean'
        elif s in ['Float', 'Double', 'Numeric']:
            return 'number'
        else:
            raise TypeError("unrecognized type " + s + ".")

    def oeps_type_to_bq_type(self, s):
        """ Convert the type stored in the data dictionary to one that aligns
        with the big query data type list. """

        if s == "Date":
            return "DATE"
        elif s in ["Character / Factor", "String / Factor"]:
            return "STRING"
        elif s == "Binary":
            return "BOOLEAN"
        else:
            return s.upper()

    def make_fields(self, data_dict):
        """ make_fields takes in a Pandas DataFrame with
        Variable, Type, Example, Description, Data Limitations,
        Theme, Source Long, and Comments columns and returns a
        "fields" array for the data dictionary.  """

        SKIP_FIELDS = [
            # 'GEOID',
            'G_STATEFP',
            'STUSPS',
            'TRACTCE',
            'STATEFP',
            'COUNTYFP',
            'ZIP',
        ]

        fields = []
        records = data_dict.to_dict('records')
        for record in records:
            name = record.get('Variable')
            if name in SKIP_FIELDS:
                continue

            title = name
            if name in self.variable_extras and self.variable_extras[name]['title']:
                title = self.variable_extras[name]['title']
            longitudinal = True if record.get('Longitudinal', "").lower() == "x" else False
            analysis = True if record.get('Analysis', "").lower() == "x" else False
            field = {
                'title': title,
                'name': name,
                'src_name': record.get('Variable'),
                'type': self.oeps_type_to_schema_type(record.get('Type')),
                'example': str(record.get('Example')),
                'description': record.get('Description'),
                'constraints': record.get('Data Limitations'),
                'theme': record.get('Theme'),
                'source': record.get('Source'),
                'source_long': record.get('Source Long'),
                'oeps_v1_table': record.get('OEPS '),
                'comments': record.get('Comments'),
                'metadata_doc_url': record.get('Metadata Location'),
                'longitudinal': longitudinal,
                'analysis': analysis,
            }

            fields.append(field)

        return fields
    
    def sort_fields(self):
        """ Look in the schema, find the source file, and sort the field list based on the file header."""

        print(self.schema['path'])
        df = pd.read_csv(self.schema['path'])
        headers = list(df)
        schema_fields = [i['name'] for i in self.schema['schema']['fields']]


        ## CHECK WHETHER THERE ARE MISSING FIELDS IN THE CSV OR SCHEMA
        extra_in_csv = [i for i in headers if i not in schema_fields]
        extra_in_schema = [i for i in schema_fields if i not in headers]

        presence_test_passed = False
        if not extra_in_csv and not extra_in_schema:
            print("  PASS: all expected fields are present in CSV and in schema")
            presence_test_passed = True

        else:
            print("  FAIL: discrepancies between fields that are present in CSV and in schema")
            print(f"    extra_in_csv: {extra_in_csv}")
            print(f"    extra_in_schema: {extra_in_schema}")

        if not presence_test_passed:
            return
        
        ## SET THE ORDER OF THE FIELDS IN SCHEMA TO MATCH CSV
        if not headers == schema_fields:
            reordered_fields = []
            for col_name in headers:
                for field_def in self.schema['schema']['fields']:
                    if field_def['name'] == col_name:
                        reordered_fields.append(field_def)
            self.schema['schema']['fields'] = reordered_fields
            schema_fields = [i['name'] for i in self.schema['schema']['fields']]
        
        print(f"  FIELD ORDER MATCH: {headers == schema_fields}")

    def create_from_oeps_xlsx_data_dict(self, xlsx_file, dest_directory):
        """ Creates a schema from our pre-made external data dictionaries. """

        REPO_BASE_URL = "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/full_tables"
        GY_LOOKUP = {
            'S': [1980, 1990, 2000, 2010, 'Latest'],
            'C': [1980, 1990, 2000, 2010, 'Latest'],
            'T': [1980, 1990, 2000, 2010, 'Latest'],
            'Z': ['Latest'],
        }
        GEO_LOOKUP = {
            "S": "State",
            "C": "Census Tract",
            "T": "County",
            "Z": "Zip-Code Tabulation Area (ZCTA)",
        }

        #### Script ----
        geo = os.path.basename(xlsx_file).split("_")[0]

        output_files = []

        def _generate_title(geo, year):
            
            try:
                title = f"OEPS Data Aggregated by {GEO_LOOKUP[geo]} ({year})"
            except KeyError:
                raise KeyError(f"invalid geography {geo}")

            return title
        
        def _generate_description(geo, year):

            try:
                desc = f"This CSV aggregates all {year} data variables from the OEPS v2 release at the {GEO_LOOKUP[geo]} level."
            except KeyError:
                raise KeyError(f"invalid geography {geo}")

            return desc

        # Create and save a table for each pair.
        for year in GY_LOOKUP[geo]:

            # Generate the relevant path.
            csv_name = f'{geo}_{year}.csv'
            print(f'making table definition for {csv_name}!')

            # Path to the CSV dataset itself
            dataset_path = f"{REPO_BASE_URL}/{csv_name}"

            # Read in data
            data_dict = pd.read_excel(xlsx_file)
            data_dict = data_dict.fillna("")

            # Filter to only relevant rows
            data_dict = data_dict[(data_dict[year] == 'x')]

            dataset = "tabular"

            title = _generate_title(geo, year)
            description = _generate_description(geo, year)

            self.schema = {
                'bq_dataset_name': dataset,
                'bq_table_name':  f'{geo}_{year}',
                'name': f'{geo}-{year}'.lower(),
                'path': dataset_path,
                'title': title,
                'description': description,
                'scheme': 'file',
                'schema': {
                    'primaryKey': 'HEROP_ID',
                    # very sloppy way of handling sloppy data, for now.......
                    'missingValues': ["NA"],
                    'fields': self.make_fields(data_dict)
                }
            }

            self.sort_fields()

            out_path = os.path.join(dest_directory, f'{dataset}_{geo}_{year}.json')
            self.export_schema(out_path)

            output_files.append(out_path)

        return output_files

    def export_schema(self, path):
        """ Dump this object's schema to a JSON file. """
            
        with open(path, 'w') as outfile:
            json.dump(self.schema, outfile, indent=4)

    def load_rows_from_file(self, verbose=False):
        """Loads all data from the file indicated in the provided schema, and
        performs some data validation and cleaning along the way.

        Returns a list of serialized JSON strings, and a list of error messages"""

        rows, errors = [], []

        dataset_path = self.schema['path']

        # get the format, assume CSV if not present
        format = self.schema.get("format", "csv")

        if format not in ["csv", "shp"]:
            errors.append(f"Invalid dataset format: {format}")
            return rows, errors

        try:
            if format == "shp":
                if isinstance(dataset_path, list):
                    dataset_path = [i for i in dataset_path if i.endswith(".shp")][0]
                    df = gpd.read_file(dataset_path)
                elif dataset_path.endswith(".zip"):
                    df = gpd.read_file(f"/vsizip/vsicurl/{dataset_path}")
            elif format == "csv":
                df = pd.read_csv(dataset_path, dtype='object')

        except Exception as e:
            errors.append(f"error reading file: {str(e)}")
            return rows, errors

        # use any src_name properties to rename columns where needed
        field_mapping = {}
        for f in self.schema['schema']['fields']:
            src_name = f.get('src_name')
            if src_name:
                field_mapping[src_name] = f['name']
            else:
                errors.append(f"warning: {f['name']} missing required src_name attribute")
        if field_mapping:
            df.rename(columns=field_mapping, inplace=True)

        # remove any input columns that are not in the schema
        drop_columns = [i for i in df.columns if i not in field_mapping.values()]
        if drop_columns:
            errors.append(f"{len(drop_columns)} source columns missing from schema: " + \
                        ", ".join(drop_columns))
        df.drop(columns=drop_columns, inplace=True)

        # check for schema columns that are not found in the source data
        missing_columns = [i for i in field_mapping.values() if i not in df.columns]
        if missing_columns:
            errors.append(f"{len(missing_columns)} schema fields missing from source: " +\
                        ", ".join(missing_columns))

        # iterate fields and zfill columns where needed
        for f in self.schema['schema']['fields']:
            if f.get('zfill', False) is True:
                df[f['name']] = df[f['name']].apply(lambda x: str(x).zfill(f['max_length']))

        field_types = {f['name']: f['type'] for f in self.schema['schema']['fields']}
        bq_field_types = {f['name']: BQ_TYPE_LOOKUP[f['type']] for f in self.schema['schema']['fields']}

        # iterate the dataframe and turn each row into a dict that gets appened to rows.
        # this list is later loaded as if it were a newline-delimited JSON file.
        rows = []
        for i in df.index:
            row = {col: df.at[i, col] for col in df.columns if not col == "geom"}

            # cast all values to strings for string fields. necessary because some
            # NULL shapefile attribute values were interpreted as float('nan'), which
            # breaks json parsing
            for k in row:
                val_str = str(row[k])
                # test for float('nan') type, set to None
                if val_str == 'nan':
                    row[k] = None
                if "NA" in val_str:
                    row[k] = None
                # handle some infinite number variations
                if 'inf' in val_str.lower():
                    row[k] = None
                if row[k]:
                    if field_types[k] == "string":
                        row[k] = val_str
                    if field_types[k] == "integer":
                        try:
                            row[k] = int(row[k])
                        except ValueError:
                            # special handle string values like '23493.3434'
                            row[k] = int(round(float(row[k])))
                    if field_types[k] == "number":
                        row[k] = float(row[k])
                    if field_types[k] == "boolean":
                        if row[k] in [1, "1", "Yes", "YES", "yes", True, 'True', 'TRUE', 'true']:
                            row[k] = True
                        elif row[k] in [0, "0", "No", "NO", "no", False, 'False', 'FALSE', 'false']:
                            row[k] = False
                        else:
                            row[k] = None
                    if bq_field_types[k] == "DATE":
                        try:
                            val = datetime.strptime(row[k], "%m/%d/%Y").strftime("%Y-%m-%d")
                            row[k] = val
                        except Exception as e:
                            raise e

            # handle geometry column by dumping it to GeoJSON string. this fixes
            # some Polygon format errors that occurred with the default WKT that
            # GeoPandas returns for shapes. geom.__geo_interface__ is a shapely thing.
            if 'geom' in df.columns:
                row['geom'] = json.dumps(df.at[i, 'geom'].__geo_interface__)
            try:
                rows.append(json.dumps(row))
            except Exception as e:
                for k, v in row.items():
                    print(field_types[k])
                    print(k, v, type(v))
                    print(isinstance(v, numpy.int64))
                raise(e)

        return rows, errors