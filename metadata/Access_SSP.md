**Meta Data Name**: Access to Syringe Services Programs  
**Date Added**: December 18, 2025  
**Authors**: Catherine Discenza, Adam Cox  
**Date Last Modified**: March 4, 2026  
**Last Modified By**: Catherine Discenza  

### Data Source(s) Description:  
Syringe Servies Programs (SSP) data was sourced from the [North American Syringe Exchange Network (NASEN)](https://www.nasen.org/).  

Census Tract shapefiles were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html).
A copy of the geographic boundary files used can be found at the [HEROP GeoData Web Archive](https://geodata.healthyregions.org/).

#### Street Network Topology & Travel Time Matrices
Data on street and pedestrian networks to calculate travel time metrics were sourced from multiple open source data portals. Street network topologies (including street orientations and speed/travel time) all derive from [OpenStreetMap](https://www.openstreetmap.org), also known as OSM.

- For 2025, the **travel time matrices** for driving, biking and walking were sourced from OpenStreetMap using [OSMnx](https://osmnx.readthedocs.io/en/stable/) and [SPASTC](https://doi.org/10.1080/13658816.2024.2326445), calculated by [Alex Michels](https://alexandermichels.github.io/) (University of Texas at Dallas), and are available at the tract scales.

In our approach, a travel time is calculated from the center of each census tract, to the center of another census tract, up to 90 minutes away. These time tables are calculated for across the country, and can be referenced by tract FIPS (unique ID) code.


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

 ![Choropleth map of travel time to substance use treatment by census tract.](https://private-user-images.githubusercontent.com/142624966/555536285-7e723adf-88d5-462d-bb07-4fb334c07c63.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIxMjg0NjUsIm5iZiI6MTc3MjEyODE2NSwicGF0aCI6Ii8xNDI2MjQ5NjYvNTU1NTM2Mjg1LTdlNzIzYWRmLTg4ZDUtNDYyZC1iYjA3LTRmYjMzNGMwN2M2My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMjI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDIyNlQxNzQ5MjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NjQwYzI1MzUzODdiYTJmNjk1OTEzZjA2YmYzYTA2NWE0ZGJlNzhmZWU5MWIwOTA4NmJkYmQ0YzQzNjRhYWY0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.esLwG7LQjAvStDsR7FISiH7Q2vTC3ft2JUWmA8NbJoE)


### Data Limitations:   
*NASEN advises against using their data as a proxy for the presence of SSP/harm reduction services.*  
The travel times are capped at a 90-minute threshold. Any data exceeding this limit is left blank.
Count of resources within a 30-minute threshold was excluded from the final dataset due to low occurence. 

### Comments/Notes:  
* All nearest travel time calculations are in minutes.
* Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
