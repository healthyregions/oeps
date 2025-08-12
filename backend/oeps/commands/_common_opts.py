import os
from pathlib import Path

import click

from oeps.config import (
    TEMP_DIR,
    EXPLORER_ROOT_DIR,
    REGISTRY_DIR,
)

# Make relative paths for directory configs so they can properly be used as default values for
# CLI arguments. Using absolute paths (e.g. those in the config) would result in absolute paths
# in the generated docs... this would be incorrect on every system besides the one that had
# generated the docs.
backend_dir = Path(__file__).parent.parent.parent

EXPLORER_ROOT_DIR_rel = Path(os.path.relpath(EXPLORER_ROOT_DIR, start=backend_dir))
TEMP_DIR_rel = Path(os.path.relpath(TEMP_DIR, start=backend_dir))
REGISTRY_DIR_rel = Path(os.path.relpath(REGISTRY_DIR, start=backend_dir))


def add_common_opts(*options):
    """Helper function for grouping multiple options into a single decorator
    so they can easily be applied multiple commands.
    see: https://stackoverflow.com/a/67138197/3873885"""

    def wrapper(function):
        for option in reversed(options):
            function = option(function)
        return function

    return wrapper


## define some basic command options that can be reused in many places.
verbose_opt = click.option(
    "--verbose",
    is_flag=True,
    help="Enable verbose logging.",
)
overwrite_opt = click.option(
    "--overwrite",
    is_flag=True,
    help="Overwrite output content if it already exists.",
)
registry_opt = click.option(
    "--registry-path",
    help="Optional override for the registry directory.",
    default=REGISTRY_DIR_rel,
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
explorer_opt = click.option(
    "--explorer-path",
    help="Optional override for the root directory of the explorer.",
    default=EXPLORER_ROOT_DIR_rel,
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
