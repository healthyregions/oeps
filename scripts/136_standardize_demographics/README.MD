### author: Ashlynn Wimer
### date: 8/31/2025
### contact me at: awimer(at)g.harvard.edu (or, on Slack!)

This is the replication materials for the code used to resolve issues #136, #137, #138 on the healthyregions/oeps repository. In more words, these materials aimed to standardize race, age, ethnicity, and education variables at the county, state, and tract scale for the years 1980, 1990, 2000, 2010, 2018, 2020, and 2023.

## Start by getting data archive from S3

Data files used in these scripts have been zipped and uploaded to S3. Begin by downloading this zip file:

https://herop-oeps.s3.us-east-2.amazonaws.com/archive/136_standardize_demographics_data.zip

and then extract it into this directory. It has two folders: `temp_data` and `exported`, which are described below.

## Rundown of the files present:
- `temp_data` contains source data downloaded from IPUMS NHGIS, seperated by year, a file called `shapes`, and a set of tract crosswalk files. Due to GitHub file size limits.
  - Due to file size storage limits on GitHub, `shapes` is empty. This isn't an issue if one is attempting to replicate the data pipelines for data after 2010, but it will cause issues for older data. If you _are_ grabbing older data, you need the following files from NGHIS: the 1992 Tiger/LINE version of the 1980 US County Subdivisions boundaries, and the 2008 Tiger/LINE version of the 1980, 1990, and 2000 US County and Tract shapefiles. (Alternatively, reach out to the author of this notebook and tell her to rerun her 38th NHGIS query).
- `exported` contains dat exports retrieved using the scripts.
- `get_demographic_acs.R` was used to retrieve ACS data for 2018 and 2023.
- `get_demographic_dec.R` was used to retrieve the data for 2010, and is based on a file already present in the repository. Weirdly, it doesn't run for 2020 (see limitations below, or the PR).
- `get_standardized_county_demos.R` uses data from `temp_data` and `temp_data/shapes` to create datasets at the county level for 1980, 1990, and 2000. This file runs a lot of population weighted interpolation, so it both takes forever to run and needs the relevant tracts (1990 and 2000) or county subdivisions (1980) to run.
- `get_standardized_tract_demos.R` uses data from `temp_data` and `temp_data/shapes` to create datasets at the tract level for 1980, 1990, and 2000. This file crosswalks, so it needs each of the `crosswalk_[year]_2010.csv` files, and takes forever to run. 
- `get_standardized_tract_demos.R` uses data from `temp_data` to create state level datasets for 1980, 1990, and 2000. This file does not take forever to run (yippee!).
- `add_data_to_registry.py` is a file used to attach the new data to the registry. Running it is a bit finnicky: 
- - First, it needs to be placed in `backend` to work due to it's usage of the `Registry()` class 
- - If -- in the process of running -- it ever completely removes a variable from all data tables (e.g. for the deletion of deprecated variables), that variable's registry entry must be deleted before the script can be used again (due to how the `json` package in Python works).
- - Lastly, if any of the incoming variables are not already present in the registry, this file will not add them to the data tables. So, create your registry jsons first!
- `validate_data.ipynb` is a _really_ quick and dirty EDA script I threw together to idiot check incoming data.

## Limitations and Technical Notes

- Currently, **2020 data is not included in this revision**. Unfortunately, I was unable to figure out which census tables these variables originated in before the summer ended, and didn't pull the trigger on just redoing the 2020 data early enough to do so. As a parallel result, `get_demographic_dec.R` doesn't work on 2020. 
- County data has a population weighted interpolation using tract level data for 1990 and 2000, but county subidivison data in 1980.
- Tract data is interpolated using the LTDB.


This _should_ be enough to work with any of the files in here, but feel free to reach out to me if any additional information is needed!