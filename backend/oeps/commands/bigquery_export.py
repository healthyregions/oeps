import click

from oeps.clients.bigquery import BigQuery


@click.command()
@click.option(
    "--output",
    "-o",
    help="Output file for export. Must end with .csv for CSV or .shp for ESRI Shapefile.",
)
@click.option("--sql-file", help="Path to file with SQL SELECT statement to run.")
def bigquery_export(output, sql_file):
    """Runs a SQL statement, which must be provided in a .sql file, and the results are printed to the console
    or saved to a CSV or SHP output file, based on the destination argument."""

    client = BigQuery()

    if sql_file:
        client.run_query_from_file(sql_file)

    if output:
        client.export_results(output)

    else:
        client.print_results()
