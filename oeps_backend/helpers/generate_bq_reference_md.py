import os
import json
import dotenv
from glob import glob
from pathlib import Path

dotenv.load_dotenv()

TABLE_DEF_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'table_definitions')

if __name__ == "__main__":

    project_id = os.getenv("BQ_PROJECT_ID")

    datasets = {}

    files = glob(TABLE_DEF_DIR + "/*.json")

    for f in files:
        with open(f, "r") as openf:
            d = json.load(openf)

        ds_name = d['bq_dataset_name']
        t_name = d['bq_table_name']

        if not ds_name in datasets:
            datasets[ds_name] = {}

        if not t_name in datasets[ds_name]:
            datasets[ds_name][t_name] = []

        for f in d['fields']:
            datasets[ds_name][t_name].append({
                'name': f.get('name'),
                'data_type': f.get('bq_data_type'),
                'description': f.get('description'),
                'source': f.get('source')
            })

    out_path = Path(Path(__file__).resolve()).parent.parent.parent / "BQ-Reference.md"
    with open(out_path, 'w') as openf:

        ds_ct = len(datasets)
        openf.write(f"""# Project Id: {project_id}

{ds_ct} dataset{'s' if ds_ct != 1 else ''} in this project: {', '.join(datasets.keys())}

""")
        for ds in datasets:
            t_ct = len(datasets[ds])
            openf.write(f"""## {ds}

{t_ct} table{'s' if t_ct != 1 else ''} in this dataset.

""")

            for t in datasets[ds]:

                c_ct = len(datasets[ds][t])
                openf.write(f"""### {t}

ID: `{project_id}.{ds}.{t}`

{c_ct} column{'s' if c_ct != 1 else ''} in this table.

Name|Data Type|Description|Source
-|-|-|-
""")

                for c in datasets[ds][t]:
                    openf.write(f"{c['name']}|{c['data_type']}|{c['description']}|{c['source']}\n")

                openf.write("\n")