from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

from oeps.utils import load_json
from oeps.config import REGISTRY_DIR, DATA_DIR


class Registry:
    def __init__(self, directory: Path = REGISTRY_DIR):
        self.directory = directory
        self.variable_lookup = None
        self.geodata_lookup = None
        self.table_lookup = None
        self.themes = None
        self.construct_lookup = None
        self.load_variables()

        # load in the theme and construct structure used in certain exports
        self.themes = load_json(Path(self.directory, "themes.json"))
        self.theme_lookup = {}
        self.proxy_lookup = {}
        for theme, constructs in self.themes.items():
            for construct, proxy in constructs.items():
                self.theme_lookup[construct] = theme
                self.proxy_lookup[construct] = proxy

    def load_geodata_sources(self):
        """Creates a lookup of all geodata sources in the registry. If explorer_only=True,
        then only include sources that have the extra `explorer_config` section in them."""

        lookup = {}
        paths = Path(self.directory, "geodata_sources").glob("*.json")
        for path in paths:
            data = load_json(path)
            data["csv_abbrev"] = data["name"][0]
            lookup[data["name"]] = data

        self.geodata_lookup = lookup
        print(f"registry: {len(self.geodata_lookup)} geodata sources loaded")

    def load_table_sources(self):
        """Creates a lookup of all table sources in the registry. Only tables sources
        that link to geodata in the current geodata_lookup will be included."""

        if self.geodata_lookup is None:
            self.load_geodata_sources()

        lookup = {}
        paths = Path(self.directory, "table_sources").glob("*.json")
        for path in paths:
            data = load_json(path)
            if data["geodata_source"] in self.geodata_lookup:
                lookup[data["name"]] = data

        self.table_lookup = lookup
        print(f"registry: {len(self.table_lookup)} table sources loaded")

    def load_variables(self):
        if self.table_lookup is None:
            self.load_table_sources()

        lookup = {}
        variables = self.get_variables()
        for k, v in variables.items():
            usable_sources = []
            for ds in v["table_sources"]:
                if ds in self.table_lookup:
                    usable_sources.append(ds)

            if len(usable_sources) > 0:
                lookup[k] = v
        self.variable_lookup = lookup
        print(f"registry: {len(self.variable_lookup)} variables loaded")

    def get_variables(self, include_disabled=False):
        variables = load_json(Path(self.directory, "variables.json"))
        if not include_disabled:
            variables = {
                k: v for k, v in variables.items() if v.get("enabled", True) is True
            }
        return variables

    def create_tabular_resource(self, source_id: str, trim_props: bool = False):
        resource = self.table_lookup.get(source_id)
        if resource is None:
            print(f"can't find this table source: {source_id}")
            return

        schema = {
            "primaryKey": "HEROP_ID",
            "foreignKeys": [
                {
                    "fields": "HEROP_ID",
                    "reference": {
                        "resource": resource["geodata_source"],
                        "fields": "HEROP_ID",
                    },
                }
            ],
            "missingValues": ["NA"],
            "fields": [],
        }

        variables = load_json(Path(self.directory, "variables.json"))
        for field in variables.values():
            if source_id in field["table_sources"]:
                schema["fields"].append(field)

        for field in schema["fields"]:
            field.pop("bq_data_type", None)
            field.pop("table_sources", None)
            constraint = field.pop("constraints", "")
            if not constraint == "":
                field["data_note"] = constraint

        if trim_props:
            resource.pop("bq_table_name", None)
            resource.pop("bq_dataset_name", None)
            resource.pop("geodata_source", None)

        resource["theme"] = self.theme_lookup.get(resource["construct"])

        resource["schema"] = schema
        return resource

    def create_geodata_resource(self, source_id: str, trim_props: bool = False):
        resource = self.geodata_lookup.get(source_id)
        if resource is None:
            print(f"can't find this geodata source: {source_id}")
            return

        if trim_props:
            resource.pop("bq_table_name", None)
            resource.pop("bq_dataset_name", None)
            resource.pop("explorer_config", None)

        return resource

    def get_all_table_resources(self, trim_props: bool = False):
        return [
            self.create_tabular_resource(i, trim_props=trim_props)
            for i in self.table_lookup.keys()
        ]

    def get_all_geodata_resources(self, trim_props: bool = False):
        return [
            self.create_geodata_resource(i, trim_props=trim_props)
            for i in self.geodata_lookup.keys()
        ]

    def create_data_dictionaries(self, destination: Path = None):
        """Generate MS Excel formatted data dictionaries for all content."""

        if not destination:
            destination = Path(DATA_DIR, "dictionaries")
        destination.mkdir(exist_ok=True)

        summary_levels = [
            {
                "id": v["summary_level"],
                "csv_abbreviation": v["summary_level"][0].upper(),
            }
            for v in self.geodata_lookup.values()
        ]

        all_table_sources = self.get_all_table_resources()

        all_fields = []
        for v in self.variable_lookup.values():
            years = list(set([i.split("-")[1] for i in v["table_sources"]]))
            v["years"] = years
            all_fields.append(v)

        for geo in summary_levels:
            tabular = [
                i
                for i in all_table_sources
                if self.geodata_lookup[i["geodata_source"]]["summary_level"]
                == geo["id"]
            ]

            # get all variables (fields) that are in any of these tables
            fields = []
            for table in tabular:
                for i in all_fields:
                    if table["name"] in i["table_sources"]:
                        fields.append(i)

            all_fields_list = []
            for t in tabular:
                file_year = t["name"].split("-")[1]
                for f in t["schema"]["fields"]:
                    if not f.get("year"):
                        f["year"] = file_year
                    all_fields_list.append(f)

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
            wb.save(Path(destination, f"{geo['csv_abbreviation']}_Dict.xlsx"))

    def validate(self):
        valid_constructs = []
        for c in self.themes.values():
            valid_constructs += list(c.keys())

        missing = 0
        used = set()
        for v in self.variable_lookup.values():
            construct = v.get("construct")
            if construct not in valid_constructs:
                print(f"{v['name']}: invalid construct {construct}")
                missing += 1
            else:
                used.add(construct)
        unused = [i for i in valid_constructs if i not in used]
        print(f"{missing} variables with invalid 'construct'")
        print(f"{len(unused)} unused 'construct':")
        if unused:
            print(unused)
