import os
import json
import numpy
import pandas as pd
import geopandas as gpd


class DataResource():

    def __init__(self, resource_file=None):

        if resource_file:
            with open(resource_file, "r") as o:
                data = json.load(o)
            self.schema = data
        else:
            self.schema = None

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

    def make_field_entry(self, data_dict_row):
        """ Compose a full field entry from a row of an oeps data dict. """

        field = {
            'name': data_dict_row.loc['Variable'],
            'src_name': data_dict_row.loc['Variable'],
            'type': self.oeps_type_to_schema_type(data_dict_row.loc['Type']),
            'example': str(data_dict_row.loc['Example']),
            'description': data_dict_row.loc['Description'],
            'constraints': data_dict_row.loc['Data Limitations'],
            'theme': data_dict_row.loc['Theme'],
            'source': data_dict_row.loc['Source Long'],
            'comments': data_dict_row.loc['Comments'],
            'bq_data_type': self.oeps_type_to_bq_type(data_dict_row.loc['Type'])
        }

        # fix float('nan') ("not a number") values which seem to pop up.
        # checking if a value equals itself is the best test for NaN (?!)
        for k in field:
            if field[k] != field[k]:
                field[k] = None
        return field

    def make_fields(self, data_dict):
        """ make_fields takes in a Pandas DataFrame with
        Variable, Type, Example, Description, Data Limitations,
        Theme, Source Long, and Comments columns and returns a
        "fields" array for the data dictionary.  """

        SKIP_FIELDS = [
            'GEOID',
            'G_STATEFP',
            'STUSPS',
            'TRACTCE',
            'STATEFP',
            'COUNTYFP',
            'ZIP',
        ]

        fields = []

        for row in range(0, len(data_dict)):

            if data_dict.iloc[row].loc['Variable'] in SKIP_FIELDS:
                continue
            fields.append(self.make_field_entry(data_dict.iloc[row]))

        return fields

    def create_from_oeps_xlsx_data_dict(self, xlsx_file, dest_directory):
        """ Creates a schema from our pre-made external data dictionaries. """

        REPO_BASE_URL = "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/full_tables"
        GY_LOOKUP = {
            'S': [1980, 1990, 2000, 2010, 'Latest'],
            'C': [1980, 1990, 2000, 2010, 'Latest'],
            'T': [1980, 1990, 2000, 2010, 'Latest'],
            'Z': ['Latest'],
        }

        #### Script ----
        geo = os.path.basename(xlsx_file).split("_")[0]

        output_files = []

        # Create and save a table for each pair.
        for year in GY_LOOKUP[geo]:

            # Generate the relevant path.
            csv_name = f'{geo}_{year}.csv'
            print(f'making table definition for {csv_name}!')

            # Path to the CSV dataset itself
            dataset_path = os.path.join('csv', csv_name)
            dataset_path = f"{REPO_BASE_URL}/{csv_name}"

            # Read in data
            data_dict = pd.read_excel(xlsx_file)

            # Filter to only relevant rows
            data_dict = data_dict[(data_dict[year] == 'x')]

            dataset = "tabular"

            self.schema = {
                'bq_dataset_name': dataset,
                'bq_table_name':  f'{geo}_{year}',
                'name': f'{geo}-{year}',
                'path': dataset_path,
                'schema': {
                    'primaryKey': 'HEROP_ID',
                    'fields': self.make_fields(data_dict)
                }
            }

            out_path = os.path.join(dest_directory, f'{dataset}_{geo}_{year}.json')
            self.export_schema(out_path)

            output_files.append(out_path)

        return output_files

    def export_schema(self, path):
        """ Dump this object's schema to a JSON file. """
            
        with open(path, 'w') as outfile:
            json.dump(self.schema, outfile, indent=4)

    def load_rows_from_file(self):
        """Loads all data from the file indicated in the provided schema, and
        performs some data validation and cleaning along the way.

        Returns a list of serialized JSON strings, and a list of error messages"""

        rows, errors = [], []

        dataset_path = self.schema['path']

        try:
            if dataset_path.endswith('.shp'):
                df = gpd.read_file(dataset_path)
            elif dataset_path.endswith('.csv'):
                # set all columns as object type
                df = pd.read_csv(dataset_path, dtype='object')
            else:
                print(f"Invalid dataset: {dataset_path}")
                return
        except Exception as e:
            errors.append(str(e))
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
        drop_columns = [i for i in df.columns if not i in field_mapping.values()]
        if drop_columns:
            errors.append(f"{len(drop_columns)} source columns missing from schema: " + \
                        ", ".join(drop_columns))
        df.drop(columns=drop_columns, inplace=True)

        # check for schema columns that are not found in the source data
        missing_columns = [i for i in field_mapping.values() if not i in df.columns]
        if missing_columns:
            errors.append(f"{len(missing_columns)} schema fields missing from source: " +\
                        ", ".join(missing_columns))

        # iterate fields and zfill columns where needed
        for f in self.schema['schema']['fields']:
            if f.get('zfill', False) is True:
                df[f['name']] = df[f['name']].apply(lambda x: str(x).zfill(f['max_length']))

        field_types = {f['name']: f['type'] for f in self.schema['schema']['fields']}

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