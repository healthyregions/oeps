**Meta Data Name**: Urbanicity
**Date Added**: March 20, 2020
**Author**: Wataru Morioka, Moksha Menghaney, Susan Paykin
**Date Last Modified**: January 3, 2024
**Last Modified By**: Wataru Morioka

### Theme: 
Environment

### Data Location: 
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions/download).

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  
Note: Every variable can be found in the **Latest** files.

### Data Source(s) Description:

#### Counties

Percentage of rural and urban population is sourced from the Census Bureau. Raw data and more details can be found [here](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html).

#### Census Tracts & Zipcodes

Tract and ZCTA level classifications were calculated using the [Rural-Urban Commuting Area Codes (RUCA codes)](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes.aspx). These codes classify U.S. census tracts using measures of population density, urbanization, and daily commuting. A second dataset then applies the 2010 RUCA classifications to ZIP code areas by transferring RUCA values from the census tracts that comprise them.

### Description of Data Source Tables:

#### Counties

After each decennial census, the bureau identifies Urban Areas under two categories :
* Urbanized Areas (UAs) of 50,000 or more people;
* Urban Clusters (UCs) of at least 2,500 and less than 50,000 people.

All other areas are classified as Rural. These classifications are done at a census block/tract level and are primarily based on population density and land use. 
Using these classifications, for each county, the bureau calculates a percent rurality measure which is the percentage of population living in non-urban areas. We source this variable. More details on methodology can be found [here](https://www2.census.gov/geo/pdfs/reference/ua/Defining_Rural.pdf).

#### Census Tracts & Zipcodes

For each census tract, the USDA calculates 10 primary and 21 secondary codes. Tract-to-tract commuting patterns are utilized for calculation of these codes. Primary codes use the largest share commuting flow to classify tracts. 

* Codes 1, 4 and 7 are Core Codes, i.e., these identify the tract equivalents for cores of Metropolitan, Micropolitan and Small Towns respectively. 

* Codes 2, 5 and 8 are High Commuting Codes, i.e., these identify the tract equivalents for communities with primary flows to Metropolitan, Mitropolitan and Small Towns cores respectively. The primary flow accounts for more than 30% of the communities total commuting flow.

* Codes 3, 6 and 9 are Low Commuting Codes, i.e., these identify the tract equivalents for communities with primary flows to Metropolitan, Mitropolitan and Small Towns respectively, but these flows account for less than 30% of the communities total commute. Please note, this flow is still the largest commuting flow, but it is less than 30%. 

Secondary codes utilize the second largest share of commuting patterns to further classify census tracts. Exact definitons can be found [here](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/documentation/).


### Description of Data Processing:

#### Counties

For each county, from the census data, the percentage of population living in non-urban areas is identified as percentage rurality.

For each county, the percentage of tracts classified as urban/suburban/rural, using the RUCA code definitions were calculated. Details on the classification methodology can be found [here](Policy_Scan/data_final/metadata/Rural_Urban_Classification_T_Z.md).

#### Census Tracts & Zipcodes

Classified as:

* Urban, if their RUCA2 codes were 1.0 and 1.1 
* Suburban, if their RUCA2 codes were 2.0, 2.1, 4.0, and 4.1 
* All other RUCA2 codes were classified as Rural.

  
### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| % Urban | RcaUrbanP | Percent census tracts in the county classified as Urban using RUCA codes | 2018 | County |
| % Suburban | RcaSubrbP | Percent census tracts in the county classified as Suburban using RUCA codes | 2018 | County |
| % Rural  | RcaRuralP | Percent census tracts in the county classified as Rural using RUCA codes | 2018 | County |
| CensusFlags | CenFlags | Three different values indicating three things: [1] - Revised count, so urban and rural components will not add to total. [2] - Geography name and FIPS code were changed since 2010. Shannon County, Sotuh Dakota name changed to Oglala Lakota County, new FIPS 46102. Wade Hampton Census Area, Alaska, name changed to Kusilvak CEnsus Area, nwe FIPS 02158. [3] - Bedford City, Virginia, was consolidated with Bedford County, Virginia (FIPS 51019) since 2010. | 2010 | County |
| RUCA Codes | Ruca1 | Primary RUCA Code | 2010 | Tract, Zip |
| RUCA Codes | Ruca2 | Secondary RUCA Code | 2010 | Tract, Zip |
| Classification | Rurality | Urban/Suburban/Rural | 2010 | Tract, Zip |

### Data Limitations:
n/a

### Comments/Notes:
The datasets come from two different sources. As a result, there might have some gaps or mismatches in the rurality categorization. Furthermore, for Census rurality, there are additional notes included for certain counties, e.g. changes in FIPS codes. These can be found under the `note` column.
