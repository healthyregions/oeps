**Meta Data Name**: Access to Hospitals  
**Date Added**: January 6, 2021  
**Author**: Susan Paykin, Wataru Morioka, Mahjabin Kabir Adrita  
**Date Last Modified:** August 13, 2025   
**Last Modified By:** Mahjabin Kabir Adrita

### Data Source(s) Description:  
In 2021, hospital locations were sourced from [CovidCareMap Healthcare System Capacity data](https://github.com/covidcaremap/covid19-healthsystemcapacity/tree/master/data), an aggregated dataset which sources data from the [Healthcare Cost Report Information System (HCRIS)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Cost-Reports/Hospital-2010-form) and [Definitive Healthcare](https://coronavirus-resources.esri.com/datasets/definitivehc::definitive-healthcare-usa-hospital-beds?geometry=125.859%2C-16.820%2C-150.821%2C72.123). In 2025, Hospital locations were sourced from https://data.cms.gov/provider-data/topics/hospitals. These are the official datasets used on Medicare.gov provided by the Centers for Medicare & Medicaid Services.

Zip code tract area (ZCTA) and Census Tract files were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html). 

### Description of Data Source Tables: 
The source datatable from CovidCareMap included the hospital name, address, city, state, county, latitude and longitude, as well as additional variables for hospital bed and ICU bed capacity, current bed occupancy rates, and staffing rates. For this analysis, we used only the hospital name and location variables. 

### Description of Data Processing: 

#### Tract and Zip Code

##### Distance
Data was cleaned and prepared for analysis. Centroids were calculated for ZCTA and Census Tract geometries. For the nearest resource analysis, Euclidean distance was calculated from the centroid of each tract/ZCTA to the nearest hospital location.

##### Travel Time and Count Within Threshold
We calculated travel-network access metrics for the driving travel time to the nearest hospital location and count of hospitals within a 30 minute driving threshold. We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. For *zip code tabulation areas*, overlapping tract-level measures were averaged, weighted by proportion of the overlapping tract, using the corresponding HUD tract-to-zip code crosswalks. 

This analysis was conducted in Python. The scripts are available in code/AccessMetrics - MOUDs. Some of the scripts are available in [code/AccessMetrics - MOUDs.](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20MOUD), with complete computational notebooks forthcoming in 2026.

#### County and State 
County and state-level variables include the **count** of Census tracts and the **percent** of Census tracts located within a 30 minute driving threshold of hospital, as well as the mean (average) driving time in minutes from Census tracts within the county or state. 

### Data Limitations:
*Euclidean distance or straight-line distance is a simple approximation of distance or travel time from an origin centroid to the nearest health center. It is not a precise calculation of real travel times or distances. The travel times are capped at a 90-minute threshold; any data exceeding this limit is left blank.

### Comments/Notes:
* All nearest distance calculations are in miles. 
* All nearest travel time calculations are in minutes.
* Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
* While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
* The zip code calculation was updated in 2025 to an average of overlapping tract-level metrics, rather than distance from the center of a zip code area. Because zip code areas are large, when compared to census tracts, distance from the geometric center was deemed less meaningful. A detailed notebook comparing the differences will be shared in 2026.
* During the crosswalk process, we used the total ratio from the HUD USPS Crosswalk Files. This ratio represents the proportion of total addresses in a given geographic unit (e.g., census tract) that fall within a corresponding target geographic unit (e.g., ZIP Code). The total ratio was used as a weighting factor to allocate counts and measures proportionally between geographies.
