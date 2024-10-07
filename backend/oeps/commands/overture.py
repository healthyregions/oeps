from pathlib import Path
from argparse import Namespace

import click
from flask.cli import AppGroup

from oeps.clients.overture import get_filter_shape, get_data

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
@click.option("--tippecanoe-path",
    default=None,
    help="Path to tippecanoe binary needed for conversion to PMTiles."
)
@click.option("--upload",
    is_flag=True,
    default=False,
    help="Upload the output file to S3."
)
@click.option("--upload-prefix",
    is_flag=True,
    default=False,
    help="Upload the output file to S3."
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

    if (args.outfile and Path(args.outfile).suffix == ".pmtiles") and args.tippecanoe_path is None:
        print('Tippecanoe path needed for PMTiles output.')
        exit()

    print(geom_filter)

    get_data(
        outpath=Path(args.outfile) if args.outfile else None,
        categories=args.categories,
        confidence=args.confidence,
        geom_filter=geom_filter,
        export_category_list=args.export_category_list,
        tippecanoe_path=args.tippecanoe_path
    )
