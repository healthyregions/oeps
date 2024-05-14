import os
import json
from datetime import datetime
from glob import glob
from pathlib import Path

import click
from flask import current_app
from flask.cli import with_appcontext, AppGroup

from oeps.bigquery import BigQuery, get_client
from oeps.frictionless import DataResource, create_package
from oeps.overture import get_filter_shape, get_data
from oeps.census.client import CensusClient
from oeps.utils import upload_to_s3

@click.command()
@with_appcontext
@click.argument('operation', type=click.Choice(['full-export']))
@click.option('--destination', "-d", help="Output path for export. Must end with .csv for CSV or .shp for shapefile.")
@click.option('--source', "-s", help="Data Resource JSON file to export, or directory with multiple files.")
@click.option("--zip", 'zip_', is_flag=True, default=False, help="Zip the output directory.")
def create_data_package(operation, destination, source, zip_):

    if not source:
        source = current_app.config['RESOURCES_DIR']

    create_package(operation, destination, source, zip_)


overture_grp = AppGroup('overture')

@overture_grp.command()
@click.argument('categories', nargs=-1)
@click.option('--outfile', "-o", help="path to output file")
@click.option('--confidence', default=".8", help="level of confidence to use (greater than or equal to)")
@click.option('--filter-file', help="spatial file with geometry to filter against")
@click.option('--filter-unit', help="GEOID of unit to filter out")

@click.option("--no-cache", is_flag=True, default=False, help="Force re-retrieval of data.")
@click.option("--upload", is_flag=True, default=False, help="Force re-retrieval of data.")
@click.option("--category-list", is_flag=True, default=False, help="Force re-retrieval of data.")
@click.option("--separate-files", is_flag=True, default=False, help="Export a separate file for each category.")
def get_pois(categories, outfile, confidence, filter_file, filter_unit, no_cache, upload, category_list, separate_files):


    geom_filter = None
    if filter_file and filter_unit:
        geom_filter = get_filter_shape(filter_file, filter_unit)

    print(geom_filter)

    get_data(
        outpath=Path(outfile) if outfile else None,
        categories=categories,
        confidence=confidence,
        geom_filter=geom_filter,
        export_category_list=category_list,
    )


census_grp = AppGroup('census')

@census_grp.command()
@click.argument(
    'format',
    type=click.Choice(
        ["shp","geojson","pmtiles"]
    ),
    nargs=-1,
)
@click.option(
    "--geography", "-g",
    type=click.Choice(
        ["place", "bg", "tract", "zcta", "county", "state"]
    ),
    help="Specify a geography to prepare. If left empty, all geographies will be processed."
)
@click.option(
    '--year', "-y",
    type=click.Choice(["2018", "2010"]),
    help="Specify a year. If left empty, both 2010 and 2018 will be processed."
)
@click.option(
    '--tippecanoe-path',
    help="Full path to tippecanoe binary, required for PMTiles generation."
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Force re-retrieval of files from FTP."
)
@click.option(
    "--upload",
    is_flag=True,
    default=False,
    help="Upload the processed files to S3."
)
def get_geodata(format, geography, year, tippecanoe_path, no_cache, upload):

    client = CensusClient()

    to_upload = []

    for k, v in client.lookups['census-sources'].items():

        geography, yr = k.split("-")

        if year and not yr == year:
            continue
        if geography and not geography == geography:
            continue

        print(f"PROCESSING: {k}")

        download_dir = Path(current_app.config['CACHE_DIR'], geography, 'raw', str(yr))
        download_dir.mkdir(exist_ok=True, parents=True)

        ftp_paths = client.collect_ftp_paths(v['ftp_root'], geography=geography)
        paths = client.download_from_census_ftp(ftp_paths, outdir=download_dir, no_cache=no_cache)

        paths = client.download_all_files(geography, yr, current_app.config['CACHE_DIR'], no_cache=no_cache)

        unzipped = client.unzip_files(paths)

        print("creating dataframe...")
        df = client.create_dataframe_from_files(unzipped)

        print("add HEROP_ID...")
        df = client.add_herop_id_to_dataframe(df, geography, yr, v['id_field'])

        print("add BBOX...")
        df = client.add_bbox_to_dataframe(df)

        print("add DISPLAY_NAME...")
        df = client.add_name_to_dataframe(df, geography, yr, v['name_field'])

        if "shp" in format:
            print("generating shapefile...")
            shp_paths = client.export_to_shapefile(df, geography, yr)
            to_upload += shp_paths

        if "geojson" in format:
            print("generating geojson...")
            geojson_path = client.export_to_geojson(df, geography, yr, overwrite=True)
            to_upload.append(geojson_path)

        if "pmtiles" in format:
            print("generating pmtiles...")
            if not tippecanoe_path:
                print("pmtiles output must be accompanied by --tippecanoe-path")
                exit()

            geojson_path = client.export_to_geojson(df, geography, yr, overwrite=True)
            pmtiles_path = client.export_to_pmtiles(geojson_path, geography, yr, tippecanoe_path)

            to_upload.append(pmtiles_path)

    if upload:
        print(f"uploading {len(to_upload)} files to S3...")
        upload_to_s3(to_upload)

    print("done.")


