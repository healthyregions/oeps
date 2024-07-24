import json
from pathlib import Path

from oeps.utils import load_json, write_json

class Explorer():

    def build_config(self, schema_dir, output_dir):


        source_info = [
            {
                "id": "state",
                "name": "US States",
                "dataset": "cb_2018_us_state_20m.geojson",
                "join_id": "HEROP_ID",
                "bounds": [
                    -125.109215,
                    -66.925621,
                    25.043926,
                    49.295128
                ],
                "csv_abbrev": "S",
            },
            {
                "id": "county",
                "name": "US Counties",
                "dataset": "cb_2018_us_county_20m.geojson",
                "join_id": "HEROP_ID",
                "bounds": [
                    -125.109215,
                    -66.925621,
                    25.043926,
                    49.295128
                ],
                "csv_abbrev": "C",
            },
        ]

        out_variables = {}
        for source in source_info:

            out_source = {
                "name": source["name"],
                "geodata": source["dataset"],
                "id": source["join_id"],
                "bounds": source["bounds"],
                "tables": {}
            }

            table_files = Path(schema_dir).glob(f"*{source['csv_abbrev']}*.json")
            for path in table_files:

                table_data = load_json(path)
                table_name = table_data['name'].split("-")[1]

                year = path.stem.split("_")[-1]
                table_data = load_json(path)
                table_entry = {
                    "file": table_data['path'],
                    "type": "characteristic",
                    "join": "HEROP_ID",
                }
                out_source['tables'][table_name] = table_entry

                for field in table_data['schema']['fields']:
                    v = f"{field['name']} ({year})"
                    if v not in out_variables:
                        field_entry ={
                            "variable": f"{field['name']} ({year})",
                            "numerator": table_name,
                            "nProperty": field['src_name'],
                            "theme": field['theme'],
                            "year": field.get("year", year),
                            "binning": field.get("binning", "naturalBreaks"),
                            "numberOfBins": 8,
                            "colorScale": field.get("colorScale", "YlOrBr"),
                        }
                        out_variables[v] = field_entry
                    # out_variables.append(field_entry)

            write_json(out_source, Path(output_dir, 'sources', f"{source['id']}.json"))

        write_json(list(out_variables.values()), Path(output_dir, 'variables.json'))
