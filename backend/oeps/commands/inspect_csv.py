import csv
from pathlib import Path

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
    help="Path to CSV or directory of CSVs to be inspected.",
)
@add_common_opts(registry_opt)
def inspect_csv(source, registry_path):
    """Inspects an incoming CSV, or directory of CSVs, to test their columns against existing variables in the registry."""

    registry = Registry(registry_path)

    all_unmatched = []

    if Path(source).is_file() and source.endswith("csv"):
        files = [source]
    elif Path(source).is_dir():
        files = [i for i in Path(source).glob("**/*.csv")]
    else:
        print("invalid source input. must be CSV or directory.")

    for f in files:
        print(f"\n{f}")
        with open(f, "r") as o:
            reader = csv.reader(o)
            headers = next(reader)
        matched = [i for i in headers if i in registry.variables]
        notmatched = [i for i in headers if i not in registry.variables]
        print(len(headers), " columns")
        print(
            f"{len(matched)} matched: ",
            ", ".join([i for i in headers if i in registry.variables]),
        )
        print(
            f"{len(notmatched)} not matched: ",
            ", ".join([i for i in headers if i not in registry.variables]),
        )
        for i in notmatched:
            all_unmatched.append(i)

    all_unique = list(set(all_unmatched))
    print(f"\nFULL LIST OF UNMATCHED VARIABLES ({len(all_unique)}):")
    for i in all_unique:
        print(i)
