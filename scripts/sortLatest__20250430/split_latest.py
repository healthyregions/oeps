import json
import pandas as pd
from pathlib import Path

geo_lookup = {
    "S": {
        "geodata_source": "states-2018",
        "latest_csv": "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/refs/tags/v2.0/data_final/full_tables/S_Latest.csv"
    },
    "C": {
        "geodata_source": "counties-2018",
        "latest_csv": "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/refs/tags/v2.0/data_final/full_tables/C_Latest.csv"
    },
    "T": {
        "geodata_source": "tracts-2018",
        "latest_csv": "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/refs/tags/v2.0/data_final/full_tables/T_Latest.csv"
    },
    "Z": {
        "geodata_source": "zctas-2018",
        "latest_csv": "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/refs/tags/v2.0/data_final/full_tables/Z_Latest.csv"
    },
}

table_source_update = {}

base_path = Path("../../backend/oeps")
table_cache_path = Path("../../backend/.cache/tables")

for abbr, info in geo_lookup.items():
    print(abbr)
    lookup = pd.read_csv(f"year-lookups/{abbr}_sort-latest.csv")
    sdf = pd.read_csv(info["latest_csv"])

    years = list(lookup["Year"].unique())

    var_lookup = {i: ["HEROP_ID"] + lookup.loc[lookup['Year'] == i]['Variable'].to_list() for i in years}

    for y, vars in var_lookup.items():
        print(y, vars)
        table_source_name = f"{str(y)}-{abbr.lower()}-latest-split"
        table_source_def = {
            "bq_dataset_name": "tabular",
            "bq_table_name": table_source_name,
            "name": table_source_name,
            "path": f"https://herop-oeps.s3.us-east-2.amazonaws.com/data/tables/{table_source_name}.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "title": table_source_name,
            "description": f"This CSV aggregates all 1980 data variables from the OEPS v2 release at the {abbr} level.",
            "year": "1980",
            "geodata_source": info["geodata_source"]
        }
        try:
            df = sdf[vars]
            df.to_csv(Path(table_cache_path, f"{table_source_name}.csv"), index=False, na_rep="NA")
            for v in vars:
                table_source_update[v] = table_source_update.get(v, []) + [table_source_name]

            with open(Path(base_path, f"registry/table_sources/{table_source_name}.json"), "w") as o:
                json.dump(table_source_def, o, indent=2)
        except Exception as e:
            print("ERROR:::", e)

with open(Path(base_path, "registry/variables.json"), "r") as o:
    variables = json.load(o)

for k, v in variables.items():
    # remove all old references to Latest files, etc
    print(k)
    v['table_sources'] = [i for i in v['table_sources'] if i not in [
        's-latest',
        'c-latest',
        't-latest',
        'z-latest',
    ]]

    # now add the new table sources
    v['table_sources'] += table_source_update.get(k, [])
    newlist = []
    for i in v['table_sources']:
        if i not in newlist:
            newlist.append(i)
    v['table_sources'] = newlist

with open(Path(base_path, "registry/variables.json"), "w") as o:
    json.dump(variables, o, indent=2)