from pathlib import Path
from typing import Literal

import pandas as pd
from pydantic import BaseModel

from .config import DATA_DIR
from .utils import load_json, write_json


class GeographyLevelModel(BaseModel):
    name: str
    code: str
    geoid_length: int
    allowed_id_columns: list[str]

GEOGRAPHY_LOOKUP = {
    "state": GeographyLevelModel(
        name="state",
        code="040",
        geoid_length=2,
        allowed_id_columns=["HEROP_ID","GEOID", "GEO ID", "GEO_ID", "FIPS", "STATEFP"]
    ),
    "county": GeographyLevelModel(
        name="county",
        code="050",
        geoid_length=5,
        allowed_id_columns=["HEROP_ID","GEOID", "GEO ID", "GEO_ID", "FIPS", "COUNTYFP"]
    ),
    "tract": GeographyLevelModel(
        name="tract",
        code="140",
        geoid_length=11,
        allowed_id_columns=["HEROP_ID","GEOID", "GEO ID", "GEO_ID", "FIPS", "TRACTCE"]
    ),
    "zcta": GeographyLevelModel(
        name="zcta",
        code="860",
        geoid_length=5,
        allowed_id_columns=["HEROP_ID","GEOID", "GEO ID", "GEO_ID", "ZCTA5", "ZIP"]
    ),
}


def load_entry(path):
    data = load_json(path)
    if "name" not in data:
        raise Exception(f"ERROR: {path.name} | name property is required")
    if path.stem != data["name"]:
        raise Exception(f"ERROR: {data['name']}, {path.name} | name and file name must match")
    return data


class GeodataSourceModel(BaseModel):
    name: str
    title: str
    description: str
    path: str
    explorer_config: dict = None
    summary_level: GeographyLevelModel

    @property
    def full_path(self) -> str:
        return self.path if self.path.startswith("http") else str(Path(DATA_DIR, self.path))

    @classmethod
    def from_json_file(cls, path: Path) -> "GeodataSourceModel":
        data = load_entry(path)
        data["summary_level"] = GEOGRAPHY_LOOKUP[data["summary_level"]]
        return cls(**data)


class TableSourceModel(BaseModel):
    name: str
    title: str
    path: str
    description: str
    data_year: str
    geodata_source: str
    variables: list["VariableModel"] = []
    df: pd.DataFrame = None

    class Config:
        arbitrary_types_allowed = True

    @property
    def full_path(self) -> str:
        return self.path if self.path.startswith("http") else \
            str(Path(DATA_DIR, self.path))

    @classmethod
    def from_json_file(cls, path: Path) -> "TableSourceModel":
        data = load_entry(path)
        return cls(**data)

    def to_json_file(self, registry_path: Path):
        output = self.model_dump(
            exclude=[
                "geodata_source",
                "variables",
                "df"
            ]
        )
        output["geodata_source"] = self.geodata_source
        json_path = Path(registry_path, "table_sources", f"{self.name}.json")
        write_json(output, json_path)


class VariableModel(BaseModel):
    name: str
    title: str
    type: Literal['string', 'number', 'integer', 'boolean', 'date']
    example: str
    format: str = None
    description: str
    longitudinal: bool = False
    analysis: bool = False
    table_sources: list[str]
    metadata: str

    @classmethod
    def from_json_file(cls, path: Path) -> "VariableModel":
        data = load_entry(path)
        return cls(**data)

    def to_json_file(self, registry_path: Path):
        output = self.model_dump(
            exclude=[
                "table_sources"
            ],
            exclude_none=True,
        )
        output["table_sources"] = self.table_sources
        json_path = Path(registry_path, "variables", f"{self.name}.json")
        write_json(output, json_path)


class MetadataModel(BaseModel):
    name: str
    theme: str
    ## need to avoid the upstream BaseModel.construct() method
    construct2: str
    proxy: str
    url: str
    source: str
    source_long: str

    @classmethod
    def from_json_file(cls, path: Path) -> "MetadataModel":
        data = load_entry(path)
        data['construct2'] = data['construct']
        return cls(**data)
