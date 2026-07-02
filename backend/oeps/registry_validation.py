"""Registry validation helpers for flask validate-registry."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .handlers import Registry

POINT_TMDR_VARIABLES = frozenset({"MetTmDr", "BupTmDr", "NaltTmDr", "OtpTmDr"})
IMPEDANCE_TMDR_VARIABLES = frozenset({"MetTmDr2", "BupTmDr2", "NaltTmDr2", "OtpTmDr2"})
IMPEDANCE_TRACT_TABLE = "tract-2025"

class RegistryValidationError(Exception):
    """Raised when registry validation fails."""


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _table_summary_level(registry: Registry, table_source_name: str) -> str | None:
    ts = registry.table_sources.get(table_source_name)
    if not ts:
        return None
    gs = registry.geodata_sources.get(ts.geodata_source)
    if not gs:
        return None
    return gs.summary_level.name


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
        pathpath = Path(v.full_path)
        if pathpath.stem != v.name:
            result.errors.append(
                f"{k} | CSV file name must match table_source name: {pathpath.stem}"
            )
        if not pathpath.is_file():
            result.errors.append(f"{k} | CSV not found: {v.full_path}")

    return result


def validate_registry_csv_columns(registry: Registry) -> ValidationResult:
    """Every table_sources entry must have the variable column in that CSV."""
    result = ValidationResult()
    table_columns: dict[str, set[str]] = {}

    for ts_name, ts in registry.table_sources.items():
        pathpath = Path(ts.full_path)
        if not pathpath.is_file():
            continue
        ts.load_dataframe()
        table_columns[ts_name] = set(ts.df.columns)

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


def validate_geography_rules(registry: Registry) -> ValidationResult:
    """MOUD/access geography rules from issue #391."""
    result = ValidationResult()
    tract_cols: set[str] | None = None
    tract_ts = registry.table_sources.get(IMPEDANCE_TRACT_TABLE)
    if tract_ts and Path(tract_ts.full_path).is_file():
        tract_ts.load_dataframe()
        tract_cols = set(tract_ts.df.columns)

    for var_name, variable in registry.variables.items():
        if (
            var_name in IMPEDANCE_TMDR_VARIABLES
            and tract_cols is not None
            and var_name in tract_cols
            and IMPEDANCE_TRACT_TABLE not in variable.table_sources
        ):
            result.errors.append(
                f"{var_name} | column exists in {IMPEDANCE_TRACT_TABLE} but "
                f"{IMPEDANCE_TRACT_TABLE} is not in table_sources"
            )

        for ts_name in variable.table_sources:
            level = _table_summary_level(registry, ts_name)
            if not level:
                continue

            if var_name in POINT_TMDR_VARIABLES and level in {"state", "county"}:
                result.errors.append(
                    f"{var_name} | point-to-point driving time must not use "
                    f"{ts_name} ({level} level); remove from table_sources"
                )

            if any(
                marker in var_name
                for marker in ("TmDrP", "CtTmDr")
            ) and level in {"tract", "zcta"}:
                result.errors.append(
                    f"{var_name} | rollup variable must not use "
                    f"{ts_name} ({level} level)"
                )

            if "AvTmDr" in var_name and level in {"tract", "zcta"}:
                result.errors.append(
                    f"{var_name} | average driving time must not use "
                    f"{ts_name} ({level} level)"
                )

    return result


def run_registry_validation(
    registry: Registry,
    *,
    check_columns: bool = False,
    check_duplicate_titles: bool = False,
    check_geography_rules: bool = False,
    duplicate_titles_as_error: bool = False,
) -> ValidationResult:
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

    if check_duplicate_titles:
        partial = validate_duplicate_titles(registry)
        if duplicate_titles_as_error:
            combined.errors.extend(partial.warnings)
            partial.warnings = []
        combined.warnings.extend(partial.warnings)

    if check_geography_rules:
        partial = validate_geography_rules(registry)
        combined.errors.extend(partial.errors)
        combined.warnings.extend(partial.warnings)

    return combined


def print_validation_result(result: ValidationResult) -> None:
    for message in result.warnings:
        print(f"WARNING: {message}")
    for message in result.errors:
        print(f"ERROR: {message}")
