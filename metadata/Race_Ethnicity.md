**Meta Data Name**: Race and Ethnicity Variables  
**Date Added**: July 8, 2021  
**Author**: Moksha Menghaney, Susan Paykin, Wataru Morioka, Mahjabin Kabir Adrita  
**Date Last Modified**: May 14, 2025  
**Last Modified By**: Wataru Morioka, Mahjabin Kabir Adrita  

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

### Data Limitations:  
- Note that the Zip code scale data is only available for the "latest" file.
- County shapes changed between 2000 and 2010, so county level data from 1980, 1990, and 2000 were interpolated onto 2018 geometries. This process was done using population weighted interpolation, a method which takes data on a given geometry and attempts to predict its distribution on a second geometry through the usage of higher-resolution population data. For 1980, this higher-resolution population data was at the county subdivision level, but for 1990 and 2000 it was at the tract level.
- Tract data predating 2010 were crosswalked to 2010 geometries through files provided by the Longitudinal Tract Data Base (LTDB). For more information on the LTDB data, see their website [here](https://s4.ad.brown.edu/projects/diversity/Researcher/Bridging.htm).


### Comments/Notes:
**Note on missing data:** Missing and/or unavailable data are coded as blank or _NA_.
