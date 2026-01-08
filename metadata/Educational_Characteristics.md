**Meta Data Name:** Educational Attainment Variables  
**Date Added:** August 30th, 2025    
**Authors:** Ashlynn Wimer, Mandela Gadri, Mahjabin Kabir Adrita   
**Date Last Modified:** August 30th, 2025    
**Last Modified By:** Ashlynn Wimer

### Data Source(s) Description:  
Variables were obtained from the *American Community Survey (ACS)* 5-Year Estimates, using table B15003 and related education summary tables for the years 2010, 2018, 2020 and 2023. Historical data from 1980, 1990, and 2000 were obtained from IPUMS NHGIS data tables NT7, NP37, NP037C which were themselves sourced from the 1980, 1990, and 2000 Decennial Censuses, respectively. 

### Description of Data Source Tables:  
**Table B15003:**: Educational Attainment for the Population 25 Years and Over (ACS)
**Table B06007**: Place of Birth by Language Spoken at Home and Ability to Speak English in the United States (ACS) 
**Table NT7**: Educational Attainment in 1980 (IPUMS NHGIS)
**Table NP37**: Educational Attainment in 1990 (IPUMS NHGIS)
**Table NP037C**: Educational Attainment in 2000 (IPUMS NHGIS)

This table includes the number and percent of people aged 25 years and older who have completed various levels of education, from no formal education to graduate or professional degrees.

### Description of Data Processing:  
- Percentages represent the proportion of the population 25 years and over with a specified level of education.  
- Some variables are reported as counts (e.g., total with high school or higher).  
- Estimates are rounded to two decimal places where applicable.  
- Calculations are based on total educational attainment population, excluding those under 25.

### Data Limitations:  
- Only individuals aged 25 years or older are included in these statistics.  
- Percentages may not sum to 100% due to rounding or individuals falling into excluded categories (e.g., GED vs diploma).  
- ZCTA data may be unavailable or unstable for very small populations, and is often unavailable pre-2018.  
- County shapes changed between 2000 and 2010, so county level data from 1980, 1990, and 2000 were interpolated onto 2018 geometries. This process was done using population weighted interpolation, a method which takes data on a given geometry and attempts to predict its distribution on a second geometry through the usage of higher-resolution population data. For 1980, this higher-resolution population data was at the county subdivision level, but for 1990 and 2000 it was at the tract level.
- Tract data predating 2010 were crosswalked to 2010 geometries through files provided by the Longitudinal Tract Data Base (LTDB). For more information on the LTDB data, see their website [here](https://s4.ad.brown.edu/projects/diversity/Researcher/Bridging.htm).

### Comments/Notes:  
See the [ACS Subject Definitions](https://www.census.gov/programs-surveys/acs/technical-documentation/code-lists.html) for more information on education variable definitions and data processing methodology.
**Note on missing data:** Missing and/or unavailable data are coded as blank or _NA_.