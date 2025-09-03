**Meta Data Name**: Race and Ethnicity Variables  
**Date Added**: July 8, 2021  
**Author**: Moksha Menghaney, Susan Paykin, Wataru Morioka, Mahjabin Kabir Adrita  
**Date Last Modified**: May 14, 2025  
**Last Modified By**: Wataru Morioka, Mahjabin Kabir Adrita  

### Theme: 
Social

### Data Location: 
You can find the variables described in this document in the CSV files [here](../oeps/data/tables).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in county-2000.csv.  

### Data Source(s) Description:  
Variables were obtained from the 2018 5-year average American Community Survey (ACS), table B02001, B03002, at State, County, Tract and ZIP Code Tabulation Area (ZCTA) level. Raw data and more details can be found at https://data.census.gov.

Historical data from 1980, 1990, and 2000 were obtained from IPUMS NHGIS data tables N7, NP9, NT7, NT8, NP007A, and NP008A which were themselves sourced from the 1980, 1990, and 2000 Decennial Censuses. 


### Description of Data Source Tables:
**Table B02001** : Provides breakdown by Race of the total population. (ACS) <br>
**Table B03002** : Hispanic or Latino origin by race table, provides ethnicity breakdown of the total population. (ACS) <br>
**Table N7**: Provides breakdown by Race of the total population in 1980. (IPUMS NHGIS) <br>
**Table NT8**: Provides breakdown by Hispanic or Latino origin of the total population in 1980. (IPUMS NHGIS) <br> 
**Table NP7**: Provides breakdown by Race of the total population in 1990. (IPUMS NHGIS) <br>
**Table NP9**: Provides breakdown by Hispanic or Latino origin of the total population in 1990. (IPUMS NHGIS) <br> 
**Table NP004A**: Provides breakdown by Hispanic or Latino origin of the total population in 2000. (IPUMS NHGIS) <br>
**Table NP008A**: Proivdes breakdown by Race of the total population in 2000. (IPUMS NHGIS) <br>

### Description of Data Processing: 

Percentage for each racial/ethnic group was calculated as: *estimate for the group / total population*, e.g.
  -  *% White = White alone / Total population* 
  -  *% Other  = 1 - (% White alone + % Black alone + % American Indian alone + % Asian alone + % Native Hawaiian alone)*

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable              | Variable ID in .csv | Description                                                                                            | Years Available | Spatial Scale |
|:----------------------|:--------------------|:-------------------------------------------------------------------------------------------------------|:----------------|:--------------|
| Count White           | WhiteE              | Count persons with race identified as white alone                                                      | 1980, 1990, 2000, 2010, 2018, 2023| Tract, Zip*, County, State |
| % White               | WhiteP              | Percentage of population with race identified as white alone                                           | 1980, 1990, 2000, 2010, 2018, 2020, 2023| Tract, Zip*, County, State |
| Count Black           | BlackE              | Count persons with race identified as Black or African American alone                                  | 1980, 1990, 2000, 2010, 2018, 2023| Tract, Zip*, County, State |
| % Black               | BlackP              | Percentage of population with race identified as Black or African American alone                       | 1980, 1990, 2000, 2010, 2018, 2020, 2023| Tract, Zip*, County, State |
| Count Hispanic        | HispE               | Count persons with ethnicity identified as of Hispanic or Latinx origin                                | 1980, 1990, 2000, 2010, 2018, 2023| Tract, Zip*, County, State |
| % Hispanic            | HispP               | Percentage of population with ethnicity identified as of Hispanic or Latinx origin                     | 1980, 1990, 2000, 2010, 2018, 2020, 2023| Tract, Zip*, County, State |
| Count American Indian | AmIndE              | Count persons with race identified as Native American or Alaska Native alone                           | 1980, 1990, 2000, 2010, 2018, 2023| Tract, Zip*, County, State |
| % American Indian     | AmIndP              | Percentage of population with race identified as Native American or Alaska Native alone                | 1980, 1990, 2000, 2010, 2018, 2020, 2023| Tract, Zip*, County, State |
| Count Asian           | AsianE              | Count persons with race identified as Asian alone                                                      | 1980, 1990, 2000, 2010, 2018, 2020, 2023| Tract, Zip*, County, State |
| % Asian               | AsianP              | Percentage of population with race identified as Asian alone                                           | 1980, 1990, 2000, 2010, 2018, 2020, 2023| Tract, Zip*, County, State |
| Count Native Hawaiian | PacIsE              | Count persons with race identified as Native Hawaiian and Other Pacific Islander alone                 | 1980, 1990, 2000, 2010, 2018, 2023| Tract, Zip*, County, State |
| % Native Hawaiian     | PacIsP              | Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone      | 1980, 1990, 2000, 2010, 2018, 2020, 2023| Tract, Zip*, County, State |
| Count Other           | OtherE              | Count persons with race not mentioned in any of the options above (includes two race or more races)    | 1980, 1990, 2000, 2010, 2018, 2023| Tract, Zip*, County, State |
| % Other               | OtherP              | Percentage of Population with race not mentioned in any of the options above (includes two race or more races) | 1980, 1990, 2000, 2010, 2018, 2020 | Tract, Zip*, County, State |
| Count 2+ races        | TwoRaceE            | Count persons identifying as two or more races                                                         | 1980, 1990, 2000, 2010, 2018, 2018, 2023 | Tract, ZCTA, County    |
| % 2+ races            | TwoRaceP            | Percent of population identifying as two or more races                                                 | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, ZCTA, County    |


### Data Limitations:  
- Note that the Zip code scale data is only available for the "latest" file.
- County shapes changed between 2000 and 2010, so county level data from 1980, 1990, and 2000 were interpolated onto 2018 geometries. This process was done using population weighted interpolation, a method which takes data on a given geometry and attempts to predict its distribution on a second geometry through the usage of higher-resolution population data. For 1980, this higher-resolution population data was at the county subdivision level, but for 1990 and 2000 it was at the tract level.
- Tract data predating 2010 were crosswalked to 2010 geometries through files provided by the Longitudinal Tract Data Base (LTDB). For more information on the LTDB data, see their website [here](https://s4.ad.brown.edu/projects/diversity/Researcher/Bridging.htm).


### Comments/Notes:
**Note on missing data:** Missing and/or unavailable data are coded as blank or _NA_.
