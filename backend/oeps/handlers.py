import os
from pathlib import Path
from warnings import warn
from typing import Union

import pandas as pd
import geopandas as gpd
from pydantic import BaseModel

from .config import THEME_ORDER
from .models import (
    TableSourceModel,
    VariableModel,
    GeodataSourceModel,
    MetadataModel,
)


class TableSource(TableSourceModel):

    def load_dataframe(self) -> pd.DataFrame:
        """Load this TableSource's CSV data into a pandas DataFrame"""
        self.df = pd.read_csv(self.full_path)
        return self.df

    def get_variable_data(self, names: list[str]):
        if self.df is None:
            self.load_dataframe()
        fields = ["HEROP_ID"] + names
        return pd.DataFrame(self.df, columns=fields)

    def delete_variable_data(self, name: str):
        if self.df is None:
            self.load_dataframe()
        self.df.drop(name, axis=1, inplace=True)
        self.df.to_csv(self.full_path, index=False)

    def merge_df(self, incoming_df: pd.DataFrame, overwrite: bool = False):
        if self.df is None:
            self.load_dataframe()
        new_vars = [i for i in incoming_df.columns if not i == "HEROP_ID"]
        dupe_vars = [i for i in new_vars if i in self.df.columns]
        if len(dupe_vars) > 0:
            if not overwrite:
                raise Exception(
                    "Incoming variables exist in the dataframe, cancelling merge. Use overwrite=True to continue."
                )
            for var in dupe_vars:
                self.delete_variable_data(var)

        merged_df = pd.merge(self.df, incoming_df, how="left", on="HEROP_ID")

        merged_df.to_csv(self.full_path, index=False)

    def to_frictionless_resource(self):

        return {
            "name": self.name,
            "title": self.title,
            "format": "csv",
            "mediatype": "text/csv",
            "path": self.path,
            "schema": {
                "primaryKey": "HEROP_ID",
                "fields": [i.to_frictionless_field() for i in self.variables]
            }
        }

class Variable(VariableModel):

    def to_frictionless_field(self):
        field_def = {
            "name": self.name,
            "title": self.title,
            "type": self.type,
            "example": self.example,
            "description": self.description,
            "metadata": self.metadata
        }
        if self.format:
            field_def["format"] = self.format
        return field_def

class GeodataSource(GeodataSourceModel):

    def get_blank_dataframe(self) -> pd.DataFrame:
        gdf = gpd.read_file(self.full_path)[["HEROP_ID"]]

        extra_foreign_key = "ZCTA5" if self.summary_level.name == "zcta" else "FIPS"
        gdf[extra_foreign_key] = gdf.HEROP_ID.apply(lambda x: x[5:])

        return gdf

    def to_frictionless_resource(self):

        return {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "format": "shp",
            "mediatype": "application/vnd.shp",
            "path": self.path,
            "schema": {
                "primaryKey": "HEROP_ID",
                "fields": [
                    {
                        "name": "HEROP_ID",
                        "title": "HEROP_ID",
                        "type": "string"
                    },
                    {
                        "name": "name",
                        "title": "Name",
                        "type": "string"
                    }
                ]
            }
        }

class Metadata(MetadataModel):
    pass

