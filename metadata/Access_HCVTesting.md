**Meta Data Name**: Access to HCV Testing  
**Date Added**: June 23, 2025  
**Author**: Mahjabin Kabir Adrita  
**Date Last Modified**: June 23, 2025  
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

Travel cost matrices were sourced from [Project OSRM](http://project-osrm.org/) and are available for multiple transit modes via [this Box folder](https://uchicago.app.box.com/s/ae2mtsw7f5tb4rhciczufdxd0owc23as).  

Analysis was conducted in Python. The script is available in the repository at  
[`code/Access Metrics - Health Resources`](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20Health%20Resources).

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
The final dataset includes U.S. states, Washington D.C., and Puerto Rico, but excludes other U.S. territories (Guam, Northern Mariana Islands, American Samoa, Palau).  
ZCTA and tract centroids are not population-weighted.
