**Meta Data Name**: Access to Syringe Services Programs  
**Date Added**: December 18, 2025  
**Authors**: Catherine Discenza, Adam Cox  
**Date Last Modified**: May 4, 2026  
**Last Modified By**: Catherine Discenza  

### Data Source(s) Description: 

#### Resources
Syringe Servies Programs (SSP) data was sourced from the [North American Syringe Exchange Network (NASEN)](https://www.nasen.org/).  

#### Street Network Topology & Travel Time Matrices
Data on street and pedestrian networks to calculate travel time metrics were sourced from multiple open source data portals. Street network topologies (including street orientations and speed/travel time) all derive from [OpenStreetMap](https://www.openstreetmap.org), also known as OSM.

- For 2025, the **travel time matrices** for driving, biking and walking were sourced from OpenStreetMap using [OSMnx](https://osmnx.readthedocs.io/en/stable/) and [SPASTC](https://doi.org/10.1080/13658816.2024.2326445), calculated by [Alex Michels](https://alexandermichels.github.io/) (University of Texas at Dallas), and are available at the tract scales.

In our approach, a travel time is calculated from the center of each census tract, to the center of another census tract, up to 90 minutes away. These time tables are calculated for across the country, and can be referenced by tract FIPS (unique ID) code.

#### Geographic Boundaries
Census Tract shapefiles were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html).
A copy of the geographic boundary files used can be found at the [HEROP GeoData Web Archive](https://geodata.healthyregions.org/).

### Description of Data Source Tables:  
The NASEN SSP dataset includes:  
- Provider name  
- Location (address, city, state, ZIP)  
- Description
- Services offered

### Description of Data Processing:  

#### NASEN SSP

NASEN SSP data was scraped and geocoded using python scripts.

#### Tracts 

##### Travel Time and Count Within Threshold    
Centroids were calculated for Census Tract geometries. Driving-network access metrics to the nearest SSP were computed.

We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. 

This analysis was conducted using a Python Computational notebook. The script is available in scripts/Access_SSP.ipynb.

In addition, an **impedance factor** was introduced in 2025 access metrics. Raw travel time measures assume pristine conditions in a best-case-scenario. 
An impedance approach instead multiples the estimated travel time by a factor, in this case a factor of 2, better approximating actual travel time due to traffic, congestion, etc.

 ![Choropleth map of travel time to substance use treatment by census tract.](https://private-user-images.githubusercontent.com/142624966/555536285-7e723adf-88d5-462d-bb07-4fb334c07c63.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzc5OTQwNTgsIm5iZiI6MTc3Nzk5Mzc1OCwicGF0aCI6Ii8xNDI2MjQ5NjYvNTU1NTM2Mjg1LTdlNzIzYWRmLTg4ZDUtNDYyZC1iYjA3LTRmYjMzNGMwN2M2My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUwNVQxNTA5MThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xYTcwNDJjZGJkNTdkNDlkZWNhYTRiYTdkN2U5OGJlY2Y5NDJlYzcwMTEyN2Y1ZTY5OTI4MTJmMGEwZDE1OGE2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.bllKqz6ud38Qh_jDe3d_T3YynepuhPBvStbIVRXzkQ8)


### Data Limitations:   
*NASEN advises against using their data as a proxy for the presence of SSP/harm reduction services.*  
- The travel times are capped at a 90-minute threshold. Any data exceeding this limit is left blank.
- Count of resources within a 30-minute threshold was excluded from the final dataset due to low occurence. 
- Travel times are calculated from centroid to centroid of each census tract, meaning that the travel time will equal zero if there is a resource in the census tract. Thus, travel times must be considered approximations, and best suited for relative understanding of potential spatial access.
- Unlike most U.S. states, Connecticut’s traditional eight counties do not function as active government units and have not been used for statistical reporting for decades. More recently, the U.S. Census Bureau replaced Connecticut’s eight historical counties with nine planning regions as official county-equivalent geographies, effective in Census Bureau products beginning in 2022, with full adoption in federal data products through 2023–2024. Because this redefinition means that county FIPS codes and county-level boundaries no longer align consistently with the definitions used elsewhere in our dataset (which assume stable county geographies), some Connecticut tracts may appear as empty or missing in the county summary table. This is especially true where tract identifiers include legacy county codes that no longer match current county-equivalent definitions.
- Note that Alaska travel times may reflect the data technically, but due to the geographic complexities of the state, we don't recommend using measures for that state at this time. Tracts are very large, and while there may be an SSP location within the tract -- giving it a travel time of zero -- the physical size of the tract boundary makes that actual time a bit unreasonable. Please proceed with caution in frontier locations.

![Limitations of Alaska travel times due to tract boundary size and approach utilized](https://github.com/user-attachments/assets/b9ea8e36-6643-4851-9f9a-62ea9b9dd72b)
*Limitations of Alaska travel times due to tract boundary size and approach utilized*

### Comments/Notes:  
- All nearest travel time calculations are in minutes.
- Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
- Null values correspond to the worst access, where travel takes over 90 minutes in optimal conditions, or 180 minutes in normal conditions.
- Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
