**Meta Data Name**: Access to Syringe Services Programs  
**Date Added**: December 18, 2025  
**Authors**: Catherine Discenza, Adam Cox  
**Date Last Modified**: February 26, 2026  
**Last Modified By**: Catherine Discenza  

### Data Source(s) Description:  
Syringe Servies Programs (SSP) data was sourced from the [North American Syringe Exchange Network (NASEN)](https://www.nasen.org/).  

Census Tract shapefiles were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html).

### Description of Data Source Tables:  
The NASEN SSP dataset includes:  
- Provider name  
- Location (address, city, state, ZIP)  
- Description
- Services offered

### Description of Data Processing:  

#### NASEN SSP

NASEN SSP data was scraped and geocoded using python scripts available [here](https://drive.google.com/file/d/1f3RPEQXylNSesptOLoYMcINNQgQrqpHR/view?usp=drive_link).

#### Tracts 

##### Distance  
Nearest resource analysis was conducted using minimum Euclidean distance as a proxy for access. This involved:  
- Calculating centroids for all census tracts   
- Identifying the nearest SSP provider to each centroid  
- Calculating the straight-line distance in miles  

##### Travel Time and Count Within Threshold    
Driving-network access metrics to the nearest SSP were computed.

We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. 

This analysis was conducted in Python. The script is available in scripts/Access_SSP.ipynb. 

 ![Choropleth map of travel time to substance use treatment by census tract.](https://private-user-images.githubusercontent.com/142624966/555536285-7e723adf-88d5-462d-bb07-4fb334c07c63.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIxMjg0NjUsIm5iZiI6MTc3MjEyODE2NSwicGF0aCI6Ii8xNDI2MjQ5NjYvNTU1NTM2Mjg1LTdlNzIzYWRmLTg4ZDUtNDYyZC1iYjA3LTRmYjMzNGMwN2M2My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMjI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDIyNlQxNzQ5MjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NjQwYzI1MzUzODdiYTJmNjk1OTEzZjA2YmYzYTA2NWE0ZGJlNzhmZWU5MWIwOTA4NmJkYmQ0YzQzNjRhYWY0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.esLwG7LQjAvStDsR7FISiH7Q2vTC3ft2JUWmA8NbJoE)


### Data Limitations:  
*Euclidean or straight-line distance is a basic proxy for access. It does not account for real-world travel constraints.*  
*NASEN advises against using their data as a proxy for the presence of SSP/harm reduction services.*  
The travel times are capped at a 90-minute threshold. Any data exceeding this limit is left blank.

### Comments/Notes:  
* All nearest travel time calculations are in minutes.
* Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
