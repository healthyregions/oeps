**Meta Data Name**: Access to Hospitals  
**Date Added**: January 6, 2021  
**Author**: Susan Paykin, Wataru Morioka, Mahjabin Kabir Adrita  
**Date Last Modified:** January 28, 2026  
**Last Modified By:** Mahjabin Kabir Adrita

### Data Source(s) Description:  

#### Resources

- In 2021, hospital locations were sourced from [CovidCareMap Healthcare System Capacity data](https://github.com/covidcaremap/covid19-healthsystemcapacity/tree/master/data), an aggregated dataset which sources data from the [Healthcare Cost Report Information System (HCRIS)](https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Cost-Reports/Hospital-2010-form) and [Definitive Healthcare](https://coronavirus-resources.esri.com/datasets/definitivehc::definitive-healthcare-usa-hospital-beds?geometry=125.859%2C-16.820%2C-150.821%2C72.123). 
- In 2025, Hospital locations were sourced from https://data.cms.gov/provider-data/topics/hospitals. These are the official datasets used on Medicare.gov provided by the Centers for Medicare & Medicaid Services.

#### Street Network Topology & Travel Time Matrices
Data on street and pedestrian networks to calculate travel time metrics were sourced from multiple open source data portals. Street network topologies (including street orientations and speed/travel time) all derive from [OpenStreetMap](https://www.openstreetmap.org), also known as OSM.

- For 2019, the **travel time matrices** for driving, biking and walking were sourced from [Project OSRM](https://project-osrm.org/), calculated by Vidal Anguiano (University of Chicago), and are available at the Tract or ZCTA scales.
- For 2025, the **travel time matrices** for driving, biking and walking were sourced from OpenStreetMap using [OSMnx](https://osmnx.readthedocs.io/en/stable/) and [SPASTC](https://doi.org/10.1080/13658816.2024.2326445), calculated by [Alex Michels](https://alexandermichels.github.io/) (University of Texas at Dallas), and are available at the tract scales.

In our approach, a travel time is calculated from the center of each census tract, to the center of another census tract, up to 90 minutes away. These time tables are calculated for across the country, and can be referenced by tract FIPS (unique ID) code.

#### Geographic Boundaries
ZIP Code Tract Area (ZCTA) and Census Tract boundary files were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018, 2020](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html). 
A copy of the geographic boundary files used can be found at the [HEROP GeoData Web Archive](https://geodata.healthyregions.org/).

### Description of Data Source Tables: 
The source datatable from CovidCareMap included the hospital name, address, city, state, county, latitude and longitude, as well as additional variables for hospital bed and ICU bed capacity, current bed occupancy rates, and staffing rates. For this analysis, we used only the hospital name and location variables. 

### Description of Data Processing: 

#### Tract and Zip Code

##### Distance
Data was cleaned and prepared for analysis. Centroids were calculated for ZCTA and Census Tract geometries. For the nearest resource analysis, Euclidean distance was calculated from the centroid of each tract/ZCTA to the nearest hospital location.

##### Travel Time and Count Within Threshold
We calculated travel-network access metrics for the driving travel time to the nearest hospital location and count of hospitals within a 30 minute driving threshold. We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. For *zip code tabulation areas*, overlapping tract-level measures were averaged, weighted by proportion of the overlapping tract, using the corresponding HUD tract-to-zip code crosswalks. 

<img width="1491" height="658" alt="image" src="https://github.com/user-attachments/assets/51dc2b58-67df-45c9-b01d-2c286d2163c9" />

This travel time analysis was conducted using a Python Computational notebook. 

- For 2021 measures, some of the scripts are available in [code/AccessMetrics - MOUDs.](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20MOUD).
- The updated 2025 notebook will be released in late January 2026, due to some refinements and updates.

In addition, an **impedance factor** was introduced in 2025 access metrics. Raw travel time measures assume pristine conditions in a best-case-scenario. 
An impedance approach instead multiples the estimated travel time by a factor, in this case a factor of 2, better approximating actual travel time due to traffic, congestion, etc.

#### County and State 
County and state-level variables include the **count** of Census tracts and the **percent** of Census tracts located within a 30 minute driving threshold of hospital, as well as the mean (average) driving time in minutes from Census tracts within the county or state. 

For 2025 measures, the tract to county conversion were completed using R code, and can be found
[scripts/HospitalTract2County.R.](https://github.com/healthyregions/oeps/tree/main/scripts).

<img width="714" height="521" alt="image" src="https://github.com/user-attachments/assets/83538524-1153-43ac-8b64-14fbecf0af10" />

### Data Limitations:
- Euclidean distance or straight-line distance is a simple approximation of distance or travel time from an origin centroid to the nearest health center. It is not a precise calculation of real travel times or distances. 
- The travel times are capped at a 90-minute threshold (or 180 minutes, with impedance factor) were not calculated, as they were deemed too far = no access. 
- Travel times are calculated from centroid to centroid of each census tract, meaning that the travel time will equal zero if there is a resource in the census tract. Thus, travel times must be considered approximations, and best suited for relative
understanding of potential spatial access. 
- Note that Alaska travel times may reflect the data technically, but due to the geographic complexities of the state, we don't recommend using measures for that state at this time. Tracts are very large, and while there may
be a Hospital location within the tract -- giving it a travel time of zero -- the physical size of the tract boundary makes that actual time a bit unreasonable. Please proceed with caution in frontier locations.


### Comments/Notes:
- All nearest distance calculations are in miles. 
- All nearest travel time calculations are in minutes.
- Null values correspond to the worst access, where travel takes over 90 minutes in optimal conditions, or 180 minutes in normal conditions.
- Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
- While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
- The zip code calculation was updated in 2025 to an average of overlapping tract-level metrics, rather than distance from the center of a zip code area. Because zip code areas are large, when compared to census tracts, distance from the geometric center was deemed less meaningful. A detailed notebook comparing the differences will be shared in 2026.
- During the crosswalk process, we used the total ratio from the HUD USPS Crosswalk Files. This ratio represents the proportion of total addresses in a given geographic unit (e.g., census tract) that fall within a corresponding target geographic unit (e.g., ZIP Code). The total ratio was used as a weighting factor to allocate counts and measures proportionally between geographies.
