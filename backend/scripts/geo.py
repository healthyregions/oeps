import argparse
import shutil
from pathlib import Path

from oeps_backend.geographies import download_from_census_ftp, get_ftp_paths, unzip_and_concat_df, generate_herop_id
from oeps_backend.utils import upload_to_s3

CACHE_DIR = Path(__file__).parent.parent / '.cache'
DATA_DIR = Path(__file__).parent.parent / 'data'
RESOURCES_DIR = Path(__file__).parent.parent / 'resources'


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("operation",
                        choices=[
                            "process",
                        ],
                        help="Operation to run.")
    parser.add_argument("--geography",
                        choices=[
                            "place",
                            "tract",
                            "zcta",
                            "county",
                            "state",
                        ],
                        help="Specify a geography to prepare. If left empty, all geographies will be processed.")
    parser.add_argument("--year",
                        choices=[
                            "2018",
                            "2010",
                        ],
                        help="Specify a year. If left empty 2010 and 2018 will be processed.")
    parser.add_argument("--no-cache",
                        action="store_true",
                        default=False,
                        help="Force re-retrieval of files from FTP.")
    parser.add_argument("--upload",
                        action="store_true",
                        default=False,
                        help="Upload the processed files to S3.")
    parser.add_argument("--source",
                        help="Location of shapefile to add id to.")
    args = parser.parse_args()

    ftp_root_lookup = {
        "2010":"/geo/tiger/GENZ2010",
        "2018":"/geo/tiger/GENZ2018/shp",
    }

    # list of source data configs.
    # (geography name, year, field name to use in HEROP_ID)
    download_list = [
        ("place", "2010", "PLACE"),
        ("place", "2018", "PLACEFP"),
        ("tract", "2010", "TRACT"),
        ("tract", "2018", "GEOID"),
        ("zcta", "2018", "ZCTA5CE10"),
        ("county", "2010", "COUNTY"),
        ("county", "2018", "GEOID"),
        ("state", "2010", "STATE"),
        ("state", "2018", "GEOID"),
    ]

    if args.operation == "process":

        for item in download_list:

            geography, year, pk = item

            if args.year and not year == args.year:
                continue
            if args.geography and not geography == args.geography:
                continue

            download_dir = Path(CACHE_DIR, geography, 'raw', str(year))
            download_dir.mkdir(exist_ok=True, parents=True)

            ftp_paths = get_ftp_paths(ftp_root_lookup[year], geography=geography)
            paths = download_from_census_ftp(ftp_paths, outdir=download_dir, no_cache=args.no_cache)

            processed_dir = Path(CACHE_DIR, f"{geography}-{year}")
            processed_dir.mkdir(parents=True, exist_ok=True)

            outfile = Path(processed_dir, f"{geography}-{year}.shp")

            # acquire the dataframe from downloaded zips. If multiple zips where downloaded, they are
            # unioned into a single dataframe
            df = unzip_and_concat_df(paths)

            # add HEROP_ID field to the dataframe
            df = generate_herop_id(df, geography, pk)

            ## do other things to the dataframe?

            df.to_file(outfile)

            shutil.make_archive(processed_dir, 'zip', processed_dir)

            to_upload = list(processed_dir.glob("*"))
            to_upload.append(Path(f"{processed_dir}.zip"))

            if args.upload:
                upload_to_s3(to_upload)
