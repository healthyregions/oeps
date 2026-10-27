"""Constrained interactive download planner and BigQuery runner.

Builds allowlisted SQL from year / scale / theme / variable filters.
No free-form user SQL is accepted.
"""

from __future__ import annotations

import io
import os
import re
import zipfile
from dataclasses import dataclass, field

from google.api_core.exceptions import NotFound
from google.cloud import bigquery

from oeps.clients.bigquery import get_client
from oeps.clients.state_filter import (
    ZCTA_VINTAGE_BY_GEODATA,
    allowlisted_state_fips,
    state_names,
    zcta_codes_for_states,
)
from oeps.config import REGISTRY_DIR
from oeps.handlers import Registry

SAFE_COLUMN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
SAFE_TABLE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")

SCALE_TO_PREFIX = {
    "State": "state",
    "County": "county",
    "Tract": "tract",
    "ZCTA": "zcta",
}

# State, county, and tract GEOIDs are FIPS. ZCTA GEOIDs are 5-digit ZIP codes.
GEOGRAPHY_CODE_COLUMN = {
    "state": "FIPS",
    "county": "FIPS",
    "tract": "FIPS",
    "zcta": "ZCTA5",
}

ALLOWED_SCALES = frozenset(SCALE_TO_PREFIX.keys())
ALLOWED_THEMES = frozenset(
    {
        "Geography",
        "Social",
        "Environment",
        "Economic",
        "Policy",
        "Outcome",
        "Composite",
    }
)

# Safeguards
MAX_VARIABLES = 50
MAX_ROWS = 50_000
QUERY_TIMEOUT_SEC = 60


def row_limit_error_message() -> str:
    """User-facing error when a download is over MAX_ROWS. No file is created."""
    return (
        f"This selection has more than {MAX_ROWS:,} rows, so no file was created. "
        "Select a state to narrow the download, or use a per-scale zip on the "
        "Data Access page for a national file."
    )


def missing_table_error_message(plan: DownloadPlan) -> str:
    """User-facing error when the year/scale table is not in BigQuery."""
    year = plan.years[0] if plan.years else "the selected year"
    scale = plan.scales[0] if plan.scales else "the selected scale"
    return (
        f"There is no BigQuery table for {year} {scale}, so no file was created. "
        "Use a per-scale zip on the Data Access page to download this scale."
    )


class InteractiveDownloadError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


@dataclass
class DownloadPlan:
    years: list[str]
    scales: list[str]
    variable_names: list[str]
    tables: dict[str, list[str]]  # table_name -> columns (excluding HEROP_ID)
    sql: str
    states: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def _quote_table(project_id: str, table_name: str) -> str:
    if not SAFE_TABLE.match(table_name):
        raise InteractiveDownloadError(f"Invalid table name: {table_name}")
    return f"`{project_id}.tabular.{table_name}`"


def _quote_column(name: str) -> str:
    if not SAFE_COLUMN.match(name):
        raise InteractiveDownloadError(f"Invalid column name: {name}")
    return f"`{name}`"


def geography_code_column(scale: str) -> str:
    """Column name for the code carried inside HEROP_ID at this scale."""
    prefix = SCALE_TO_PREFIX.get(scale)
    column = GEOGRAPHY_CODE_COLUMN.get(prefix or "")
    if column is None:
        raise InteractiveDownloadError(f"Unknown scale: {scale}")
    return column


def code_from_herop_id(value) -> str:
    """Return the FIPS or ZIP stored after the ``###US`` prefix.

    ``050US01001`` becomes ``01001``. Values without that prefix are kept
    as text so a leading zero is not dropped.
    """
    if value is None:
        return ""
    try:
        if value != value:  # NaN
            return ""
    except TypeError:
        pass
    text = str(value).strip()
    if text.endswith(".0") and text[:-2].isdigit():
        text = text[:-2]
    if len(text) > 5 and text[3:5] == "US" and text[:3].isdigit():
        return text[5:]
    return text


