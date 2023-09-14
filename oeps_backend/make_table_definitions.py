import os
from glob import glob
import argparse
import pandas as pd
import json

from oeps_backend.utils import TABLE_DEF_DIR

#### Constants ----

# The following constants can be updated as needed for table generation
# All possible duples of GEOGRAPHY and RELEVANT_YEAR will be used by the program,
# so set excluded pairings in EXCLUDED_COMBOS

GY_LOOKUP = {
	'S': [1980, 1990, 2000, 2010, 'Latest'],
	'C': [1980, 1990, 2000, 2010, 'Latest'],
	'T': [1980, 1990, 2000, 2010, 'Latest'],
	'Z': ['Latest'],
}

SKIP_GEO_FIELDS = [
	'GEOID',
	'G_STATEFP',
	'STUSPS',
	'TRACTCE',
	'STATEFP',
	'COUNTYFP',
	'ZIP',
]

#### Helper Functions ----

# make_fields takes in a Pandas DataFrame with
# Variable, Type, Example, Description, Data Limitations,
# Theme, Source Long, and Comments columns and returns a
# "fields" array for the data dictionary.
def make_fields(data_dict):
	fields = []

	for row in range(0, len(data_dict)):

		if data_dict.iloc[row].loc['Variable'] in SKIP_GEO_FIELDS:
			continue
		fields.append(make_field_entry(data_dict.iloc[row]))

	return(fields)

# make_field_entry is called row-by-row by make_fields 
# to return an additional "field" for the fields array.
def make_field_entry(data_dict_row):
	field = {
		'name': data_dict_row.loc['Variable'],
		'src_name': data_dict_row.loc['Variable'],
		'type': to_schema_type(data_dict_row.loc['Type']),
		'example': str(data_dict_row.loc['Example']),
		'description': data_dict_row.loc['Description'],
		'constraints': data_dict_row.loc['Data Limitations'],
		'theme': data_dict_row.loc['Theme'],
		'source': data_dict_row.loc['Source Long'],
		'comments': data_dict_row.loc['Comments'],
		'bq_data_type': to_bq_type(data_dict_row.loc['Type'])
	}

	# fix float('nan') ("not a number") values which seem to pop up.
	# checking if a value equals itself is the best test for NaN (?!)
	for k in field:
		if field[k] != field[k]:
			field[k] = None
	return(field)

# Convert the type stored in the data dictionary to one that aligns
# with the table schema.
def to_schema_type(s):
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

# Convert the type stored in the data dictionary to one that aligns
# with the big query data type list.
def to_bq_type(s):
	if s == "Date":
		return "DATE"
	elif s in ["Character / Factor", "String / Factor"]:
		return "STRING"
	elif s == "Binary":
		return "BOOLEAN"
	else:
		return s.upper()

def make_table_definitions(xlsx_file):

	#### Script ----
	geo = os.path.basename(xlsx_file).split("_")[0]

	# Create and save a table for each pair.
	for year in GY_LOOKUP[geo]:

		# Generate the relevant path.
		csv_name = f'{geo}_{year}.csv'
		print(f'making table definition for {csv_name}!')

		# Path to the CSV dataset itself
		dataset_path = os.path.join('csv', csv_name)
		gh_raw_base = "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/full_tables"
		dataset_path = f"{gh_raw_base}/{csv_name}"

		# Read in data
		data_dict = pd.read_excel(xlsx_file)

		# Filter to only relevant rows
		data_dict = data_dict[(data_dict[year] == 'x')]

		dataset = "tabular"

		table = {
			'bq_dataset_name': dataset,
			'bq_table_name':  f'{geo}_{year}',
			'data_source': dataset_path,
			'fields': make_fields(data_dict)
		}

		out_path = os.path.join(TABLE_DEF_DIR, f'{dataset}_{geo}_{year}.json')
		with open(out_path, 'w+') as outfile:
			json.dump(table, outfile, indent=4)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--input")
	args = parser.parse_args()

	if args.input:
		if os.path.isdir(args.input):
			paths = glob(os.path.join(args.input, "*.xlsx"))
		elif os.path.isfile(args.input):
			paths = [args.input]
		else:
			print("invalid dict file input")
			exit()
	else:
		print("using preset remote dicts")
		paths = [
			"https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/S_Dict.xlsx",
			"https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/C_Dict.xlsx",
			"https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/T_Dict.xlsx",
			"https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/Z_Dict.xlsx",
		]

	for path in paths:
		print(path)
		make_table_definitions(path)
