"""Optional state limit for interactive downloads.

State, county, and tract rows carry the 2-digit state FIPS inside HEROP_ID.
ZCTA rows are ZIP codes, so they use the Census ZCTA–county relationship
files (2010 and 2020), reduced to state FIPS.
"""

from __future__ import annotations

import json
from pathlib import Path

# 50 states and the District of Columbia. Territories are not in the OEPS state tables.
STATES = (
    ("01", "AL", "Alabama"),
    ("02", "AK", "Alaska"),
    ("04", "AZ", "Arizona"),
    ("05", "AR", "Arkansas"),
    ("06", "CA", "California"),
    ("08", "CO", "Colorado"),
    ("09", "CT", "Connecticut"),
    ("10", "DE", "Delaware"),
    ("11", "DC", "District of Columbia"),
    ("12", "FL", "Florida"),
    ("13", "GA", "Georgia"),
    ("15", "HI", "Hawaii"),
    ("16", "ID", "Idaho"),
    ("17", "IL", "Illinois"),
    ("18", "IN", "Indiana"),
    ("19", "IA", "Iowa"),
    ("20", "KS", "Kansas"),
    ("21", "KY", "Kentucky"),
    ("22", "LA", "Louisiana"),
    ("23", "ME", "Maine"),
    ("24", "MD", "Maryland"),
    ("25", "MA", "Massachusetts"),
    ("26", "MI", "Michigan"),
    ("27", "MN", "Minnesota"),
    ("28", "MS", "Mississippi"),
    ("29", "MO", "Missouri"),
    ("30", "MT", "Montana"),
    ("31", "NE", "Nebraska"),
    ("32", "NV", "Nevada"),
    ("33", "NH", "New Hampshire"),
    ("34", "NJ", "New Jersey"),
    ("35", "NM", "New Mexico"),
    ("36", "NY", "New York"),
    ("37", "NC", "North Carolina"),
    ("38", "ND", "North Dakota"),
    ("39", "OH", "Ohio"),
    ("40", "OK", "Oklahoma"),
    ("41", "OR", "Oregon"),
    ("42", "PA", "Pennsylvania"),
    ("44", "RI", "Rhode Island"),
    ("45", "SC", "South Carolina"),
    ("46", "SD", "South Dakota"),
    ("47", "TN", "Tennessee"),
    ("48", "TX", "Texas"),
    ("49", "UT", "Utah"),
    ("50", "VT", "Vermont"),
    ("51", "VA", "Virginia"),
    ("53", "WA", "Washington"),
    ("54", "WV", "West Virginia"),
    ("55", "WI", "Wisconsin"),
    ("56", "WY", "Wyoming"),
)

STATE_FIPS = {code for code, _abbr, _name in STATES}
STATE_NAMES = {code: name for code, _abbr, name in STATES}

# Census cartographic ZCTAs labeled 2018 in this repo are the 2010 ZCTA vintage.
ZCTA_VINTAGE_BY_GEODATA = {
    "geo-2010-zcta": "2010",
    "geo-2018-zcta": "2010",
    "geo-2020-zcta": "2020",
}

_CROSSWALK: dict | None = None


def allowlisted_state_fips(codes) -> list[str]:
    """Keep known 2-digit state FIPS, in first-seen order. Drop anything else."""
    chosen = []
    for code in codes or []:
        text = str(code).strip()
        if text in STATE_FIPS and text not in chosen:
            chosen.append(text)
    return chosen


def state_names(codes: list[str]) -> list[str]:
    return [STATE_NAMES[code] for code in codes if code in STATE_NAMES]


def _crosswalk() -> dict:
    global _CROSSWALK
    if _CROSSWALK is None:
        path = Path(__file__).resolve().parent.parent / "data" / "zcta_state_crosswalk.json"
        _CROSSWALK = json.loads(path.read_text(encoding="utf-8"))
    return _CROSSWALK


def zcta_codes_for_states(state_fips: list[str], vintages: list[str]) -> list[str]:
    """Five-digit ZCTAs that meet any selected state, across the given vintages."""
    data = _crosswalk()
    found = set()
    for vintage in vintages:
        table = data.get(vintage, {})
        for fips in state_fips:
            found.update(table.get(fips, []))
    return sorted(code for code in found if len(code) == 5 and code.isdigit())
