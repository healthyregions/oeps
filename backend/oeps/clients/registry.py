from pathlib import Path

from oeps.utils import load_json

REGISTRY_DIR = Path(Path(__file__).parent.parent, "data", "registry")

class Registry():

    def __init__(self, directory: Path=REGISTRY_DIR):

        self.directory = directory
        self.variable_lookup = None
        self.geodata_lookup = None
        self.table_lookup = None
        if directory:
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
        paths = Path(self.directory, "data_sources").glob('*.json')
        for path in paths:
            data = load_json(path)
            ds_name = data["name"]
            joins = data["schema"].get("foreignKeys", [])
            if not joins:
                print(f"warning: data source {ds_name} has no foreignKeys...")
                continue
            geodata_id = joins[0]["reference"]["resource"]
            if geodata_id in self.geodata_lookup:
                data['geodata_source'] = geodata_id
                lookup[ds_name] = data

        self.table_lookup = lookup
        print(f"registry: {len(self.table_lookup)} table sources loaded")

    def load_variables(self):

        if self.table_lookup is None:
            self.load_table_sources()

        lookup = {}
        variables = load_json(Path(self.directory, "variables.json"))
        for k, v in variables.items():
            usable_sources = []
            for ds in v['data_sources']:
                if ds in self.table_lookup:
                    # geodata_lookup[table_lookup[ds]['geodata_source']]["variables"].append(k)
                    usable_sources.append(ds)

            if len(usable_sources) > 0:
                lookup[k] = v
        self.variable_lookup = lookup
        print(f"registry: {len(self.variable_lookup)} variables loaded")