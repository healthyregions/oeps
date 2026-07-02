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
    help="Fail if a variable table_sources entry has no matching column in that CSV.",
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
    help="Enforce MOUD/access geography rules for table_sources.",
)
@click.option(
    "--strict",
    is_flag=True,
    default=False,
    help="Enable --check-columns, --check-duplicate-titles, and --check-geography-rules.",
)
def validate_registry(
    registry_path: Path,
    sync_table_sources: bool,
    check_columns: bool,
    check_duplicate_titles: bool,
    duplicate_titles_as_error: bool,
    check_geography_rules: bool,
    strict: bool,
):
    """Runs validation processes against the current registry content."""

    if strict:
        check_columns = True
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
            duplicate_titles_as_error=duplicate_titles_as_error,
        )
    except RegistryValidationError as exc:
        raise click.ClickException(str(exc)) from exc

    if sync_table_sources:
        registry.update_variable_table_sources()
