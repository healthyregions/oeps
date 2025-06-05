import os
import sys
import threading
import boto3
from typing import List
from pathlib import Path

BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
REGION = os.getenv("AWS_REGION")


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

    key = f"{prefix}/{path.name}" if prefix else path.name
    cb = S3ProgressPercentage(str(path)) if progress_bar else None
    s3.Bucket(BUCKET_NAME).upload_file(str(path), key, Callback=cb)
    if progress_bar:
        print(f"\n  {get_base_url()}{key}")


def batch_upload_to_s3(
    paths: List[Path], prefix: str = None, progress_bar: bool = False
):
    for path in paths:
        upload_to_s3(path, prefix, progress_bar)

def clear_s3_bucket(bucket: boto3.s3.Bucket, prefix: str = None):
    ''' Empty all contents in an s3 bucket beginning with a given prefix '''
    for i in bucket.objects.filter(Prefix=prefix):
        print(f'Deleting {i}..')
        i.delete()

def sync_to_s3(local_dir: Path, prefix: str = None, progress_bar: bool = False, clear_bucket: bool = False):
    s3 = boto3.resource("s3")

    if clear_bucket: clear_s3_bucket(s3.Bucket(BUCKET_NAME), prefix)

    paths = local_dir.glob("*")
    batch_upload_to_s3(paths, prefix, progress_bar)


def get_base_url():
    return f"https://{BUCKET_NAME}.s3.{REGION}.amazonaws.com/"
