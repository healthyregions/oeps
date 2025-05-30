import copy
import json
from pathlib import Path

base_path = Path("../../backend/oeps")
vars_path = Path(base_path, "registry/variables.json")

with open(vars_path, "r") as o:
    variables = json.load(o)

with open("./variable-collapse-lookup.json", "r") as o:
    lookup = json.load(o)

new_variables = {}
replaced_variables = {}
csvs_to_update = {}

for new, olds in lookup.items():
    new_entry = copy.deepcopy(variables[olds[0]])
    new_entry["name"] = new
    new_entry["table_sources"] = []
    for old in olds:
        print(f"{old} -> {new}")
        new_entry["table_sources"] += variables[old]["table_sources"]

        for i in variables[old]["table_sources"]:
            csvs_to_update[i] = csvs_to_update.get(i, []) + [{
                    "old-name": old,
                    "new-name": new,
            }]

        replaced_variables[old] = new

    new_variables[new] = new_entry

with open("new-variables.json", "w") as o:
    json.dump(new_variables, o, indent=2)

with open("csvs-to-update.json", "w") as o:
    json.dump(csvs_to_update, o, indent=2)

for fname, updates in csvs_to_update.items():
    path = f"../../backend/.cache/tables/{fname}.csv"
    with open(path, "r") as f:
        first_line, remainder = f.readline(), f.read()

    # change the column names in the first line of the CSV directly
    for u in updates:
        first_line = first_line.replace(u["old-name"], u["new-name"])

    with open(path, "w") as o:
        o.write(first_line)
        o.write(remainder)

new_variables_full = {}

for k, v in variables.items():
    if k in replaced_variables:
        new_variables_full[replaced_variables[k]] = new_variables[replaced_variables[k]]
    else:
        new_variables_full[k] = v

with open(vars_path, "w") as o:
    json.dump(new_variables_full, o, indent=2)
