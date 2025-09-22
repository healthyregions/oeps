import os
from pathlib import Path
from warnings import warn
from typing import Union

import pandas as pd
import geopandas as gpd
from pydantic import BaseModel

from ..config import THEME_ORDER
from .models import (
    GEOGRAPHY_LOOKUP,
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

        if isinstance(target_ts, str):
            target_ts = self.table_sources[target_ts]
        target_ts.load_dataframe()

        id_column = None
        lvl = GEOGRAPHY_LOOKUP[target_ts.summary_level]

        if "HEROP_ID" in incoming_df.columns:
            id_column = "HEROP_ID"
        else:
            for i in lvl.allowed_id_columns:
                if i in incoming_df.columns:
                    id_column = i

        if id_column is None:
            raise Exception(
                "No valid id column in this dataframe."
            )

        ## determine which columns to take from the incoming dataframe
        matched = [i for i in incoming_df.columns if i in self.variables]
        missed = [i for i in incoming_df.columns if i not in self.variables]
        overlap = [i for i in matched if i in target_ts.df.columns if i not in lvl.allowed_id_columns]

        use_columns = [i for i in matched if i not in target_ts.df.columns and i not in overlap]

        ## create and begin modifying the staged dataframe
        prep_df = incoming_df.copy(deep=True)

        ## may need to transform the 
        if id_column != "HEROP_ID":
            prep_df["HEROP_ID"] = f"{lvl.code}US" + prep_df[id_column].astype("Int64").astype(str).str.zfill(
                lvl.geoid_length
            )

        ## make sure whatever column that is used for the join ID is unique
        if not pd.Series(prep_df[id_column]).is_unique:
            raise Exception(
                f"There are duplicate {id_column} values in the input CSV. {id_column} must be unique across all rows."
            )

        if "HEROP_ID" not in prep_df.columns:
            raise Exception(
                "input data frame must have one of these fields: HEROP_ID, GEOID, GEO ID, GEO_ID, FIPS, ZCTA5"
            )

        ## drop any rows where the ID column is NaN after be
        prep_df = prep_df.dropna(subset=[id_column])

        prep_df = self.set_data_types(prep_df)
        prep_df = prep_df.round(2)

        prep_df = prep_df[["HEROP_ID"] + use_columns]

        print("initial loaded dataframe:")
        print(incoming_df)
        print(f"dataframe shape: {incoming_df.shape}")

        print("staged dataframe:")
        print(prep_df)
        print(f"dataframe shape: {prep_df.shape}")

        print(f"{len(matched)} columns match to variables already in the registry")
        print(
            f"{len(missed)} columns are not yet in the registry and will be ignored. List of unmatched columns:"
        )
        for i in missed:
            print(f"  {i}")
        print(
            f"{len(overlap)} columns in the incoming dataset already exist in the target"
        )
        if overlap:
            print("  -- overlapping columns from incoming data will be ignored.")

        print(f"{len(use_columns)} new column(s) will be added to the existing CSV")

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
                if self.table_sources[ts].year <= year:
                    use_source = self.table_sources[ts]

        return use_source

    def remove_variable(self, variable_name: str):
        os.remove(Path(self.path, "variables", f"{variable_name}.json"))
        self._load_variables(self.path)

    def create_table_source(
        self, year: str, geodata_source: str, dry_run: bool = False
    ) -> TableSource:

        gs = self.geodata_sources.get(geodata_source)

        name = f"{gs.summary_level.name}-{year}"

        ts = TableSource(
            name=name,
            title=name,
            description=f"This CSV aggregates all OEPS data values from {year} at the {gs.summary_level.name} level.",
            year=year,
            geodata_source=geodata_source,
            path=f"tables/{name}.csv",
        )

        gdf = gs.get_blank_dataframe()

        print("new data table:")
        print(gdf)

        if not dry_run:
            ts.to_json_file(self.path)
            gdf.to_csv(ts.full_path, index=False)
