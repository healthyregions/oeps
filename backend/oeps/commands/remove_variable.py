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
        
        if not yes:
            if len(variable_names) == 1:
                prompt = f"\n{variable_names[0]} column will be removed from the {ts.name} CSV. Continue? Y/n "
            else:
                prompt = f"\n{len(variable_names)} variables will be removed from the {ts.name} CSV:\n  {', '.join(variable_names)}\nContinue? Y/n "
            
            if input(prompt).lower().startswith("n"):
                print(" -- cancel operation")
                return
        
        # Proceed with removal
        # Load dataframe to check which variables actually exist
        if ts.df is None:
            ts.load_dataframe()
        
        # Filter to only variables that exist in this table source
        existing_vars = [var_name for var_name in variable_names if var_name in ts.df.columns]
        missing_vars = [var_name for var_name in variable_names if var_name not in ts.df.columns]
        
        if missing_vars:
            print(f"Warning: The following variables are not in {ts.name} and will be skipped: {', '.join(missing_vars)}")
        
        # Only delete variables that exist
        for var_name in existing_vars:
            ts.delete_variable_data(var_name)
            # Update table_sources for this specific variable only
            variable = registry.variables.get(var_name)
            if variable and ts.name in variable.table_sources:
                variable.table_sources = [i for i in variable.table_sources if i != ts.name]
                registry.save_variable(variable)
        print(f"Successfully removed {len(existing_vars)} variable(s) from {ts.name}")

    else:
        # Remove from all table sources where variables exist
        # Build summary of what will be removed
        all_sources = set()
        for var_name in variable_names:
            variable = registry.variables.get(var_name)
            sources = [i.name for i in registry.table_sources.values() if i.name in variable.table_sources]
            all_sources.update(sources)
        
        source_names = "\n  ".join(sorted(all_sources))
        if len(variable_names) == 1:
            print(
                f"\nVariable will be removed from registry, and {variable_names[0]} column will be removed from the following CSVs:\n  {source_names}"
            )
        else:
            print(
                f"\n{len(variable_names)} variables will be removed from registry, and their columns will be removed from the following CSVs:\n  {source_names}"
            )
            print(f"\nVariables to remove: {', '.join(variable_names)}")
        
        # Confirm before proceeding
        if not yes and input("Continue? Y/n").lower().startswith("n"):
            print(" -- cancel operation")
            return
        
        # Remove each variable from all its sources
        for var_name in variable_names:
            variable = registry.variables.get(var_name)
            sources = [i for i in registry.table_sources.values() if i.name in variable.table_sources]
            for source in sources:
                if source.df is None:
                    source.load_dataframe()
                if var_name in source.df.columns:
                    source.delete_variable_data(var_name)
            registry.remove_variable(var_name)
        
        print(f"Successfully removed {len(variable_names)} variable(s)")
