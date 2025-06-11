from pathlib import Path

import click

from oeps.clients.explorer import Explorer
from oeps.clients.registry import Registry
from oeps.clients.s3 import clear_s3_bucket
from oeps.utils import load_json

from ._common_opts import (
    add_common_opts,
    explorer_opt,
)


@click.command()
@add_common_opts(explorer_opt)
def clean_explorer_bucket(
    explorer_path: Path
):
    """Deletes all files from the S3 bucket which are not mentioned in the local
    explorer/configs/sources.json file. If no sources.json file exists, optionally
    deletes all uploaded files.
    """
    config_dir = Path(explorer_path, "config")
    objs_in_use = []

    # command is highly destructive if sources.json is missing
    # so prompt user in that case
    try:
        sources = load_json(Path(config_dir, 'sources.json'))['sources']
        tables = [source['tables'] for source in sources]

        # grab all filenames nested in the sources.json
        objs_in_use = [
            value['file'].split('/')[-1] 
            for table in tables
            for value in table.values()
        ]

    except FileNotFoundError:            
        print(f"{Path(config_dir, 'sources.json')} not found, so continuing will delete all files in the bucket which start with `explorer/csv`.")
        resp = input("Would you like to continue with deletion? (y/N)")
        if resp.lower() != 'y':
            print("Exiting without deleting files.")
            return
    
    objs_in_use = objs_in_use + ['counties.csv', 'states.csv']

    clear_s3_bucket(prefix='explorer/csv', objs_to_keep=objs_in_use)

