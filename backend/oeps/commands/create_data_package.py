from datetime import datetime
from pathlib import Path
import shutil

import click
from ..clients.frictionless import DataPackage
from ..handlers import Registry

from ._utils import (
    handle_overwrite,
)

from ._common_opts import (
    add_common_opts,
    overwrite_opt,
    registry_opt,
    data_dir_opt,
    verbose_opt,
    TEMP_DIR_rel,
)


@click.command()
@click.option(
    "--destination",
    "-d",
    help="Output location for export directory. The package will be placed within this directory and given "
    "a name generated from the current date and time.",
    default=Path(TEMP_DIR_rel, "data-packages"),
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option(
    "--config",
    "-c",
    help="Name of folder in data/package_rules that holds configs for the export.",
)
@click.option(
    "--make-all",
    is_flag=True,
    default=False,
    help="Create data packages from all configs in the package_rules directory.",
)
@click.option(
    "--zip", "zip_", is_flag=True, default=False, help="Zip the output data package."
)
@click.option(
    "--upload",
    is_flag=True,
    default=False,
    help="Upload the zipped data package to S3. Bucket is determined by `AWS_BUCKET_NAME` environment variable.",
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Force re-download of any remote files.",
)
@click.option(
    "--check-rules",
    is_flag=True,
    default=False,
    help="Only check the rules file, don't create any dataframes or output files.",
)
@click.option(
    "--skip-foreign-keys",
    is_flag=True,
    default=False,
    help="Don't define foreign keys in the output data package. This is needed to avoid validation errors that "
    "occur when Shapefiles are used in foreign keys.",
)
@click.option(
    "--skip-validation",
    is_flag=True,
    default=False,
    help="Don't run data package validation on the final output.",
)
@add_common_opts(overwrite_opt, registry_opt, data_dir_opt, verbose_opt)
def create_data_package(
    destination,
    config,
    make_all,
    zip_,
    upload,
    no_cache,
    skip_foreign_keys,
    skip_validation,
    check_rules,
    overwrite,
    registry_path,
    data_dir_path,
    verbose,
):
    """Generates a Frictionless data package from the Data Resource definitions in this backend. This export
    process was developed specifically to support integration of the OEPS data warehouse into the JCOIN commons.

    The resulting package will be validated against the `frictionless` standard using that Python library.

    `--skip-foreign-keys` to skip the creation of foreign keys--useful because foreign keys to shapefiles break
    validation.

    `--skip-validation` to skip the final step of running validation on the output package.
    """

    package_rules_dir = Path(data_dir_path, "package_rules")

    if config:
        config_names = [config]
    elif make_all:
        config_names = [i.name for i in package_rules_dir.glob("*") if i.is_dir()]
    else:
        print("Must include one of -c <config name> or --make_all")
        exit()

    for config_name in config_names:
        print(f"CREATE DATA PACKAGE: {config_name}\n----\n")
        rules_dir = Path(package_rules_dir, config_name)

        if not rules_dir.is_dir():
            print(f"No directory for data rules: {config_name}")
            print(f"Expected path: {rules_dir.resolve()}")
            exit()

        out_name = f"oeps-{config_name}_{datetime.now().date().isoformat()}"
        out_name = out_name + "_no_foreign_keys" if skip_foreign_keys else out_name
        out_path = Path(destination, out_name)

        if not overwrite:
            handle_overwrite(out_path)

        if out_path.is_dir():
            shutil.rmtree(out_path)

        registry = Registry.create_from_directory(registry_path)
        dp = DataPackage(out_path)

        dp.create_from_rules(
            registry,
            rules_dir,
            check_rules=check_rules,
            zip_output=zip_,
            upload=upload,
            no_cache=no_cache,
            skip_foreign_keys=skip_foreign_keys,
            run_validation=not skip_validation,
            verbose=verbose,
        )
