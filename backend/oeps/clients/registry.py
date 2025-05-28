from enum import Enum
from pathlib import Path
import shutil

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
import pandas as pd
import geopandas as gpd

from oeps.clients.s3 import get_base_url
from oeps.config import REGISTRY_DIR, TEMP_DIR, DATA_DIR
from oeps.utils import load_json, write_json


summary_lookup = {
    "state": {
        "code": "040",
        "geoid_length": 2,
    },
    "county": {
        "code": "050",
        "geoid_length": 5,
    },
    "zcta": {
        "code": "860",
        "geoid_length": 5,
    },
    "tract": {
        "code": "140",
        "geoid_length": 11,
    },
}


class SummaryLevel(Enum):
    state = "state"
    county = "county"
    zcta = "zcta"
    tract = "tract"


class Registry:
    def __init__(self, directory: Path = REGISTRY_DIR):
        self.directory = directory

        ## load in this order so that some attributes can be cascaded
        self.geodata_sources = self._load_geodata_sources()
        self.table_sources = self._load_table_sources()
        self.variables = self._load_variables()

        ## declare public attributes for type hinting
        self.themes = {}
        self.theme_lookup = {}
        self.proxy_lookup = {}
        self._load_themes()  # updates self.themes, self.theme_lookup, and self.proxy_lookup

        print(
            f"registry initialized | variables: {len(self.variables)}, tables: {len(self.table_sources)}, geodata: {len(self.geodata_sources)}"
        )

    def _load_geodata_sources(self) -> dict:
        """Creates a lookup of all geodata sources in the registry."""

        output = {}
        paths = Path(self.directory, "geodata_sources").glob("*.json")
        for path in paths:
            data = load_json(path)
            output[data["name"]] = data
        return output

    def _load_table_sources(self) -> dict:
        """Creates a lookup of all table sources in the registry."""

        output = {}
        paths = Path(self.directory, "table_sources").glob("*.json")
        for path in paths:
            resource = load_json(path)
            resource_id = resource["name"]

            schema = {
                "primaryKey": "HEROP_ID",
                "missingValues": ["NA"],
                "foreignKeys": [],
                "fields": [],
            }

            ## if there is a geodata_source (which there should be), then
            ## attach information from it to this table_source
            join_resource = resource.get("geodata_source")
            if join_resource:
                schema["foreignKeys"].append(
                    {
                        "fields": "HEROP_ID",
                        "reference": {
                            "resource": join_resource,
                            "fields": "HEROP_ID",
                        },
                    }
                )
                geodata = self.geodata_sources[join_resource]
                resource["summary_level"] = geodata["summary_level"]

            resource["schema"] = schema
            output[resource_id] = resource

        return output

    def _load_variables(self) -> dict:
        """Creates a lookup of all variables."""

        variables = load_json(Path(self.directory, "variables.json"))

        ## iterate all table_sources and add field lists to their schema
        ## using these variables.
        for k, v in self.table_sources.items():
            v["schema"]["fields"] = [
                i for i in variables.values() if k in i["table_sources"]
            ]

        ## add year
        for v in variables.values():
            sources = [
                i
                for i in self.table_sources.values()
                if i["name"] in v.get("table_sources", [])
            ]
            v["years"] = list(set([i["year"] for i in sources]))

        return variables

    def _load_themes(self):
        """load in the theme and construct structure used in certain exports."""

        self.themes = load_json(Path(self.directory, "themes.json"))
        self.theme_lookup = {}
        self.proxy_lookup = {}
        for theme, constructs in self.themes.items():
            for construct, proxy in constructs.items():
                self.theme_lookup[construct] = theme
                self.proxy_lookup[construct] = proxy

    def get_all_sources(self):
        sources = list(self.table_sources.values())
        sources += list(self.geodata_sources.values())
        return sources

    def create_data_dictionaries(self, destination: Path = None):
        """Generate MS Excel formatted data dictionaries for all content."""

        if not destination:
            destination = Path(DATA_DIR, "dictionaries")
        destination.mkdir(exist_ok=True)

        summary_levels = {}
        for geodata in self.geodata_sources.values():
            summary_levels[geodata["summary_level"][0].upper()] = geodata[
                "summary_level"
            ]

        for id, label in summary_levels.items():
            tabular = [
                i
                for i in self.table_sources.values()
                if self.geodata_sources[i["geodata_source"]]["summary_level"] == label
            ]

            # get all variables (fields) that are in any of these tables
            fields = []
            for table in tabular:
                for i in self.variables.values():
                    if table["name"] in i.get("table_sources", {}):
                        fields.append(i)

            ordered = []
            for theme in self.themes.keys():
                matched = [
                    i for i in fields if self.theme_lookup[i["construct"]] == theme
                ]
                ordered += sorted(matched, key=lambda i: i["metadata_doc_url"])

            all_variables = {}
            for f in ordered:
                all_variables[f["name"]] = {"years": f["years"], "info": f}

            years_list = set()
            for v in all_variables.values():
                for y in v["years"]:
                    years_list.add(y)

            headers = {"Theme": 15}
            for y in sorted(years_list):
                headers[y] = 5
            headers.update(
                {
                    "Analysis": 10,
                    "Longitudinal": 10,
                    "Variable": 20,
                    "Title": 30,
                    "Description": 25,
                    "Metadata Location": 25,
                    "Source": 25,
                    "Source Long": 25,
                    "OEPS v1 Table": 25,
                    "Type": 25,
                    "Example": 25,
                    "Data Limitations": 25,
                    "Comments": 100,
                }
            )

            wb = Workbook()
            ws = wb.active
            ws.append(list(headers.keys()))

            ft = Font(bold=True, name="Calibri")
            for row in ws["A1:Z1"]:
                for cell in row:
                    cell.font = ft

            def parse_attribute_from_variable(attribute, variable):
                v = variable["info"]
                if attribute == "Longitudinal":
                    if v["longitudinal"]:
                        return "x"
                elif attribute == "Analysis":
                    if v["analysis"]:
                        return "x"
                elif attribute == "Theme":
                    return self.theme_lookup.get(v["construct"])
                elif attribute in variable.get("years", []):
                    return "x"
                elif attribute == "Title":
                    return v.get("title")
                elif attribute == "Variable":
                    return v.get("name")
                elif attribute == "Metadata Location":
                    return v.get("metadata_doc_url")
                elif attribute == "Data Limitations":
                    return v.get("constraints")
                elif attribute == "Source Long":
                    return v.get("source_long")
                elif attribute == "OEPS v1 Table":
                    return v.get("oeps_v1_table")
                elif attribute.lower() in v:
                    return v.get(attribute.lower())

                return ""

            for v in all_variables.values():
                row = [parse_attribute_from_variable(i, v) for i in headers.keys()]
                ws.append(row)

            for n, k in enumerate(headers.keys()):
                ws.column_dimensions[get_column_letter(n + 1)].width = headers[k]

            # Save the file
            wb.save(Path(destination, f"{id}_Dict.xlsx"))

    def validate(self):
        print("\n## Checking variables against table source data")

        df_lookup = {}
        variables_valid = True
        for k, v in self.variables.items():
            for ts in v["table_sources"]:
                if ts not in self.table_sources:
                    print(f"{k} references a table_source not in the registry: {ts}")
                    variables_valid = False
                    continue

                df = df_lookup.get(ts)
                if df is None:
                    df = self.load_table_source(ts)
                    df_lookup[ts] = df

                if k not in df.columns:
                    print(
                        f"{k} should be in table_source {ts} but that column is not present in the CSV"
                    )
                    variables_valid = False
        if variables_valid:
            print("all good")

        print("\n## Checking constructs & themes")
        valid_constructs = []
        for c in self.themes.values():
            valid_constructs += list(c.keys())

        missing = 0
        used = set()
        for v in self.variables.values():
            construct = v.get("construct")
            if construct not in valid_constructs:
                print(f"{v['name']}: invalid construct {construct}")
                missing += 1
            else:
                used.add(construct)
        unused = [i for i in valid_constructs if i not in used]
        if missing:
            print(f"{missing} variables with invalid 'construct'")
        if unused:
            print(f"{len(unused)} unused 'construct':")
            print(unused)
        if missing == 0 and len(unused) == 0:
            print("all good")

        print("\n## Checking geodata sources")
        geodata_valid = True
        for k, v in self.geodata_sources.items():
            try:
                SummaryLevel(v["summary_level"])
            except Exception:
                print(k)
                geodata_valid = False
        if geodata_valid:
            print("all good")

    def get_or_create_table_source(self, name: str, geodata_source: str, dry_run=True):
        lvl, year = name.split("-")

        ## validate these components
        lvl = SummaryLevel(lvl)
        int(year)
        gs = self.geodata_sources[geodata_source]

        ts = self.table_sources.get(name)

        file_name = f"{name}.csv"
        temp_path = Path(TEMP_DIR, "tables", file_name)
        local_path = Path(DATA_DIR, "tables", file_name)
        s3_path = f"{get_base_url()}data/tables/{file_name}"
        if not ts:
            ts = {
                "bq_dataset_name": "tabular",
                "bq_table_name": name,
                "name": name,
                "path": temp_path.absolute() if dry_run else s3_path,
                "format": "csv",
                "mediatype": "text/csv",
                "title": name,
                "description": f"This CSV aggregates all OEPS data values from {year} at the {gs['summary_level']} level.",
                "year": str(year),
                "geodata_source": geodata_source,
            }

            ## write the definition to a new JSON file
            if not dry_run:
                outpath = Path(REGISTRY_DIR, "table_sources", f"{name}.json")
                write_json(ts, outpath)
            self.table_sources[name] = ts

            ## now create and upload a dummy CSV with all HEROP_IDs, based on the geodata_source
            temp_path = Path(TEMP_DIR, "tables", file_name)
            gdf = gpd.read_file(gs["path"])
            gdf_sm = gdf["HEROP_ID"]
            gdf_sm.to_csv(temp_path, index=False)

            if not dry_run:
                shutil.copy(temp_path, local_path)
                # upload_to_s3(temp_path, "data/tables", True)

        return ts

    def load_table_source(self, table_source_name: str) -> pd.DataFrame:
        if table_source_name not in self.table_sources:
            print(f"invalid table_source name: {table_source_name}")
            return None

        path = self.table_sources[table_source_name]["path"]
        if not path.startswith("http"):
            path = Path(DATA_DIR, path)

        return pd.read_csv(path)

    def load_incoming_csv_to_data_frame(self, path: Path, summary_level: str):
        df = pd.read_csv(path)

        lvl = summary_lookup[summary_level]

        ## all good if HEROP_ID already exists in the data frame
        if "HEROP_IP" not in df.columns:
            for id in ["GEOID", "GEO ID", "GEO_ID", "FIPS"]:
                if id in df.columns:
                    df["HEROP_ID"] = f"{lvl['code']}US" + df[id].astype(str).str.zfill(
                        lvl["geoid_length"]
                    )

        print("incoming data frame loaded")
        print(df)

        if "HEROP_ID" in df.columns:
            return df
        ## if it wasn't added above based on other incoming fields, abort process
        else:
            print(
                "input data frame must have one of these fields: HEROP_ID, GEOID, GEO ID, GEO_ID, FIPS"
            )
            return None

    def validate_input_table(self, input_path: Path, summary_level: str):
        df = self.load_incoming_csv_to_data_frame(input_path, summary_level)
        all_fields = list(df.columns)
        matched = [i for i in all_fields if i in self.variables]
        missed = [i for i in all_fields if i not in self.variables]

        return (matched, missed)

    def merge_table(
        self, input_path: str, geodata_source: str, year: int, dry_run=True
    ):
        temp_out = Path(TEMP_DIR, "tables")
        temp_out.mkdir(parents=True, exist_ok=True)

        summary_level = self.geodata_sources[geodata_source]["summary_level"]

        # need to pass in summary level in order to generate HEROP_ID (if necessary)
        source_df = self.load_incoming_csv_to_data_frame(input_path, summary_level)

        target_ts_name = f"{summary_level}-{year}"
        target_ts = self.table_sources.get(target_ts_name)
        if not target_ts:
            target_ts = self.create_table_source(
                target_ts_name, geodata_source, dry_run=dry_run
            )

        ts_path = target_ts["path"]
        if not ts_path.startswith("http"):
            ts_path = Path(DATA_DIR, ts_path)
        print(ts_path.absolute())
        target_df = pd.read_csv(ts_path)

        ## determine which columns to take from the incoming dataframe
        matched = [i for i in source_df.columns if i in self.variables]
        overlap = [i for i in matched if i in target_df.columns if not i == "HEROP_ID"]
        print(
            f"{len(overlap)} columns in the incoming dataset already exist in the target"
        )
        if overlap:
            print("  -- overlapping columns from incoming data will be ignored.")
        new = [i for i in matched if i not in target_df.columns and i not in overlap]
        if not new:
            print("No new columns to add from this input CSV.")
            return

        print(f"{len(new)} new column(s) will be added to the existing CSV")
        source_df_trim = source_df[["HEROP_ID"] + new]
        print(source_df_trim)
        print(f"shape of incoming data: {source_df_trim.shape}")
        merged_df = pd.merge(target_df, source_df_trim, how="outer", on="HEROP_ID")

        temp_path = Path(temp_out, f"{target_ts_name}.csv")
        local_path = Path(DATA_DIR, "tables", f"{target_ts_name}.csv")
        merged_df.to_csv(temp_path, index=False)

        if not dry_run:
            shutil.copy(temp_path, local_path)
            # upload_to_s3(temp_path, "data/tables", True)

        for col in source_df_trim.columns:
            var = self.variables[col]
            if target_ts_name not in var["table_sources"]:
                var["table_sources"].append(target_ts_name)

        for k, v in self.variables.items():
            del v["years"]

        if not dry_run:
            write_json(self.variables, Path(self.directory, "variables.json"))
