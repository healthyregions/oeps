from pathlib import Path

from natsort import natsorted
import pandas as pd

from oeps.utils import write_json
from .registry import Registry


class Explorer:
    def __init__(
        self, registry: Registry = Registry, root_dir: Path = Path(".explorer")
    ):
        self.registry = registry
        self.root_dir = root_dir
        self.dataframe_lookup = {}

    def build_map_config(self, write_csvs: bool = True):
        csv_dir = Path(self.root_dir, "public", "csv")
        csv_dir.mkdir(parents=True, exist_ok=True)

        config_dir = Path(self.root_dir, "config")
        config_dir.mkdir(parents=True, exist_ok=True)

        # begin by creating a lookup for all geodata sources that will be used in the explorer.
        # only source files with an "explorer_config" entry will be used
        geodata_lookup = {}
        for id, data in self.registry.geodata_sources.items():
            entry = data.get("explorer_config")
            if entry:
                entry["csv_abbrev"] = id[0]
                geodata_lookup[id] = entry

        # create lookup of all table data sources that are linked to a valid geodata_source
        table_lookup = {
            k: v
            for k, v in self.registry.table_sources.items()
            if v.get("geodata_source") in geodata_lookup
        }

        # iterate all variables and create a lookup for all combinations of data sources
        # in which each variable has a value
        variables = {
            k: v
            for k, v in self.registry.variables.items()
            if not self.registry.themes["Geography"] == v["construct"]
        }
        ds_combo_lookup = {}
        for k, v in variables.items():
            usable_sources = []
            for ds in v["table_sources"]:
                if ds in table_lookup:
                    usable_sources.append(ds)

            if len(usable_sources) > 0:
                ds_group_code = "__".join(usable_sources)
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
                ds_schema = table_lookup[ds]
                abbrev = ds_schema["geodata_source"][0]
                out_path = Path(csv_dir, f"{k}_{abbrev}.csv")

                if write_csvs:
                    print(f"writing {out_path}")
                    df = self.dataframe_lookup.get(ds, pd.read_csv(ds_schema["path"]))
                    df_filtered = df.filter(field_list)
                    df_filtered.to_csv(out_path, index=False)

                table_entry = {
                    "file": out_path.name,
                    "type": "characteristic",
                    "join": "HEROP_ID",
                }
                geodata_lookup[ds_schema["geodata_source"]]["tables"][k] = table_entry

        out_variables = {
            k: {
                "variable": v["title"],
                "numerator": variables_to_ds_combos[k],
                "nProperty": k,
                "theme": self.registry.theme_lookup[v["construct"]],
                "metadataUrl": v.get("metadata_doc_url"),
            }
            for k, v in variables.items()
            if k in variables_to_ds_combos
        }

        # hacky method for creating the output geodata source list in descending order of
        # spatial resolution
        out_sources = {"sources": []}
        for v in geodata_lookup.values():
            if v["csv_abbrev"] == "s":
                out_sources["sources"].append(v)
        for v in geodata_lookup.values():
            if v["csv_abbrev"] == "c":
                out_sources["sources"].append(v)
        for v in geodata_lookup.values():
            if v["csv_abbrev"] == "z":
                out_sources["sources"].append(v)
        for v in geodata_lookup.values():
            if v["csv_abbrev"] == "t":
                out_sources["sources"].append(v)

        write_json(out_sources, Path(config_dir, "sources.json"))

        write_json(list(out_variables.values()), Path(config_dir, "variables.json"))

    def build_docs_config(self):
        output = {}
        for theme, constructs in self.registry.themes.items():
            output[theme] = []
            for construct in constructs:
                geodata = set()
                titles = set()
                sources = set()
                metadata_docs = set()
                years = set()
                for v in self.registry.variables.values():
                    if v["construct"] == construct:
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
                                    in self.registry.table_sources[ts]["geodata_source"]
                                ):
                                    geodata.add(p[1])
                        sources.add(v["source"])
                        titles.add(v["title"])
                        md_url = v["metadata_doc_url"]
                        md_name = md_url.split("/")[-1].rstrip(".md")
                        metadata_docs.add(md_name)

                sorted_geodata = [
                    i for i in ["Tract", "Zip", "County", "State"] if i in geodata
                ]

                output[theme].append(
                    {
                        "Variable Construct": construct,
                        "Variable Proxy": self.registry.proxy_lookup[construct],
                        "Variables": natsorted(list(titles)),
                        "Source": "; ".join(sources),
                        "Metadata": list(metadata_docs),
                        "Spatial Scale": ", ".join(sorted_geodata),
                        "Years": ", ".join(natsorted(years)),
                    }
                )

        meta_dir = Path(self.root_dir, "meta")
        meta_dir.mkdir(exist_ok=True)
        write_json(output, Path(meta_dir, "variables.json"))
