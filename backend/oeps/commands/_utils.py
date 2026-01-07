import os
import click
from pathlib import Path

def handle_overwrite(path):
    """Takes a path to a folder and prompts the user on overwrite risk if the folder
    exists and is nonempty."""

    if not Path(path).exists():
        return

    if not os.listdir(Path(path)):
        return

    click.confirm(
        f"The folder {Path(path)} already exists and contains files which may be overwritten. Proceed?",
        default=True,
        abort=True,
    )
