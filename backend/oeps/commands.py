import os
import json
from datetime import datetime
from glob import glob
from pathlib import Path
from argparse import Namespace

import click
from flask import current_app
from flask.cli import AppGroup

from oeps.clients.bigquery import BigQuery, get_client
from oeps.clients.jcoin import DataResource, DataPackage
from oeps.clients.overture import get_filter_shape, get_data
from oeps.clients.census import CensusClient
from oeps.utils import upload_to_s3, handle_overwrite

jcoin_grp = AppGroup('jcoin')

@jcoin_grp.command()
@click.option('--destination', "-d", help="Output path for export. Must end with .csv for CSV or .shp for shapefile.")
@click.option('--source', "-s", help="Data Resource JSON file to export, or directory with multiple files.")
@click.option("--zip", 'zip_', is_flag=True, default=False, help="Zip the output directory.")
@click.option("--upload", is_flag=True, default=False, help="Upload the processed files to S3.")
@click.option("--no-cache", is_flag=True, default=False, help="Force re-download of any remote files.")
@click.option("--skip-foreign-keys", is_flag=True, default=False, help="Don't define foreign keys in the output data package.")
@click.option("--overwrite", is_flag=True, default=False, help="Overwrite data packages with the same name.")
def create_data_package(**kwargs):

    args = Namespace(**kwargs)

    if not args.destination:
        file_name = f"oeps-data-package-v2_{datetime.now().date().isoformat()}"
        file_name = file_name + "_no_foreign_keys" if args.skip_foreign_keys else file_name
        args.destination = Path(current_app.config['CACHE_DIR'], "data-packages", file_name)

    if not args.overwrite:
        handle_overwrite(args.destination)
            
    if not args.source:
        args.source = current_app.config['RESOURCES_DIR']

    dp = DataPackage()
    dp.create(args.destination, args.source, args.zip_, args.upload, no_cache=args.no_cache, skip_foreign_keys=args.skip_foreign_keys)

@jcoin_grp.command()
def list_resources():

    for i in glob(os.path.join(current_app.config['RESOURCES_DIR'], '*.json')):
        print(os.path.basename(i))
                       

@jcoin_grp.command()
@click.option('--destination', "-d", help="Output path for export. Must end with .csv for CSV or .shp for shapefile.")
def generate_resources_from_oeps_dicts(destination):

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
        print(f"\nINPUT: {path}")
        files = DataResource().create_from_oeps_xlsx_data_dict(path, out_dir)
        print("OUTPUT:")
        for f in files:
            print(f"  {f}")


overture_grp = AppGroup('overture')

@overture_grp.command()
@click.argument('categories', nargs=-1)
@click.option('--outfile', "-o", help="path to output file")
@click.option('--confidence', default=".8", help="level of confidence to use (greater than or equal to)")
@click.option('--filter-file', help="spatial file with geometry to filter against")
@click.option('--filter-unit', help="GEOID of unit to filter out")
@click.option("--category-list", is_flag=True, default=False, help="Export a list of all categeories.")
@click.option("--separate-files", is_flag=True, default=False, help="Export a separate file for each category.")
def get_pois(**kwargs):

    args = Namespace(**kwargs)

    # --filter-file "https://herop-geodata.s3.us-east-2.amazonaws.com/place-2018.shp" -c hospital --filter-unit 3651000

    geom_filter = None
    if args.filter_file and args.filter_unit:
        geom_filter = get_filter_shape(args.filter_file, args.filter_unit)

    print(geom_filter)

    get_data(
        outpath=Path(args.outfile) if args.outfile else None,
        categories=args.categories,
        confidence=args.confidence,
        geom_filter=geom_filter,
        export_category_list=args.category_list,
    )


census_grp = AppGroup('census')

@census_grp.command()
@click.argument('format',
    type=click.Choice(["shp","geojson","pmtiles"]), nargs=-1
)
@click.option("--geography", "-g",
    type=click.Choice(["place", "bg", "tract", "zcta", "county", "state"]),
    help="Specify a geography to prepare. If left empty, all geographies will be processed."
)
@click.option('--year', "-y",
    type=click.Choice(["2018", "2010"]),
    help="Specify a year. If left empty, both 2010 and 2018 will be processed."
)
@click.option('--tippecanoe-path',
    help="Full path to tippecanoe binary, required for PMTiles generation."
)
@click.option(
    "--no-cache",
    is_flag=True, default=False,
    help="Force re-retrieval of files from FTP."
)
@click.option("--upload",
    is_flag=True, default=False,
    help="Upload the processed files to S3."
)
@click.option("--destination", 
              default=False, 
              help='Output directory for export. Treated as a directory, and not a file path.')