def _table_geography_prefix(table_name: str) -> str | None:
    lower = table_name.lower()
    for prefix in SCALE_TO_PREFIX.values():
        if lower.startswith(f"{prefix}-") or lower.startswith(f"{prefix}_"):
            return prefix
    return None


def _resolve_variable_names(
    registry: Registry,
    themes: list[str],
    variables: list[str],
) -> list[str]:
    """Variables win when any are provided; otherwise expand themes."""
    if variables:
        names = []
        for name in variables:
            if name not in registry.variables:
                raise InteractiveDownloadError(f"Unknown variable: {name}")
            if not SAFE_COLUMN.match(name):
                raise InteractiveDownloadError(f"Invalid variable id: {name}")
            names.append(name)
        # de-dupe preserve order
        seen = set()
        out = []
        for n in names:
            if n not in seen:
                seen.add(n)
                out.append(n)
        if len(out) > MAX_VARIABLES:
            raise InteractiveDownloadError(
                f"Too many variables (max {MAX_VARIABLES}). Narrow your selection."
            )
        return out

    if not themes:
        raise InteractiveDownloadError(
            "Select at least one theme or one or more variables."
        )

    for theme in themes:
        if theme not in ALLOWED_THEMES:
            raise InteractiveDownloadError(f"Unknown theme: {theme}")

    names = []
    for var in registry.variables.values():
        md = registry.metadata.get(var.metadata)
        if md and md.theme in themes:
            names.append(var.name)

    names = sorted(set(names))
    if not names:
        raise InteractiveDownloadError("No variables found for the selected theme(s).")
    if len(names) > MAX_VARIABLES:
        raise InteractiveDownloadError(
            f"Theme selection expands to {len(names)} variables "
            f"(max {MAX_VARIABLES}). Pick specific variables instead."
        )
    return names


def build_download_plan(
    *,
    years: list[str],
    scales: list[str],
    themes: list[str] | None = None,
    variables: list[str] | None = None,
    states: list[str] | None = None,
    registry: Registry | None = None,
    project_id: str | None = None,
) -> DownloadPlan:
    """Validate filters and build a single allowlisted SELECT statement."""
    themes = themes or []
    variables = variables or []
    registry = registry or Registry.create_from_directory(REGISTRY_DIR)

    if not years or len(years) != 1:
        raise InteractiveDownloadError(
            "Select exactly one year for download (multi-year joins are not supported yet)."
        )
    if not scales or len(scales) != 1:
        raise InteractiveDownloadError(
            "Select exactly one spatial scale for download."
        )

    year = str(years[0])
    if not re.fullmatch(r"\d{4}", year):
        raise InteractiveDownloadError(f"Invalid year: {year}")

    scale = scales[0]
    if scale not in ALLOWED_SCALES:
        raise InteractiveDownloadError(f"Invalid scale: {scale}")
    prefix = SCALE_TO_PREFIX[scale]

    variable_names = _resolve_variable_names(registry, themes, variables)

    # Map tables -> columns that exist for this year + scale
    tables: dict[str, list[str]] = {}
    available: list[str] = []
    missing: list[str] = []
    for var_name in variable_names:
        var = registry.variables[var_name]
        matched = False
        for ts_name in var.table_sources:
            ts = registry.table_sources.get(ts_name)
            if not ts:
                continue
            if str(ts.data_year) != year:
                continue
            if _table_geography_prefix(ts.name) != prefix:
                continue
            if not SAFE_TABLE.match(ts.name):
                continue
            tables.setdefault(ts.name, [])
            if var_name not in tables[ts.name]:
                tables[ts.name].append(var_name)
            matched = True
        if matched:
            available.append(var_name)
        else:
            missing.append(var_name)

    # Explicit variable picks must all exist; theme expansion may drop gaps.
    if variables and missing:
        sample = ", ".join(missing[:8])
        more = f" (+{len(missing) - 8} more)" if len(missing) > 8 else ""
        raise InteractiveDownloadError(
            f"No {year} {scale} data for: {sample}{more}. "
            "Adjust year, scale, or variable selection."
        )

    if not available:
        raise InteractiveDownloadError(
            f"No BigQuery tables match {year} {scale} for the selected "
            f"{'variables' if variables else 'theme(s)'}."
        )

    notes = [
        f"Resolved {len(available)} variable(s) across {len(tables)} table(s).",
    ]
    if missing and not variables:
        sample = ", ".join(missing[:6])
        more = f" (+{len(missing) - 6} more)" if len(missing) > 6 else ""
        notes.append(
            f"Skipped {len(missing)} theme variable(s) with no {year} {scale} "
            f"data: {sample}{more}."
        )
    if variables:
        notes.append("Mode: variables win (theme used only for browsing, if at all).")
    else:
        notes.append("Mode: whole theme(s) expanded to variables available for this year/scale.")

    selected_states = allowlisted_state_fips(states)
    zcta_ids: list[str] = []
    if selected_states and scale == "ZCTA":
        vintages = []
        for table_name in tables:
            geo = registry.table_sources[table_name].geodata_source
            vintage = ZCTA_VINTAGE_BY_GEODATA.get(geo, "2010")
            if vintage not in vintages:
                vintages.append(vintage)
        zcta_ids = zcta_codes_for_states(selected_states, vintages)
        if not zcta_ids:
            raise InteractiveDownloadError(
                "No ZCTAs match the selected states, so no file was created."
            )
    if selected_states:
        notes.append(f"States: {', '.join(state_names(selected_states))}.")
    else:
        notes.append("States: whole United States.")

    project_id = project_id or os.getenv("BQ_PROJECT_ID")
    if not project_id:
        raise InteractiveDownloadError(
            "BQ_PROJECT_ID is not configured on the server.",
            status_code=503,
        )
    sql = _build_join_sql(
        project_id,
        tables,
        scale=scale,
        state_fips=selected_states,
        zcta_ids=zcta_ids,
    )
    return DownloadPlan(
        years=[year],
        scales=[scale],
        variable_names=available,
        tables=tables,
        sql=sql,
        states=selected_states,
        notes=notes,
    )


