import click

from oeps.clients.registry import Registry, TableSource

from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@click.option(
    "--name",
    "-n",
    help="Name of variable to remove.",
)
@click.option(
    "--table-source",
    "-t",
    help="Name of single table source from which the variable will be removed.",
)
@add_common_opts(registry_opt)
def remove_variable(name, table_source, registry_path):
    """Move a variable from one table to another. This command is primarily meant to
    be a corrective tool to help move a set of values for a variable to a different year,
    after being initially placed in the wrong year.
    """

    registry = Registry(registry_path)

    variable = registry.variables.get(name)
    if not variable:
        print(
            f"Invalid variable name: {name} -- This variable does not exist in the registry."
        )
        exit()

    if table_source:
        source = TableSource(table_source, with_data=True)
        if (
            not input(
                f"\n{name} column will be removed from the {source.name} CSV. Continue? Y/n "
            )
            .lower()
            .startswith("n")
        ):
            source.delete_variable_data(name)
            registry.sync_variable_table_sources(source)
        else:
            print(" -- cancel operation")

    else:
        sources = [TableSource(i, with_data=True) for i in variable["table_sources"]]
        source_names = "\n  ".join([i.name for i in sources])
        print(
            f"\nVariable will be removed from registry, and {name} column will be removed from the following CSVs:\n  {source_names}"
        )
        if not input("Continue? Y/n").lower().startswith("n"):
            for source in sources:
                source.delete_variable_data(name)
            registry.remove_variable(name)
        else:
            print(" -- cancel operation")
            exit()

    print("""
To complete this variable's removal, the following operations must be run and all resulting files committed to version control:

    flask create-data-dictionaries
    flask build-docs registry-summary
    flask build-explorer-docs
    flask build-explorer-map --upload
""")
