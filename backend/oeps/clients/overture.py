from datetime import datetime
from pathlib import Path
import uuid
import subprocess

import duckdb
import geopandas as gpd


def get_connection():
    connection = duckdb.connect()

    # these props must be set to empty before the query to s3, otherwise it fails. See:
    # https://github.com/duckdb/duckdb/issues/7970#issuecomment-2118343680
    connection.execute("SET s3_access_key_id='';SET s3_secret_access_key='';")

    connection.install_extension("spatial")
    connection.install_extension("httpfs")
    connection.load_extension("spatial")
    connection.load_extension("httpfs")

    return connection


def get_filter_shape(input_file: str, filter_value: str):
    print(input_file)

    gdf = gpd.read_file(input_file)
    filter_row = gdf[gdf["GEOID"] == filter_value]

    return {
        "bbox": filter_row["BBOX"].values[0],
        "geom": filter_row["geometry"].values[0],
        "series": filter_row,
    }


def get_data(
    outpath: Path = None,
    categories: list = [],
    confidence: str = ".8",
    geom_filter: dict = None,
    export_category_list=False,
    tippecanoe_path: str = None,
):
    con_clause = f"confidence >= {confidence} AND" if confidence != "-1" else ""
    print(f"confidence filter: {con_clause}")

    cat_clause = (
        "category IN ('{}') AND".format("', '".join(categories)) if categories else ""
    )
    print(f"category filter: {cat_clause}")

    if geom_filter:
        filter_bbox = geom_filter["bbox"].split(",")
    else:
        # approximate extent of the US (48 states)
        filter_bbox = ["-124.211606", "25.837377", "-67.158958", "49.384359"]

    print(f"extent filter: {filter_bbox}")
    if geom_filter:
        print("-- result will be clipped to filter geometry")

    overture_url = (
        "s3://overturemaps-us-west-2/release/2023-11-14-alpha.0/theme=places/type=*/*"
    )

    query_sql = """SELECT
        FILTER(names.common, x->x.language = 'local') [ 1 ].value as name,
        categories.main as category,
        addresses[1].freeform as address,
        addresses[1].locality as city,
        addresses[1].postcode as zip,
        addresses[1].region as state,
        ROUND(confidence,2) as confidence,
        ST_AsText(geometry) as wkt
    FROM read_parquet('{}', filename=true, hive_partitioning=1)
    WHERE
        {}
        {}
        bbox.minX BETWEEN {} AND {} AND
        bbox.minY BETWEEN {} AND {}
        """.format(
        overture_url,
        con_clause,
        cat_clause,
        filter_bbox[0],
        filter_bbox[2],
        filter_bbox[1],
        filter_bbox[3],
    )

    print(query_sql)

    start = datetime.now()
    connection = get_connection()
    df = connection.execute(query_sql).df()
    print(datetime.now() - start)

    # strip the extra 4 from zip codes
    df["zip"] = df["zip"].str[:5]

    if export_category_list:
        # Get the distinct values of the column
        distinct_values = df["category"].drop_duplicates()

        fpath = (
            outpath.name + "__categories.csv"
            if outpath
            else f"categories__{uuid.uuid4().hex}.csv"
        )

        # Write the distinct values to a CSV file
        distinct_values.to_csv(fpath, index=False, header=None)

    print(df)

    gs = gpd.GeoSeries.from_wkt(df["wkt"])
    gdf = gpd.GeoDataFrame(df, geometry=gs, crs="EPSG:4326")

    del gdf["wkt"]

    print(gdf)

    if geom_filter:
        gdf = gdf.clip(geom_filter["series"])

    if outpath:
        if outpath.suffix == ".geojson":
            gdf.to_file(outpath, driver="GeoJSON")
        elif outpath.suffix == ".shp":
            gdf.to_file(outpath)
        elif outpath.suffix == ".pmtiles":
            if not tippecanoe_path:
                print("tippecanoe_path required for pmtiles output")
                return
            json_path = outpath.stem + ".pmtiles"
            gdf.to_file(json_path, driver="GeoJSON")
            cmd = [
                tippecanoe_path,
                # "-zg",
                # tried a lot of zoom level directives, and seems like for block group
                # (which I believe is the densest)shp_paths 10 is needed to preserve shapes well enough.
                "-z10",
                "--projection",
                "EPSG:4326",
                "-o",
                str(outpath),
                "-l",
                "resources",
                "--force",
                str(json_path),
            ]
            subprocess.run(cmd)

    return outpath
