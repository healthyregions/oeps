import argparse
import dotenv
import json
import ftplib
import shutil
import subprocess
import pandas as pd
import geopandas as gpd
from pathlib import Path

from oeps_backend.utils import upload_to_s3

dotenv.load_dotenv()

CACHE_DIR = Path(__file__).parent.parent / '.cache'
DATA_DIR = Path(__file__).parent.parent / 'data'
RESOURCES_DIR = Path(__file__).parent.parent / 'resources'

def load_json(path):
    with open(path, "r") as o:
        return json.load(o)

SUMMARY_LEVEL_LOOKUP = load_json(Path(__file__).parent.parent / 'lookups' / 'summary-level-lookup.json')
LSAD_LOOKUP = load_json(Path(__file__).parent.parent / 'lookups' / 'lsad-lookup.json')
CENSUS_SOURCES = load_json(Path(__file__).parent.parent / 'lookups' / 'census-sources.json')

def ftp_connection():

    return ftplib.FTP('ftp2.census.gov', user="anonymous")

def collect_ftp_paths(root: str, geography: str, scale="500k"):
    """ Connect to the census FTP site and get a list of all files download all cartographic boundary files
    that pertain to the given criteria.

    Valid geographies are "state", "county", "zcta", "tract", "bg", and "place".
    """

    server = ftp_connection()
    files = server.nlst(root)

    # filter file list with simple string matching
    files = [i for i in files if scale in i]

    # use the summary level code as some older years only include that code
    files = [i for i in files if geography in i or SUMMARY_LEVEL_LOOKUP[geography] in i]

    # special handling for county, exclude the within_ua files (present in 2018)
    if geography == "county":
        files = [i for i in files if "within" not in i]

    return files

def download_from_census_ftp(ftp_paths, outdir=".", no_cache=False):

    server = ftp_connection()

    outpaths = []
    for ftp_path in ftp_paths:
        print(ftp_path)
        filename = ftp_path.split("/")[-1]
        outpath = Path(outdir, filename)
        if not outpath.is_file() or no_cache is True:
            with open(outpath, 'wb' ) as file:
                server.retrbinary('RETR %s' % ftp_path, file.write)
        else:
            print("  using local file.")
        outpaths.append(outpath)

    return outpaths

def download_all_files(geography, year, no_cache=False):

    download_dir = Path(CACHE_DIR, geography, 'raw', str(year))
    download_dir.mkdir(exist_ok=True, parents=True)

    ftp_paths = collect_ftp_paths(v['ftp_root'], geography=geography)
    paths = download_from_census_ftp(ftp_paths, outdir=download_dir, no_cache=args.no_cache)

    return paths

def unzip_files(paths):

    shp_paths = []
    for p in paths:
        name = p.name
        shp_file = Path(p.parent, name.replace("zip","shp"))
        shutil.unpack_archive(p, p.parent)
        shp_paths.append(shp_file)
        
    return shp_paths

def create_dataframe_from_files(paths):

    df_list = []
    for p in paths:
        df = gpd.read_file(p)
        df_list.append(df)

    if len(df_list) > 1:
        out_df = gpd.GeoDataFrame(pd.concat(df_list, ignore_index=True), crs=df_list[0].crs)
    else:
        out_df = df_list[0]
        
    return out_df

def add_herop_id_to_dataframe(df, geography, year, pk_field):

    lvl = SUMMARY_LEVEL_LOOKUP[geography]

    if geography == "bg" and year == "2010":
        df['HEROP_ID'] = df.apply(lambda row: f"{lvl}US{str(row[pk_field][6:])}-{year}", axis = 1)
    else:
        df['HEROP_ID'] = df.apply(lambda row: f"{lvl}US{str(row[pk_field])}-{year}", axis = 1)

    return df

def add_bbox_to_dataframe(df: pd.DataFrame):

    df = pd.concat([df, df.bounds], axis=1)

    def concat_bounds(row):
        minx = round(row['minx'], 3)
        miny = round(row['miny'], 3)
        maxx = round(row['maxx'], 3)
        maxy = round(row['maxy'], 3)
        return f"{minx},{miny},{maxx},{maxy}"

    df['BBOX'] = df.apply(concat_bounds, axis = 1)

    return df

def add_name_to_dataframe(df: pd.DataFrame, geography: str, year: str, name_field: str):

    def generate_display_name(row):
        lsad = row.get('LSAD')
        name = row.get('NAME')
        if lsad:
            # print(lsad)
            position = None
            if lsad in LSAD_LOOKUP:
                lsad_value = LSAD_LOOKUP[lsad]['value']
                position = LSAD_LOOKUP[lsad]['position']
            else:
                for k, v in LSAD_LOOKUP.items():
                    if lsad == v['value']:
                        lsad_value = lsad
                        position = v['position']
            
            if position:
                if position == "prefix":
                    name = f"{lsad_value} {name}"
                else:
                    name = f"{name} {lsad_value}"
               
        return name

    df['DISPLAY_NAME'] = df.apply(generate_display_name, axis=1)

    return df

