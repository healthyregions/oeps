import os
from datetime import datetime
from pathlib import Path
from argparse import Namespace

import click
from flask.cli import AppGroup

from oeps.clients.frictionless import DataResource, DataPackage, create_data_dictionaries
from oeps.config import (
    RESOURCES_DIR,
    CACHE_DIR,
)
from oeps.utils import handle_overwrite

# Make relative paths for directory configs so they can properly be used as default values for 
# CLI arguments. Using absolute paths (e.g. those in the config) would result in absolute paths
# in the generated docs... this would be incorrect on every system besides the one that had 
# generated the docs.
RESOURCES_DIR_rel = os.path.relpath(RESOURCES_DIR, start=Path(__file__).parent.parent.parent)
CACHE_DIR_rel = os.path.relpath(CACHE_DIR, start=Path(__file__).parent.parent.parent)

frictionless_grp = AppGroup('frictionless',
    help="A group of operations for interacting with Frictionless data specs. These commands allow us to "\
    "export Frictionless-compliant derivations of the data in OEPS."
)

@frictionless_grp.command()
@click.option('--destination', "-d",
    help="Output location for export directory. The package will be placed within this directory and given "\
        "a name generated from the current date and time.",
    default=Path(CACHE_DIR_rel, "data-packages"),
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option("--zip", 'zip_',
    is_flag=True,
    default=False,
    help="Zip the output data package."
)
@click.option("--upload",
    is_flag=True,
    default=False,
    help="Upload the zipped data package to S3. Bucket is determined by `AWS_BUCKET_NAME` environment variable."
)
@click.option("--no-cache",
    is_flag=True,
    default=False,
    help="Force re-download of any remote files."
)
@click.option("--skip-foreign-keys",
    is_flag=True,
    default=False,
    help="Don't define foreign keys in the output data package. This is needed to avoid validation errors that "\
        "occur when Shapefiles are used in foreign keys.")
@click.option("--skip-validation",
    is_flag=True,
    default=False,
    help="Don't run data package validation on the final output.")
@click.option("--overwrite",
    is_flag=True,
    default=False,
    help="Overwrite existing data package with the same name."
)
def create_data_package(
    destination: Path,
    zip_: bool=False,
    upload: bool=False,
    no_cache: bool=False,
    skip_foreign_keys: bool=False,
    skip_validation: bool=False,
    overwrite: bool=False,
):
    """Generates a Frictionless data package from the Data Resource definitions in this backend. This export
process was developed specifically to support integration of the OEPS data warehouse into the JCOIN commons.

The resulting package will be validated against the `frictionless` standard using that Python library.

`--skip-foreign-keys` to skip the creation of foreign keys--useful because foreign keys to shapefiles break
validation.

`--skip-validation` to skip the final step of running validation on the output package.
"""

    out_name = f"oeps-data-package-v2_{datetime.now().date().isoformat()}"
    out_name = out_name + "_no_foreign_keys" if skip_foreign_keys else out_name
    out_path = Path(destination, out_name)

    if not overwrite:
        handle_overwrite(out_path)

    dp = DataPackage()
    dp.create(out_path,
        zip_,
        upload,
        no_cache=no_cache,
        skip_foreign_keys=skip_foreign_keys,
        run_validation=not skip_validation,
    )

@frictionless_grp.command()
def list_resources():
    """Print a list of all data resources in the data/resources directory."""
    for i in RESOURCES_DIR.glob('*.json'):
        print(i.name)
                       
@frictionless_grp.command()
@click.option('--source', "-s",
    help="Local path to directory with Excel data dictionaries in it, or the path to a single dictionary "\
        "file. If not provided, all dictionaries stored in the GeoDaCenter/opioid-policy-scan repo will "\
        "be used.",
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    )
)
@click.option('--destination', "-d",
    default=RESOURCES_DIR_rel,
    help="Output location for generated schema files.",
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    )
)
def generate_resources_from_oeps_dicts(destination: Path, source: Path=None):
    """Creates data resource schema files from external data dictionaries.

TO DEPRECATE: Ultimately, this pattern will be deprecated in favor of the opposite: The Excel data dictionaries
will be generated directly from the data resource schema files."""

    remote_files = [
        "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/S_Dict.xlsx",
        "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/C_Dict.xlsx",
        "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/T_Dict.xlsx",
        "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/Z_Dict.xlsx",
    ]
    if source:
        if source.is_file():
            paths = [source]
        if source.is_dir():
            paths = source.glob("*_Dict.xlsx")
    else:
        paths = remote_files

    destination.mkdir(exist_ok=True)

    for path in paths:
        print(f"\nINPUT: {path}")
        files = DataResource().create_from_oeps_xlsx_data_dict(path, destination)
        print("OUTPUT:")
        for f in files:
            print(f"  {f}")

@frictionless_grp.command()
@click.option('--source', "-s",
    default=RESOURCES_DIR_rel,
    help="Input directory that holds the data resource JSON schemas to process.",
)
@click.option('--destination', "-d",
    default=Path(CACHE_DIR_rel, "dicts"),
    help="Output directory for new dictionaries.",
)
def create_oeps_dicts(**kwargs):
    """Create the human readable, MS Excel data dictionaries from the data resource schemas."""
    args = Namespace(**kwargs)

    Path(args.destination).mkdir(exist_ok=True)

    create_data_dictionaries(args.source, args.destination)
