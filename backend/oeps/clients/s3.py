import os
import sys
import threading
import boto3
from typing import List
from pathlib import Path


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


def upload_to_s3(path: Path, prefix: str = None, progress_bar: bool = False):
    s3 = boto3.resource("s3")
    bucket = os.getenv("AWS_BUCKET_NAME")
    region = "us-east-2"

    key = f"{prefix}/{path.name}" if prefix else path.name
    cb = S3ProgressPercentage(str(path)) if progress_bar else None
    s3.Bucket(bucket).upload_file(str(path), key, Callback=cb)
    if progress_bar:
        print(f"\n  https://{bucket}.s3.{region}.amazonaws.com/{key}")


def batch_upload_to_s3(
    paths: List[Path], prefix: str = None, progress_bar: bool = False
):
    for path in paths:
        upload_to_s3(path, prefix, progress_bar)


def sync_to_s3(local_dir: Path, prefix: str = None, progress_bar: bool = False):
    s3 = boto3.resource("s3")
    bucket = os.getenv("AWS_BUCKET_NAME")

    for i in s3.Bucket(bucket).objects.filter(Prefix=prefix):
        print(i)
        i.delete()

    paths = local_dir.glob("*")
    batch_upload_to_s3(paths, prefix, progress_bar)
