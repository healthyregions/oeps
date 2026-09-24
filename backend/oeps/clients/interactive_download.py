"""Constrained interactive download planner and BigQuery runner.

Builds allowlisted SQL from year / scale / theme / variable filters.
No free-form user SQL is accepted.
"""

from __future__ import annotations

import io
import os
import re
from dataclasses import dataclass, field

from google.cloud import bigquery

from oeps.clients.bigquery import get_client
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
    notes: list[str] = field(default_factory=list)


def _quote_table(project_id: str, table_name: str) -> str:
    if not SAFE_TABLE.match(table_name):
        raise InteractiveDownloadError(f"Invalid table name: {table_name}")
    return f"`{project_id}.tabular.{table_name}`"


def _quote_column(name: str) -> str:
    if not SAFE_COLUMN.match(name):
        raise InteractiveDownloadError(f"Invalid column name: {name}")
    return f"`{name}`"


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

    project_id = project_id or os.getenv("BQ_PROJECT_ID")
    if not project_id:
        raise InteractiveDownloadError(
            "BQ_PROJECT_ID is not configured on the server.",
            status_code=503,
        )
    sql = _build_join_sql(project_id, tables)
    return DownloadPlan(
        years=[year],
        scales=[scale],
        variable_names=available,
        tables=tables,
        sql=sql,
        notes=notes,
    )


def _build_join_sql(project_id: str, tables: dict[str, list[str]]) -> str:
    """FULL OUTER JOIN tables on HEROP_ID; select HEROP_ID + requested columns."""
    table_names = sorted(tables.keys())
    if len(table_names) == 1:
        t = table_names[0]
        cols = [_quote_column("HEROP_ID")] + [
            _quote_column(c) for c in sorted(tables[t])
        ]
        return (
            f"SELECT {', '.join(cols)}\n"
            f"FROM {_quote_table(project_id, t)}\n"
            f"LIMIT {MAX_ROWS + 1}"
        )

    aliases = {name: f"t{i}" for i, name in enumerate(table_names)}
    first = table_names[0]
    first_alias = aliases[first]

    herop_parts = [f"{aliases[n]}.HEROP_ID" for n in table_names]
    select_cols = [f"COALESCE({', '.join(herop_parts)}) AS HEROP_ID"]
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
    sql_parts.append(f"LIMIT {MAX_ROWS + 1}")
    return "\n".join(sql_parts)


def run_download_query(plan: DownloadPlan) -> tuple[str, int]:
    """Execute plan against BigQuery; return (csv_text, row_count)."""
    client = get_client()
    job_config = bigquery.QueryJobConfig(use_legacy_sql=False)
    try:
        query_job = client.query(plan.sql, job_config=job_config)
        result = query_job.result(timeout=QUERY_TIMEOUT_SEC)
    except Exception as exc:  # noqa: BLE001 — surface as user-facing error
        raise InteractiveDownloadError(
            f"BigQuery query failed: {exc}",
            status_code=502,
        ) from exc

    df = result.to_dataframe()
    if len(df) > MAX_ROWS:
        raise InteractiveDownloadError(
            f"Result exceeds row limit ({MAX_ROWS:,}). Narrow year, scale, or variables.",
            status_code=413,
        )
    if df.empty:
        raise InteractiveDownloadError(
            "Query returned no rows for this selection.",
            status_code=404,
        )

    buf = io.StringIO()
    df.to_csv(buf, index=False)
    return buf.getvalue(), len(df)
