**Meta Data Name**: Demographic and Age Variables  
**Date Added**: October 16, 2020  
**Author**: Ashlynn Wimer, Mahjabin Kabir Adrita, Wataru Morioka, Susan Paykin, Moksha Menghaney
**Date Last Modified**: August 28, 2025      
**Last Modified By**: Ashlynn Wimer

### Data Source(s) Description:  
Variables were obtained from multiple sources, dependent upon variable year. Variables for 2018 and 2023 were obtained from the American Community Survey (ACS), tables S0101, B23001, and B01001 at State, County, Tract and ZIP Code Tabulation Area level. For 2010, variables were obtained from the Decennial Census groups P03, P11, P13, and P14. For 2020, variables were obtained from the Decennial Census tables DP05 and DP02. Raw data and more details can be found at https://data.census.gov.

Historical data from 1980, 1990, and 2000 were obtained from IPUMS NHGIS data tables NP1, NP11, C7L, NT10A, NP012B, which were themselves sourced from the 1980, 1990, and 2000 Decennial Censuses. 

### Description of Data Source Tables:

**S0101** : Age & Sex Characteristics with Some Prebuilt Categories
**B23001**: Sex By Age By Employment Status for the Population 16 Years and Older
**B01001**: Sex by Age
**P3**: Race
**P11**: Hispanic Origin
**P12**: Sex by Age

### Description of Data Processing: 

Variables were retrieved from the above data tables and used to calculate all below gender and age categories. Variables were converted to percentages using Total Population as a base. When aggregating multiple categories, the largest pre-built categories from the Census were used to reduce measurement error. Historical tract data were crosswalked to modern tracts using Longitudinal Tract Data Base (LTDB) crosswalks, while historical county data were interpolated to modern tracts using population weighted interpolation. See Data Limitations for more information, or the relevant files [here](https://github.com/healthyregions/oeps/tree/main/scripts/136_standardize_demographics/)

### Data Limitations:
- ZCTA data is only available for 2018, 2020, and 2023.
- County shapes changed between 2000 and 2010, so county level data from 1980, 1990, and 2000 were interpolated onto 2018 geometries. This process was done using population weighted interpolation, a method which takes data on a given geometry and attempts to predict its distribution on a second geometry through the usage of higher-resolution population data. For 1980, this higher-resolution population data was at the county subdivision level, but for 1990 and 2000 it was at the tract level.
- Tract data predating 2010 were crosswalked to 2010 geometries through files provided by the Longitudinal Tract Data Base (LTDB). For more information on the LTDB data, see their website [here](https://s4.ad.brown.edu/projects/diversity/Researcher/Bridging.htm).


### Comments/Notes:
**Note on missing data:** Missing and/or unavailable data are coded as blank or _NA_.
Specific age ranges (e.g. 25 to 34) can be retrieved from the Census API directly, or from IPUMS NHGIS. If interacting with the Census API in R, we recommend using [tidycensus](https://walker-data.com/tidycensus/articles/basic-usage.html). 
