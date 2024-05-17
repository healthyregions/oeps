import json
import ftplib
import shutil
import subprocess
import pandas as pd
import geopandas as gpd
from pathlib import Path


class CensusClient():

    def __init__(self):

        self.lookups = self.get_lookups()

    def get_lookups(self):
        lookups = {}
        lookups_dir = Path(__file__).parent / "lookups"
        for f in lookups_dir.glob("*.json"):
            with open(f, 'r') as o:
                data = json.load(o)
                lookups[f.stem] = data
        return lookups

    def ftp_connection(self):

        return ftplib.FTP('ftp2.census.gov', user="anonymous")

    def collect_ftp_paths(self, root: str, geography: str, scale="500k"):
        """ Connect to the census FTP site and get a list of all files download all cartographic boundary files
        that pertain to the given criteria.

        Valid geographies are "state", "county", "zcta", "tract", "bg", and "place".
        """

        print("getting connection")
        # server = self.ftp_connection()
        server = ftplib.FTP('ftp2.census.gov')
        server.connect()
        print('connnected')
        files = server.nlst('/geo/tiger/GENZ2010')
        print(files)

        # filter file list with simple string matching
        files = [i for i in files if scale in i]
        print(1)

        # use the summary level code as some older years only include that code
        files = [i for i in files if geography in i or self.lookups['summary-levels'][geography] in i]
        print(2)

        # special handling for county, exclude the within_ua files (present in 2018)
        if geography == "county":
            files = [i for i in files if "within" not in i]

        print(3)
        return files

    def download_from_census_ftp(self, ftp_paths, outdir=".", no_cache=False):

        server = self.ftp_connection()

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

    def download_all_files(self, geography, year, destination, no_cache=False):

        download_dir = Path(destination, geography, 'raw', str(year))
        download_dir.mkdir(exist_ok=True, parents=True)

        ftp_root = self.lookups['census-sources'][f'{geography}-{year}']['ftp_root']
        ftp_paths = self.collect_ftp_paths(ftp_root, geography=geography)
        paths = self.download_from_census_ftp(ftp_paths, outdir=download_dir, no_cache=no_cache)

        return paths

    def unzip_files(self, paths):

        shp_paths = []
        for p in paths:
            name = p.name
            shp_file = Path(p.parent, name.replace("zip","shp"))
            shutil.unpack_archive(p, p.parent)
            shp_paths.append(shp_file)
            
        return shp_paths

    def create_dataframe_from_files(self, paths):

        df_list = []
        for p in paths:
            df = gpd.read_file(p)
            df_list.append(df)

        if len(df_list) > 1:
            out_df = gpd.GeoDataFrame(pd.concat(df_list, ignore_index=True), crs=df_list[0].crs)
        else:
            out_df = df_list[0]
            
        return out_df

    def add_herop_id_to_dataframe(self, df, geography, year, pk_field):

        lvl = self.lookups['summary-levels'][geography]

        if geography == "bg" and year == "2010":
            df['HEROP_ID'] = df.apply(lambda row: f"{lvl}US{str(row[pk_field][6:])}-{year}", axis = 1)
        else:
            df['HEROP_ID'] = df.apply(lambda row: f"{lvl}US{str(row[pk_field])}-{year}", axis = 1)

        return df

    def add_bbox_to_dataframe(self, df: pd.DataFrame):

        df = pd.concat([df, df.bounds], axis=1)

        def concat_bounds(row):
            minx = round(row['minx'], 3)
            miny = round(row['miny'], 3)
            maxx = round(row['maxx'], 3)
            maxy = round(row['maxy'], 3)
            return f"{minx},{miny},{maxx},{maxy}"

        df['BBOX'] = df.apply(concat_bounds, axis = 1)

        return df

    def add_name_to_dataframe(self, df: pd.DataFrame, geography: str, year: str, name_field: str):

        def generate_display_name(row):
            lsad = row.get('LSAD')
            name = row.get('NAME')
            if lsad:
                # print(lsad)
                position = None
                if lsad in self.lookups['lsad']:
                    lsad_value = self.lookups['lsad'][lsad]['value']
                    position = self.lookups['lsad'][lsad]['position']
                else:
                    for k, v in self.lookups['lsad'].items():
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

    def export_to_shapefile(self, df: pd.DataFrame, geography, year, destination):

        processed_dir = Path(destination, f"{geography}-{year}-shp")
        processed_dir.mkdir(parents=True, exist_ok=True)
        outfile_shp = Path(processed_dir, f"{geography}-{year}.shp")
        df.to_file(outfile_shp)

        shutil.make_archive(processed_dir, 'zip', processed_dir)

        shp_files = list(processed_dir.glob("*"))
        shp_files.append(Path(f"{processed_dir}.zip"))

        return shp_files

    def export_to_geojson(self, df: pd.DataFrame, geography: str, year: str, destination, overwrite=False):
        df = df.to_crs("EPSG:4326")
        outfile = Path(destination, f"{geography}-{year}.geojson")

        if not outfile.is_file() or overwrite:
            df.to_file(outfile, driver="GeoJSON")

        return outfile

    def export_to_pmtiles(self, geojson_path, geography, year, destination, tippecanoe_path):

        outfile_pmtiles = Path(destination, f"{geography}-{year}.pmtiles")
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
