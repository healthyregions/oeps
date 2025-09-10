import click

from oeps.clients.registry import Registry, TableSource
from ..registry.handlers import Registry as Registry2

from ._common_opts import (
    add_common_opts,
    registry_opt,
    overwrite_opt,
)


@click.command()
@click.option(
    "--name",
    "-n",
    help="Name of variable to move.",
)
@click.option(
    "--source",
    "-s",
    help="Name of table source from which the variable will be moved.",
)
@click.option(
    "--target",
    "-t",
    help="Name of table source to which this variable will be moved.",
)
@add_common_opts(overwrite_opt)
@add_common_opts(registry_opt)
def move_variable(name, source, target, overwrite, registry_path):
    """Move a variable from one table to another. This command is primarily meant to
    be a corrective tool to help move a set of values for a variable to a different year,
    after being initially placed in the wrong year.
    """

    # registry = Registry(registry_path)
    registry = Registry2.create_from_directory(registry_path)

    variable = registry.variables.get(name)
    if not variable:
        print(
            f"Invalid variable name: {name} -- This variable does not exist in the registry."
        )
        exit()

    # source = TableSource(source, with_data=True)
    # target = TableSource(target, with_data=True)

    ts_source = registry.table_sources.get(source)
    if ts_source is None:
        print(
            f"Invalid source name: {source} -- This table_source does not exist in the registry."
        )
        exit()
    ts_target = registry.table_sources.get(target)
    if ts_target is None:
        print(
            f"Invalid source name: {target} -- This table_source does not exist in the registry."
        )
        exit()

    if registry.geodata_sources[ts_source.geodata_source].summary_level.name != \
          registry.geodata_sources[ts_target.geodata_source].summary_level.name:
        print("Summary level is not the same between these table_sourcs.")
        print("cancelling operation")
        exit()

    ts_source.load_dataframe()
    ts_target.load_dataframe()

    if name not in ts_source.df.columns:
        print(f"This variable does not exist in the source table: {name}.")
        exit()

    if name in ts_target.df.columns:
        print("This variable already has data in the target table source.")
        if overwrite:
            c = input("Overwrite that data? Y/n ")
            if c.lower().startswith("n"):
                print("cancelling operation")
                exit()
        else:
            print("Use --overwrite to overwrite existing data for this column.")
            exit()

    var_df = ts_source.get_variable_data([name])
    source_heropids = set(ts_source.df["HEROP_ID"])
    target_heropids = set(ts_target.df["HEROP_ID"])

    var_df = registry.set_data_types(var_df)
    var_df = var_df.round(2)

    print(
        f"Number of incoming data points (i.e. unique HEROP_IDs): {len(source_heropids)}"
    )
    print(f"Length of target df: {len(target_heropids)}")

    in_source_not_in_target = source_heropids - target_heropids
    print(
        f"\nHEROP_IDs in source but not in target (data will be lost): {len(in_source_not_in_target)}"
    )
    print(var_df[var_df["HEROP_ID"].isin(in_source_not_in_target)])

    in_target_not_in_source = target_heropids - source_heropids
    print(
        f"\nHEROP_IDs in target but not in source (data will be empty): {len(in_target_not_in_source)}"
    )
    print(in_target_not_in_source)

    c = input("\nContinue?? Y/n ")
    if c.lower().startswith("n"):
        exit()

    ts_target.merge_df(var_df, overwrite=overwrite)
    ts_source.delete_variable_data(name)

    registry.update_variable_table_sources(ts_source)
    registry.update_variable_table_sources(ts_target)
