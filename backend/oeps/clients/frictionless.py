import os
import shutil
import pandas as pd
from pathlib import Path

from frictionless import validate

from oeps.utils import fetch_files, upload_to_s3, load_json, write_json


class DataPackage:
    def create_from_registry(
        self,
        registry,
        destination,
        zip_output: bool = False,
        upload: bool = False,
        no_cache: bool = False,
        skip_foreign_keys: bool = False,
        run_validation: bool = True,
    ):
        """Single command to generate an output data package. Should probably be
        refactored to more modular methods on this class."""

        dest = Path(destination)
        dest.mkdir(exist_ok=True, parents=True)
        s_path = Path(dest, "schemas")
        s_path.mkdir(exist_ok=True)
        d_path = Path(dest, "data")
        d_path.mkdir(exist_ok=True)

        data_package = {
            "profile": "data-package",
            "name": "oeps",
            "title": "Opioid Environment Policy Scan (OEPS) v2",
            "homepage": "https://oeps.healthyregions.org",
            "licenses": [
                {
                    "name": "ODC-PDDL-1.0",
                    "path": "http://opendatacommons.org/licenses/pddl/",
                    "title": "Open Data Commons Public Domain Dedication and License v1.0",
                }
            ],
            "resources": [],
        }

        resources = registry.get_all_geodata_resources(
            trim_props=True
        ) + registry.get_all_table_resources(trim_props=True)
        for res in resources:
            # remove foreignKeys from schema if needed
            if skip_foreign_keys:
                res["schema"].pop("foreignKeys", None)

            # write the schema out to its own file in the schemas dir
            schema = res.pop("schema")
            schema_filename = f"{res['name']}.json"

            write_json(schema, Path(s_path, schema_filename))

            # copy the data files and generate the list of local paths
            local_paths = fetch_files(res.pop("path"), d_path, no_cache=no_cache)

            res["path"] = [f"data/{i.name}" for i in local_paths]
            res["schema"] = f"schemas/{schema_filename}"

            data_package["resources"].append(res)

        package_json_path = Path(dest, "data-package.json")
        write_json(data_package, package_json_path)

        self.clean_datasets(package_json_path)

        if run_validation:
            print("\nvalidating output data package...")
            report = validate(package_json_path, skip_errors=["type-error"])

            print("VALIDATION REPORT SUMMARY:")
            for t in report.tasks:
                print(t.name, t.stats["errors"])

            print(f"Totals: {report.stats}")

            report.to_json(Path(dest, "error-report.json"))

        else:
            print("skipping data package validation...")

        if zip_output or upload:
            print("zipping output...")
            shutil.make_archive(f"{Path(dest.parent, dest.name)}", "zip", dest)

            zip_path = dest.with_suffix(".zip")

            if upload:
                print("uploading zip to S3...")
                upload_to_s3([zip_path], prefix="oeps", progress_bar=True)

            if not zip_output:
                print("deleting local copy of zipped output...")
                os.remove(zip_path)

        print("done.")

    def clean_datasets(self, package_json_path):
        pkg = load_json(package_json_path)

        # skip shapefiles
        non_shps = [i for i in pkg["resources"] if i["format"] != "shp"]
        for res in non_shps:
            print(f"cleaning data for {res['name']}")

            data_path = package_json_path.parent / res["path"][0]
            schema_path = package_json_path.parent / res["schema"]

            schema = load_json(schema_path)
            fields = {i["name"]: i for i in schema["fields"]}

            df = pd.read_csv(data_path)

            # create new dataframe with only fields as defined in the schema
            # (this takes care of ordering the fields properly as well)
            clean_df = df[fields.keys()]

            # set all dtypes to generic "object" so they can hold "NA"
            clean_df = clean_df.astype(object)

            # convert all NaN to NA, use this context and infer_objects to avoid a warning
            # see: https://stackoverflow.com/a/78066237/3873885
            with pd.option_context("future.no_silent_downcasting", True):
                clean_df = clean_df.fillna("NA").infer_objects(copy=False)

            # iterate all fields and if integer, cast to int to remove .0
            for k, v in fields.items():
                if v["type"] == "integer":
                    clean_df[k] = clean_df[k].apply(
                        lambda x: int(x) if x != "NA" else "NA"
                    )

            clean_df.to_csv(data_path, index=False)
