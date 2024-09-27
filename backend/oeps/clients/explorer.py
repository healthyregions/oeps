from pathlib import Path

import pandas as pd

from oeps.utils import load_json, write_json


class Explorer():

    def __init__(self, root_dir: Path=None):

        self.root_dir = root_dir if root_dir else Path(".explorer")
        self.df_lookup = {}

    def build_config(self, schema_dir: Path, write_csvs: bool=True):

        csv_dir = Path(self.root_dir, "public", "csv")
        config_dir = Path(self.root_dir, "config")

        csv_dir.mkdir(parents=True, exist_ok=True)
        config_dir.mkdir(parents=True, exist_ok=True)

        source_lookup = {
            "state": {
                "csv_abbrev": "S",
                "variables": [],
                "explorer_config": {
                    "name": "US States",
                    "geodata": "cb_2018_us_state_20m.geojson",
                    "id": "HEROP_ID",
                    "bounds": [-125.109215, -66.925621, 25.043926, 49.295128],
                    "tables": {},
                },
            },
            "county": {
                "csv_abbrev": "C",
                "variables": [],
                "explorer_config": {
                    "name": "US Counties",
                    "geodata": "cb_2018_us_county_20m.geojson",
                    "id": "HEROP_ID",
                    "bounds": [-125.109215, -66.925621, 25.043926, 49.295128],
                    "tables": {},
                },
            },
            "zcta": {
                "csv_abbrev": "Z",
                "variables": [],
                "explorer_config": {
                    "name": "US Zip Codes",
                    "geodata": "Zip Codes [tiles]",
                    "tiles": "herop-lab.7o9tctx9",
                    "id": "HEROP_ID",
                    "bounds": [-125.109215, -66.925621, 25.043926, 49.295128],
                    "tables": {},
                },
            },
            "tract": {
                "csv_abbrev": "T",
                "variables": [],
                "explorer_config": {
                    "name": "US Tracts",
                    "geodata": "Tracts [tiles]",
                    "tiles": "herop-lab.0eeozlm3",
                    "id": "HEROP_ID",
                    "bounds": [-125.109215, -66.925621, 25.043926, 49.295128],
                    "tables": {},
                },
            },
        }

        ## load the schemas for all items and pull out the variable names
        for k, v in source_lookup.items():

            latest_csv = Path(schema_dir, f"tabular_{v['csv_abbrev']}_Latest.json")
            res_data = load_json(latest_csv)
            v['variables'] = [i['src_name'] for i in res_data['schema']['fields'] if i['theme'] != "Geography"]
            # v['variables'].insert(0, "HEROP_ID")

            print(k, len(v['variables']))
            print(len(v['variables']), len(set(v['variables'])))

        ## create a lookup of all variables and the source geogs that they exist for
        variables_to_geog_combos = {}
        for k, v in source_lookup.items():
            for i in v['variables']:
                variables_to_geog_combos[i] = variables_to_geog_combos.get(i, []) + [k]
        print(variables_to_geog_combos)

        ## reverse the above lookup, so concatenate source geog list is linked to all its variables
        geog_combos_to_variables = {}
        for k, v in variables_to_geog_combos.items():
            group_code = "-".join(v)
            geog_combos_to_variables[group_code] = geog_combos_to_variables.get(group_code, []) + [k]
        print(geog_combos_to_variables)

        ## need to create a single CSV for each geog in the list, that only has the relevant fields
        ## and add these to the table entries in the source definition
        for k, field_list in geog_combos_to_variables.items():
            field_list.insert(0, "HEROP_ID")
            print(f"splitting {k}:")
            for geog in k.split("-"):
                out_path = Path(csv_dir, f"{k}_{source_lookup[geog]['csv_abbrev']}.csv")
                print(out_path)

                latest_schema_path = Path(schema_dir, f"tabular_{source_lookup[geog]['csv_abbrev']}_Latest.json")
                latest_schema = load_json(latest_schema_path)

                if write_csvs:
                    df = self.df_lookup.get(geog, pd.read_csv(latest_schema['path']))
                    df_filtered = df.filter(field_list)
                    df_filtered.to_csv(out_path, index=False)

                table_entry = {
                    "file": out_path.name,
                    "type": "characteristic",
                    "join": "HEROP_ID",
                }
                source_lookup[geog]['explorer_config']['tables'][k] = table_entry

        ## Collect all variables, now that the numerator is known
        out_variables2 = {}
        for k, v in source_lookup.items():

            latest_csv = Path(schema_dir, f"tabular_{v['csv_abbrev']}_Latest.json")
            res_data = load_json(latest_csv)
            for field in res_data['schema']['fields']:
                if field['theme'] == "Geography":
                    continue
                id = field['src_name']
                if id not in out_variables2:
                    field_entry = {
                        "variable": field['title'],
                        "numerator": "-".join(variables_to_geog_combos[id]),
                        "nProperty": id,
                        "theme": field['theme'],
                        "metadataUrl": field.get('metadata_doc_url')
                    }
                    out_variables2[id] = field_entry


        for k, v in source_lookup.items():
            write_json(v['explorer_config'], Path(config_dir, 'sources', f"{k}.json"))

        write_json(list(out_variables2.values()), Path(config_dir, 'variables.json'))
