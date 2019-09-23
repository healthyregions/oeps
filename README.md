# oeps-backend

This project builds from the Opioid Environment Policy Scan (OEPS) data warehouse stored in [github.com/GeoDaCenter/opioid-policy-scan](https://github.com/GeoDaCenter/opioid-policy-scan), and published on Zenodo at [doi.org/10.5281/zenodo.5842465](https://doi.org/10.5281/zenodo.5842465). This repo allows us to pull the final data from the latest OEPS release and push it into Google BigQuery, which will enable new ways of accessing and analyzing that data.

## Getting Started

### Install the Python Package

0. Create and activate a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) with [venv](https://docs.python.org/3/library/venv.html), [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), or your other tool of choice.

1. Clone this repo

        git clone https://github.com/healthyregions/oeps-backend
        cd oeps-backend

2. Install this package and its dependencies

        pip install -e .

3. Enter the `oeps_backend` directory, this is where you'll run scripts from.

        cd oeps_backend

### Setup BigQuery Credentials

Enviroment variables allow us to keep BigQuery credentials outside of version control.

- Make a copy of `.env.example` and name it `.env`. Any variables defined in this file will now be available via `os.getenv('VARIABLE_NAME')`

- Obtain a set of JSON credentials for the project, and store the file anywhere on your computer (but outside of this repository).

- In your `.env` file, update the `BQ_CREDENTIALS_FILE_PATH` variable with the full path to this file.

    ```
    BQ_CREDENTIALS_FILE_PATH="/home/my_username/bq_credentials/oeps-391119-5783b2b59b83.json"
    ```

- It is also possible to set BigQuery credentials without storing a local JSON file. More info on this is in the `.env.example`.

## BigQuery Import/Export

### Importing Data

Use the following command to load a new table into BigQuery:

    python bq_load.py table_definitions/table.json

Where `table.json` is a [table definition file](#table-definitions). Optional flags on this command are:

- `--table-only` will create the BQ dataset and table, but will not attempt to load data into it.
- `--dry-run` will validate the input dataset against the table definition, but not attempt to load it.
- `--overwrite` will drop and recreate the BQ table if it already exists in the dataset.


### Exporting Data

Use the following command to query the OEPS BigQuery tables:

    python bq_query.py --sql sql/states.sql --output states.shp

Where `states.sql` is an example of a file that holds the SQL query to perform against one or more tables. In the SQL, `PROJECT_ID` is a placeholder (it will be replaced with the actual project identifier before the query is performed), such that table references look like `PROJECT_ID.dataset_name.table_name`, or `PROJECT_ID.spatial.states2018` for the table that holds state boundaries.

- `--sql-file` path to a file whose contents is a complete SQL query. 
- `--output` is the name of a file to which the query results will be written. Either .csv or .shp files can be specified, and if a spatial result is written to CSV the geometries will be in WKT format. If this argument is omitted, the query results will be printed to the console (helpful for testing queries).

You can write your own SQL into a file and use the same command to perform your query and export the results.

Use the [BQ-Reference](BQ-Reference.md) page for quick access to all table and column names.

### Table Definitions

A **table definition** is a JSON file that specifies

1. The location of a source dataset to load
2. The Google BigQuery project and table name to load into
3. A thorough schema defining all fields from the source dataset and how they will be stored in BigQuery

This information is used in various contexts to

1. Create (or re-create) table schemas in BigQuery
2. Load data into these tables
3. Export data from BigQuery into various formats and file types

The structure of a table definition is inspired by the [Table Schema](https://specs.frictionlessdata.io/table-schema) specification published by [Frictionless Standards](https://specs.frictionlessdata.io), with a few additions for our own use case.

#### Structure

The top-level properties of a table definition are:

Property|Format|Description
-|-|-
`data_source`|String|Path or URL for CSV or SHP dataset to load
`bq_table_name`|String|Target table in BigQuery
`bq_dataset_name`|String|Target dataset in BigQuery
`fields`|List|List of definitions for all table fields

Note that in BigQuery, a `dataset` is akin to a database in other RDBS implementations, such that a dataset holds one or more tables. Often, tables are identified by their fully-qualified identifier: `project_id.dataset_name.table_name`.

The `fields` property is a list of one or more field objects, as described below. The only requirement of the `fields` list is that **must** contain an entry for a [`HEROP_ID`](#herop_id-field) field. This is our unique GIS join field.

#### Field Descriptors

Fields are defined by a JSON object that adheres to the [field descriptors](https://specs.frictionlessdata.io/table-schema/#field-descriptors) portion of the table schema standard, though not all possible attributes are required or implemented.

Property|Format|Description|OEPS Use
-|-|-|-
`name`|String|Canonical name for this column (used in BigQuery)|Required
`title`|String|A nicer human readable label or title for the field|Required
`type`|String|A string specifying the type. See [types](https://specs.frictionlessdata.io/table-schema/#types-and-formats).|Required
`format`|String|A string specifying a format|Not Implemented
`example`|String|An example value for the field|Optional
`description`|String|A description for the field|Optional
`constraints`|JSON|A [constraints descriptor](https://specs.frictionlessdata.io/table-schema/#constraints)|Not Implemented

The following additional attributes are also supported and in some cases required:

Property|Format|Description|OEPS Use
-|-|-|-
`src_name`|String|Name of column in source dataset|Required
`bq_data_type`|String|[Field type for BigQuery schema](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#TableFieldSchema.FIELDS.type)|Required
`theme`|String|One of `Social`, `Environment`, `Economic`, `Policy`, `Outcome`, or `Geography`. See [OEPS docs](https://oeps.healthyregions.org/docs).|Optional
`comment`|String|Additional information about the data in this field|Optional
`source`|String|Source of the data in this field|Optional
`max_length`|Integer|Max length of field (used in BigQuery schema)|Optional

#### HEROP_ID Field

For now, please see [this comment](https://github.com/GeoDaCenter/opioid-policy-scan/issues/68#issuecomment-1701863572) for a detailed description of how `HEROP_ID` values are constructed.

A field descriptor for this field will look something like this:

```
{
    "name": "HEROP_ID",
    "src_name": "HEROP_ID",
    "type": "string",
    "example": "040US01-2018",
    "description": "A derived unique id corresponding to the relevant geographic unit.",
    "theme": "Geography",
    "bq_data_type": "STRING"
}
```

#### Geometry Fields

To load a shapefile you must include the following field descriptor in your `fields` list:

```
{
    "name": "geom",
    "title": "Geom",
    "type": "string",
    "src_name": "geometry",
    "bq_data_type": "GEOGRAPHY"
}
```

Note that for spatial data Table Schema only allows `geojson` or `geopoint` as valid geographic types, while Google BigQuery uses `GEOGRAPHY`. For now, we'll just use the above configuration, and more nuances can be pursued down the road. 

#### Example

The following is a truncated version of a table definition for the 2010 State-level data published in OEPS v2.0. This defines a table `project_id.tabular.S_2010` with two fields, `HEROP_ID` and `TotPop`. Note also the direct URL to the raw `data_source` on GitHub.

```
{
    "bq_dataset_name": "tabular",
    "bq_table_name": "S_2010",
    "data_source": "https://raw.githubusercontent.com/GeoDaCenter/opioid-policy-scan/main/data_final/full_tables/S_2010.csv",
    "fields": [
        {
            "name": "HEROP_ID",
            "src_name": "HEROP_ID",
            "type": "string",
            "description": "A derived unique id corresponding to the relevant geographic unit.",
            "constraints": null,
            "theme": "Geography",
            "bq_data_type": "STRING"
        },
        {
            "name": "TotPop",
            "src_name": "TotPop",
            "type": "integer",
            "example": "7294336",
            "description": "Estimated total population",
            "constraints": null,
            "theme": "Social",
            "source": "American Community Survey 2014-2018 5 Year Estimates; 2010 Decennial Census; Integrated Public Use Microdata Service National Historic Geographic Information Systems",
            "comments": "1980, 1990, and 2000 data from respective decennial censuses downloaded from IPUMS NHGIS and aggregated upwards.",
            "bq_data_type": "INTEGER"
        }
    ]
}
```

## Contributing to this Repo

For contributions we'll use a standard branching pattern--make a new branch from `main`, add commits to it, and then create a pull request to get those changes merged back into `main`.

In the command line, this would look like the following steps. (VSCode and other editors have great git integrations as well, but the steps are generally the same):

1. Make sure you are on the main branch locally

        git branch

2. Create a new branch from `main`

        git checkout -b your_new_branch_name

    You will now be on a new branch, as `git branch` will show you.

3. Change code, add commits

        git add path/to/your/new_file
        git commit -m "short description of the change you made"

    If you are addressing an open ticket with your commit, say ticket number 10, you should add `#10` to your commit message, like

        git commit -m "update file list for initialization #10"

4. Push your branch to the GitHub repo

        git push --set-upstream origin your_new_branch_name

5. Create the [Pull Request](https://github.com/healthyregions/pulls) in GitHub, including a description of the changes your branch contains.

<!-- README.md is generated from README.Rmd. Please edit that file -->

# Opioid Environment Policy Scan (OEPS) Database

## Public Site - OEPS Explorer
Explore, download, and map OEPS data on the [OEPS Explorer](https://oeps.netlify.app/). 

## About

The Opioid Environment Policy Scan (OEPS) is a free, open-source data warehouse providing access to data at multiple spatial scales to help characterize the multi-dimensional risk environment impacting opioid use in justice populations across the United States. 

The OEPS developed for the [Justice Community Opioid Innovation Network (JCOIN)](https://heal.nih.gov/research/research-to-practice/jcoin) by the team at the [Healthy Regions and Policies Lab](https://voices.uchicago.edu/herop/team), [Center for Spatial Data Science](https://spatial.uchicago.edu/) at the University of Chicago Data is also available to the JCOIN Network through the [JCOIN Data Commons](https://jcoin.datacommons.io/).

We developed the OEPS as a free, open-source platform to aggregate and share publicly-available data at the Census tract, zip code, county, and state levels. Geographic boundary shapefiles are provided for ease of merging datasets (csv files) for exploration, spatial analysis, or visualization. Download the entire data repository, or you can filter and download by theme or spatial scale with the [OEPS Explorer](https://oeps.netlify.app/). All datasets are accompanied by metadata docs, detailing their source data, year, and more. Learn more about our methods and approaches, including the risk environment framework, in [Methodology](https://oeps.netlify.app/methods).

## Data Overview

![](/images/oeps-diagram.png)

Variable constructs are grouped thematically below to highlight the multi-dimensional risk environment of opioid use in justice populations. In the **Metadata** column, linked pages provide more detail about the data source, descriptions of data cleaning or processing, and individual variables included.

### Geographic Boundaries

| Variable Construct | Variable Proxy | Source | Metadata | Spatial Scale | 
|:------------------ | :------------- | :----- | :------- | :------------ | 
| Geographic Boundaries | State, County, Census Tract, Zip Code Tract Area (ZCTA) | US Census, 2018 | [Geographic Boundaries](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/GeographicBoundaries_2018.md) | State, County, Tract, Zip |
| Crosswalk files | County, Census Tract, Zip Code Tract Area (ZCTA) | HUD’s Office of Policy Development and Research (PD&R) | [Crosswalk Files](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/crosswalk.md) | County, Tract, Zip |

### Policy Variables

| Variable Construct | Variable Proxy | Source | Metadata | Spatial Scale | 
|:------------------ | :------------- | :----- | :------- | :------------ | 
| Prison Incarceration Rates | Prison population rate and prison admission rate by gender and ethnicity | Vera Institute of Justice, 2016 | PS01 / [Prison Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Prison%20variables_2016.md) | County | 
| Jail Incarceration Rates | Jail population rate by gender and ethnicity | Vera Institute of Justice, 2017 | PS02 / [Jail Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Jail%20variables_2017.md) | County |
| Prescription Drug Monitoring Programs (PDMP) | Any PDMP; Operational PDMP; Must-access PDMP; Electronic PDMP | OPTIC, 2017 | PS03 / [PDMP](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/PDMP_2017.md) | State | 
| Good Samaritan Laws | Any Good Samaritan Law; Good Samaritan Law protecting arrest | OPTIC, 2017 | PS04 / [GSL](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/GSL_2018.md) | State | 
| Naloxone Access Laws |  Any Naloxone law; law allowing distribution through a standing or protocal order; law allowing pharmacists prescriptive authority | OPTIC, 2017 | PS05 / [NAL](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/NAL_2017.md) | State |  
| Medicaid Expenditure | Total Medicaid spending | KFF, 2019 | PS06 / [MedExp](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/MedExp_2019.md) | State | 
| Medicaid Expansion | Spending for adults who have enrolled through Medicaid expansion | KFF, 2018 | PS07 / [MedExpan](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/MedExpan_2018.md) | State | 
| Syringe Services Laws | Laws clarifying legal status for syringe exchange, distribution, and possession programs | LawAtlas, 2019 | PS08 / [Syringe](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Syringe.md) | State | 
| Medical Marijuana Laws | Law authorizing adults to use medical marijuana | PDAPS, 2017 | PS09 / [MedMarijLaw](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/MedMarijLaw.md) | State |
| State & Local Government Expenditures | Government spending on public health, welfare, public safety, and corrections | US Census, 2018 | PS11 / [Government Expenditures](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/PublicExpenditures.md) | State, Local |

<br>

### Health Variables

| Variable Construct | Variable Proxy | Source | Metadata | Spatial Scale |
|:------------------ | :------------- | :----- | :------- | :------------ |
| Drug-related death rate | Death rate from drug-related causes | CDC WONDER, 2019 10-year ave. | Health01 / [Drug-Related Death Rate](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Health_DrugDeaths.md) | State, County | 
| Hepatitis C rates | HepC prevalence and mortality | HepVu | Health02 / [Hepatitis C](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/HepC_rate.md) | State, County | 
| Physicians | Number of Primary Care and Specialist Physicians | Dartmouth Atlas, 2010 | Health03 / [Physicians](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Health_PCPs.md) | Tract, County, State | 
| Access to MOUDs | Distance to nearest MOUD | US Census, SAMHSA, Vivitrol, 2020 | Access01 / [Access: MOUDs](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Access_MOUDs.md) | County, Tract, Zip | 
| Access to Health Centers | Distance to nearest FQHC | US Census, US COVID Atlas, HRSA, 2020  | Access02 / [Access: FQHCs](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Access_FQHCs_MinDistance.md) | Tract, Zip | 
| Access to Hospitals | Distance to nearest hospital | US Census, CovidCareMap, 2020 |  Access03 / [Access: Hospitals](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Acesss_Hospitals_MinDistance.md) | Tract, Zip |
| Access to Pharmacies | Distance to nearest pharmacy | US Census, InfoGroup 2018 | Access04 / [Access: Pharmacies](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Access_Pharmacies_MinDistance.md) | Tract, Zip |
| Access to Mental Health Providers |  Distance to nearest mental health provider | US Census, SAMSHA 2020 |  Access05 / [Access: Mental Health Providers](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Access_MentalHealth_MinDistance.md) | Tract, Zip |
|Access to Substance Use Treatment Facilities| Distance to nearest substance use treatment facility| SAMHSA, SSATS 2021| Access06 / [Access: Substance Use Treatment](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Access_SubstanceUseTreatment.md)|Tract, Zip|
|Access to Opioid Treatment Programs| Distance to nearest Opioid treatment program| SAMHSA, SSATS 2021| Access 07 / [Access: Opioid Treatment Programs](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Access_OpioidUseTreatment.md)|Tract, Zip|

<br>

### Demographic Variables

| Variable Construct | Variable Proxy | Source | Metadata | Spatial Scale | 
|:------------------ | -------------- | ------ | -------- | ------------- | 
| Race & Ethnicity | Percentages of population defined by categories of race and ethnicity | ACS, 2018 5-year | DS01/ [Race & Ethnicity Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Race_Ethnicity_2018.md) | State, County, Tract, Zip |
| Age | Age group estimates and percentages of population | ACS, 2018 5-year | DS01 / [Age Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Age_2018.md) | State, County, Tract, Zip | 
| Population with a Disability | Percentage of population with a disability | ACS, 2018 5-year | DS01 / [Other Demographic Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Other_Demographic_2018.md) | State, County, Tract, Zip | 
| Educational Attainment | Population without a high school degree | ACS, 2018 5-year | DS01 / [Other Demographic Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Other_Demographic_2018.md) | State, County, Tract, Zip | 
| Social Determinants of Health (SDOH) | SDOH Neighborhood Typologies | Kolak et al, 2020 | DS02 / [SDOH Typology](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/SDOH_2014.md) | Tract | 
| Social Vulnerability Index (SVI) | SVI Rankings | CDC, 2018 | DS03 / [SVI](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/SVI_2018.md) | County, Tract, Zip | 
| Veteran Population | Population as defined by veteran status | ACS, 2017 5-year | DS04 / [Veteran Population Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/VetPop.md) | State, County, Tract, Zip |
| Group Quarter | Population living in group quarters | ACS, 2018 5-year | DS05 / [Group Quarter Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/GroupQuar.md) | State, County, Tract, Zip |
| Homeless Population | Population as defined by veteran status | HUD Point in Time Count, 2018  | DS06 / [Homeless Population Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/HomelessPop.md) | State, County, Tract, Zip |

<br>

### Economic Variables

| Variable Construct | Variable Proxy | Source | Metadata | Spatial Scale | 
|:------------------ | -------------- | ------ | -------- | ------------- | 
| Employment Trends | Percentages of population employed in High Risk of Injury Jobs, Educational Services, Health Care, Retail industries | ACS, 2018 5-year | EC01/ [Jobs by Industry](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Job_Categories_byIndustry_2018.md) | State, County, Tract, Zip | 
| Unemployment Rate | Unemployment rate | ACS, 2014-2018 | EC03/ [Economic Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Economic_2018.md)| State, County, Tract, Zip | 
| Poverty Rate | Percent classified as below poverty level, based on income | ACS, 2018 5-year | EC03/ [Economic Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Economic_2018.md) | State, County, Tract, Zip | 
| Per Capita Income | Per capita income in the past 12 months | ACS, 2018 5-year |  EC03/ [Economic Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Economic_2018.md) | State, County, Tract, Zip | 
| Foreclosure Rate | Mortgage foreclosure and severe delinquency rate | HUD, 2009 | EC04 / [Foreclosure Rate](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/ForeclosureRate.md) | State, County, Tract | 

<br>

### Built Environment Variables

| Variable Construct | Variable Proxy | Source | Metadata | Spatial Scale | 
|:------------------ | -------------- | ------ | -------- | ------------- | 
| Housing Occupancy Rate | Percent occupied units | ACS, 2018 5-year | BE01 / [Housing](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Housing_2018.md) | State, County, Tract, Zip | 
| Housing Vacancy Rate | Percent vacant units | ACS, 2018 5-year | BE01 / [Housing](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Housing_2018.md) | State, County, Tract, Zip | 
| Long Term Occupancy | Percentage of population living in current housing for 20+ years | ACS, 2018 5-year | BE01 / [Housing](/data_final/metadata/Housing_2018.md) | State, County, Tract, Zip |
| Mobile Homes | Percent of housing units classified as mobile homes | ACS, 2018 5-year | BE01 / [Housing](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Housing_2018.md) | State, County, Tract, Zip | 
| Rental Rates | Percent of housing units occupied by renters  | ACS, 2018 5-year | BE01 / [Housing](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Housing_2018.md) | State, County, Tract, Zip | 
| Housing Unit Density | Housing units per square mile | ACS, 2018 5-year | BE01 / [Housing](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Housing_2018.md) | State, County, Tract, Zip |
| Urban/Suburban/Rural Classification | Classification of areas as rural, urban or suburban | USDA-ERS | BE02 / [Rural-Urban Classifications](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/rural_urban_classifications) | County, Tract, Zip | 
| Alcohol Outlet Density | Alcohol outlets per square mile, alcohol outlets per capita | InfoGroup, 2018 | BE03 / [Alcohol Outlets](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/AlcoholOutlets_2018.md)  | State, County, Tract, Zip | 
| Hypersegregated Cities | US metropolitan areas where black residents experience hypersegregation | Massey et al, 2015 | BE04 / [Community Overlays](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Overlay.md) | County | 
| Southern Black Belt | US counties where 30% of the population identified as Black or African American | US Census, 2000 | BE04 / [Community Overlays](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Overlay.md) | County | 
| Native American Reservations | Percent area of total land in Native American Reservations | US Census, TIGER, 2018 | BE04 / [Community Overlays](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Overlay.md) | County | 
| Residential Segregation Indices | Three index measures of segregation: dissimilarity, interaction, isolation | ACS, 2018 5-year | BE05 / [Residential Segregation](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Residential_Seg_Indices.md) | County |

<br>

### COVID Variables
| Variable Construct | Variable Proxy | Source | Metadata | Spatial Scale | 
|:------------------ | -------------- | ------ | -------- | ------------- | 
| Essential Worker Jobs | Percentage of population employed in Essential Jobs as defined during the COVID-19 pandemic | ACS, 2014-2018 | EC02 / [Jobs by Occupation](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/Job_Categories_byOccupation_2018.md) | State, County, Tract, Zip | 
| Cumulative Case Count | Daily cumulative raw case count (01/21/20 - 03/03/2021) | The New York Times, 2021 | COVID01 / [COVID Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/COVID.md) | State, County | 
| Adjusted Case Count per 100K | Daily cumulative adjusted case count per 100K population (01/21/20 - 03/03/2021) | The New York Times, 2021 | COVID02 / [COVID Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/COVID.md) | State, County |
| 7-day Average Case Count | 7-day average case count (01/21/20 - 03/03/2021) | The New York Times, 2021 | COVID03 / [COVID Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/COVID.md) | State, County | 
| Historical 7-day Average Adjusted Case Count per 100K | 7-day average adjusted case count per 100K population (01/21/20 - 03/03/2021)| The New York Times, 2021 | COVID04 / [COVID Variables](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/data_final/metadata/COVID.md) | State, County | 

## Documentation
Please refer to the complete [Data Documentation](https://docs.google.com/document/d/18NPWpuUfFTrKll9_ERHzVDmpNCETTzwjJt_FsIvmSrc/edit?usp=sharing) for more information about individual datasets, variables, and data methods.  Contact [Susan Paykin](mailto:spaykin@uchicago.edu) with any questions. 

## Citation
Marynia Kolak, Qinyun Lin, Susan Paykin, Moksha Menghaney, & Angela Li. (2021, May 11). GeoDaCenter/opioid-policy-scan: *Opioid Environment Policy Scan Data Warehouse* (Version v0.1-beta). Zenodo. http://doi.org/10.5281/zenodo.4747876

## Team
The OEPS database was developed for the [Justice Community Opioid Innovation Network (JCOIN)](https://heal.nih.gov/research/research-to-practice/jcoin) by [Marynia Kolak](https://github.com/Makosak), [Qinyun Lin](https://github.com/linqinyu), [Susan Paykin](https://github.com/spaykin), Moksha Menghaney, and Angela Li of the [Healthy Regions and Policies Lab](https://voices.uchicago.edu/herop/) and [Center for Spatial Data Science](https://spatial.uchicago.edu/) at the University of Chicago. The University of Chicago serves as the JCOIN Methodology and Advanced Analytics Resource Center (MAARC), providing data infrastructure and statistical and analytic expertise to support individual JCOIN studies and cross-site data synchronization.

## Acknowledgements
This research was supported by the National Institute on Drug Abuse, National Institutes of Health, through the NIH HEAL Initiative under award number UG3DA123456. The contents of this publication are solely the responsibility of the authors and do not necessarily represent the official views of the NIH, the Initiative, or the participating sites.
