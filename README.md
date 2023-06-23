# oeps-backend

Data migration and management code for the transition of the OEPS data into Google BigQuery.

## how this fits into existing work

This project builds from the Opioid Environment Policy Scan (OEPS) data warehouse stored in [github.com/GeoDaCenter/opioid-policy-scan](https://github.com/GeoDaCenter/opioid-policy-scan), and published on Zenodo at [doi.org/10.5281/zenodo.5842465](https://doi.org/10.5281/zenodo.5842465). This repo allows us to pull the final data from the latest OEPS release and push it into Google BigQuery, which will enable new ways of accessing and analyzing that data.

Keep in mind, some details of this implementation may change over the course of the summer, so we will update this document as needed.

## getting started

0. Create and activate a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) with [venv](https://docs.python.org/3/library/venv.html), [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), or your other tool of choice.

1. Clone this repo

        git clone https://github.com/healthyregions/oeps-backend
        cd oeps-backend

2. Install python requirements

        pip install -r requirements.txt

3. Initialize the data locally

    For now, we will pull CSV, SHP, and metadata files directly from the GeoDaCenter/opioid-policy-scan repository, rather than committing these files to this repo. Run the following:

        python initialize_data.py

    The main reasons for this approach are

    1) The relevant OEPS data is a small subset of that entire repo, so we don't want to download more than we need to
    2) There are pending updates to that repository, so it may be better for us to not have to manually do those updates in two different locations
    3) We should control our blank slate for beginning this work in a replicable way

    Datasets from the `data_final` directory in the [opioid-policy-scan](https://github.com/GeoDaCenter/opioid-policy-scan) will be copied into the `data` directory. **For now, only the state, county, tract, and zcta shapefiles are downloaded, plus all CSV and metadata files.**
    This means that some datasets, like mouds, are excluded for now (for the sake of simplicity). We'll add more to the initialize script as the project progresses.

Once initialized, you can create ETL scripts in the `scripts` directory to begin moving these local datasets into Google BigQuery.
