import os
import json
import subprocess
from datetime import datetime
from glob import glob
from pathlib import Path
from argparse import Namespace

import click
from flask import current_app
from flask.cli import AppGroup

from oeps.clients.explorer import Explorer
from oeps.clients.bigquery import BigQuery, get_client
from oeps.clients.frictionless import DataResource, DataPackage, create_data_dictionaries
from oeps.clients.overture import get_filter_shape, get_data
from oeps.clients.census import CensusClient
from oeps.config import (
    EXPLORER_CONFIG_DIR,
    RESOURCES_DIR,
    CACHE_DIR,
)
from oeps.utils import upload_to_s3, handle_overwrite

# Make relative paths for directory configs so they can properly be used as default values for 
# CLI arguments. Using absolute paths (e.g. those in the config) would result in absolute paths
# in the generated docs... this would be incorrect on every system besides the one that had 
# generated the docs.
EXPLORER_CONFIG_DIR_rel = os.path.relpath(EXPLORER_CONFIG_DIR, start=os.path.dirname(__file__))
RESOURCES_DIR_rel = os.path.relpath(RESOURCES_DIR, start=os.path.dirname(__file__))
CACHE_DIR_rel = os.path.relpath(CACHE_DIR, start=os.path.dirname(__file__))


explorer_grp = AppGroup('explorer',
    help="Commands for configuring the OEPS Explorer.")

@explorer_grp.command()
@click.option('--destination', "-d",
    help="Optional output path for config files. The default location will overwrite existing configs.",
    default=EXPLORER_CONFIG_DIR_rel,
)
def build_config(**kwargs):
    """Build configs for the frontend OEPS Explorer application, based on resource schemas stored
in the `./data/resources` directory."""

    args = Namespace(**kwargs)

    ex = Explorer()
    ex.build_config(schema_dir=RESOURCES_DIR_rel, output_dir=args.destination)


frictionless_grp = AppGroup('frictionless')

@frictionless_grp.command()
@click.option('--destination', "-d",
    help="Output location for export directory. The package will be placed within this directory and given "\
        "a name generated from the current date and time.",
    default=CACHE_DIR_rel,
)
@click.option('--source', "-s",
    default=RESOURCES_DIR_rel,
    help="Path to a data resource JSON file to export, or a directory containing multiple data resources."
)
@click.option("--zip", 'zip_',
    is_flag=True,
    default=False,
    help="Zip the output data package."
)
@click.option("--upload",
    is_flag=True,
    default=False,
    help="Upload the zipped data package to S3. Bucket is determined by `AWS_BUCKET_NAME` environment variable."
)
@click.option("--no-cache",
    is_flag=True,
    default=False,
    help="Force re-download of any remote files."
)
@click.option("--skip-foreign-keys",
    is_flag=True,
    default=False,
    help="Don't define foreign keys in the output data package. This is needed to avoid validation errors that "\
        "occur when Shapefiles are used in foreign keys.")
@click.option("--overwrite",
    is_flag=True,
    default=False,
    help="Overwrite existing data package with the same name."
)
def create_data_package(**kwargs):
    """Generates a Frictionless data package from the Data Resource definitions in this backend. This export
process was developed specifically to support integration of the OEPS data warehouse into the JCOIN commons.

The resulting package will be validated against the `frictionless` standard using that Python library. Use
`--no-foreign-keys` to allow validation to pass when shapefiles are involved in join fields.
"""

    args = Namespace(**kwargs)

    out_name = f"oeps-data-package-v2_{datetime.now().date().isoformat()}"
    out_name = out_name + "_no_foreign_keys" if args.skip_foreign_keys else out_name
    out_path = Path(args.destination, out_name)

    if not args.overwrite:
        handle_overwrite(out_path)

    dp = DataPackage()
    dp.create(out_path, args.source, args.zip_, args.upload, no_cache=args.no_cache, skip_foreign_keys=args.skip_foreign_keys)

@frictionless_grp.command()
def list_resources():
    """Print a list of all data resources in the data/resources directory."""
    for i in RESOURCES_DIR.glob('*.json'):
        print(i.name)
                       
@frictionless_grp.command()
@click.option('--source', "-s",
    help="Local path to directory with Excel data dictionaries in it. If not provided, the dictionaries stored "\
        "in the GeoDaCenter/opioid-policy-scan repo will be used."
)
@click.option('--destination', "-d",
    default=RESOURCES_DIR_rel,
    help="Output location for generated schema files.",
)
def generate_resources_from_oeps_dicts(**kwargs):
    """Creates data resource schema files from external data dictionaries.

TO DEPRECATE: Ultimately, this pattern will be deprecated in favor of the opposite: The Excel data dictionaries
will be generated directly from the data resource schema files."""
    args = Namespace(**kwargs)

    remote_files = [
        "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/S_Dict.xlsx",
        "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/C_Dict.xlsx",
        "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/T_Dict.xlsx",
        "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/dictionaries/Z_Dict.xlsx",
    ]
    paths = Path(args.source).glob("*_Dict.xlsx") if args.source else remote_files

    Path(args.destination).mkdir(exist_ok=True)

    for path in paths:
        print(f"\nINPUT: {path}")
        files = DataResource().create_from_oeps_xlsx_data_dict(path, args.destination)
        print("OUTPUT:")
        for f in files:
            print(f"  {f}")

