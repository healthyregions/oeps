**Meta Data Name**: Access to Syringe Services Programs 
**Date Added**: December 18, 2025  
**Authors**: Catherine Discenza, Adam Cox 
**Date Last Modified**: December 18, 2025  
**Last Modified By**: Catherine Discenza 

### Theme:  
Environment  

### Data Location:  
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in `C_2000.csv`.  

### Data Source(s) Description:  
SSP data was sourced from the [North American Syringe Exchange Network (NASEN)](https://www.nasen.org/).  

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

##### Travel Time and Count Within Threshold    
Driving-network access metrics to the nearest SSP were computed

We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. 

This analysis was conducted in Python. The scripts are available in code/AccessMetrics - MOUDs. Some of the scripts are available in [code/AccessMetrics - MOUDs.](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20MOUD), with complete computational notebooks forthcoming in 2026.
 

### Key Variable and Definitions:

- **Variable** – Title of the variable  
- **Variable ID** – Exact name used in the dataset  
- **Description** – Short explanation of what the variable measures  
- **Years Available** – Data availability by year  
- **Spatial Scale** – Level of geography for the variable  

#### Tract and Zip Code

| Variable                          | Variable ID in .csv | Description | Years Available | Spatial Scale |
|----------------------------------|----------------------|-----------------------------------------------------------------------------|------------------|----------------|
| Driving time to nearest SSP | SSPTmDr | Driving time from origin to nearest SSP (minutes)                  | 2025 | Tract |



### Data Limitations:  
*Euclidean or straight-line distance is a basic proxy for access. It does not account for real-world travel constraints.*  
*NASEN advises against using their data as a proxy for the presence of SSP/harm reduction services.*
The travel times are capped at a 90-minute threshold. Any data exceeding this limit is left blank.

### Comments/Notes:  
* All nearest travel time calculations are in minutes.
* Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
* While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