def _geography_code_select(herop_expr: str, table_names: list[str]) -> str:
    """Select the FIPS or ZIP inside HEROP_ID. No extra table is joined."""
    prefixes = {_table_geography_prefix(name) for name in table_names}
    prefixes.discard(None)
    if len(prefixes) != 1:
        raise InteractiveDownloadError("Download tables must share one scale.")
    column = GEOGRAPHY_CODE_COLUMN[prefixes.pop()]
    return f"SUBSTR({herop_expr}, 6) AS {_quote_column(column)}"


def _sql_literal(value: str) -> str:
    if not re.fullmatch(r"[0-9]{3}US[0-9]+", value):
        raise InteractiveDownloadError("Invalid geography id.")
    return f"'{value}'"


def _state_where(scale: str, herop_expr: str, state_fips: list[str], zcta_ids: list[str]) -> str | None:
    """Allowlisted state limit. Empty means the whole United States."""
    if not state_fips:
        return None
    if scale == "ZCTA":
        literals = ", ".join(_sql_literal(f"860US{code}") for code in zcta_ids)
        return f"{herop_expr} IN ({literals})"
    summary = {"State": "040", "County": "050", "Tract": "140"}[scale]
    if scale == "State":
        literals = ", ".join(_sql_literal(f"{summary}US{fips}") for fips in state_fips)
        return f"{herop_expr} IN ({literals})"
    parts = [
        f"STARTS_WITH({herop_expr}, '{summary}US{fips}')" for fips in state_fips
    ]
    return "(" + " OR ".join(parts) + ")"


