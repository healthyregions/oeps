import json
import shutil
import subprocess
import pandas as pd
import geopandas as gpd
from pathlib import Path

from oeps.utils import download_file
from oeps.config import LOOKUPS_DIR, CACHE_DIR

GEODATA_CACHE_DIR = Path(CACHE_DIR, "geodata")


class CensusClient:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.lookups = self.load_lookups()

        self.year = ""
        self.geography = ""
        self.scale = ""

    @property
    def name_string(self):
        return f"{self.geography}-{self.year}-{self.scale}"

    def load_lookups(self):
        if self.verbose:
            print("loading lookups...")
        lookups = {}
        for f in LOOKUPS_DIR.glob("*.json"):
            with open(f, "r") as o:
                data = json.load(o)
                lookups[f.stem] = data

        return lookups

    def download_all_files(self, no_cache=False):
        download_dir = Path(
            GEODATA_CACHE_DIR, self.geography, "raw", self.year, self.scale
        )
        download_dir.mkdir(exist_ok=True, parents=True)

        download_urls = self.lookups["census-sources"][self.year][self.scale][
            self.geography
        ]["file_list"]
        if self.verbose:
            for i in download_urls:
                print(" -", i)
            print("downloading...")

        out_paths = []
        for url in download_urls:
            filename = url.split("/")[-1]
            outpath = Path(download_dir, filename)
            out_path = download_file(
                url,
                outpath,
                desc=f" - {filename}",
                progress_bar=self.verbose,
                no_cache=no_cache,
            )
            out_paths.append(out_path)

        return out_paths

    def unzip_files(self, paths):
        shp_paths = []
        for p in paths:
            name = p.name
            shp_file = Path(p.parent, name.replace("zip", "shp"))
            shutil.unpack_archive(p, p.parent)
            shp_paths.append(shp_file)

        return shp_paths

    def create_dataframe_from_files(self, paths):
        df_list = []
        for p in paths:
            df = gpd.read_file(p)
            df_list.append(df)

        if len(df_list) > 1:
            out_df = gpd.GeoDataFrame(
                pd.concat(df_list, ignore_index=True), crs=df_list[0].crs
            )
        else:
            out_df = df_list[0]

        return out_df

    def add_herop_id_to_dataframe(self, df: pd.DataFrame):
        lvl = self.lookups["census-summary-levels"][self.geography]
        suffixes = self.lookups["census-sources"][self.year][self.scale][
            self.geography
        ]["herop_id_suffixes"]

        df["HEROP_ID"] = df.apply(
            lambda row: f"{lvl}US{''.join([row[i] for i in suffixes])}", axis=1
        )

        return df

    def add_bbox_to_dataframe(self, df: pd.DataFrame):
        df = pd.concat([df, df.bounds], axis=1)

        def concat_bounds(row):
            minx = round(row["minx"], 3)
            miny = round(row["miny"], 3)
            maxx = round(row["maxx"], 3)
            maxy = round(row["maxy"], 3)
            return f"{minx},{miny},{maxx},{maxy}"

        df["BBOX"] = df.apply(concat_bounds, axis=1)

        return df

    def add_label_to_dataframe(self, df: pd.DataFrame):
        name_field = self.lookups["census-sources"][self.year][self.scale][
            self.geography
        ]["name_field"]

        def generate_label(row):
            lsad = row.get("LSAD")
            name = row.get(name_field)
            if lsad:
                position = None
                if lsad in self.lookups["census-lsad"]:
                    lsad_value = self.lookups["census-lsad"][lsad]["value"]
                    position = self.lookups["census-lsad"][lsad]["position"]
                else:
                    for k, v in self.lookups["census-lsad"].items():
                        if lsad == v["value"]:
                            lsad_value = lsad
                            position = v["position"]

                if position:
                    if position == "prefix":
                        name = f"{lsad_value} {name}"
                    else:
                        name = f"{name} {lsad_value}"

            return name

        df["LABEL"] = df.apply(generate_label, axis=1)

        return df

    def export_to_shapefile(self, df: pd.DataFrame, output_dir=None):
        if not output_dir:
            output_dir = Path(GEODATA_CACHE_DIR, self.geography, "processed")
        output_dir.mkdir(exist_ok=True, parents=True)

        processed_dir = Path(output_dir, f"{self.name_string}-shp")
        processed_dir.mkdir(parents=True, exist_ok=True)
        outfile_shp = Path(processed_dir, f"{self.name_string}.shp")
        df.to_file(outfile_shp)

        shutil.make_archive(processed_dir, "zip", processed_dir)

        shp_files = list(processed_dir.glob("*"))
        zip_file = Path(f"{processed_dir}.zip")

        return {
            "files": shp_files,
            "zipped": zip_file,
        }

    def export_to_geojson(self, df: pd.DataFrame, output_dir=None, overwrite=False):
        if not output_dir:
            output_dir = Path(GEODATA_CACHE_DIR, self.geography, "processed")
        output_dir.mkdir(exist_ok=True, parents=True)

        df = df.to_crs("EPSG:4326")
        outfile = Path(output_dir, f"{self.name_string}.geojson")

        if not outfile.is_file() or overwrite:
            df.to_file(outfile, driver="GeoJSON")

        return outfile

    def export_to_pmtiles(self, geojson_path, tippecanoe_path, output_dir=None):
        if not output_dir:
            output_dir = Path(GEODATA_CACHE_DIR, self.geography, "processed")
        output_dir.mkdir(exist_ok=True, parents=True)

        outfile_pmtiles = Path(output_dir, f"{self.name_string}.pmtiles")
        cmd = [
            tippecanoe_path,
            # "-zg",
            # tried a lot of zoom level directives, and seems like for block group
            # (which I believe is the densest)shp_paths 10 is needed to preserve shapes well enough.
            "-z10",
            "-x",
            "STATEFP",
            "-x",
            "COUNTYFP",
            "-x",
            "COUNTYNS",
            "-x",
            "TRACTCE",
            "-x",
            "BLKGRPCE",
            "-x",
            "STATENS",
            "-x",
            "STATE",
            "-x",
            "AFFGEOID",
            "-x",
            "CENSUSAREA",
            "-x",
            "GEOID",
            "-x",
            "GEO_ID",
            "-x",
            "STUSPS",
            "-x",
            "NAME",
            "-x",
            "LSAD",
            "-x",
            "ALAND",
            "-x",
            "AWATER",
            "-x",
            "minx",
            "-x",
            "miny",
            "-x",
            "maxx",
            "-x",
            "maxy",
            "--no-simplification-of-shared-nodes",
            "--coalesce-densest-as-needed",
            "--extend-zooms-if-still-dropping",
            "--projection",
            "EPSG:4326",
            "-o",
            str(outfile_pmtiles),
            "-l",
            f"{self.name_string}",
            "--force",
            str(geojson_path),
        ]
        subprocess.run(cmd)

        return outfile_pmtiles
