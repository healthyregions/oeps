import os
import shutil
import pandas as pd
from pathlib import Path

from frictionless import validate

from oeps.clients.registry import Registry
from oeps.clients.s3 import upload_to_s3
from oeps.utils import fetch_files, load_json, write_json


class DataPackage:
    def __init__(self, path: Path = None):
        self.path = path

    def create_from_registry(
        self,
        registry: Registry,
        zip_output: bool = False,
        upload: bool = False,
        no_cache: bool = False,
        skip_foreign_keys: bool = False,
        run_validation: bool = True,
        verbose: bool = False,
    ):
        """Single command to generate an output data package. Should probably be
        refactored to more modular methods on this class."""

        self.path.mkdir(exist_ok=True, parents=True)
        s_path = Path(self.path, "schemas")
        s_path.mkdir(exist_ok=True)
        d_path = Path(self.path, "data")
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

        for res in registry.get_all_sources():
            ## remove unneeded top-level attributes (outside of Data Package spec)
            res.pop("bq_table_name", None)
            res.pop("bq_dataset_name", None)
            res.pop("geodata_source", None)
            res.pop("explorer_config", None)

            # remove foreignKeys from schema if needed
            if skip_foreign_keys:
                res["schema"].pop("foreignKeys", None)

            ## remove unneeded attributes from each field (outside of Data Package spec)
            for field in res["schema"]["fields"]:
                field.pop("table_sources", None)
                field.pop("years", None)
                field.pop("analysis", None)
                field.pop("longitudinal", None)

                ## convert our "constraints" field to generic "data_note"
                ## because our "constraints" doesn't match Data Package specs
                constraint = field.pop("constraints", "")
                if not constraint == "":
                    field["data_note"] = constraint

            # write the schema out to its own file in the schemas dir
            schema = res.pop("schema")
            schema_filename = f"{res['name']}.json"

            write_json(schema, Path(s_path, schema_filename))

            # copy the data files and generate the list of local paths
            local_paths = fetch_files(res.pop("path"), d_path, no_cache=no_cache)

            res["path"] = [f"data/{i.name}" for i in local_paths]
            res["schema"] = f"schemas/{schema_filename}"

            data_package["resources"].append(res)

        package_json_path = Path(self.path, "data-package.json")
        write_json(data_package, package_json_path)

        non_shps = [i for i in data_package["resources"] if i["format"] != "shp"]
        for res in non_shps:
            self.clean_data_resource(res)

        if run_validation:
            print("\nvalidating output data package...")
            report = validate(package_json_path, skip_errors=["type-error"])

            print("VALIDATION REPORT SUMMARY:")
            for t in report.tasks:
                print(t.name, t.stats["errors"])
                if verbose:
                    if len(t.errors) > 0:
                        for e in t.errors:
                            print(e)

            print(f"Totals: {report.stats}")

            report.to_json(Path(self.path, "error-report.json"))

        else:
            print("skipping data package validation...")

        if zip_output or upload:
            print("zipping output...")
            shutil.make_archive(
                f"{Path(self.path.parent, self.path.name)}", "zip", self.path
            )

            zip_path = self.path.with_suffix(".zip")

            if upload:
                print("uploading zip to S3...")
                upload_to_s3(zip_path, prefix="oeps", progress_bar=True)

            if not zip_output:
                print("deleting local copy of zipped output...")
                os.remove(zip_path)

        print("done.")

    def clean_data_resource(self, res):
        print(f"cleaning data for {res['name']}")

        data_path = self.path / res["path"][0]
        schema_path = self.path / res["schema"]

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
                clean_df[k] = clean_df[k].apply(lambda x: int(x) if x != "NA" else "NA")

        clean_df.to_csv(data_path, index=False)