def _build_join_sql(
    project_id: str,
    tables: dict[str, list[str]],
    scale: str | None = None,
    state_fips: list[str] | None = None,
    zcta_ids: list[str] | None = None,
) -> str:
    """FULL OUTER JOIN tables on HEROP_ID; select HEROP_ID, its FIPS or ZIP, and requested columns."""
    table_names = sorted(tables.keys())
    state_fips = state_fips or []
    zcta_ids = zcta_ids or []
    if len(table_names) == 1:
        t = table_names[0]
        herop_expr = _quote_column("HEROP_ID")
        cols = [
            herop_expr,
            _geography_code_select(herop_expr, table_names),
        ] + [_quote_column(c) for c in sorted(tables[t])]
        lines = [
            f"SELECT {', '.join(cols)}",
            f"FROM {_quote_table(project_id, t)}",
        ]
        where = _state_where(scale or "", herop_expr, state_fips, zcta_ids) if scale else None
        if where:
            lines.append(f"WHERE {where}")
        lines.append(f"LIMIT {MAX_ROWS + 1}")
        return "\n".join(lines)

    aliases = {name: f"t{i}" for i, name in enumerate(table_names)}
    first = table_names[0]
    first_alias = aliases[first]

    herop_parts = [f"{aliases[n]}.HEROP_ID" for n in table_names]
    herop_expr = f"COALESCE({', '.join(herop_parts)})"
    select_cols = [
        f"{herop_expr} AS HEROP_ID",
        _geography_code_select(herop_expr, table_names),
    ]
    for tname, cols in tables.items():
        alias = aliases[tname]
        for col in sorted(cols):
            q = _quote_column(col)
            select_cols.append(f"{alias}.{q} AS {q}")

    sql_parts = [
        f"SELECT {', '.join(select_cols)}",
        f"FROM {_quote_table(project_id, first)} AS {first_alias}",
    ]
    for tname in table_names[1:]:
        alias = aliases[tname]
        sql_parts.append(
            f"FULL OUTER JOIN {_quote_table(project_id, tname)} AS {alias} "
            f"ON {first_alias}.HEROP_ID = {alias}.HEROP_ID"
        )
    where = _state_where(scale or "", herop_expr, state_fips, zcta_ids) if scale else None
    if where:
        sql_parts.append(f"WHERE {where}")
    sql_parts.append(f"LIMIT {MAX_ROWS + 1}")
    return "\n".join(sql_parts)


def run_download_query(plan: DownloadPlan) -> tuple[str, int]:
    """Execute plan against BigQuery; return (csv_text, row_count)."""
    client = get_client()
    job_config = bigquery.QueryJobConfig(use_legacy_sql=False)
    try:
        query_job = client.query(plan.sql, job_config=job_config)
        result = query_job.result(timeout=QUERY_TIMEOUT_SEC)
    except NotFound as exc:
        raise InteractiveDownloadError(
            missing_table_error_message(plan),
            status_code=404,
        ) from exc
    except Exception as exc:  # noqa: BLE001 — surface as user-facing error
        raise InteractiveDownloadError(
            f"BigQuery query failed: {exc}",
            status_code=502,
        ) from exc

    df = result.to_dataframe()
    if len(df) > MAX_ROWS:
        raise InteractiveDownloadError(
            row_limit_error_message(),
            status_code=413,
        )
    if df.empty:
        raise InteractiveDownloadError(
            "Query returned no rows for this selection.",
            status_code=404,
        )

    df = _attach_geography_code(df, plan.scales[0] if plan.scales else "")
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    return buf.getvalue(), len(df)


def _attach_geography_code(df, scale: str):
    """Write FIPS or ZCTA5 from HEROP_ID so leading zeros survive the CSV."""
    if "HEROP_ID" not in df.columns or not scale:
        return df
    column = geography_code_column(scale)
    out = df.copy()
    out[column] = out["HEROP_ID"].map(code_from_herop_id)
    front = ["HEROP_ID", column]
    rest = [name for name in out.columns if name not in front]
    return out[front + rest]


def csv_text_as_zip(csv_text: str, csv_name: str) -> bytes:
    """Wrap one CSV in a zip archive. Does not change row-limit handling."""
    if not csv_name.endswith(".csv") or "/" in csv_name or "\\" in csv_name:
        raise InteractiveDownloadError(f"Invalid CSV name: {csv_name}")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(csv_name, csv_text.encode("utf-8"))
    return buf.getvalue()
