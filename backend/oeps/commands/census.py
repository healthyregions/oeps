import os
from typing import List
from pathlib import Path

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
CACHE_DIR_rel = os.path.relpath(CACHE_DIR, start=Path(__file__).parent.parent.parent)

census_grp = AppGroup('census',
    help="A group of commands for obtaining and managing geospatial data from the US Census Bureau."
)

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
    help="Specify a year."
)
@click.option('--tippecanoe-path',
    help="Full path to tippecanoe binary, required for PMTiles generation.",
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
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
    help='Output directory for export. Treated as a directory, and not a file path.',
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
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
def get_geodata(
        format: List[str],
        year: str,
        destination: Path,
        geography: List[str]=['state', 'county', 'tract', 'bg', 'tract', 'place', 'zcta'],
        tippecanoe_path: str=None,
        upload: bool=False,
        no_cache: bool=False,
        prefix: str=None,
        verbose: bool=False,
    ):
    """This command retrieves geodata from the US Census Bureau's FTP server, merges the files into single,
nation-wide coverages, and then exports the merged files into various formats. Optionally upload these
files directly to S3."""

    client = CensusClient(verbose=verbose)

    os.makedirs(destination, exist_ok=True)

    for geog in geography:

        to_upload = []
        print(f"\nPROCESSING: {geog}, {year}")

        # skip if there isn't a config entry for this geography/year combo
        if year not in client.lookups['census-sources'] or \
            geog not in client.lookups['census-sources'][year]["configs"]:
            print("no source configuration for this combo, skipping")
            continue

        print("downloading files...")
        paths = client.download_all_files(geog, year, destination, no_cache=no_cache)

        print("unzipping files...")
        unzipped = client.unzip_files(paths)

        print("creating dataframe...")
        df = client.create_dataframe_from_files(unzipped)

        print("add HEROP_ID...")
        df = client.add_herop_id_to_dataframe(df, geog, year)

        print("add BBOX...")
        df = client.add_bbox_to_dataframe(df)

        print("add DISPLAY_NAME...")
        name_field = client.lookups['census-sources'][str(year)]['configs'][geog]['name_field']
        df = client.add_name_to_dataframe(df, geog, year, name_field)

        if "shp" in format:
            print("generating shapefile...")
            shp_paths = client.export_to_shapefile(df, geog, year, destination)
            to_upload += shp_paths

        geojson_path = None
        if "geojson" in format:
            print("generating geojson...")
            geojson_path = client.export_to_geojson(df, geog, year, destination, overwrite=True)
            to_upload.append(geojson_path)

        if "pmtiles" in format:
            print("generating pmtiles...")
            if not tippecanoe_path:
                print("pmtiles output must be accompanied by --tippecanoe-path")
                exit()

            # need geojson for this, but use existing if it was created already
            if not geojson_path:
                geojson_path = client.export_to_geojson(df, geog, year, destination, overwrite=True)
            pmtiles_path = client.export_to_pmtiles(geojson_path, geog, year, destination, tippecanoe_path)

            to_upload.append(pmtiles_path)

        if upload:
            print(f"uploading {len(to_upload)} files to S3...")
            upload_to_s3(to_upload, prefix=prefix, progress_bar=verbose)

    print("\ndone.")
