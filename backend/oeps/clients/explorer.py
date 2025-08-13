import os
from pathlib import Path

from natsort import natsorted
import pandas as pd

from oeps.clients.s3 import sync_to_s3, get_base_url
from oeps.config import DATA_DIR
from oeps.utils import write_json, make_id
from .registry import Registry


class Explorer:
    def __init__(
        self, registry: Registry = Registry, root_dir: Path = Path(".explorer")
    ):
        self.registry = registry
        self.root_dir = root_dir
        self.dataframe_lookup = {}

    def build_map_config(self, upload: bool = False):
        csv_dir = Path(self.root_dir, "public", "csv")
        for f in csv_dir.glob("_*.csv"):
            os.remove(f)

        config_dir = Path(self.root_dir, "config")
        config_dir.mkdir(parents=True, exist_ok=True)

        # begin by creating a lookup for all geodata sources that will be used in the explorer.
        # only source files with an "explorer_config" entry will be used
        geodata_lookup = {}
        for id, data in self.registry.geodata_sources.items():
            entry = data.get("explorer_config")
            if entry:
                entry["summary_level"] = data["summary_level"]
                geodata_lookup[entry["summary_level"]] = entry

        # iterate all variables and create a lookup for all combinations of data sources
        # in which each variable has a value
        variables = {
            k: v
            for k, v in self.registry.variables.items()
            if k not in ["HEROP_ID", "GEOID"]
        }
        ds_combo_lookup = {}
        for k, v in variables.items():
            use_sources = [
                self.registry.find_table_source(k, "state"),
                self.registry.find_table_source(k, "county"),
                self.registry.find_table_source(k, "zcta"),
                self.registry.find_table_source(k, "tract"),
            ]

            latest_sources = [i for i in use_sources if i]
            if latest_sources:
                ds_group_code = "__".join([i["name"] for i in latest_sources])
                ds_combo_lookup[ds_group_code] = ds_combo_lookup.get(
                    ds_group_code, []
                ) + [k]

        ## create a lookup of all variables and the combined data sources that they exist for
        variables_to_ds_combos = {}
        for k, v in ds_combo_lookup.items():
            for i in v:
                variables_to_ds_combos[i] = k

        ## need to create a single CSV for each geog in the list, that only has the relevant fields
        ## and add these to the table entries in the source definition
        for k, field_list in ds_combo_lookup.items():
            field_list.insert(0, "HEROP_ID")
            for ds in k.split("__"):
                ds_schema = self.registry.table_sources[ds]

                filename = f"_{make_id()}"
                out_path = Path(csv_dir, f"{filename}.csv")

                print(f"writing {out_path}")
                read_path = ds_schema["path"]
                if read_path.startswith("tables"):
                    read_path = Path(DATA_DIR, read_path)
                df = self.dataframe_lookup.get(ds, pd.read_csv(read_path))
                df_filtered = df.filter(field_list)

                ## write CSV to local
                df_filtered.to_csv(out_path, index=False)

                table_entry = {
                    "file": out_path.name,
                    "type": "characteristic",
                    "join": "HEROP_ID",
                }
                geodata_lookup[ds_schema["summary_level"]]["tables"][k] = table_entry

        out_variables = {
            k: {
                "variable": v["title"],
                "numerator": variables_to_ds_combos[k],
                "nProperty": k,
                "theme": self.registry.metadata.get(v.get("metadata", ""))["theme"],
                "metadataUrl": self.registry.metadata[v["metadata"]]["url"],
            }
            for k, v in variables.items()
            if k in variables_to_ds_combos
        }

        # hacky method for creating the output geodata source list in descending order of
        # spatial resolution
        s_geodata = [
            i for i in geodata_lookup.values() if i["summary_level"] == "state"
        ]
        c_geodata = [
            i for i in geodata_lookup.values() if i["summary_level"] == "county"
        ]
        z_geodata = [i for i in geodata_lookup.values() if i["summary_level"] == "zcta"]
        t_geodata = [
            i for i in geodata_lookup.values() if i["summary_level"] == "tract"
        ]
        out_sources = {"sources": []}
        for sorted_src_list in [s_geodata, c_geodata, z_geodata, t_geodata]:
            if len(sorted_src_list) > 0:
                out_sources["sources"].append(sorted_src_list[0])

        if upload:
            prefix = "explorer/csvs"
            sync_to_s3(csv_dir, prefix, True)

            base_url = get_base_url()
            for source in out_sources["sources"]:
                for t in source["tables"].values():
                    t["file"] = f"{base_url}{prefix}/{t['file']}"

        write_json(out_sources, Path(config_dir, "sources.json"))

        write_json(list(out_variables.values()), Path(config_dir, "variables.json"))

    def build_docs_config(self):
        output = {}
        for theme, constructs in self.registry.theme_tree.items():
            output[theme] = {}
            for construct, metadata_entries in constructs.items():
                output[theme][construct] = []
                for id in metadata_entries:
                    metadata = self.registry.metadata[id]
                    geodata = set()
                    titles = set()
                    sources = set()
                    years = set()
                    for v in self.registry.variables.values():
                        if v["metadata"] == id:
                            for ts in v["table_sources"]:
                                years.add(ts.split("-")[1])
                                for p in [
                                    ("state", "State"),
                                    ("count", "County"),
                                    ("tract", "Tract"),
                                    ("zcta", "Zip"),
                                ]:
                                    if (
                                        p[0]
                                        in self.registry.table_sources[ts][
                                            "geodata_source"
                                        ]
                                    ):
                                        geodata.add(p[1])
                            sources.add(v["source"])
                            titles.add(v["title"])

                    sorted_geodata = [
                        i for i in ["Tract", "Zip", "County", "State"] if i in geodata
                    ]
                    if len(titles) > 0:
                        output[theme][construct].append(
                            {
                                "Variable Construct": construct,
                                "Variable Proxy": metadata["proxy"],
                                "Variables": natsorted(list(titles)),
                                "Source": "; ".join(sources),
                                "Metadata": id,
                                "Spatial Scale": ", ".join(sorted_geodata),
                                "Years": ", ".join(natsorted(years)),
                            }
                        )

        csv_downloads = {"state": [], "county": [], "zcta": [], "tract": []}
        for ts in self.registry.table_sources.values():
            filename = Path(ts["path"]).name
            csv_downloads[ts["summary_level"]].append(
                {
                    "name": filename,
                    "url": f"https://github.com/healthyregions/oeps/raw/refs/heads/main/backend/oeps/data/tables/{filename}",
                    "year": ts["year"],
                }
            )
        for csv_list in csv_downloads.values():
            csv_list.sort(key=lambda k: k["year"])

        meta_dir = Path(self.root_dir, "meta")
        meta_dir.mkdir(exist_ok=True)

        write_json(output, Path(meta_dir, "variables.json"))
        write_json(csv_downloads, Path(meta_dir, "csvDownloads.json"))
