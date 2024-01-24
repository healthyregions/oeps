import ftplib
import shutil
import dotenv
import pandas as pd
import geopandas as gpd
from pathlib import Path

dotenv.load_dotenv()

SUMMARY_LEVEL_LOOKUP = {
    "state": "040",
    "county": "050",
    "tract": "140",
    "place": "160",
    "zcta": "860",
}

def ftp_connection():

    return ftplib.FTP('ftp2.census.gov', user="anonymous")

def get_ftp_paths(root: str, geography: str, scale="500k"):
    """ Connect to the census FTP site and get a list of all files download all cartographic boundary files
    that pertain to the given criteria. For now, only 2018 and 2010 are valid years.

    Valid geographies are "state", "county", "zcta", "tract", and "place".
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

def unzip_and_concat_df(paths):

    df_list = []
    for p in paths:
        name = p.name
        print(name)
        shutil.unpack_archive(p, p.parent)
        shp_file = Path(p.parent, name.replace("zip","shp"))
        df = gpd.read_file(shp_file)
        df_list.append(df)

    if len(df_list) > 1:
        out_df = gpd.GeoDataFrame(pd.concat(df_list, ignore_index=True), crs=df_list[0].crs)
    else:
        out_df = df_list[0]
        
    return out_df

def generate_herop_id(df, geography, pk_field):

    lvl = SUMMARY_LEVEL_LOOKUP[geography]

    df['HEROP_ID'] = df.apply(lambda row: f"{lvl}US{str(row[pk_field])}", axis = 1)

    return df
