import click

from oeps.clients.registry import Registry

from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@click.option(
    "--source",
    "-s",
    help="Path to CSV that will be merged into the data registry.",
)
@click.option(
    "--geodata-source",
    "-g",
    help="Name of the geodata source this table will be joined to.",
)
@click.option(
    "--year",
    "-y",
    help="Name of the geodata source this table will be joined to.",
)
@click.option(
    "--force",
    is_flag=True,
    default=False,
    help="Continue without any prompts",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Continue without any prompts",
)
@add_common_opts(registry_opt)
def merge_data_table(source, geodata_source, year, force, registry_path, dry_run):
    """Merge data from an external CSV into the canonical CSVs in OEPS."""

    registry = Registry(registry_path)
    if geodata_source not in registry.geodata_sources:
        raise ValueError(
            f"Invalid geodata_source name: {geodata_source}. Must be one of: {', '.join(registry.geodata_sources.keys())}"
        )

    matched, missing = registry.check_input_table(source)
    print(f"{len(matched)} columns match to variables already in the registry")
    print(
        f"{len(missing)} columns are not yet in the registry and will be ignored. List of unmatched columns:"
    )
    for i in missing:
        print(i)
    if len(missing) > 0 and not force:
        c = input("continue? Y/n ")
        if c and c.lower().startswith("n"):
            exit()
    registry.merge_table(source, geodata_source, year, dry_run=dry_run)
