**Meta Data Name**: Nearest Distance for Substance Use Treatment   
**Date Added**: July 23, 2021  
**Author**: Rachel Vigil,  Wataru Morioka, Mahjabin Kabir Adrita  
**Date Last Modified:** August 13, 2025  
**Last Modified By:** Mahjabin Kabir Adrita

### Theme: 
Environment  

### Data Location: 
You can find the variables described in this document in the CSV files [here](../full_tables).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  
Note: Every variable can be found in the **Latest** files.

### Data Source(s) Description:  
Variables were obtained from the SAMHSA service locator. substance use treatment facilities are collected in SAMHSA's annual National Survey of Substance Abuse Treatment Services. The lists and locations of these facilities are based off of certification and data collection for treatment facilities by state abuse agencies for the Behavioral Health Services Information System. Also included in this set are treatment facilities that state substance abuse agencies, for a variety of reasons, do not fund, license, or certify which are found through periodic screening of alternative databases. Raw data can be found [here](https://findtreatment.samhsa.gov/locator), and more details about data collection can be found [here](https://www.samhsa.gov/data/data-we-collect/n-ssats-national-survey-substance-abuse-treatment-services).

### Description of Data Processing: 

#### Tract and Zip Code

##### Distance
Data was cleaned and prepared for analysis. Centroids were calculated for ZCTA and Census Tract geometries. For the nearest resource analysis, Euclidean distance* was calculated from the centroid of each tract/ZCTA to the nearest SUT location. 

##### Travel Time and Count Within Threshold
We calculated travel-network access metrics for the driving travel time to the nearest SUT service location and count of SUT services within a 30 minute driving threshold. The driving travel cost matrices were sourced from [Project OSRM](http://project-osrm.org/) and are available at the Tract or ZCTA scales for multiple transit modes via [this Box folder](https://uchicago.app.box.com/s/ae2mtsw7f5tb4rhciczufdxd0owc23as). This analysis was conducted in Python. The script is available in [code/Access Metrics - Health Resources](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20Health%20Resources).

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
| Distance to nearest SUT | SutMinDis | Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles | 2019, 2025 | Tract, Zip |
| Driving time to nearest SUT | SutTmDr | Driving time from tract/zip origin centroid to the nearest tract/zip SUT destination centroid, in minutes | 2019, 2025 | Tract, Zip |
| Count of SUTs | SutCntDr | Count of SUT services within a 30-minute driving threshold | 2019, 2025t | Tract, Zip |

#### County and State
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Count of tracts | TotTracts | Total number of tracts in county/state | 2019, 2025 | County, State |
| Count of tracts within 30-min driving range | SutpCtTmDr | Number of tracts with SUT within a 30-min driving range | 2019, 2025 | County, State |
| Average time drive to nearest SUT | SutpAvTmDr | Average driving time (minutes) across tracts in county/state to nearest SUT | 2019, 2025 | County, State |
| Percent of tracts within 30-min driving range | SutpTmDrP | Percent of tracts with SUT within a 30-min driving range | 2019, 2025 | County, State |

### Data Limitations:
*Euclidean distance or straight-line distance is a simple approximation of distance or travel time from an origin centroid to the nearest health center. It is not a precise calculation of real travel times or distances. The travel times are capped at a 90-minute threshold; any data exceeding this limit is left blank.
### Comments/Notes:
* All nearest distance calculations are in miles. 
* All nearest travel time calculations are in minutes.
* Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
* While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
* The zip code calculation was updated in 2025 to an average of overlapping tract-level metrics, rather than distance from the center of a zip code area. Because zip code areas are large, when compared to census tracts, distance from the geometric center was deemed less meaningful. A detailed notebook comparing the differences will be shared in 2026.
* During the crosswalk process, we used the total ratio from the HUD USPS Crosswalk Files. This ratio represents the proportion of total addresses in a given geographic unit (e.g., census tract) that fall within a corresponding target geographic unit (e.g., ZIP Code). The total ratio was used as a weighting factor to allocate counts and measures proportionally between geographies.
