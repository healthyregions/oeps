from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

from oeps.utils import load_json
from oeps.config import REGISTRY_DIR, DATA_DIR


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
        print(f"{missing} variables with invalid 'construct'")
        print(f"{len(unused)} unused 'construct':")
        if unused:
            print(unused)
