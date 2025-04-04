import os
import sys
import json
import click
import shutil
import threading
import boto3
import requests
from typing import List
from tqdm import tqdm
from glob import glob
from pathlib import Path

BQ_TYPE_LOOKUP = {
    "string": "STRING",
    "boolean": "BOOLEAN",
    "integer": "INTEGER",
    "date": "DATE",
    "number": "NUMERIC",
}


def load_json(path) -> dict:
    with open(path, "r") as o:
        return json.load(o)


def write_json(data, path):
    with open(path, "w") as o:
        return json.dump(data, o, indent=2)
    return path


class S3ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename

        def b_to_mb(bytes):
            return round(bytes / (1024 * 1024), 2)

        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r - %s  %s / %s  (%.2f%%)"
                % (
                    Path(self._filename).name,
                    b_to_mb(self._seen_so_far),
                    b_to_mb(self._size),
                    percentage,
                )
            )
            sys.stdout.flush()


def upload_to_s3(paths: List[Path], prefix: str = None, progress_bar: bool = False):
    s3 = boto3.resource("s3")
    bucket = os.getenv("AWS_BUCKET_NAME")
    region = "us-east-2"

    for path in paths:
        key = f"{prefix}/{path.name}" if prefix else path.name
        cb = S3ProgressPercentage(str(path)) if progress_bar else None
        s3.Bucket(bucket).upload_file(str(path), key, Callback=cb)
        if progress_bar:
            print(f"\n  https://{bucket}.s3.{region}.amazonaws.com/{key}")


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
        name = path.split("/")[-1]
        out_path = Path(out_dir, name)
        if not out_path.exists() or no_cache:
            print(f"  get: {path} --> {out_path}")
            if path.startswith("http"):
                response = requests.get(path, stream=True)
                if response.status_code == 200:
                    with open(Path(out_dir, name), mode="wb") as file:
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
