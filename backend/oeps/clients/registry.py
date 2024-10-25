from pathlib import Path

from oeps.utils import load_json, write_json

REGISTRY_DIR = Path(Path(__file__).parent.parent, "data", "registry")

class Registry():

    def __init__(self, directory: Path=REGISTRY_DIR):

        self.directory = directory
        self.variable_lookup = None
        self.geodata_lookup = None
        self.table_lookup = None
        self.load_variables()

    def load_geodata_sources(self):
        """ Creates a lookup of all geodata sources in the registry. If explorer_only=True,
        then only include sources that have the extra `explorer_config` section in them. """

        lookup = {}
        paths = Path(self.directory, "geodata_sources").glob('*.json')
        for path in paths:
            data = load_json(path)
            data["csv_abbrev"] = data["name"][0]
            lookup[data['name']] = data

        self.geodata_lookup = lookup
        print(f"registry: {len(self.geodata_lookup)} geodata sources loaded")

    def load_table_sources(self):
        """ Creates a lookup of all table sources in the registry. Only tables sources
         that link to geodata in the current geodata_lookup will be included. """
        
        if self.geodata_lookup is None:
            self.load_geodata_sources()

        lookup = {}
        paths = Path(self.directory, "table_sources").glob('*.json')
        for path in paths:
            data = load_json(path)
            if data['geodata_source'] in self.geodata_lookup:
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
            for ds in v['table_sources']:
                if ds in self.table_lookup:
                    usable_sources.append(ds)

            if len(usable_sources) > 0:
                lookup[k] = v
        self.variable_lookup = lookup
        print(f"registry: {len(self.variable_lookup)} variables loaded")

    def get_variables(self, include_disabled=False):

        variables = load_json(Path(self.directory, "variables.json"))
        if not include_disabled:
            variables = {k: v for k, v
                in variables.items()
                if v.get("enabled", True) is True
            }
        return variables

    def create_tabular_resource(self, source_id: str, trim_props: bool=False):

        resource = self.table_lookup.get(source_id)
        if resource is None:
            print(f"can't find this table source: {source_id}")
            return

        schema =  {
            "primaryKey": "HEROP_ID",
            "foreignKeys": [
                {
                    "fields": "HEROP_ID",
                    "reference": {
                        "resource": resource["geodata_source"],
                        "fields": "HEROP_ID"
                    }
                }
            ],
            "missingValues": [
                "NA"
            ],
            "fields": []
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

        resource["schema"] = schema
        return resource
    
    def create_geodata_resource(self, source_id: str, trim_props: bool=False):

        resource = self.geodata_lookup.get(source_id)
        if resource is None:
            print(f"can't find this geodata source: {source_id}")
            return

        if trim_props:
            resource.pop("bq_table_name", None)
            resource.pop("bq_dataset_name", None)
            resource.pop("explorer_config", None)

        return resource

    def get_all_table_resources(self, trim_props: bool=False):

        return [self.create_tabular_resource(i, trim_props=trim_props) for i in self.table_lookup.keys()]
    
    def get_all_geodata_resources(self, trim_props: bool=False):

        return [self.create_geodata_resource(i, trim_props=trim_props) for i in self.geodata_lookup.keys()]