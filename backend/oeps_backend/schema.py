import os
import argparse
from glob import glob

from oeps_backend.src.data_resource import DataResource

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), 'resources')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("operation",
                        choices=[
                            "list",
                            "generate-from-oeps-data-dicts",
                        ],
                        help="operation to run")
    parser.add_argument("--destination", "-d",
                        help="Output path for export. Must end with .csv for CSV or .shp for shapefile.")
    parser.add_argument("--source", "-s",
                        help="Data Resource JSON file to load, or directory with multiple files.")
    args = parser.parse_args()

    if args.operation == "list":
        for i in glob(os.path.join(RESOURCES_DIR, '*.json')):\
            print(os.path.basename(i))
                       
    elif args.operation == "generate-from-oeps-data-dicts":

        if args.source:
            if os.path.isdir(args.source):
                paths = glob(os.path.join(args.source, "*.xlsx"))
            elif os.path.isfile(args.source):
                paths = [args.source]
            else:
                print("invalid dict file input")
                exit()

        else:
            print("using preset remote dicts")
            paths = [
                "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/S_Dict.xlsx",
                "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/C_Dict.xlsx",
                "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/T_Dict.xlsx",
                "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/Z_Dict.xlsx",
            ]

        if args.destination:
            out_dir = args.destination
            if not os.path.isdir(out_dir):
                os.mkdir(out_dir)
        else:
            out_dir = RESOURCES_DIR

        for path in paths:
            print(path)
            files = DataResource().create_from_oeps_xlsx_data_dict(path, out_dir)
            print("output resources:")
            for f in files:
                print(f)
