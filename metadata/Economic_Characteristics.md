**Meta Data Name**: Economic Variables  
**Date Added**: October 22, 2020  
**Authors**: Marynia Kolak, Mahjabin Kabir Adrita, Wataru Morika, Susan Paykin, Moksha Menghaney  
**Date Last Modified**: August 26, 2025  
**Last Modified By**: Mahjabin Kabir Adrita

### Theme: 
Economic

### Data Location: 
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  

### Data Source(s) Description:  

Variables were obtained from the multiple periods of the [American Community Survey (ACS)](https://data.census.gov) at State, County, Tract and ZIP Code Tabulation Area (ZCTA) levels.  

Prior to 2014, data was extracted from the Decennial Census.

### Description of Data Source Tables:

**Table B19301**: Per capita income in the past 12 months (in years' inflation-adjusted dollars) <br>

**Table S1701:** Poverty status in the past 12 months

### Description of Data Processing: 

The following variables were included from **B19301**.

  * **Estimate; Per capita income in the past 12 months (in years' inflation-adjusted dollars)**. Per capita income is the mean income computed for every man, woman, and child in a particular group including those living in group quarters. It is derived by dividing the aggregate income of a particular group by the total population in that group. This measure is rounded to the nearest whole dollar. Note: Employment and unemployment estimates may vary from the official labor force data released by the Bureau of Labor Statistics because of differences in survey design and data collection. 
 
The following variables were included from **S1701**:
  * **Percent Estimate; Percent below poverty level**. The total number of people below the poverty level is the sum of people in families and the number of unrelated individuals with incomes in the last 12 months below the poverty threshold. Note: Poverty status was determined for all people except institutionalized people, people in military group quarters, people in college dormitories, and unrelated individuals under 15 years old. These groups were excluded from the numerator and denominator when calculating poverty rates.

For more on variable definitions, see [ACS 2018 Subject Definitions](https://www2.census.gov/programs-surveys/acs/tech_docs/subject_definitions/2018_ACSSubjectDefinitions.pdf) as our intial reference that we replicated in subsequent time periods. 
  
### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Poverty Rate | PovP | Number of individuals earning below the poverty income threshold as a percentage of the total population | 1980, 1990, 2000, 2010, 2018, 2023 | Tract, Zip, County, State |
| Median Income | MedInc | Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars) | 2010, 2018, 2023 | Tract, Zip, County, State |
| Per Capita Income | PciE | Mean income for individuals in the past 12 months (in 2018 inflation-adjusted dollars) | 2010, 2018, 2023 | Tract, Zip, County, State |
| Gini Coefficient | GiniCoeff | Income Inequality (Gini Coefficient) | 2010, 2019, 2023 | Tract, Zip, County, State |

### Data Limitations:

- The ACS does not gather information in the U.S. territories American Samoa, Guam, Northern Mariana Islands and U.S. Virgin Islands. It does include information for Puerto Rico & Washington, D.C.  
- Note that the Zip code scale data may only be available for more recent time periods due to changes in boundaries.

### Comments/Notes:
**Note on missing data:** Missing and/or unavailable data are coded as blank/empty cells or _NA_.
