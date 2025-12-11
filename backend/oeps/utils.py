import csv
import json
import requests
from tqdm import tqdm
from pathlib import Path
import random


def make_id(length: int = 6):
    """Creates a random hexadecimal identifier."""
    return "".join(random.choices("0123456789ABCDEF", k=length))


def load_json(path) -> dict:
    """Loads a .json file into a dict object."""
    with open(path, "r") as o:
        return json.load(o)


def write_json(data, path):
    """Writes a dict to JSON format in the specified path."""
    with open(path, "w") as o:
        return json.dump(data, o, indent=2)
    return path


def write_csv(path: Path, header: list, rows: list):
    """Uses the basic CSV writer to create a file from input headers and rows"""
    with open(path, "w") as o:
        writer = csv.writer(o)
        writer.writerow(header)
        writer.writerows(rows)


def download_file(url, filepath, desc=None, progress_bar=False, no_cache: bool = False):
    """Download a single file. Optionally print a progress bar. If a local file
    already exists it will be used unless no_cache=True."""

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
