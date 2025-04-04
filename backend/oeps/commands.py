import os
import csv
from datetime import datetime
from pathlib import Path
import subprocess

import click
from flask.cli import AppGroup

from oeps.clients.bigquery import BigQuery, get_client
from oeps.clients.census import CensusClient
from oeps.clients.explorer import Explorer
from oeps.clients.frictionless import DataPackage
from oeps.clients.registry import Registry
from oeps.config import (
    CACHE_DIR,
    EXPLORER_ROOT_DIR,
    REGISTRY_DIR,
)

from oeps.utils import (
    upload_to_s3,
    handle_overwrite,
)

# Make relative paths for directory configs so they can properly be used as default values for
# CLI arguments. Using absolute paths (e.g. those in the config) would result in absolute paths
# in the generated docs... this would be incorrect on every system besides the one that had
# generated the docs.
EXPLORER_ROOT_DIR_rel = os.path.relpath(EXPLORER_ROOT_DIR, start=Path(__file__).parent)
CACHE_DIR_rel = os.path.relpath(CACHE_DIR, start=Path(__file__).parent.parent)
REGISTRY_DIR_rel = os.path.relpath(REGISTRY_DIR, start=Path(__file__).parent.parent)


def add_common_opts(*options):
    """Helper function for grouping multiple options into a single decorator
    so they can easily be applied multiple commands.
    see: https://stackoverflow.com/a/67138197/3873885"""

    def wrapper(function):
        for option in reversed(options):
            function = option(function)
        return function

    return wrapper


