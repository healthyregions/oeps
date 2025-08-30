**Meta Data Name:** Educational Attainment Variables  
**Date Added:** August 30th, 2025    
**Authors:** Ashlynn Wimer, Mandela Gadri, Mahjabin Kabir Adrita   
**Date Last Modified:** August 30th, 2025    
**Last Modified By:** Ashlynn Wimer


### Theme:  
Education – Levels of Educational Attainment

### Data Location:  
<<<<<<< HEAD
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).
=======
You can find the variables described in this document in the CSV files [here](../oeps/data/tables).
>>>>>>> be17f8c1e199def7d04cc2ed21d0e8c31eae9d77

CSV files are organized by year and spatial scale. For example, county-level variables from 2020 will be found in `county-2020.csv`.  

### Data Source(s) Description:  
Variables were obtained from the *American Community Survey (ACS)* 5-Year Estimates, using table B15003 and related education summary tables for the years 2010, 2018, 2020 and 2023. Historical data from 1980, 1990, and 2000 were obtained from IPUMS NHGIS data tables NT7, NP37, NP037C which were themselves sourced from the 1980, 1990, and 2000 Decennial Censuses, respectively. 

### Description of Data Source Tables:  
**Table B15003:**: Educational Attainment for the Population 25 Years and Over (ACS)
**Table NT7**: Educational Attainment in 1980 (IPUMS NHGIS)
**Table NP37**: Educational Attainment in 1990 (IPUMS NHGIS)
**Table NP037C**: Educational Attainment in 2000 (IPUMS NHGIS)

This table includes the number and percent of people aged 25 years and older who have completed various levels of education, from no formal education to graduate or professional degrees.

### Description of Data Processing:  
- Percentages represent the proportion of the population 25 years and over with a specified level of education.  
- Some variables are reported as counts (e.g., total with high school or higher).  
- Estimates are rounded to two decimal places where applicable.  
- Calculations are based on total educational attainment population, excluding those under 25.

### Key Variable and Definitions:

| Variable                           | Variable ID in .csv | Description                                                       | Years Available | Spatial Scale        |
|------------------------------------|---------------------|-------------------------------------------------------------------|------------------|-----------------------|
| Bachelor's degree or higher        | BachelorsP          | Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education                    | 2020, 2023       | Tract, County, ZCTA   |
| High school graduate               | EduHsP              | Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)                    | 2020, 2023       | Tract, County, ZCTA   |
| Less than 9th grade               | Eduless9P           | Percent with less than a 9th grade education                      | 2020, 2023       | County only           |
| No high school diploma             | EduNoHsP            | Percent population aged 25 years and over with less than a high school diploma                            | 2020, 2023       | Tract, County, ZCTA   |
| Graduate or professional degree    | GradSclP            | Percent population aged 25 years and over with a graduate or professional degree                      | 2020, 2023       | Tract, County, ZCTA   |
| Some college, no degree            | SomeCollegeP        | Percent population 25 years and over with some college, but no degree                 | 2020, 2023       | Tract, County, ZCTA   |
| English Proficiency (18+) | engProf18   | Proportion of the population aged 5+ who speak a language other than English at home but are proficient in English             | 2020, 2023       | Tract, County, ZCTA     |

### Data Limitations:  
- Only individuals aged 25 years or older are included in these statistics.  
- Percentages may not sum to 100% due to rounding or individuals falling into excluded categories (e.g., GED vs diploma).  
- ZCTA data may be unavailable or unstable for very small populations.  
- County-level data for some variables (e.g., Eduless9P) may not exist at tract or ZCTA scales.
- County shapes changed between 2000 and 2010, so county level data from 1980, 1990, and 2000 were interpolated onto 2018 geometries. This process was done using population weighted interpolation, a method which takes data on a given geometry and attempts to predict its distribution on a second geometry through the usage of higher-resolution population data. For 1980, this higher-resolution population data was at the county subdivision level, but for 1990 and 2000 it was at the tract level.
- Tract data predating 2010 were crosswalked to 2010 geometries through files provided by the Longitudinal Tract Data Base (LTDB). For more information on the LTDB data, see their website [here](https://s4.ad.brown.edu/projects/diversity/Researcher/Bridging.htm).

### Comments/Notes:  
See the [ACS Subject Definitions](https://www.census.gov/programs-surveys/acs/technical-documentation/code-lists.html) for more information on education variable definitions and data processing methodology.