def get_geodata(format, geography, year, tippecanoe_path, no_cache, upload, destination):

    client = CensusClient(lookups_dir=current_app.config['LOOKUPS_DIR'])

    to_upload = []

    if not destination:
        destination = Path(current_app.config['CACHE_DIR'], 'geodata')
    os.makedirs(destination, exist_ok=True)

    for k, v in client.lookups['census-sources'].items():

        file_geography, yr = k.split("-")

        if year and not yr == year:
            continue
        if geography and not file_geography == geography:
            continue

        print(f"PROCESSING: {k}")

        # download_dir = Path(current_app.config['CACHE_DIR'], geography, 'raw', str(yr))
        # download_dir.mkdir(exist_ok=True, parents=True)

        # ftp_paths = client.collect_ftp_paths(v['ftp_root'], geography=geography)
        # paths = client.download_from_census_ftp(ftp_paths, outdir=download_dir, no_cache=no_cache)

        paths = client.download_all_files(geography, yr, current_app.config['CACHE_DIR'], no_cache=no_cache)

        unzipped = client.unzip_files(paths)

        print("creating dataframe...")
        df = client.create_dataframe_from_files(unzipped)

        print(df.columns)
        print("add HEROP_ID...")
        df = client.add_herop_id_to_dataframe(df, file_geography, yr, v['id_field'])

        print("add BBOX...")
        df = client.add_bbox_to_dataframe(df)

        print("add DISPLAY_NAME...")
        df = client.add_name_to_dataframe(df, file_geography, yr, v['name_field'])

        if "shp" in format:
            print("generating shapefile...")
            shp_paths = client.export_to_shapefile(df, file_geography, yr, destination)
            to_upload += shp_paths

        if "geojson" in format:
            print("generating geojson...")
            geojson_path = client.export_to_geojson(df, file_geography, yr, destination, overwrite=True)
            to_upload.append(geojson_path)

        if "pmtiles" in format:
            print("generating pmtiles...")
            if not tippecanoe_path:
                print("pmtiles output must be accompanied by --tippecanoe-path")
                exit()

            geojson_path = client.export_to_geojson(df, file_geography, yr, overwrite=True)
            pmtiles_path = client.export_to_pmtiles(geojson_path, file_geography, yr, destination, tippecanoe_path)

            to_upload.append(pmtiles_path)

    if upload:
        print(f"uploading {len(to_upload)} files to S3...")
        upload_to_s3(to_upload)

    print("done.")


## Group of commands for Google Big Query operations
bigquery_grp = AppGroup('bigquery')

@bigquery_grp.command()
def check_credentials():
    """ Check the credentials for Big Query client. """
    get_client()
    print('ok')
    exit()

@bigquery_grp.command()
@click.option('--source', "-s", help="Data Resource JSON file to export, or directory with multiple files.")
@click.option("--overwrite", is_flag=True, default=False, help="Overwrite BQ table if it already exists.")
@click.option("--table-only", is_flag=True, default=False, help="Only create the new table, don't load data into it.")
@click.option("--dry-run", is_flag=True, default=False, help="Mock operation and perform no create/delete actions.")
def load(**kwargs):
    """ Load a source to a big query table. """

    args = Namespace(**kwargs)
    client = BigQuery()

    if os.path.isdir(args.source):
        paths = glob(os.path.join(args.source, "*.json"))
    elif os.path.isfile(args.source):
        paths = [args.source]
    else:
        print('invalid path input')
        exit()

    all_errors = []
    
    for path in paths:
        
        dr = DataResource(path)

        if args.table_only:
            table = client.create_table(dr.schema, overwrite=args.overwrite)
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

            if not args.dry_run:
                print(f"\nBEGIN LOAD: {path}")
                table = client.create_table(dr.schema, overwrite=args.overwrite)
                print(f"TABLE CREATED: {table}")
                load_job = client.load_table(rows, dr.schema['bq_dataset_name'], dr.schema['bq_table_name'])
                print(f"TIME ELAPSED: {datetime.now()-start}")

@bigquery_grp.command()
@click.option('--destination', "-d", help="Output path for export. Must end with .csv for CSV or .shp for shapefile.")
@click.option('--sql-file', help="Path to file with SQL statement to run.")
def export(**kwargs):

    args = Namespace(**kwargs)

    client = BigQuery()

    if args.sql_file:
        client.run_query_from_file(args.sql_file)

    if args.destination:
        client.export_results(args.destination)

    else:
        client.print_results()


@bigquery_grp.command()
def generate_reference_md():

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
