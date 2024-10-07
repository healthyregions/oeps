import os
from pathlib import Path
from argparse import Namespace

import click
from flask.cli import AppGroup
from oeps.clients.census import CensusClient
from oeps.config import (
    CACHE_DIR,
)
from oeps.utils import upload_to_s3

# Make relative paths for directory configs so they can properly be used as default values for 
# CLI arguments. Using absolute paths (e.g. those in the config) would result in absolute paths
# in the generated docs... this would be incorrect on every system besides the one that had 
# generated the docs.
CACHE_DIR_rel = os.path.relpath(CACHE_DIR, start=Path(__file__).parent.parent)

census_grp = AppGroup('census')

@census_grp.command()
@click.option('--format', '-f',
    type=click.Choice(["shp","geojson","pmtiles"]),
    default=["shp","geojson","pmtiles"],
    multiple=True,
    help="Choose what output formats will be created. Options are `shp` (shapefile), `geojson` "\
        "(GeoJSON), and/or `pmtiles` (PMTiles)."
)
@click.option("--geography", "-g",
    type=click.Choice(["state", "county", "tract", "bg", "place", "zcta"]),
    default=["state", "county", "tract", "bg", "place", "zcta"],
    multiple=True,
    help="Specify a geography to prepare. If left empty, all geographies will be processed."
)
@click.option('--year', "-y",
    type=click.Choice(["2018", "2010"]),
    help="Specify a year. If left empty, both 2010 and 2018 will be processed."
)
@click.option('--tippecanoe-path',
    help="Full path to tippecanoe binary, required for PMTiles generation."
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Force re-retrieval of files from FTP."
)
@click.option("--upload",
    is_flag=True,
    default=False,
    help="Upload the processed files to S3."
)
@click.option("--destination",
    default=Path(CACHE_DIR_rel, "geodata"),
    help='Output directory for export. Treated as a directory, and not a file path.'
)
@click.option("--prefix",
    default="oeps",
    help='If output is uploaded to S3, use this prefix for the objects.'
)
@click.option("--verbose",
    is_flag=True,
    default=False,
    help='Enable verbose print statements'
)
def get_geodata(**kwargs):
    """This command retrieves geodata from the US Census Bureau's FTP server, merges the files into single,
nation-wide coverages, and then exports the merged files into various formats. Optionally upload these
files directly to S3."""

    args = Namespace(**kwargs)

    client = CensusClient(verbose=args.verbose)

    os.makedirs(args.destination, exist_ok=True)

    geogs = args.geography
    if not geogs:
        geogs = ['state', 'county', 'tract', 'bg', 'tract', 'place', 'zcta']

    for geog in geogs:

        to_upload = []
        print(f"\nPROCESSING: {geog}, {args.year}")

        print("downloading files...")
        paths = client.download_all_files(geog, args.year, args.destination, no_cache=args.no_cache)

        print("unzipping files...")
        unzipped = client.unzip_files(paths)

        print("creating dataframe...")
        df = client.create_dataframe_from_files(unzipped)

        print("add HEROP_ID...")
        id_field = client.lookups['census-sources'][str(args.year)]['configs'][geog]['id_field']
        df = client.add_herop_id_to_dataframe(df, geog, args.year, id_field)

        print("add BBOX...")
        df = client.add_bbox_to_dataframe(df)

        print("add DISPLAY_NAME...")
        name_field = client.lookups['census-sources'][str(args.year)]['configs'][geog]['name_field']
        df = client.add_name_to_dataframe(df, geog, args.year, name_field)

        if "shp" in args.format:
            print("generating shapefile...")
            shp_paths = client.export_to_shapefile(df, geog, args.year, args.destination)
            to_upload += shp_paths

        geojson_path = None
        if "geojson" in args.format:
            print("generating geojson...")
            geojson_path = client.export_to_geojson(df, geog, args.year, args.destination, overwrite=True)
            to_upload.append(geojson_path)

        if "pmtiles" in args.format:
            print("generating pmtiles...")
            if not args.tippecanoe_path:
                print("pmtiles output must be accompanied by --tippecanoe-path")
                exit()

            # need geojson for this, but use existing if it was created already
            if not geojson_path:
                geojson_path = client.export_to_geojson(df, geog, args.year, args.destination, overwrite=True)
            pmtiles_path = client.export_to_pmtiles(geojson_path, geog, args.year, args.destination, args.tippecanoe_path)

            to_upload.append(pmtiles_path)

        if args.upload:
            print(f"uploading {len(to_upload)} files to S3...")
            for fpath in to_upload:
                upload_to_s3(fpath, prefix=args.prefix, progress_bar=args.verbose)

    print("\ndone.")
