**Meta Data Name**: Access to HIV Testing  
**Date Added**: June 23, 2025  
**Author**: Mahjabin Kabir Adrita  
**Date Last Modified**: February 15, 2026  
**Last Modified By**: Mahjabin Kabir Adrita  

### Data Source(s) Description:

#### Resources
For the 2025 measure, HIV Testing provider data was sourced from the [Substance Abuse and Mental Health Services Administration (SAMHSA)](https://www.samhsa.gov/) via its [Treatment Services Locator Tool](https://findtreatment.samhsa.gov/locator).  

#### Street Network Topology & Travel Time Matrices
Data on street and pedestrian networks to calculate travel time metrics were sourced from multiple open source data portals. Street network topologies (including street orientations and speed/travel time) all derive from [OpenStreetMap](https://www.openstreetmap.org), also known as OSM.

- For 2025, the **travel time matrices** for driving, biking and walking were sourced from OpenStreetMap using [OSMnx](https://osmnx.readthedocs.io/en/stable/) and [SPASTC](https://doi.org/10.1080/13658816.2024.2326445), calculated by [Alex Michels](https://alexandermichels.github.io/) (University of Texas at Dallas), and are available at the tract scales.

In our approach, a travel time is calculated from the center of each census tract, to the center of another census tract, up to 90 minutes away. These time tables are calculated for across the country, and can be referenced by tract FIPS (unique ID) code.

#### Geographic Boundaries
ZIP Code Tract Area (ZCTA) and Census Tract boundary files were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018, 2020](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html). 
A copy of the geographic boundary files used can be found at the [HEROP GeoData Web Archive](https://geodata.healthyregions.org/).

### Description of Data Source Tables:  
The SAMHSA HIV Testing dataset includes:  
- Provider name  
- Location (address, city, state, ZIP, county, latitude, longitude)  
- Contact information (website, phone number)  

### Description of Data Processing:  

#### Tract and Zip Code

##### Minimum Distance
Data was cleaned and prepared for analysis. Centroids were calculated for ZCTA and Census Tract geometries. 
For the nearest resource analysis, Euclidean distance was calculated from the centroid of each tract/ZCTA to the 
nearest HIV Testing Facility location. The original 2021 script is available in [ our codes folder](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/).

##### Travel Time and Count Within Threshold
We calculated travel-network access metrics for the driving travel time to the nearest HIV Testing Facility location and count of HiV Testing Facilities within a 30 minute driving threshold. We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. For *zip code tabulation areas*, overlapping tract-level measures were averaged, weighted by proportion of the overlapping tract, using the corresponding HUD tract-to-zip code crosswalks. 

This travel time analysis was conducted using a Python Computational notebook.

- The updated 2025 notebook will be released in late January 2026, due to some refinements and updates.

<img width="1491" height="658" alt="image" src="https://github.com/user-attachments/assets/05ddd5c8-1503-4925-a46d-8e5d12c310a5" />


In addition, an **impedance factor** was introduced in 2025 access metrics. Raw travel time measures assume pristine conditions in a best-case-scenario. 
An impedance approach instead multiples the estimated travel time by a factor, in this case a factor of 2, better approximating actual travel time due to traffic, congestion, etc.

#### County and State 
County and state-level variables include the **count** of Census tracts and the **percent** of Census tracts located within a 30 minute driving threshold of an HIV Testing Facility, as well as the mean (average) driving time in minutes from Census tracts within the county or state. 

For 2025 measures, the tract to county conversion were completed using R code, and can be found
[scripts/HIV-tract2county.R.](https://github.com/healthyregions/oeps/tree/main/scripts). 

### Data Limitations:  
- Euclidean distance or straight-line distance is a simple approximation of distance or travel time from an origin centroid to the nearest health center. It is not a precise calculation of real travel times or distances. 
- The travel times are capped at a 90-minute threshold (or 180 minutes, with impedance factor) were not calculated, as they were deemed too far = no access. 
- Missing data and Travel Times that were capped both show up as blank on the data table.  
- Travel times are calculated from centroid to centroid of each census tract, meaning that the travel time will equal zero if there is a resource in the census tract. Thus, travel times must be considered approximations, and best suited for relative
understanding of potential spatial access.
- Unlike most U.S. states, Connecticut’s traditional eight counties do not function as active government units and have not been used for statistical reporting for decades. More recently, the U.S. Census Bureau replaced Connecticut’s eight historical counties with nine planning regions as official county-equivalent geographies, effective in Census Bureau products beginning in 2022, with full adoption in federal data products through 2023–2024. Because this redefinition means that county FIPS codes and county-level boundaries no longer align consistently with the definitions used elsewhere in our dataset (which assume stable county geographies), some Connecticut tracts may appear as empty or missing in the county summary table. This is especially true where tract identifiers include legacy county codes that no longer match current county-equivalent definitions.
- Note that Alaska travel times may reflect the data technically, but due to the geographic complexities of the state, we don't recommend using measures for that state at this time. Tracts are very large, and while there may
be a HIV Testing Facility location within the tract -- giving it a travel time of zero -- the physical size of the tract boundary makes that actual time a bit unreasonable. Please proceed with caution in frontier locations.

### Comments/Notes:  
- All nearest distance calculations are in miles. 
- All nearest travel time calculations are in minutes.
- Null values correspond to the worst access, where travel takes over 90 minutes in optimal conditions, or 180 minutes in normal conditions.
- Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
- While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
- The zip code calculation was updated in 2025 to an average of overlapping tract-level metrics, rather than distance from the center of a zip code area. Because zip code areas are large, when compared to census tracts, distance from the geometric center was deemed less meaningful. A detailed notebook comparing the differences will be shared in 2026.
- During the crosswalk process, we used the total ratio from the HUD USPS Crosswalk Files. This ratio represents the proportion of total addresses in a given geographic unit (e.g., census tract) that fall within a corresponding target geographic unit (e.g., ZIP Code). The total ratio was used as a weighting factor to allocate counts and measures proportionally between geographies.
