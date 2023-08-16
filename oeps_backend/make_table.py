from itertools import product
import pandas as pd
import json

#### Constants ----

# The following constants can be updated as needed for table generation
# All possible duples of GEOGRAPHY and RELEVANT_YEAR will be used by the program,
# so set excluded pairings in EXCLUDED_COMBOS

GEOGRAPHY = ['T', 'Z', 'S', 'C']
RELEVANT_YEAR = [1980, 1990, 2000, 2010, 'Latest']
EXCLUDED_PAIRS = [('C', 'Latest'), ('C', 1980), ('C', 1990), ('C', 2000), ('C', 2010)]

#### Helper Functions ----

# make_fields takes in a Pandas DataFrame with
# Variable, Type, Example, Description, Data Limitations,
# Theme, Source Long, and Comments columns and returns a
# "fields" array for the data dictionary.
def make_fields(data_dict):
	fields = []

	for row in range(0, len(data_dict)):
		fields.append(make_field_entry(data_dict.iloc[row]))

	return(fields)

# make_field_entry is called row-by-row by make_fields 
# to return an additional "field" for the fields array.
def make_field_entry(data_dict_row):
	field = {
		'name': data_dict_row.loc['Variable'],
		'type': to_schema_type(data_dict_row.loc['Type']),
		'example': str(data_dict_row.loc['Example']),
		'description': data_dict_row.loc['Description'],
		'constraints': data_dict_row.loc['Data Limitations'],
		'theme': data_dict_row.loc['Theme'],
		'source': data_dict_row.loc['Source Long'],
		'comments': data_dict_row.loc['Comments'],
		'bq_data_type': to_bq_type(data_dict_row.loc['Type'])
	}

	return(field)

# Convert the type stored in the data dictionary to one that aligns
# with the table schema.
def to_schema_type(s):
	match s:
		case "Integer":
			return 'integer'
		case ('Date' | 'String' | 'Character / Factor' | 'String / Factor'):
			return 'string'
		case 'Binary':
			return 'boolean'
		case ('Float' | 'Double' | 'Numeric'):
			return 'numeric'
		case _:
			raise TypeError("unrecognized type " + s + ".")

# Convert the type stored in the data dictionary to one that aligns
# with the big query data type list.
def to_bq_type(s):
	match s:
		case "Date":
			return "TIMESTAMP"
		case ("Character / Factor" | "String / Factor"):
			return "STRING"
		case "Binary":
			return "BOOLEAN"
		case _:
			return s.upper()

#### Script ----

# Acquire all relevant pairs of geography and year.
pairs_to_grab = list(product(GEOGRAPHY, RELEVANT_YEAR))

# Exclude irrelevant pairs
for exclusion in EXCLUDED_PAIRS:
	if exclusion in pairs_to_grab:
		pairs_to_grab.remove(exclusion)

# Create and save a table for each pair.
for geo, year in pairs_to_grab:

	# Generate the relevant path.
	path = f'./data_local/dictionaries/{geo}_Dict.xlsx'
	print(f'working on {geo}_{year}.csv!')


	# Read in data
	data_dict = pd.read_excel(path)

	# Filter to only relevant rows
	data_dict = data_dict[(data_dict[year] == 'x')]

	table = {
		'bq_dataset_name': 'csv',
		'bq_table_name':  f'{geo}_{year}',
		'data_source': path,
		'fields': make_fields(data_dict)
	}

	with open(f'table_definitions\\csv_{geo}_{year}.json', 'w+') as outfile:
		json.dump(table, outfile, indent=4)