@frictionless_grp.command()
@click.option('--source', "-s",
    default=RESOURCES_DIR_rel,
    help="Input directory that holds the data resource JSON schemas to process.",
)
@click.option('--destination', "-d",
    default=Path(CACHE_DIR_rel, "dicts"),
    help="Output directory for new dictionaries.",
)
def create_oeps_dicts(**kwargs):
    """Create the human readable, MS Excel data dictionaries from the data resource schemas."""
    args = Namespace(**kwargs)

    Path(args.destination).mkdir(exist_ok=True)

    create_data_dictionaries(args.source, args.destination)


overture_grp = AppGroup('overture')

@overture_grp.command()
@click.option(
    '--categories', "-c",
    multiple=True,
    help="The exact name of one or more categories to include in the query. If not provided, all points "\
        "will be included in the export.",
)
@click.option(
    '--outfile', "-o",
    help="Path to output file. If not provided, a small preview of the query result will be printed to "\
        "the console."
)
@click.option('--confidence',
    default=".8",
    help="level of confidence to use when querying Overture data (greater than or equal to)",
)
@click.option('--filter-file',
    help="Geospatial dataset with geometry to filter against. Can be a shapefile or geojson dataset, either "
    "a local path or a url to one stored in S3.",
)
@click.option('--filter-unit',
    help="GEOID of unit to find in the filter-file and use as a spatial filter in the query."
)
@click.option(
    "--export-category-list",
    is_flag=True,
    default=False,
    help="Export a list of all categories included in the query to a CSV file. Only really useful if "\
        "you don't include any categories in the filter."
)
@click.option("--separate-files",
    is_flag=True,
    default=False,
    help="Write separate file for each category in the results."
)
def get_pois(**kwargs):
    """This operation will query the Overture Places (a.k.a. Point of Interest) dataset and extract all points
matching the specified categories that fall within the provided spatial boundary.

Example:

```
flask overture get-pois --filter-file "https://herop-geodata.s3.us-east-2.amazonaws.com/place-2018.shp" -c hospital --filter-unit 3651000
```
"""
    args = Namespace(**kwargs)

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
@click.option('--format', '-f',
    type=click.Choice(["shp","geojson","pmtiles"]),
    default=["shp","geojson","pmtiles"],
    multiple=True,
    help="Choose what output formats will be created. Options are `shp` (shapefile), `geojson` "\
        "(GeoJSON), and/or `pmtiles` (PMTiles)."
)
@click.option("--geography", "-g",
    type=click.Choice(["state", "county", "tract", "bg", "place", "zcta"]),
    default=["state", "county", "tract", "bg", "place", "zcta"],
    multiple=True,
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
    is_flag=True,
    default=False,
    help="Force re-retrieval of files from FTP."
)
@click.option("--upload",
    is_flag=True,
    default=False,
    help="Upload the processed files to S3."
)
@click.option("--destination",
    default=Path(CACHE_DIR_rel, "geodata"),
    help='Output directory for export. Treated as a directory, and not a file path.'
)
@click.option("--verbose",
    is_flag=True,
    default=False,
    help='Enable verbose print statements'
)
def get_geodata(**kwargs):
    """This command retrieves geodata from the US Census Bureau's FTP server, merges the files into single,
nation-wide coverages, and then exports the merged files into various formats. Optionally upload these
files directly to S3."""

    args = Namespace(**kwargs)

    client = CensusClient(verbose=args.verbose)

    os.makedirs(args.destination, exist_ok=True)

    geogs = args.geography
    if not geogs:
        geogs = ['state', 'county', 'tract', 'bg', 'tract', 'place', 'zcta']

    for geog in geogs:

        to_upload = []
        print(f"\nPROCESSING: {geog}, {args.year}")

        print("downloading files...")
        paths = client.download_all_files(geog, args.year, args.destination, no_cache=args.no_cache)

        print("unzipping files...")
        unzipped = client.unzip_files(paths)

        print("creating dataframe...")
        df = client.create_dataframe_from_files(unzipped)

        print("add HEROP_ID...")
        id_field = client.lookups['census-sources'][str(args.year)]['configs'][geog]['id_field']
        df = client.add_herop_id_to_dataframe(df, geog, args.year, id_field)

        print("add BBOX...")
        df = client.add_bbox_to_dataframe(df)

        print("add DISPLAY_NAME...")
        name_field = client.lookups['census-sources'][str(args.year)]['configs'][geog]['name_field']
        df = client.add_name_to_dataframe(df, geog, args.year, name_field)

        if "shp" in args.format:
            print("generating shapefile...")
            shp_paths = client.export_to_shapefile(df, geog, args.year, args.destination)
            to_upload += shp_paths

        geojson_path = None
        if "geojson" in args.format:
            print("generating geojson...")
            geojson_path = client.export_to_geojson(df, geog, args.year, args.destination, overwrite=True)
            to_upload.append(geojson_path)

        if "pmtiles" in args.format:
            print("generating pmtiles...")
            if not args.tippecanoe_path:
                print("pmtiles output must be accompanied by --tippecanoe-path")
                exit()

            # need geojson for this, but use existing if it was created already
            if not geojson_path:
                geojson_path = client.export_to_geojson(df, geog, args.year, args.destination, overwrite=True)
            pmtiles_path = client.export_to_pmtiles(geojson_path, geog, args.year, args.destination, args.tippecanoe_path)

            to_upload.append(pmtiles_path)

        if args.upload:
            print(f"uploading {len(to_upload)} files to S3...")
            for fpath in to_upload:
                upload_to_s3(fpath, prefix='oeps', progress_bar=args.verbose)

    print("\ndone.")