@click.command()
@with_appcontext
@click.argument('operation', type=click.Choice([
                            "check-credentials",
                            "load",
                            "export",
                            "generate-reference-md"
                        ]))
@click.option('--destination', "-d", help="Output path for export. Must end with .csv for CSV or .shp for shapefile.")
@click.option('--source', "-s", help="Data Resource JSON file to export, or directory with multiple files.")
@click.option('--sql-file', help="Path to file with SQL statement to run.")
@click.option("--overwrite", is_flag=True, default=False, help="Overwrite BQ table if it already exists.")
@click.option("--table-only", is_flag=True, default=False, help="Only create the new table, don't load data into it.")
@click.option("--dry-run", is_flag=True, default=False, help="Mock operation and perform no create/delete actions.")
def bq(operation, destination, source, sql_file, overwrite, table_only, dry_run):

    if operation == "check-credentials":
        client = get_client()
        print('ok')
        exit()

    bq = BigQuery()
    if operation == "load":

        if os.path.isdir(source):
            paths = glob(os.path.join(source, "*.json"))
        elif os.path.isfile(source):
            paths = [source]
        else:
            print('invalid path input')
            exit()

        all_errors = []
        
        for path in paths:
            
            dr = DataResource(path)

            if table_only:
                table = bq.create_table(dr.schema, overwrite=overwrite)
                print(table)
                exit()

            else:
                start = datetime.now()
                print(f"\nVALIDATE INPUT SOURCE: {dr.schema['path']}")
                rows, errors = dr.load_rows_from_file()
                all_errors += errors
                print(f"WARNINGS ENCOUNTERED: {len(errors)}")
                for e in errors:
                    print("  " + e)

                if not dry_run:
                    print(f"\nBEGIN LOAD: {path}")
                    table = bq.create_table(dr.schema, overwrite=overwrite)
                    print(f"TABLE CREATED: {table}")
                    load_job = bq.load_table(rows, dr.schema['bq_dataset_name'], dr.schema['bq_table_name'])
                    print(f"TIME ELAPSED: {datetime.now()-start}")

    if operation == "export":
        if sql_file:
            bq.run_query_from_file(sql_file)

        if destination:
            bq.export_results(destination)

        else:
            bq.print_results()

    if operation == "generate-reference-md":

        project_id = os.getenv("BQ_PROJECT_ID")

        datasets = {}

        files = glob(os.path.join(current_app.config['RESOURCES_DIR'], "*.json"))

        for f in files:
            with open(f, "r") as openf:
                d = json.load(openf)

            ds_name = d['bq_dataset_name']
            t_name = d['bq_table_name']

            if ds_name not in datasets:
                datasets[ds_name] = {}

            if t_name not in datasets[ds_name]:
                datasets[ds_name][t_name] = []

            for f in d['fields']:
                datasets[ds_name][t_name].append({
                    'name': f.get('name'),
                    'data_type': f.get('bq_data_type'),
                    'description': f.get('description'),
                    'source': f.get('source')
                })

        out_path = Path(Path(__file__).resolve()).parent.parent / "BQ-Reference.md"
        with open(out_path, 'w') as openf:

            ds_ct = len(datasets)
            openf.write(f"""# Project Id: {project_id}

    {ds_ct} dataset{'s' if ds_ct != 1 else ''} in this project: {', '.join(datasets.keys())}

    """)
            for ds in datasets:
                t_ct = len(datasets[ds])
                openf.write(f"""## {ds}

    {t_ct} table{'s' if t_ct != 1 else ''} in this dataset.

    """)

                for t in datasets[ds]:

                    c_ct = len(datasets[ds][t])
                    openf.write(f"""### {t}

    ID: `{project_id}.{ds}.{t}`

    {c_ct} column{'s' if c_ct != 1 else ''} in this table.

    Name|Data Type|Description|Source
    -|-|-|-
    """)

                    for c in datasets[ds][t]:
                        openf.write(f"{c['name']}|{c['data_type']}|{c['description']}|{c['source']}\n")

                    openf.write("\n")


@click.command()
@with_appcontext
@click.argument('operation', type=click.Choice(['list', 'generate-from-oeps-data-dicts']))
@click.option('--destination', "-d", help="Output path for export. Must end with .csv for CSV or .shp for shapefile.")
@click.option('--source', "-s", help="Data Resource JSON file to export, or directory with multiple files.")
@click.option("--zip", 'zip_', is_flag=True, default=False, help="Zip the output directory.")
def schema(operation, destination, source, zip_):

    if operation == "list":
        for i in glob(os.path.join(current_app.config['RESOURCES_DIR'], '*.json')):
            print(os.path.basename(i))
                       
    elif operation == "generate-from-oeps-data-dicts":

        paths = [
            "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/S_Dict.xlsx",
            "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/C_Dict.xlsx",
            "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/T_Dict.xlsx",
            "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/Z_Dict.xlsx",
        ]

        if destination:
            out_dir = destination
            if not os.path.isdir(out_dir):
                os.mkdir(out_dir)
        else:
            out_dir = current_app.config['RESOURCES_DIR']

        for path in paths:
            print(path)
            files = DataResource().create_from_oeps_xlsx_data_dict(path, out_dir)
            print("output resources:")
            for f in files:
                print(f)