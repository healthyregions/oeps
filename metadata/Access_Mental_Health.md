**Meta Data Name**: Access to Mental Health Providers  
**Date Added**: January 9, 2021  
**Author**: Susan Paykin, Wataru Morioka, Mahjabin Kabir Adrita  
**Date Last Modified**: August 13, 2025    
**Last Modified By**: Mahjabin Kabir Adrita  

### Theme: 
Environment  

### Data Location: 
You can find the variables described in this document in the CSV files [here](../full_tables).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  
Note: Every variable can be found in the **Latest** files.

### Data Source(s) Description:  
Mental health provider data was sourced from [Substance Abuse and Mental Health Services Administration (SAMSHA)](https://www.samhsa.gov/) through its [Treatment Services Locator Tool](https://findtreatment.samhsa.gov/locator). 

ZIP Code Tract Area (ZCTA) and Census Tract files were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html). 

### Description of Data Source Tables: 
The source SAMSHA mental health provider dataset includes provider name, location (address, city, state, zip, county, latitude and longitude), and contact information (website, phone number).

### Description of Data Processing: 
Data was scraped from the SAMSHA Treatment Locator tool, filtered for mental health providers, cleaned, and then converted to spatial data. 

#### Tract and Zip Code

##### Distance
Next, we conducted the nearest resource analysis using minimum Euclidean distance as a proxy variable for access. This analysis included calculating centroids for all census tracts and ZCTAs, identifying the nearest mental health (MH) provider to each centroid, and calculating the distance in miles. 

##### Travel Time and Count Within Threshold
We calculated travel-network access metrics for the driving travel time to the nearest mental health (MH) provider location and count of MH providers within a 30 minute driving threshold. We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. For *zip code tabulation areas*, overlapping tract-level measures were averaged, weighted by proportion of the overlapping tract, using the corresponding HUD tract-to-zip code crosswalks. 

Count of providers within a travel threshold (30 minutes and/or 60 minutes) were also calculated for three modes of transit: driving, walking, and biking at the tract level, with corresponding average of overlapping tracts at the ZCTA scale. 

This analysis was conducted in Python. The scripts are available in code/AccessMetrics - MOUDs. Some of the scripts are available in [code/AccessMetrics - MOUDs.](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20MOUD), with complete computational notebooks forthcoming in 2026.

#### County and State 
County and state-level variables include the **count** of Census tracts and the **percent** of Census tracts located within a 30 minute driving threshold of an FQHC, as well as the mean (average) driving time in minutes from Census tracts within the county or state. 

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

#### Tract and Zip Code
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Distance to nearest MH Provider | MhMinDis | Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles | 2019, 2025 | Tract, Zip |
| Driving time to nearest MH Provider | MhTmDr | Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes | 2019, 2025 | Tract, Zip |
| Count of MH Providers | MhCntDr | Count of MH providers within a 30-minute driving threshold | 2019, 2025 | Tract, Zip |

#### County and State
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Count of tracts | TotTracts | Total number of tracts in county/state | 2019, 2025 | County, State  
| Count of tracts within 30-min driving range | MhCtTmDr | Number of tracts with an MH provider within a 30-min driving range | 2019, 2025 | County, State |
| Average time drive to nearest MH provider | MhAvTmDr | Average driving time (minutes) across tracts in county/state to nearest MH provider | 2019, 2025 | County, State |
| Percent of tracts within 30-min driving range | MhTmDrP | Percent of tracts with an MH provider within a 30-min driving range | 2019, 2025 | County, State |

### Data Limitations:
*Euclidean or straight-line distance is a simple approximation of access or travel from an origin centroid to the nearest hospital. It is not a precise calculation of real travel times or distances. The travel times are capped at a 90-minute threshold; any data exceeding this limit is left blank. 

### Comments/Notes:
* All nearest distance calculations are in miles. 
* All nearest travel time calculations are in minutes.
* Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
* While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
* The zip code calculation was updated in 2025 to an average of overlapping tract-level metrics, rather than distance from the center of a zip code area. Because zip code areas are large, when compared to census tracts, distance from the geometric center was deemed less meaningful. A detailed notebook comparing the differences will be shared in 2026.
* During the crosswalk process, we used the total ratio from the HUD USPS Crosswalk Files. This ratio represents the proportion of total addresses in a given geographic unit (e.g., census tract) that fall within a corresponding target geographic unit (e.g., ZIP Code). The total ratio was used as a weighting factor to allocate counts and measures proportionally between geographies.
