import os
import sys
import json
import threading
import boto3
import requests
from glob import glob
from pathlib import Path

def load_json(path):
    with open(path, "r") as o:
        return json.load(o)


class S3ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename

        def b_to_mb(bytes):
            return round(bytes / (1024*1024), 2)

        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, b_to_mb(self._seen_so_far), b_to_mb(self._size),
                    percentage))
            sys.stdout.flush()

def upload_to_s3(paths):

    s3 = boto3.resource("s3")
    bucket = os.getenv("AWS_BUCKET_NAME")

    for path in paths:
        print(path)
        print(path.name)
        s3.Bucket(bucket).upload_file(str(path), path.name, Callback=S3ProgressPercentage(str(path)))
        print(" -- done")

def get_path_or_paths(path_input, extension=None):

    if os.path.isdir(path_input):
        if extension:
            paths = glob(os.path.join(path_input, f"*.{extension}"))
        else:
            paths = glob(os.path.join(path_input))
    elif os.path.isfile(path_input):
        paths = [path_input]
    else:
        print('invalid path:', path_input)
        exit()
    
    return paths

def download_path(path, out_dir):
    """ Takes an input url to a file and downloads it to specified dir.
    If that url points to a .shp file, attempt to download sidecars
    as well. Return only the path to the file from the original
    url. """

    if not isinstance(path, list):
        path = [path]

    local_paths = []
    for url in path:
        name = url.split("/")[-1]
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            out_path = Path(out_dir, name)
            print(f"  get: {url} --> {out_path}")
            with open(Path(out_dir, name), mode="wb") as file:
                for chunk in response.iter_content(chunk_size=10 * 1024):
                    file.write(chunk)
            local_paths.append(out_path)

    return local_paths