## define some basic command options that can be reused in many places.
verbose_opt = click.option(
    "--verbose",
    is_flag=True,
    help="Enable verbose logging.",
)
overwrite_opt = click.option(
    "--overwrite",
    is_flag=True,
    help="Overwrite output content if it already exists.",
)
registry_opt = click.option(
    "--registry-path",
    help="Optional override for the registry directory.",
    default=REGISTRY_DIR_rel,
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
explorer_opt = click.option(
    "--explorer-path",
    help="Optional override for the root directory of the explorer.",
    default=EXPLORER_ROOT_DIR_rel,
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)


## ~~ Big Query Commands ~~

## Group of commands for Google Big Query operations
bigquery_grp = AppGroup(
    "bigquery",
    help="A group of operations for loading, querying, and exporting data to Google Big Query.",
)


@bigquery_grp.command()
def check_credentials():
    """Check provided credentials for BigQuery client."""
    get_client()
    print("ok")


@bigquery_grp.command()
@click.option(
    "--name",
    "-n",
    help="Name can be provided to load a single Data Resource to Big Query (instead of everything in the registry)",
)
@click.option(
    "--table-only",
    is_flag=True,
    default=False,
    help="Only create the new table, don't load data into it.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Mock operation and perform no create/delete actions.",
)
@add_common_opts(overwrite_opt, registry_opt)
def load(name, table_only, dry_run, overwrite, registry_path):
    """Load a data resource to a big query table. The data resource schema should provide all field
    and table configuration information that is needed to create the table and load data into it."""

    bq = BigQuery()
    registry = Registry(registry_path)

    messages = []

    data_resources = registry.get_all_sources()

    if name:
        to_load = [i for i in data_resources if i["name"] == name]
        if len(to_load) == 0:
            print("no resource by that name in registry. cancelling load.")
            exit()
    else:
        to_load = data_resources

    for resource in to_load:
        if name and resource["name"] != name:
            continue

        if table_only:
            table = bq.create_table(resource, overwrite=overwrite)
            print(table)
            exit()

        else:
            start = datetime.now()
            print(f"\nVALIDATE INPUT SOURCE: {resource['path']}")
            rows, errors = bq.load_rows_from_resource(resource)
            messages += errors
            print(f"WARNINGS ENCOUNTERED: {len(errors)}")
            for e in errors:
                print("  " + e)

            if not dry_run:
                print(f"\nBEGIN LOAD: {resource['name']}")
                table = bq.create_table(resource, overwrite=overwrite)
                print(f"TABLE CREATED: {table}")
                load_job = bq.load_table(
                    rows, resource["bq_dataset_name"], resource["bq_table_name"]
                )
                print(f"JOB COMPLETE: {load_job}")
                print(f"TIME ELAPSED: {datetime.now()-start}")

    print(f"ERRORS/WARNINGS ENCOUNTERED: {len(messages)}")


@bigquery_grp.command()
@click.option(
    "--output",
    "-o",
    help="Output file for export. Must end with .csv for CSV or .shp for ESRI Shapefile.",
)
@click.option("--sql-file", help="Path to file with SQL SELECT statement to run.")
def export(output, sql_file):
    """Runs a SQL statement, which must be provided in a .sql file, and the results are printed to the console
    or saved to a CSV or SHP output file, based on the destination argument."""

    client = BigQuery()

    if sql_file:
        client.run_query_from_file(sql_file)

    if output:
        client.export_results(output)

    else:
        client.print_results()


@bigquery_grp.command()
@add_common_opts(registry_opt)
def generate_reference_md(registry_path):
    """Generates a reference document for the BigQuery project schema, based on the
    locally stored resource JSON schema files."""

    client = BigQuery()
    registry = Registry(registry_path)

    outfile = Path("../docs/reference/big-query-tables.md").absolute()
    client.generate_reference_doc(registry.get_all_sources(), outfile)


census_grp = AppGroup(
    "census",
    help="A group of commands for obtaining and managing geospatial data from the US Census Bureau.",
)


@census_grp.command()
@click.option(
    "--format",
    "-f",
    type=click.Choice(["shp", "geojson", "pmtiles"]),
    default=["shp", "geojson", "pmtiles"],
    multiple=True,
    help="Choose what output formats will be created. Options are `shp` (shapefile), `geojson` "
    "(GeoJSON), and/or `pmtiles` (PMTiles).",
)
@click.option(
    "--geography",
    "-g",
    type=click.Choice(["state", "county", "tract", "bg", "place", "zcta"]),
    default=["state", "county", "tract", "bg", "place", "zcta"],
    multiple=True,
    help="Specify a geography to prepare. If left empty, all geographies will be processed.",
)
@click.option(
    "--year", "-y", type=click.Choice(["2018", "2010"]), help="Specify a year."
)
@click.option(
    "--scale",
    "-s",
    type=click.Choice(["500k", "tiger"]),
    default="500k",
    help="Specify a scale of geographic boundary file.",
)
@click.option(
    "--tippecanoe-path",
    help="Full path to tippecanoe binary, required for PMTiles generation.",
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Force re-retrieval of files from FTP.",
)
@click.option(
    "--upload", is_flag=True, default=False, help="Upload the processed files to S3."
)
@click.option(
    "--destination",
    default=None,
    help="Output directory for export. If not provided, results will be in .cache/geodata.",
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option(
    "--prefix",
    default="oeps",
    help="If output is uploaded to S3, use this prefix for the objects.",
)
@add_common_opts(verbose_opt)
def get_geodata(
    format,
    year,
    destination,
    scale,
    geography,
    tippecanoe_path,
    upload,
    no_cache,
    prefix,
    verbose,
):
    """This command retrieves geodata from the US Census Bureau's FTP server, merges the files into single,
    nation-wide coverages, and then exports the merged files into various formats. Optionally upload these
    files directly to S3."""

    client = CensusClient(verbose=verbose)

    print("year:", year)
    print("format(s):", format)
    print("geography(s):", geography)
    print("scale:", scale)

    if "pmtiles" in format and not tippecanoe_path:
        print("pmtiles output must be accompanied by --tippecanoe-path")
        exit()

    for geog in geography:
        to_upload = []
        print(f"\nPROCESSING: {geog}, {scale}, {year}")

        client.year = year
        client.geography = geog
        client.scale = scale

        # skip if there isn't a config entry for this geography/year combo
        if (
            year not in client.lookups["census-sources"]
            or geog not in client.lookups["census-sources"][year][scale]
        ):
            print("no source configuration for this combo, skipping")
            continue

        print("downloading files...")
        paths = client.download_all_files(no_cache=no_cache)

        print("unzipping files...")
        unzipped = client.unzip_files(paths)

        print("creating dataframe...")
        df = client.create_dataframe_from_files(unzipped)

        print("add HEROP_ID...")
        df = client.add_herop_id_to_dataframe(df)

        print("add BBOX...")
        df = client.add_bbox_to_dataframe(df)

        print("add LABEL...")
        df = client.add_label_to_dataframe(df)

        if "shp" in format:
            print("generating shapefile...")
            shp_output = client.export_to_shapefile(df, destination)
            to_upload.append(shp_output["zipped"])

        geojson_path = None
        if "geojson" in format:
            print("generating geojson...")
            geojson_path = client.export_to_geojson(df, destination, overwrite=True)
            to_upload.append(geojson_path)

        if "pmtiles" in format:
            print("generating pmtiles...")

            # need geojson for this, but use existing if it was created already
            if not geojson_path:
                geojson_path = client.export_to_geojson(df, destination, overwrite=True)
            pmtiles_path = client.export_to_pmtiles(
                geojson_path, tippecanoe_path, destination
            )

            to_upload.append(pmtiles_path)

        if upload:
            print(f"uploading {len(to_upload)} files to S3...")
            upload_to_s3(to_upload, prefix=prefix, progress_bar=verbose)

    print("\ndone.")


## ~~ Frictionless Data Commands ~~

frictionless_grp = AppGroup(
    "frictionless",
    help="A group of operations for interacting with Frictionless data specs. These commands allow us to "
    "export Frictionless-compliant derivations of the data in OEPS.",
)


@frictionless_grp.command()
@click.option(
    "--destination",
    "-d",
    help="Output location for export directory. The package will be placed within this directory and given "
    "a name generated from the current date and time.",
    default=Path(CACHE_DIR_rel, "data-packages"),
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
@click.option(
    "--zip", "zip_", is_flag=True, default=False, help="Zip the output data package."
)
@click.option(
    "--upload",
    is_flag=True,
    default=False,
    help="Upload the zipped data package to S3. Bucket is determined by `AWS_BUCKET_NAME` environment variable.",
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Force re-download of any remote files.",
)
@click.option(
    "--skip-foreign-keys",
    is_flag=True,
    default=False,
    help="Don't define foreign keys in the output data package. This is needed to avoid validation errors that "
    "occur when Shapefiles are used in foreign keys.",
)
@click.option(
    "--skip-validation",
    is_flag=True,
    default=False,
    help="Don't run data package validation on the final output.",
)
@add_common_opts(overwrite_opt, registry_opt, verbose_opt)
def create_data_package(
    destination,
    zip_,
    upload,
    no_cache,
    skip_foreign_keys,
    skip_validation,
    overwrite,
    registry_path,
    verbose,
):
    """Generates a Frictionless data package from the Data Resource definitions in this backend. This export
    process was developed specifically to support integration of the OEPS data warehouse into the JCOIN commons.

    The resulting package will be validated against the `frictionless` standard using that Python library.

    `--skip-foreign-keys` to skip the creation of foreign keys--useful because foreign keys to shapefiles break
    validation.

    `--skip-validation` to skip the final step of running validation on the output package.
    """

    out_name = f"oeps-data-package-v2_{datetime.now().date().isoformat()}"
    out_name = out_name + "_no_foreign_keys" if skip_foreign_keys else out_name
    out_path = Path(destination, out_name)

    if not overwrite:
        handle_overwrite(out_path)

    registry = Registry(registry_path)
    dp = DataPackage(out_path)
    dp.create_from_registry(
        registry,
        zip_,
        upload,
        no_cache=no_cache,
        skip_foreign_keys=skip_foreign_keys,
        run_validation=not skip_validation,
        verbose=verbose,
    )


registry_grp = AppGroup(
    "registry",
    help="A group of operations for interacting with all data stored in the backend registry.",
)


@registry_grp.command()
@click.option(
    "--destination",
    "-d",
    default=None,
    help="Output directory for new dictionaries, if not supplied will be placed within data dir.",
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
)
@add_common_opts(registry_opt)
def create_data_dictionaries(destination, registry_path):
    """Create the human readable, MS Excel data dictionaries based on registry content."""

    registry = Registry(registry_path)
    registry.create_data_dictionaries(destination)


@registry_grp.command()
@add_common_opts(registry_opt)
def validate(registry_path):
    """Create the human readable, MS Excel data dictionaries based on registry content."""

    registry = Registry(registry_path)
    registry.validate()


explorer_grp = AppGroup(
    "explorer",
    help="Operations used to provision the fronted explorer app with static assets.",
)


@explorer_grp.command()
@click.option(
    "--make-csvs",
    help="Only write new config JSON files, assumes CSV files are already generated.",
    default=False,
    is_flag=True,
)
@add_common_opts(registry_opt, explorer_opt)
def build_map(
    make_csvs: bool,
    registry_path: Path,
    explorer_path: Path,
):
    """Builds configuration files for the frontend OEPS Explorer application."""

    registry = Registry(registry_path)
    ex = Explorer(registry=registry, root_dir=explorer_path)
    ex.build_map_config(write_csvs=make_csvs)


@explorer_grp.command()
@add_common_opts(registry_opt, explorer_opt)
def build_docs(registry_path: Path, explorer_path: Path):
    """Builds configuration files for the frontend OEPS Explorer application."""

    registry = Registry(registry_path)
    ex = Explorer(registry=registry, root_dir=explorer_path)
    ex.build_docs_config()


@click.command()
def make_cli_docs():
    """Generates markdown-formatted documentation from all CLI commands groups."""

    docs_path = Path("../docs/reference/commands")
    for path in docs_path.glob("*.md"):
        os.remove(path)

    ## list of base modules and commands to process
    command_list = [
        ("oeps.commands", "make_cli_docs"),
        ("oeps.commands", "bigquery_grp"),
        ("oeps.commands", "census_grp"),
        ("oeps.commands", "explorer_grp"),
        ("oeps.commands", "frictionless_grp"),
        ("oeps.commands", "registry_grp"),
    ]

    for mod, com in command_list:
        mdclick_cmd = [
            "mdclick",
            "dumps",
            "--baseModule",
            mod,
            "--baseCommand",
            com,
            "--docsPath",
            docs_path,
        ]
        subprocess.run(mdclick_cmd)

    index_groups = set()
    paths = sorted([i for i in docs_path.glob("*.md") if not i.name == "README.md"])
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

    with open(docs_path / "README.md", "w") as o:
        o.writelines("".join(index_content))

    for path in docs_path.glob("*.md"):
        with open(path, "a") as o:
            o.write(
                "\n_This documentation is automatically generated by "
                "[md-click](https://github.com/RiveryIo/md-click). Do not edit this file directly._\n"
            )


@click.command()
def make_registry_summary():
    def generate_md_table(header, rows):
        content = "|".join(header) + "\n"
        content += "|".join(["-" for i in header]) + "\n"
        for row in rows:
            content += "|".join(row) + "\n"
        return content

    def write_csv_file(name, header, rows):
        path = Path(f"../docs/reference/registry/{name}.csv")
        with open(path, "w") as o:
            writer = csv.writer(o)
            writer.writerow(header)
            writer.writerows(rows)

    def clean_value(value, md=False):
        if isinstance(value, str):
            return value.replace("\n", "<br>")
        elif isinstance(value, list):
            join_char = "<br/>" if md else ", "
            return join_char.join(value)
        else:
            return str(value)

    all_content_md = Path("../docs/reference/registry/all-content.md")

    registry = Registry()

    ## Create VARIABLES content

    variables = list(registry.variables.values())
    var_cols = [
        "name",
        "title",
        "type",
        "example",
        "description",
        "table_sources",
        "constraints",
        "construct",
        "source",
        "source_long",
        "oeps_v1_table",
        "comments",
        "metadata_doc_url",
        "longitudinal",
        "analysis",
    ]
    var_rows_csv = []
    var_rows_md = []
    for var in variables:
        var_rows_csv.append([clean_value(var[i]) for i in var_cols])
        var_rows_md.append([clean_value(var[i], md=True) for i in var_cols])

    ## Create THEME content

    themes = registry.themes
    theme_cols = ["theme", "construct", "proxy"]
    theme_rows = []

    for theme, constructs in themes.items():
        for construct, proxy in constructs.items():
            theme_rows.append([theme, construct, proxy])

    ## Create TABLE SOURCES content

    table_sources = list(registry.table_sources.values())
    tab_cols = [
        "name",
        "title",
        "path",
        "format",
        "mediatype",
        "description",
        "year",
        "geodata_source",
        "bq_dataset_name",
        "bq_table_name",
    ]
    tab_rows = []
    for var in table_sources:
        tab_rows.append([clean_value(var[i]) for i in tab_cols])

    ## Create GEODATA SOURCES content

    geodata_sources = list(registry.geodata_sources.values())
    geo_cols = [
        "name",
        "title",
        "path",
        "format",
        "mediatype",
        "description",
        "summary_level",
        "bq_dataset_name",
        "bq_table_name",
    ]
    geo_rows = []
    for var in geodata_sources:
        geo_rows.append([clean_value(var[i]) for i in geo_cols])

    write_csv_file("variables", var_cols, var_rows_csv)
    write_csv_file("themes", theme_cols, theme_rows)
    write_csv_file("table_sources", tab_cols, tab_rows)
    write_csv_file("geodata_sources", geo_cols, geo_rows)

    with open(all_content_md, "w") as o:
        o.write(f"""# Registry Content

This is an autogenerated searchable list of all content in the registry.
You can also access each section as a CSV if needed.

Jump to:

- [variables](#variables) [[csv](./variables.csv)]
- [themes](#themes) [[csv](./themes.csv)]
- [table_sources](#table_sources) [[csv](./table_sources.csv)]
- [geodata_sources](#geodata_sources) [[csv](./geodata_sources.csv)]

## `variables`

{generate_md_table(var_cols, var_rows_csv)}

[back to top](#)

## `themes`

{generate_md_table(theme_cols, theme_rows)}

[back to top](#)

## `table_sources`

{generate_md_table(tab_cols, tab_rows)}

[back to top](#)

## `geodata_sources`

{generate_md_table(geo_cols, geo_rows)}

[back to top](#)

_This file is automatically generated. Do not edit this file directly._
""")
