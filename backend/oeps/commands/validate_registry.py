import click
from pathlib import Path

from ..handlers import Registry
from ..registry_validation import RegistryValidationError
from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@add_common_opts(registry_opt)
@click.option(
    "--sync-table-sources",
    is_flag=True,
    default=False,
    help="Updates all variable table_sources values directly from CSV data.",
)
@click.option(
    "--check-columns",
    is_flag=True,
    default=False,
    help=(
        "Fail if table_sources miss CSV columns, or if table_sources is empty "
        "but the variable name exists as a column in a CSV."
    ),
)
@click.option(
    "--check-duplicate-titles",
    is_flag=True,
    default=False,
    help="Report variables that share the same display title.",
)
@click.option(
    "--duplicate-titles-as-error",
    is_flag=True,
    default=False,
    help="Treat duplicate titles as errors (use with --check-duplicate-titles).",
)
@click.option(
    "--check-geography-rules",
    is_flag=True,
    default=False,
    help="Enforce pattern-based geography rules for table_sources.",
)
@click.option(
    "--check-csv-orphans",
    is_flag=True,
    default=False,
    help="Warn when a registry variable column exists in a CSV but is not linked.",
)
@click.option(
    "--csv-orphans-as-error",
    is_flag=True,
    default=False,
    help="Treat CSV orphan column warnings as errors (use with --check-csv-orphans).",
)
@click.option(
    "--strict",
    is_flag=True,
    default=False,
    help="Enable --check-columns, --check-csv-orphans, --check-duplicate-titles, and --check-geography-rules.",
)
def validate_registry(
    registry_path: Path,
    sync_table_sources: bool,
    check_columns: bool,
    check_duplicate_titles: bool,
    duplicate_titles_as_error: bool,
    check_geography_rules: bool,
    check_csv_orphans: bool,
    csv_orphans_as_error: bool,
    strict: bool,
):
    """Runs validation processes against the current registry content."""

    if strict:
        check_columns = True
        check_csv_orphans = True
        check_duplicate_titles = True
        check_geography_rules = True

    registry = Registry.create_from_directory(registry_path)
    print(f"variables: {len(registry.variables)}")
    print(f"table sources: {len(registry.table_sources)}")
    print(f"geodata sources: {len(registry.geodata_sources)}")
    print(f"metadata entries: {len(registry.metadata)}")

    try:
        registry.validate(
            check_columns=check_columns,
            check_duplicate_titles=check_duplicate_titles,
            check_geography_rules=check_geography_rules,
            check_csv_orphans=check_csv_orphans,
            duplicate_titles_as_error=duplicate_titles_as_error,
            csv_orphans_as_error=csv_orphans_as_error,
        )
    except RegistryValidationError as exc:
        raise click.ClickException(str(exc)) from exc

    if sync_table_sources:
        registry.update_variable_table_sources()
