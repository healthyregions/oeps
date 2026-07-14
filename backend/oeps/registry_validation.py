"""Registry validation helpers for flask validate-registry."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

import yaml

if TYPE_CHECKING:
    from .handlers import Registry

_REGISTRY_DIR = Path(__file__).resolve().parent / "registry"
_DEFAULT_ALLOWLIST_PATH = _REGISTRY_DIR / "validation_allowlist.yaml"
_SKIP_CSV_COLUMNS = frozenset({"HEROP_ID", "FIPS", "ZCTA5", "Name"})


class RegistryValidationError(Exception):
    """Raised when registry validation fails."""


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


@dataclass(frozen=True)
class ValidationAllowlist:
    geography_table_sources: frozenset[tuple[str, str]]
    csv_orphan_columns: frozenset[tuple[str, str]]


def _load_allowlist(path: Path | None = None) -> ValidationAllowlist:
    allowlist_path = path or _DEFAULT_ALLOWLIST_PATH
    if not allowlist_path.is_file():
        return ValidationAllowlist(
            geography_table_sources=frozenset(),
            csv_orphan_columns=frozenset(),
        )

    raw = yaml.safe_load(allowlist_path.read_text(encoding="utf-8")) or {}
    geography = frozenset(
        (entry["variable"], entry["table_source"])
        for entry in raw.get("geography_table_sources", [])
        if entry.get("variable") and entry.get("table_source")
    )
    csv_orphans = frozenset(
        (entry["variable"], entry["table_source"])
        for entry in raw.get("csv_orphan_columns", [])
        if entry.get("variable") and entry.get("table_source")
    )
    return ValidationAllowlist(
        geography_table_sources=geography,
        csv_orphan_columns=csv_orphans,
    )


def is_point_tmdr(var_name: str) -> bool:
    """Point-to-point driving time (*TmDr), not rollup/average/impedance variants."""
    if "TmDr" not in var_name:
        return False
    if "AvTmDr" in var_name:
        return False
    if "TmDrP" in var_name:
        return False
    if "CtTmDr" in var_name:
        return False
    if "TmDr2" in var_name:
        return False
    return True


def is_impedance_point_tmdr(var_name: str) -> bool:
    """Impedance-adjusted point driving time (*TmDr2), not rollup/average variants."""
    if "TmDr2" not in var_name:
        return False
    if "AvTmDr" in var_name:
        return False
    if "CtTmDr" in var_name:
        return False
    if "TmDrP" in var_name:
        return False
    return True


def is_rollup_tmdr(var_name: str) -> bool:
    return "TmDrP" in var_name or "CtTmDr" in var_name


def is_average_tmdr(var_name: str) -> bool:
    return "AvTmDr" in var_name


def _table_summary_level(registry: Registry, table_source_name: str) -> str | None:
    ts = registry.table_sources.get(table_source_name)
    if not ts:
        return None
    gs = registry.geodata_sources.get(ts.geodata_source)
    if not gs:
        return None
    return gs.summary_level.name


def _is_remote_table_path(path: str) -> bool:
    return path.startswith("http://") or path.startswith("https://")


def _load_table_columns(registry: Registry) -> dict[str, set[str]]:
    table_columns: dict[str, set[str]] = {}
    for ts_name, ts in registry.table_sources.items():
        if _is_remote_table_path(ts.full_path):
            continue
        pathpath = Path(ts.full_path)
        if not pathpath.is_file():
            continue
        ts.load_dataframe()
        table_columns[ts_name] = set(ts.df.columns)
    return table_columns


def validate_registry_structure(registry: Registry) -> ValidationResult:
    """Checks that were previously print-only in Registry.validate()."""
    result = ValidationResult()

    for k, v in registry.variables.items():
        if v.metadata not in registry.metadata:
            result.errors.append(f"{k} | invalid metadata name: {v.metadata}")
        for t in v.table_sources:
            if t not in registry.table_sources:
                result.errors.append(f"{k} | invalid table source name: {t}")

    for k, v in registry.table_sources.items():
        if v.geodata_source not in registry.geodata_sources:
            result.errors.append(f"{k} | invalid geodata_source: {v.geodata_source}")
        if _is_remote_table_path(v.full_path):
            continue
        pathpath = Path(v.full_path)
        if pathpath.stem != v.name:
            result.errors.append(
                f"{k} | CSV file name must match table_source name: {pathpath.stem}"
            )
        if not pathpath.is_file():
            result.errors.append(f"{k} | CSV not found: {v.full_path}")

    return result


def validate_registry_csv_columns(registry: Registry) -> ValidationResult:
    """Check table_sources ↔ CSV column wiring both directions.

    - Forward: every table_sources entry must have the variable column in that CSV.
    - Reverse (empty links): if table_sources is empty but the variable name
      appears as a column in any local CSV, fail (map will omit real data).
    """
    result = ValidationResult()
    table_columns = _load_table_columns(registry)

    for var_name, variable in registry.variables.items():
        for ts_name in variable.table_sources:
            cols = table_columns.get(ts_name)
            if cols is None:
                continue
            if var_name not in cols:
                result.errors.append(
                    f"{var_name} | column missing from {ts_name} CSV "
                    f"(listed in table_sources but not in file)"
                )

        if not variable.table_sources:
            tables_with_col = sorted(
                ts_name
                for ts_name, cols in table_columns.items()
                if var_name in cols
            )
            if tables_with_col:
                result.errors.append(
                    f"{var_name} | empty table_sources but column exists in "
                    f"{', '.join(tables_with_col)}; link the table or remove "
                    f"the orphan column"
                )

    return result


def validate_registry_csv_orphans(
    registry: Registry,
    *,
    allowlist: ValidationAllowlist | None = None,
) -> ValidationResult:
    """Warn when a registry variable column exists in a CSV but is not linked."""
    result = ValidationResult()
    allowlist = allowlist or _load_allowlist()
    table_columns = _load_table_columns(registry)

    for ts_name, cols in table_columns.items():
        for col in cols:
            if col in _SKIP_CSV_COLUMNS:
                continue
            if col not in registry.variables:
                continue
            variable = registry.variables[col]
            if ts_name in variable.table_sources:
                continue
            if (col, ts_name) in allowlist.csv_orphan_columns:
                continue
            result.warnings.append(
                f"{col} | column in {ts_name} CSV but not in table_sources "
                f"(orphan column; link registry or remove from CSV)"
            )

    return result


def validate_duplicate_titles(registry: Registry) -> ValidationResult:
    """Warn when multiple variables share the same display title."""
    result = ValidationResult()
    by_title: dict[str, list[str]] = defaultdict(list)
    for name, variable in registry.variables.items():
        by_title[variable.title].append(name)

    for title, names in sorted(by_title.items()):
        if len(names) > 1:
            result.warnings.append(
                f"duplicate title {title!r} | variables: {', '.join(sorted(names))}"
            )

    return result


def validate_geography_rules(
    registry: Registry,
    *,
    allowlist: ValidationAllowlist | None = None,
) -> ValidationResult:
    """Pattern-based geography rules for access/driving-time variables."""
    result = ValidationResult()
    allowlist = allowlist or _load_allowlist()
    table_columns = _load_table_columns(registry)

    for var_name, variable in registry.variables.items():
        if is_impedance_point_tmdr(var_name):
            for ts_name, cols in table_columns.items():
                if _table_summary_level(registry, ts_name) != "tract":
                    continue
                if var_name not in cols:
                    continue
                if ts_name in variable.table_sources:
                    continue
                if (var_name, ts_name) in allowlist.geography_table_sources:
                    continue
                result.errors.append(
                    f"{var_name} | column exists in {ts_name} but "
                    f"{ts_name} is not in table_sources"
                )

        for ts_name in variable.table_sources:
            level = _table_summary_level(registry, ts_name)
            if not level:
                continue

            if (var_name, ts_name) in allowlist.geography_table_sources:
                continue

            if is_point_tmdr(var_name) and level in {"state", "county"}:
                result.errors.append(
                    f"{var_name} | point-to-point driving time must not use "
                    f"{ts_name} ({level} level); remove from table_sources"
                )

            if is_rollup_tmdr(var_name) and level in {"tract", "zcta"}:
                result.errors.append(
                    f"{var_name} | rollup variable must not use "
                    f"{ts_name} ({level} level)"
                )

            if is_average_tmdr(var_name) and level in {"tract", "zcta"}:
                result.errors.append(
                    f"{var_name} | average driving time must not use "
                    f"{ts_name} ({level} level)"
                )

    return result


def run_registry_validation(
    registry: Registry,
    *,
    check_columns: bool = False,
    check_csv_orphans: bool = False,
    check_duplicate_titles: bool = False,
    check_geography_rules: bool = False,
    duplicate_titles_as_error: bool = False,
    csv_orphans_as_error: bool = False,
    allowlist_path: Path | None = None,
) -> ValidationResult:
    allowlist = _load_allowlist(allowlist_path)
    combined = ValidationResult()

    for partial in (
        validate_registry_structure(registry),
    ):
        combined.errors.extend(partial.errors)
        combined.warnings.extend(partial.warnings)

    if check_columns:
        partial = validate_registry_csv_columns(registry)
        combined.errors.extend(partial.errors)
        combined.warnings.extend(partial.warnings)

    if check_csv_orphans:
        partial = validate_registry_csv_orphans(registry, allowlist=allowlist)
        if csv_orphans_as_error:
            combined.errors.extend(partial.warnings)
            partial.warnings = []
        combined.warnings.extend(partial.warnings)

    if check_duplicate_titles:
        partial = validate_duplicate_titles(registry)
        if duplicate_titles_as_error:
            combined.errors.extend(partial.warnings)
            partial.warnings = []
        combined.warnings.extend(partial.warnings)

    if check_geography_rules:
        partial = validate_geography_rules(registry, allowlist=allowlist)
        combined.errors.extend(partial.errors)
        combined.warnings.extend(partial.warnings)

    return combined


def print_validation_result(result: ValidationResult) -> None:
    for message in result.warnings:
        print(f"WARNING: {message}")
    for message in result.errors:
        print(f"ERROR: {message}")
