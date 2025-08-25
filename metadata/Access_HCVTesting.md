**Meta Data Name**: Access to HCV Testing  
**Date Added**: June 23, 2025  
**Author**: Mahjabin Kabir Adrita  
**Date Last Modified**: August 13, 2025  
**Last Modified By**: Mahjabin Kabir Adrita  

### Theme:  
Environment  

### Data Location:  
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in `C_2000.csv`.  

### Data Source(s) Description:  
HCV Testing provider data was sourced from the [Substance Abuse and Mental Health Services Administration (SAMHSA)](https://www.samhsa.gov/) via its [Treatment Services Locator Tool](https://findtreatment.samhsa.gov/locator).  

ZIP Code Tract Area (ZCTA) and Census Tract shapefiles were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html).

### Description of Data Source Tables:  
The SAMHSA HCV Testing dataset includes:  
- Provider name  
- Location (address, city, state, ZIP, county, latitude, longitude)  
- Contact information (website, phone number)  

### Description of Data Processing:  

#### Tract and Zip Code  

##### Distance  
Nearest resource analysis was conducted using minimum Euclidean distance as a proxy for access. This involved:  
- Calculating centroids for all census tracts and ZCTAs  
- Identifying the nearest HCV testing provider to each centroid  
- Calculating the straight-line distance in miles  

##### Travel Time and Count Within Threshold  
Driving-network access metrics were computed, including:  
- Travel time to the nearest HCV testing provider  
- Count of HCV testing providers within a 30-minute driving threshold  

We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. For *zip code tabulation areas*, overlapping tract-level measures were averaged, weighted by proportion of the overlapping tract, using the corresponding HUD tract-to-zip code crosswalks. 

This analysis was conducted in Python. The scripts are available in code/AccessMetrics - MOUDs. Some of the scripts are available in [code/AccessMetrics - MOUDs.](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20MOUD), with complete computational notebooks forthcoming in 2026.

#### County and State  
County and state-level variables include:  
- **Count** of Census tracts  
- **Percent** of Census tracts located within a 30-minute driving threshold  
- **Mean driving time** from Census tracts within the county/state  

### Key Variable and Definitions:

- **Variable** – Title of the variable  
- **Variable ID** – Exact name used in the dataset  
- **Description** – Short explanation of what the variable measures  
- **Years Available** – Data availability by year  
- **Spatial Scale** – Level of geography for the variable  

#### Tract and Zip Code

| Variable                          | Variable ID in .csv | Description | Years Available | Spatial Scale |
|----------------------------------|----------------------|-----------------------------------------------------------------------------|------------------|----------------|
| Distance to nearest HCV Provider  | HcvMinDis | Euclidean distance* from tract/zip centroid to nearest HCV testing provider (miles) | 2025 | Tract, Zip     |
| Driving time to nearest HCV Provider | HcvTmDr | Driving time from origin to nearest HCV testing provider (minutes)                  | 2025 | Tract, Zip     |
| Count of HCV Providers            | HcvCntDr | Number of HCV testing providers within a 30-minute drive                             | 2025 | Tract, Zip     |

#### County and State

| Variable                                   | Variable ID in .csv | Description                                                                     | Years Available | Spatial Scale |
|-------------------------------------------|----------------------|----------------------------------------------------------------------------------|------------------|----------------|
| Count of tracts                           | TotTracts | Total number of Census tracts in county/state                                   | 2025 | County, State  |
| Count of tracts within 30-min driving range | HcvCtTmDr | Number of tracts with an HCV testing provider within a 30-minute driving range           | 2025 | County, State  |
| Average time drive to nearest HCV testing provider | HcvAvTmDr | Mean driving time (minutes) from tracts to nearest HCV testing provider                  | 2025 | County, State  |
| Percent of tracts within 30-min driving range | HcvTmDrP | Percent of tracts within 30-minute drive to an HCV testing provider                      | 2025 | County, State  |

### Data Limitations:  
*Euclidean or straight-line distance is a basic proxy for access. It does not account for real-world travel constraints.*  
The travel times are capped at a 90-minute threshold. Any data exceeding this limit is left blank.

### Comments/Notes:  
* All nearest distance calculations are in miles. 
* All nearest travel time calculations are in minutes.
* Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
* While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
* The zip code calculation was updated in 2025 to an average of overlapping tract-level metrics, rather than distance from the center of a zip code area. Because zip code areas are large, when compared to census tracts, distance from the geometric center was deemed less meaningful. A detailed notebook comparing the differences will be shared in 2026.
* During the crosswalk process, we used the total ratio from the HUD USPS Crosswalk Files. This ratio represents the proportion of total addresses in a given geographic unit (e.g., census tract) that fall within a corresponding target geographic unit (e.g., ZIP Code). The total ratio was used as a weighting factor to allocate counts and measures proportionally between geographies.
