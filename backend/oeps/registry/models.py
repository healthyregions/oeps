from pathlib import Path
from typing import Literal

import pandas as pd
from pydantic import BaseModel

from ..config import DATA_DIR
from ..utils import load_json


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


class GeodataSourceModel(BaseModel):
    name: str
    title: str
    description: str
    path: str
    summary_level: GeographyLevelModel

    @classmethod
    def from_json_file(cls, path: Path) -> "GeodataSourceModel":
        data = load_json(path)
        data["summary_level"] = GEOGRAPHY_LOOKUP[data["summary_level"]]
        return cls(**data)


class TableSourceModel(BaseModel):
    name: str
    title: str
    path: str
    full_path: str
    description: str
    year: str
    geodata_source: str
    variables: list["VariableModel"] = []
    df: pd.DataFrame = None

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_json_file(cls, path: Path) -> "TableSourceModel":
        data = load_json(path)
        if data["path"].startswith("http"):
            data["full_path"] = data["path"]
        else:
            data["full_path"] = str(Path(DATA_DIR, data["path"]))
        return cls(**data)


class VariableModel(BaseModel):
    title: str
    name: str
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
        data = load_json(path)
        return cls(**data)


class MetadataModel(BaseModel):
    id: str
    theme: str
    ## need to avoid the upstream BaseModel.construct() method
    construct2: str
    proxy: str
    url: str
    source: str
    source_long: str

    @classmethod
    def from_json_file(cls, path: Path) -> "MetadataModel":
        data = load_json(path)
        data['construct2'] = data['construct']
        return cls(**data)