## Group of commands for Google Big Query operations
bigquery_grp = AppGroup('bigquery',)

@bigquery_grp.command()
def check_credentials():
    """Check provided credentials for BigQuery client."""
    get_client()
    print('ok')

@bigquery_grp.command()
@click.option("--source", "-s",
    default=RESOURCES_DIR_rel,
    help="Data resource JSON file to load, or directory with multiple files to load. If no source "\
        "is provided, will process all files in the data/resources directory.",
)
@click.option("--overwrite",
    is_flag=True,
    default=False,
    help="Overwrite BQ table if it already exists."
)
@click.option("--table-only",
    is_flag=True,
    default=False,
    help="Only create the new table, don't load data into it."
)
@click.option("--dry-run",
    is_flag=True,
    default=False,
    help="Mock operation and perform no create/delete actions."
)
def load(**kwargs):
    """Load a data resource to a big query table. The data resource schema should provide all field
and table configuration information that is needed to create the table and load data into it."""

    args = Namespace(**kwargs)
    client = BigQuery()

    source = Path(args.source)
    if source.isdir():
        paths = source.glob("*.json")
    elif source.isfile():
        paths = [source]
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
                print(F"JOB COMPLETE: {load_job}")
                print(f"TIME ELAPSED: {datetime.now()-start}")

@bigquery_grp.command()
@click.option('--output', "-o",
    help="Output file for export. Must end with .csv for CSV or .shp for ESRI Shapefile."
)
@click.option('--sql-file',
    help="Path to file with SQL SELECT statement to run."
)
def export(**kwargs):
    """ Runs a SQL statement, which must be provided in a .sql file, and the results are printed to the console
or saved to a CSV or SHP output file, based on the destination argument."""

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
    """Generates a reference document for the BigQuery project schema, based on the
locally stored resource JSON schema files. """

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

        for f in d['schema']['fields']:
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
def generate_cli_docs():
    """ Generates markdown-formatted documentation from all CLI command groups."""

    docs_path = Path("../docs/commands")

    ## list of names of command group variables in this module
    for base_command in [
        'explorer_grp',
        'frictionless_grp',
        'census_grp',
        'overture_grp',
        'bigquery_grp',
    ]:
        mdclick_cmd = [
            "mdclick", "dumps",
            "--baseModule", "oeps.commands",
            "--baseCommand", base_command,
            "--docsPath", docs_path
        ]
        subprocess.run(mdclick_cmd)

    index_groups = set()
    paths = sorted([i for i in docs_path.glob("*.md") if not i.name == 'README.md'])
    for path in paths:
        index_groups.add(path.stem.split("-")[0])

    index_content = [
        "# OEPS Backend -- CLI Commands\n\n",
        "The CLI provides the following groups of commands for managing OEPS data in different contexts.\n\n",
        "All of these commands must be invoked with the prefix `flask`, for example:\n\n",
        "```\nflask bigquery check-credentials\n```\n\n",
        "Use `--help` to get detailed information for each command, or look at the auto-generated documentation below.\n\n",
    ]
    for group in sorted(index_groups):
        index_content.append(f"- [{group}](./{group}.md)\n")
        for path in sorted(docs_path.glob(f"{group}-*.md")):
            subcommand = path.stem.replace(f"{group}-", "")
            index_content.append(f"  - [{subcommand}](./{path.stem}.md)\n")

    with open(docs_path / 'README.md', "w") as o:
        o.writelines("".join(index_content))

    for path in docs_path.glob("*.md"):
        with open(path, "a") as o:
            o.write("\n_This documentation is automatically generated by "\
                "[md-click](https://github.com/RiveryIo/md-click). Do not edit this file directly._\n")
