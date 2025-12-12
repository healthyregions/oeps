import click

from ..handlers import Registry

from ._common_opts import (
    add_common_opts,
    registry_opt,
)


@click.command()
@click.option(
    "--name",
    "-n",
    help="Name of variable(s) to remove. For multiple variables, use comma-separated values (e.g., -n 'Var1,Var2,Var3').",
)
@click.option(
    "--table-source",
    "-t",
    help="Name of single table source from which the variable will be removed.",
)
@click.option(
    "--yes",
    "-y",
    is_flag=True,
    default=False,
    help="Skip confirmation prompts. Useful for batch operations.",
)
@add_common_opts(registry_opt)
def remove_variable(name, table_source, registry_path, yes=False):
    """Remove variable(s) from the registry and all of their columns from table source CSVs.
    Optionally remove variables only from one table source.
    
    Can remove multiple variables at once by providing comma-separated names.
    Example (single): flask remove-variable -n Var1 -t county-2025
    Example (multiple): flask remove-variable -n "Var1,Var2,Var3" -t county-2025 --yes
    """

    registry = Registry.create_from_directory(registry_path)

    # Parse variable names - support comma-separated values for backward compatibility
    # Single variable: "VarName" -> ["VarName"]
    # Multiple variables: "Var1,Var2,Var3" -> ["Var1", "Var2", "Var3"]
    if not name:
        print("Error: Variable name must be provided with --name/-n")
        exit(1)
    
    variable_names = [v.strip() for v in name.split(",") if v.strip()]
    
    if not variable_names:
        print("Error: At least one variable name must be provided with --name/-n")
        exit(1)

    # Validate all variables exist
    invalid_vars = []
    for var_name in variable_names:
        if not registry.variables.get(var_name):
            invalid_vars.append(var_name)
    
    if invalid_vars:
        print(f"Invalid variable name(s): {', '.join(invalid_vars)} -- These variables do not exist in the registry.")
        exit(1)

    # If table_source is specified, remove from that table source only
    if table_source:
        ts = registry.table_sources.get(table_source)
        if not ts:
            print(f"Invalid table source name: {table_source}")
            exit(1)
        
        if len(variable_names) == 1:
            prompt = f"\n{variable_names[0]} column will be removed from the {ts.name} CSV. Continue? Y/n "
        else:
            prompt = f"\n{len(variable_names)} variables will be removed from the {ts.name} CSV:\n  {', '.join(variable_names)}\nContinue? Y/n "
        
        if yes or not input(prompt).lower().startswith("n"):
            for var_name in variable_names:
                ts.delete_variable_data(var_name)
            registry.update_variable_table_sources(ts.name)
            print(f"Successfully removed {len(variable_names)} variable(s) from {ts.name}")
        else:
            print(" -- cancel operation")
            return

    else:
        # Remove from all table sources where variables exist
        if len(variable_names) == 1:
            var_name = variable_names[0]
            variable = registry.variables.get(var_name)
            sources = [i for i in registry.table_sources.values() if i.name in variable.table_sources]
            source_names = "\n  ".join([i.name for i in sources])
            print(
                f"\nVariable will be removed from registry, and {var_name} column will be removed from the following CSVs:\n  {source_names}"
            )
            if yes or not input("Continue? Y/n").lower().startswith("n"):
                for source in sources:
                    source.delete_variable_data(var_name)
                registry.remove_variable(var_name)
            else:
                print(" -- cancel operation")
                return
        else:
            # Multiple variables - show summary
            all_sources = set()
            for var_name in variable_names:
                variable = registry.variables.get(var_name)
                sources = [i.name for i in registry.table_sources.values() if i.name in variable.table_sources]
                all_sources.update(sources)
            
            source_names = "\n  ".join(sorted(all_sources))
            print(
                f"\n{len(variable_names)} variables will be removed from registry, and their columns will be removed from the following CSVs:\n  {source_names}"
            )
            print(f"\nVariables to remove: {', '.join(variable_names)}")
            if yes or not input("Continue? Y/n").lower().startswith("n"):
                for var_name in variable_names:
                    variable = registry.variables.get(var_name)
                    sources = [i for i in registry.table_sources.values() if i.name in variable.table_sources]
                    for source in sources:
                        source.delete_variable_data(var_name)
                    registry.remove_variable(var_name)
                print(f"Successfully removed {len(variable_names)} variable(s)")
            else:
                print(" -- cancel operation")
                return

    print("""
To complete the variable removal(s), the following operations must be run and all resulting files committed to version control:

    flask create-data-dictionaries
    flask build-docs registry-summary
    flask build-explorer-docs
    flask build-explorer-map --upload
""")