def export_to_shapefile(df: pd.DataFrame, geography, year):

    processed_dir = Path(CACHE_DIR, f"{geography}-{year}-shp")
    processed_dir.mkdir(parents=True, exist_ok=True)
    outfile_shp = Path(processed_dir, f"{geography}-{year}.shp")
    df.to_file(outfile_shp)

    shutil.make_archive(processed_dir, 'zip', processed_dir)

    shp_files = list(processed_dir.glob("*"))
    shp_files.append(Path(f"{processed_dir}.zip"))

    return shp_files

def export_to_geojson(df: pd.DataFrame, geography: str, year: str, overwrite=False):
        df = df.to_crs("EPSG:4326")
        outfile = Path(CACHE_DIR, f"{geography}-{year}.geojson")

        if not outfile.is_file() or overwrite:
            df.to_file(outfile, driver="GeoJSON")

        return outfile

def export_to_pmtiles(geojson_path, geography, year, tippecanoe_path):

    outfile_pmtiles = Path(CACHE_DIR, f"{geography}-{year}.pmtiles")
    cmd = [
        tippecanoe_path,
        # "-zg",
        # tried a lot of zoom level directives, and seems like for block group
        # (which I believe is the densest)shp_paths 10 is needed to preserve shapes well enough.
        "-z10",
        "-x", "STATEFP",
        "-x", "COUNTYFP",
        "-x", "COUNTYNS",
        "-x", "TRACTCE",
        "-x", "BLKGRPCE",
        "-x", "STATENS",
        "-x", "STATE",
        "-x", "AFFGEOID",
        "-x", "CENSUSAREA",
        "-x", "GEOID",
        "-x", "GEO_ID",
        "-x", "STUSPS",
        "-x", "NAME",
        "-x", "LSAD",
        "-x", "ALAND",
        "-x", "AWATER",
        "-x", "minx",
        "-x", "miny",
        "-x", "maxx",
        "-x", "maxy",
        "--no-simplification-of-shared-nodes",
        "--coalesce-densest-as-needed",
        "--extend-zooms-if-still-dropping",
        "--projection", "EPSG:4326",
        "-o", str(outfile_pmtiles),
        "-l", f"{geography}-{year}",
        "--force",
        str(geojson_path)
    ]
    subprocess.run(cmd)

    return outfile_pmtiles

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-g", "--geography",
                        choices=[
                            "place",
                            "bg",
                            "tract",
                            "zcta",
                            "county",
                            "state",
                        ],
                        help="Specify a geography to prepare. If left empty, all geographies will be processed.")
    parser.add_argument("-y", "--year",
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
    parser.add_argument("--shp",
                        action="store_true",
                        help="Output shapefile")
    parser.add_argument("--geojson",
                        action="store_true",
                        help="Output GeoJSON")
    parser.add_argument("--pmtiles",
                        action="store_true",
                        help="Output PMTiles")
    parser.add_argument("--tippecanoe-path",
                        help="Full path to tippecanoe binary, required for PMTiles generation.")
    parser.add_argument("-f", "--format",
                        nargs="*",
                        help="Export formats: shp, geojson, or pmtiles (multiple allowed).")
    
    args = parser.parse_args()

    to_upload = []

    for k, v in CENSUS_SOURCES.items():

        geography, year = k.split("-")

        if args.year and not year == args.year:
            continue
        if args.geography and not geography == args.geography:
            continue

        print(f"PROCESSING: {k}")

        download_dir = Path(CACHE_DIR, geography, 'raw', str(year))
        download_dir.mkdir(exist_ok=True, parents=True)

        ftp_paths = collect_ftp_paths(v['ftp_root'], geography=geography)
        paths = download_from_census_ftp(ftp_paths, outdir=download_dir, no_cache=args.no_cache)

        paths = download_all_files(geography, year, no_cache=args.no_cache)

        unzipped = unzip_files(paths)

        print("creating dataframe...")
        df = create_dataframe_from_files(unzipped)

        print("add HEROP_ID...")
        df = add_herop_id_to_dataframe(df, geography, year, v['id_field'])

        print("add BBOX...")
        df = add_bbox_to_dataframe(df)

        print("add DISPLAY_NAME...")
        df = add_name_to_dataframe(df, geography, year, v['name_field'])

        if "shp" in args.format:
            print("generating shapefile...")
            shp_paths = export_to_shapefile(df, geography, year)
            to_upload += shp_paths

        if "geojson" in args.format:
            print("generating geojson...")
            geojson_path = export_to_geojson(df, geography, year, overwrite=True)
            to_upload.append(geojson_path)

        if "pmtiles" in args.format:
            print("generating pmtiles...")
            if not args.tippecanoe_path:
                print("pmtiles output must be accompanied by --tippecanoe-path")
                exit()

            geojson_path = export_to_geojson(df, geography, year, overwrite=True)
            pmtiles_path = export_to_pmtiles(geojson_path, geography, year, args.tippecanoe_path)

            to_upload.append(pmtiles_path)

    if args.upload:
        print(f"uploading {len(to_upload)} files to S3...")
        upload_to_s3(to_upload)

    print("done.")

        
