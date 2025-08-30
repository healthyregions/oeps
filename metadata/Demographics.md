**Meta Data Name**: Demographic and Age Variables  
**Date Added**: October 16, 2020  
**Author**: Ashlynn Wimer, Mahjabin Kabir Adrita, Wataru Morioka, Susan Paykin, Moksha Menghaney
**Date Last Modified**: August 28, 2025      
**Last Modified By**: Ashlynn Wimer

### Theme: 
Social 

### Data Location: 
You can find the variables described in this document in the CSV files [here](../oeps/data/tables).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in `county-2000.csv`.  

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

Variables were retrieved from the above data tables and used to calculate all below gender and age categories. Variables were converted to percentages using Total Population as a base. When aggregating multiple categories, the largest pre-built categories from the Census were used to reduce measurement error. The script used to generate these values can be found [here]().

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable                        | Variable ID in .csv | Description                                                       | Years Available                          | Spatial Scale                  |
|:--------------------------------|:------------------- |:------------------------------------------------------------------|:-----------------------------------------|:-------------------------------|
| Total population                | TotPop              | Total population                                                  | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, Zip*, County, State     |
| Total population over age 18    | AgeOv18             | Total population over age 18                                      | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, Zip*, County, State     |
| Total population over age 65    | AgeOv65             | Total population over age 65                                      | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, Zip*, County, State     |
| Total population over age 16    | Ov16                | Total population over age 16                                      | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, ZCTA, County            |
| Percent over age 16             | Ov16P               | Percent of population over age 16                                 | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, ZCTA, County            |
| Total population over age 18    | Ov18                | Total population age 16                                           | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, ZCTA, County            |
| Percent over age 18             | Ov18P               | Percent of population over age 18                                 | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, ZCTA, County            |
| Total population over age 21    | Ov21                | Total population age 21                                           | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, ZCTA, County            |
| Percent over age 21             | Ov21P               | Percent of population over age 21                                 | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, ZCTA, County            |
| Percent over age 62             | Ov62P               | Percent of population over age 62                                 | 2020, 2023                               | Tract, ZCTA, County            |
| Percent under age 18            | Und18P              | Percent of population under age 18                                | 2020, 2023                               | Tract, ZCTA, County            |
| Percent under age 5             | Und5P               | Percent of population under age 5                                 | 2020, 2023                               | Tract, ZCTA, County            |
| Percent  under 45               | Und45P              | Percentage of population below 45 years of age                    | 1980, 1990, 2000, 2010, 2020, 2023       | Tract, Zip*, County, State     |
| Total population over age 65    | Ov65P               | Total population over age 65                                      | 1980, 1990, 2000, 2010, 2020, 2023       | Tract, Zip*, County, State     |
| Percent  over 65                | Ov65P               | Percentage of population over 65                                  | 1980, 1990, 2000, 2010, 2020, 2023       | Tract, Zip*, County, State     |
| Percent female                  | FemP                | Percent of population that is female                              | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, ZCTA, County            |
| Percent male                    | MaleP               | Percent of population identifying that is male                    | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, ZCTA, County            |
| Percent  Children               | ChildrenP           | Percentage of population under age 18                             | 1980, 1990, 2000, 2010, 2020, 2023       | Tract, Zip*, County, State     |
| Median age                      | MedAge              | Median age of the population                                      | 2020, 2023                               | Tract, ZCTA, County            |
| Sex Ratio (All Ages)            | SRatio              | Sex ratio for the total population (males per 100 females)        | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, County, ZCTA            |
| Sex Ratio (18+)                 | SRatio18            | Sex ratio among adults aged 18 and older (males per 100 females)  | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, County, ZCTA            |
| Sex Ratio (65+)                 | SRatio65            | Sex ratio among seniors aged 65 and older (males per 100 females) | 1980, 1990, 2000, 2010, 2018, 2020, 2023 | Tract, County, ZCTA            |





### Data Limitations:
This data represents estimates as of the ACS 2018 5-year average.  
*Note that the Zip code scale data is only available for the "latest" file.

### Comments/Notes:
**Note on missing data:** Missing and/or unavailable data are coded as -999. 
