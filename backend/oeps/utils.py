import os
import json
import click
import shutil
import requests
from tqdm import tqdm
from glob import glob
from pathlib import Path
import random

BQ_TYPE_LOOKUP = {
    "string": "STRING",
    "boolean": "BOOLEAN",
    "integer": "INTEGER",
    "date": "DATE",
    "number": "NUMERIC",
}


def make_id(length: int = 6):
    return "".join(random.choices("0123456789ABCDEF", k=length))


def load_json(path) -> dict:
    with open(path, "r") as o:
        return json.load(o)


def write_json(data, path):
    with open(path, "w") as o:
        return json.dump(data, o, indent=2)
    return path


def print_json(data):
    print(json.dumps(data, indent=2))


def download_file(url, filepath, desc=None, progress_bar=False, no_cache: bool = False):
    if Path(filepath).is_file() and not no_cache:
        if progress_bar:
            print(f"{desc}: use cached file")
        return filepath

    # Streaming, so we can iterate over the response.
    r = requests.get(url, stream=True)

    # Total size in bytes.
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024

    if progress_bar:
        t = tqdm(total=total_size, unit="iB", unit_scale=True, desc=desc)

    with open(filepath, "wb") as f:
        for data in r.iter_content(block_size):
            if progress_bar:
                t.update(len(data))
            f.write(data)

    if progress_bar:
        t.close()

    return filepath


def get_path_or_paths(path_input, glob_pattern="*"):
    if os.path.isdir(path_input):
        paths = glob(os.path.join(path_input, glob_pattern))
    elif os.path.isfile(path_input):
        paths = [path_input]
    else:
        print("invalid path:", path_input)
        exit()

    return paths


def fetch_files(paths, out_dir, no_cache: bool = False):
    """Takes an input list of urls or local paths to fetch into the specified dir.
    Returns a list of paths to the new files.

    Will skip existing files unless no_cache=True."""

    if not isinstance(paths, list):
        paths = [paths]

    local_paths = []
    for path in paths:
        path = Path(path)
        out_path = Path(out_dir, path.name)
        if not out_path.exists() or no_cache:
            print(f"  get: {path} --> {out_path}")
            if path.startswith("http"):
                response = requests.get(path, stream=True)
                if response.status_code == 200:
                    with open(Path(out_dir, path.name), mode="wb") as file:
                        for chunk in response.iter_content(chunk_size=10 * 1024):
                            file.write(chunk)
                else:
                    print(response)
            else:
                shutil.copy(path, out_path)
        else:
            print(f"  cached: {path} --> {out_path}")

        local_paths.append(out_path)

    return local_paths


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