class Registry(BaseModel):

    path: Path
    variables: dict[str, Variable] = {}
    table_sources: dict[str, TableSource] = {}
    geodata_sources: dict[str, GeodataSource] = {}
    metadata: dict[str, Metadata] = {}
    theme_tree: dict[str, dict[str, list[str]]] = {}

    @staticmethod
    def _load_variables(path: Path) -> dict[str, Variable]:
        variables = {}
        for i in Path(path, "variables").glob("*.json"):
            v = Variable.from_json_file(i)
            variables[v.name] = v
        return variables

    @staticmethod
    def _load_table_sources(path: Path) -> dict[str, TableSource]:
        table_sources = {}
        for i in Path(path, "table_sources").glob("*.json"):
            t = TableSource.from_json_file(i)
            table_sources[t.name] = t
        return table_sources

    @staticmethod
    def _load_geodata_sources(path: Path) -> dict[str, GeodataSource]:
        geodata_sources = {}
        for i in Path(path, "geodata_sources").glob("*.json"):
            g = GeodataSource.from_json_file(i)
            geodata_sources[g.name] = g
        return geodata_sources

    @staticmethod
    def _load_metadata(path: Path) -> tuple[dict, dict]:
        metadata = {}
        theme_tree = {k: {} for k in THEME_ORDER}
        for i in Path(path, "metadata").glob("*.json"):
            md = Metadata.from_json_file(i)
            metadata[md.name] = md
            ## theme must be one of the preset options
            if md.theme not in theme_tree:
                print(f"WARNING: metadata entry {md.name} has invalid theme {md.theme}")
            else:
                if md.construct2 not in theme_tree[md.theme]:
                    theme_tree[md.theme][md.construct2] = [md.name]
                else:
                    theme_tree[md.theme][md.construct2].append(md.name)
        return (metadata, theme_tree)

    @classmethod
    def create_from_directory(cls, path: Path):
        variables = cls._load_variables(path)
        table_sources = cls._load_table_sources(path)
        geodata_sources = cls._load_geodata_sources(path)
        metadata, theme_tree = cls._load_metadata(path)

        ## set forward objects
        for t in table_sources.values():
            full_variable_objects = []
            for v in variables.values():
                if t.name in v.table_sources:
                    full_variable_objects.append(v)
            t.variables = full_variable_objects

        return cls(
            path=path,
            variables=variables,
            table_sources=table_sources,
            geodata_sources=geodata_sources,
            metadata=metadata,
            theme_tree=theme_tree,
        )

    def validate(self):

        print("\n-- checking variables...")
        for k, v in self.variables.items():
            if v.metadata not in self.metadata:
                print(f"{k} | Invalid metadata name: {v.metadata} ")
            for t in v.table_sources:
                if t not in self.table_sources:
                    print(f"{k} | Invalid table source name: {t} ")

        print("\n-- checking table sources...")
        for k, v in self.table_sources.items():
            if v.geodata_source not in self.geodata_sources:
                print(f"{k} | Invalid geodata_source: {v.geodata_source} ")
            pathpath = Path(v.full_path)
            if pathpath.stem != v.name:
                print(f"{k} | CSV file name must match table_source name: {pathpath.stem}")
            if not pathpath.is_file():
                print(f"{k} | CSV not found: {v.full_path}")

        print("\nall checks complete.")

    def reload_variables(self):
        self.variables = self._load_variables(self.path)

    def update_variable_table_sources(self, table_source: Union[str, TableSource] = None):
        if table_source:
            if isinstance(table_source, str):
                use_table_sources = [self.table_sources[table_source]]
            else:
                use_table_sources = [table_source]
        else:
            use_table_sources = self.table_sources.values()

        for ts in use_table_sources:
            ts.load_dataframe()
            for v in self.variables.values():
                if ts.name in v.table_sources:
                    v.table_sources = [i for i in v.table_sources if not i == ts.name]
                    self.save_variable(v)

                ## now add this table source if the variable is in df.columns
                if v.name in ts.df.columns:
                    v.table_sources.append(ts.name)
                    v.table_sources.sort()
                    self.save_variable(v)

    def save_variable(self, variable: Union[str, Variable]):
        if isinstance(variable, str):
            variable = self.variables[variable]
        variable.to_json_file(self.path)

    def save_table_source(self, table_source: Union[str, TableSource]):
        if isinstance(table_source, str):
            table_source = self.table_sources[table_source]
        table_source.to_json_file(self.path)

    def prepare_incoming_df(self, incoming_df: pd.DataFrame, target_ts: Union[str, TableSource]) -> pd.DataFrame:
        """Load an incoming CSV to pandas dataframe, and create HEROP_ID
        along the way if possible."""

        print("\n## PREVIEW OF INCOMING DATAFRAME\n")
        print(incoming_df)

        ## get the table source instance and load its CSV data to dataframe
        if isinstance(target_ts, str):
            target_ts = self.table_sources[target_ts]
        target_ts.load_dataframe()
        lvl = self.geodata_sources[target_ts.geodata_source].summary_level

        ## analyze the columns in the incoming dataframe
        print("\n## CHECK COLUMNS\n")

        geo_cols, matched_cols, unmatched_cols, overlap_cols = [], [], [], []

        for c in incoming_df.columns:
            ## put all geoid columns into a bucket
            if c in lvl.allowed_id_columns:
                geo_cols.append(c)
            ## now check against all variables in the registry
            elif c in self.variables:
                if c in target_ts.df.columns:
                    overlap_cols.append(c)
                else:
                    matched_cols.append(c)
            ## the rest of the colums will be ignored. Note that these could be
            ## columns that actually should be merged, but either 1) don't have
            ## exactly the right names, or 2) the variables they represent have
            ## not yet been added to the registry
            else:
                unmatched_cols.append(c)

        print(f"Geo columns: {geo_cols}")
        print(f"Matched columns: {matched_cols}")
        print(f"Matched columns already in target: {overlap_cols}")
        print(f"Unmatched columns: {unmatched_cols}")

        if overlap_cols:
            print("\n**IMPORTANT**: Incoming columns that already exist in the target "\
                "will be IGNORED during this merge. To overwrite columns in the "\
                "target you must first remove them and then re-run this command."\
                f"\n\n    flask remove-variable -n <column name> -t {target_ts.name}")

        if unmatched_cols:
            print("\n**IMPORTANT**: Unmatched columns will be IGNORED during this merge. "\
                "If a column is listed as 'unmatched' but should be included:"\
                "\n\n- Check that the variable has already been created in the registry"\
                "\n- Check that the name of the column exactly matches the variable name (case-sensitive)")

        ## create and begin modifying the staged dataframe
        prep_df = incoming_df.copy(deep=True)

        ## run a series of checks to ensure there is a joinable HEROP_ID column.
        print("\ndetermining join column...\n")

        id_column = None
        if "HEROP_ID" in incoming_df.columns:
            print("HEROP_ID is present")
            id_column = "HEROP_ID"
        else:
            print("HEROP_ID is missing, checking for other appropriate join columns...\n")
            for id_col in [i for i in lvl.allowed_id_columns if not i == "HEROP_ID"]:
                print(f"- {id_col} present?", end=" ")
                if id_col in incoming_df.columns:
                    print("Yes! This column will be converted to HEROP_ID for join.")
                    id_column = id_col
                    break
                else:
                    print("No.")

            ## if no appropriate join column has been found, then operation
            ## cannot continue
            if id_column is None:
                raise Exception(
                    "No valid id column in this dataframe."
                )

            ## generate HEROP_ID based on the matched id colum.
            prep_df["HEROP_ID"] = f"{lvl.code}US" + prep_df[id_column].astype("Int64").astype(str).str.zfill(
                lvl.geoid_length
            )

        ## make sure whatever column that is used for the join ID is unique
        if not pd.Series(prep_df[id_column]).is_unique:
            raise Exception(
                f"There are duplicate {id_column} rows in the input CSV. {id_column} must be unique across all rows."
            )

        ## Now begin checking the incoming data against what is already in the table source
        print("\n## CHECK ROWS\n")

        ## drop any rows where the ID column is NaN
        prep_df = prep_df.dropna(subset=[id_column])

        target_row_ct = target_ts.df.shape[0]

        print(f"Joinable rows in target table source: {target_row_ct}")
        print("\nNumber of rows with values for each matched/overlap column:\n")
        for mc in matched_cols + overlap_cols:
            print(f"- {mc}: {prep_df.dropna(subset=[mc]).shape[0]}")

        print(f"\n**IMPORTANT**: If any incoming columns have less than {target_row_ct} rows with values"\
              " you may need to check the data.")

        if not matched_cols:
            print("\n\nThere are no matched columns to merge. Cancelling operation.")
            exit()

        ## set all data types in the dataframe (according to attributes in the registry)
        prep_df = self.set_data_types(prep_df)

        ## round all values to 2 decimals
        prep_df = prep_df.round(2)

        ## trim all unneeded columns, leave only join field and matched columns.
        prep_df = prep_df[["HEROP_ID"] + matched_cols]

        print("\n## PREVIEW OF STAGED DATAFRAME")
        print(prep_df)

        return prep_df

    def set_data_types(self, df: pd.DataFrame):
        """set integer columns properly based on registry def of variables.
        Raise a warning if this process fails on a given column."""

        for col in df.columns:
            if col in self.variables:
                if self.variables[col].type == "integer":
                    try:
                        df[col] = df[col].astype("Int64")
                    except pd.errors.IntCastingNaNError:
                        warn(
                            message=f"Failed to coerce column {col} to Integer due to presence of NA or inf values in the dataset. Continuing without coercing."
                        )

        return df

    def get_table_source_for_variable(self,
            variable: Union[str, Variable],
            summary_level: str,
            year: str="2100") -> Union[TableSource, None]:

        if isinstance(variable, str):
            variable = self.variables.get(variable)

        use_source = None
        for ts in variable.table_sources:
            if self.geodata_sources[self.table_sources[ts].geodata_source].summary_level.name == summary_level:
                if self.table_sources[ts].data_year <= year:
                    use_source = self.table_sources[ts]

        return use_source

    def remove_variable(self, variable_name: str):
        os.remove(Path(self.path, "variables", f"{variable_name}.json"))
        self._load_variables(self.path)

    def create_table_source(
        self, name: str, data_year: str, geodata_source: str, dry_run: bool = False
    ) -> TableSource:

        gs = self.geodata_sources.get(geodata_source)

        ts = TableSource(
            name=name,
            title=name,
            description=f"This CSV aggregates OEPS data values from {data_year} at the {gs.summary_level.name} level.",
            data_year=data_year,
            geodata_source=geodata_source,
            path=f"tables/{name}.csv",
        )

        gdf = gs.get_blank_dataframe()

        print("new data table:")
        print(gdf)

        if not dry_run:
            ts.to_json_file(self.path)
            gdf.to_csv(ts.full_path, index=False)
