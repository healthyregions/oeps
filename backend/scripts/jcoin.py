import os
import json
import shutil
import argparse
from pathlib import Path

from oeps_backend.utils import get_path_or_paths, download_path

RESOURCES_DIR = Path(__file__).parent.parent / 'resources'

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("operation",
                        choices=[
                            "full-export",
                        ],
                        help="operation to run")
    parser.add_argument("--destination", "-d",
                        help="Output path for export. Must end with .csv for CSV or .shp for shapefile.")
    parser.add_argument("--source", "-s",
                        help="Data Resource JSON file to export, or directory with multiple files.")
    parser.add_argument("--zip",
                        action="store_true",
                        help="Zip the output directory.")
    
    args = parser.parse_args()

    if args.operation == "full-export":

        dest = Path(args.destination)
        dest.mkdir(exist_ok=True)
        s_path = Path(dest, "schemas")
        s_path.mkdir(exist_ok=True)
        d_path = Path(dest, "data")
        d_path.mkdir(exist_ok=True)

        if not os.path.isdir(args.destination):
            os.mkdir(args.destination)

        data_package = {
            "profile": "data-package",
            "name": "oeps",
            "title": "Opioid Environment Policy Scan (OEPS)",
            "homepage": "https://oeps.healthyregions.org",
            "resources": []
        }

        if args.source:
            resources = get_path_or_paths(args.source, extension="json")
        else:
            resources = get_path_or_paths(RESOURCES_DIR, extension="json")
        resources.sort()

        for i in resources:

            i_path = Path(i)
            print(f"processing schema: {i_path.name}")
            with open(i, "r") as f:
                data = json.load(f)

            out_filename = f"{data['name']}{i_path.suffix}"
            out_relpath = f"schemas/{out_filename}"
            out_abspath = Path(s_path, out_filename)

            # copy the data files and generate the list of local paths
            local_paths = download_path(data.pop("path"), d_path)

            # create the resource item that will be placed in the data package json
            paths = [f"data/{i.name}" for i in local_paths]
            res_item = {
                "name": data['name'],
                "path": paths,
                "schema": out_relpath
            }
            data_package['resources'].append(res_item)

            # now create the schema that will be stored in the separate data resource file
            out_schema = {
                "primaryKey": data['schema'].get('primaryKey'),
                "fields": [],
            }
            
            # rebuild the field list here with only the necessary props
            props = ['name', 'title', 'type', 'example', 'description']
            for df in data['schema']["fields"]:
                f = {}
                for p in props:
                    if df.get(p):
                        f[p] = df.get(p)
                out_schema['fields'].append(f)

            # finally, for csv resources generate foreignKeys linking back to the proper geometry files
            if res_item['path'][0].endswith(".csv"):

                # figure out which shapefile...
                scale, year = res_item['name'].split("-")
                if scale == "T":
                    resname = f"tracts-{year}"
                elif scale == "Z":
                    resname = f"zctas-{year}"
                elif scale == "C":
                    resname = f"counties-{year}"
                elif scale == "S":
                    resname = f"states-{year}"
                else:
                    print(res_item)
                    raise Exception("unanticipated res_item['name']")

                out_schema['foreignKeys'] = [{
                    'fields': 'HEROP_ID',
                    'reference': {
                        'resource': resname,
                        'fields': 'HEROP_ID',
                    }
                }]

            with open(out_abspath, "w") as f:
                json.dump(out_schema, f, indent=4)

        package_json_path = Path(dest, "data-package.json")
        with open(package_json_path, "w") as f:
            json.dump(data_package, f, indent=4)

        if args.zip:
            print("zipping output...")
            shutil.make_archive(f"{Path(dest.parent, dest.name)}", 'zip', dest)

        print("  done.")
