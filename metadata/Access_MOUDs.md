**Meta Data Name**: Access to MOUDs  
**Date Added**: February 1, 2021  
**Author**: Marynia Kolak, Mahjabin Kabir Adrita, Wataru Morioka, Susan Paykin
**Date Last Modified**: August 1, 2025  
**Last Modified By**: Marynia Kolak

### Theme: 
Environment  

### Data Location: 
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  

### Data Source(s) Description:

#### Medications for Opioid Overuse Disorder (MOUDs)
Data on providers prescribing Medications for Opioid Overuse Disorder (MOUDs) and their locations were sourced from the [U.S. Substance Abuse and Mental Health Services Administration (SAMHSA) Treatment Locator](https://findtreatment.samhsa.gov/locator) for all time periods. 

For 2019, we extracted the following from SAMSHA’s Treatment Locator Service:

- **Buprenorphine**: All prescribers listed. 
- **Methadone**: All providers tagged as providing “methadone maintenance.”
- **OTP**: All providers tagged as “opioid treatment providers.”
- **Naltrexone**: All providers tagged as providing “naltrexone.”

Naltrexone provider data from SAMHSA in 2019 was supplemented by provider data from Vivitrol.com, with duplicates removed.

The following was extracted in May 2025 from SAMSHA’s Treatment Locator Service:

 - **Buprenorphine**: All prescribers listed. 
 - **Methadone**: Methadone: All providers tagged as providing “methadone.” The term methadone maintenance was no longer visible as a feature in the locator service.
 - **OTP**: All providers tagged as “opioid treatment providers.”
 - **Naltrexone**: All providers tagged as providing “naltrexone.”

#### Street Network Topology & Travel Time Matrices
Data on street and pedestrian networks to calculate travel time metrics were sourced from multiple open source data portals. Street network topologies (including street orientations and speed/travel time) all derive from [OpenStreetMap](https://www.openstreetmap.org), also known as OSM.

- For 2019, the **travel time matrices** for driving, biking and walking were sourced from [Project OSRM](https://project-osrm.org/), calculated by Vidal Anguiano (University of Chicago), and are available at the Tract or ZCTA scales.
- For 2025, the **travel time matrices** for driving, biking and walking were sourced from OpenStreetMap using [OSMnx](https://osmnx.readthedocs.io/en/stable/) and [SPASTC](https://doi.org/10.1080/13658816.2024.2326445), calculated by [Alex Michels](https://alexandermichels.github.io/) (University of Texas at Dallas), and are available at the tract scales.

In our approach, a travel time is calculated from the center of each census tract, to the center of another census tract, up to 90 minutes away. These time tables are calculated for across the country, and can be referenced by tract FIPS (unique ID) code.

### Description of Data Processing: 
Data was identified, wrangled, cleaned, and prepared for analysis. For 2019 locations that needed geocoding, we used the [tidygeocoder](https://cran.r-project.org/web/packages/tidygeocoder/vignettes/tidygeocoder.html) package in R, as well as supplemental geocoding through University of Chicago Library GIS services. Data extracted in 2025 was already complete with spatial coordinate information.

#### Tract and ZIP Code

##### Distance
We conducted the nearest resource analysis from geography centroid to MOUD provider location by type (buprenorphine, methadone, naltrexone) to calculate the nearest Euclidean distance (i.e. straight line distance) for each MOUD. This analysis was conducted in R. Some of the scripts are available in [code/access_MOUDs.R](https://github.com/GeoDaCenter/opioid-policy-scan/blob/v1.0/code/access_MOUDs.R), and will be updated by 2026 with standardized codebooks.

##### Travel Time and Count Within Threshold

We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type, up to 90 minutes away. For *zip code tabulation areas*, overlapping tract-level measures were averaged, weighted by proportion of the overlapping tract, using the corresponding HUD tract-to-zip code crosswalks. 

Count of providers within a travel threshold (30 minutes and/or 60 minutes) were also calculated for three modes of transit: driving, walking, and biking at the tract level, with corresponding average of overlapping tracts at the ZCTA scale. 

This analysis was conducted in Python. The scripts are available in code/AccessMetrics - MOUDs. Some of the scripts are available in [code/AccessMetrics - MOUDs.](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20MOUD), with complete computational notebooks forthcoming in 2026.

#### County and State 
County and state-level variables include the **count** of Census tracts and the **percent** of Census tracts located within a 30 minute driving threshold of an MOUD type, as well as the mean (average) driving time in minutes from Census tracts within the county or state. 

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

#### Tract
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Minimum distance to nearest MOUD (all types) | MoudMinDis | Euclidean distance (miles) to nearest MOUD (all types) | 2019, 2025 | Tract |
| Minimum distance to buprenorphine | BupMinDis | Euclidean distance (miles) to nearest buprenorphine provider | 2019, 2025 | Tract |
| Driving time to nearest buprenorphine | BupTmDr | Driving time (minutes) to nearest buprenorphine provider | 2019, 2025 | Tract |
| Count of buprenorphine providers (drive) | BupCntDr30 | Count of methadone providers in 30 minute drive time threshold | 2019, 2025 | Tract |
| Minimum distance to methadone | MetMinDis | Euclidean distance (miles) to nearest methadone provider | 2019, 2025 | Tract |
| Driving time to nearest methadone | MetTmDr | Driving time (minutes) to nearest methadone provider | 2019, 2025 | Tract |
| Count of methadone providers (drive) | MetCntDr30 | Count of methadone providers in 30 minute drive time threshold | 2019, 2025 | Tract |
| Minimum distance to naltrexone | NalMinDis | Euclidean distance (miles) to nearest naltrexone/Vivitrol provider | 2019, 2025 | Tract |
| Driving time to nearest naltrexone |  NalTmDr | Driving time (minutes) to nearest naltrexone provider | 2019, 2025 | Tract |
| Count of naltrexone providers (drive) | NalCntDr30 | Count of naltrexone providers in 30 minute drive time threshold | 2019, 2025 | Tract|
| Walking time to nearest buprenorphine | BupTmWk | Driving time (minutes) to nearest buprenorphine provider | 2019, 2025 | Tract |
| Count of buprenorphine providers (walk) | BupCntWk60 | Count of buprenorphine providers in 60 minute walking time threshold | 2019, 2025 | Tract|
| Count of buprenorphine providers (walk) | BupCntWk30 | Count of buprenorphine providers in 30 minute walking time threshold | 2019, 2025 | Tract |
| Walking time to nearest methadone | MetTmWk | Driving time (minutes) to nearest methadone provider | 2019, 2025 | Tract, Zip |
| Count of methadone providers (walk) | MetCntWk60 | Count of methadone providers in 60 minute walking time threshold | 2019, 2025 | Tract |
| Count of methadone providers (walk) | MetCntWk30 | Count of methadone providers in 30 minute walking time threshold | 2019, 2025 | Tract |
| Walking time to nearest naltrexone |  NalTmWk | Driving time (minutes) to nearest naltrexone provider | 2019, 2025 | Tract, Zip |
| Count of naltrexone providers (walk) | NalCntWk60 | Count of naltrexone providers in 60 minute walking time threshold | 2019, 2025 | Tract |
| Count of naltrexone providers (walk) | NalCntWk30 | Count of naltrexone providers in 30 minute walking time threshold | 2019, 2025 | Tract |
| Biking time to nearest buprenorphine | BupTmBk | Biking time (minutes) to nearest buprenorphine provider | 2019, 2025 | Tract, Zip |
| Count of buprenorphine providers (bike) | BupCntBk60 | Count of buprenorphine providers in 60 minute biking time threshold | 2019, 2025 | Tract |
| Count of buprenorphine providers (bike) | BupCntBk30 | Count of buprenorphine providers in 30 minute biking time threshold | 2019, 2025 | Tract|
| Biking time to nearest methadone | MetTmBk | Biking time (minutes) to nearest methadone provider | 2019, 2025 | Tract, Zip |
| Count of methadone providers (bike) | MetCntBk60 | Count of methadone providers in 60 minute biking time threshold | 2019, 2025 | Tract |
| Count of methadone providers (bike) | MetCntBk30 | Count of methadone providers in 30 minute biking time threshold | 2019, 2025 | Tract |
| Biking time to nearest naltrexone | NalTmBk | Biking time (minutes) to nearest naltrexone provider | 2019, 2025  | Tract, Zip |
| Count of naltrexone providers (bike) | NalCntBk60 | Count of naltrexone providers in 60 minute biking time threshold | 2019, 2025 | Tract |
| Count of naltrexone providers (bike) | NalCntBk30 | Count of naltrexone providers in 30 minute biking time threshold | 2019, 2025 | Tract |

#### ZIP Code Tabulation Area
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Minimum distance to nearest MOUD (all types) | MoudMinDis | Average Euclidean distance (miles) to nearest MOUD (all types) | 2025 | Zip |
| Minimum distance to buprenorphine | BupMinDis | Average Euclidean distance (miles) to nearest buprenorphine provider | 2025 | Zip |
| Driving time to nearest buprenorphine | BupTmDr | Average Driving time (minutes) to nearest buprenorphine provider | 2025 | Zip |
| Count of buprenorphine providers (drive) | BupCntDr30 | Average Count of methadone providers in 30 minute drive time threshold | 2025 | Zip |
| Minimum distance to methadone | MetMinDis | Average Euclidean distance (miles) to nearest methadone provider | 2025 | Zip |
| Driving time to nearest methadone | MetTmDr | Average Driving time (minutes) to nearest methadone provider | 2025 | Zip |
| Count of methadone providers (drive) | MetCntDr30 | Average Count of methadone providers in 30 minute drive time threshold | 2025 | Zip |
| Minimum distance to naltrexone | NalMinDis | Average Euclidean distance (miles) to nearest naltrexone/Vivitrol provider | 2025 | Zip |
| Driving time to nearest naltrexone |  NalTmDr | Average Driving time (minutes) to nearest naltrexone provider | 2025 | Zip |
| Count of naltrexone providers (drive) | NalCntDr30 | Average Count of naltrexone providers in 30 minute drive time threshold | 2025 | Zip |
| Walking time to nearest buprenorphine | BupTmWk | Average Driving time (minutes) to nearest buprenorphine provider | 2025 | Zip |
| Count of buprenorphine providers (walk) | BupCntWk60 | Average Count of buprenorphine providers in 60 minute walking time threshold | 2025 | Zip |
| Count of buprenorphine providers (walk) | BupCntWk30 | Average Count of buprenorphine providers in 30 minute walking time threshold | 2025 | Zip |
| Walking time to nearest methadone | MetTmWk | Average Driving time (minutes) to nearest methadone provider | 2025 | Zip |
| Count of methadone providers (walk) | MetCntWk60 | Average Count of methadone providers in 60 minute walking time threshold | 2025 | Zip |
| Count of methadone providers (walk) | MetCntWk30 | Average Count of methadone providers in 30 minute walking time threshold | 2025 | Zip |
| Walking time to nearest naltrexone |  NalTmWk | Average Driving time (minutes) to nearest naltrexone provider | 2025 | Tract, Zip |
| Count of naltrexone providers (walk) | NalCntWk60 | Average Count of naltrexone providers in 60 minute walking time threshold | 2025 | Zip |
| Count of naltrexone providers (walk) | NalCntWk30 | Average Count of naltrexone providers in 30 minute walking time threshold | 2025 | Zip |
| Biking time to nearest buprenorphine | BupTmBk | Average Biking time (minutes) to nearest buprenorphine provider | 2025 | Zip |
| Count of buprenorphine providers (bike) | BupCntBk60 | Average Count of buprenorphine providers in 60 minute biking time threshold | 2025 | Zip |
| Count of buprenorphine providers (bike) | BupCntBk30 | Average Count of buprenorphine providers in 30 minute biking time threshold | 2025 | Zip |
| Biking time to nearest methadone | MetTmBk | Average Biking time (minutes) to nearest methadone provider | 2025 | Tract, Zip |
| Count of methadone providers (bike) | MetCntBk60 | Average Count of methadone providers in 60 minute biking time threshold | 2025 |  Zip |
| Count of methadone providers (bike) | MetCntBk30 | Average Count of methadone providers in 30 minute biking time threshold | 2025 | Zip |
| Biking time to nearest naltrexone | NalTmBk | Average Biking time (minutes) to nearest naltrexone provider | Latest | Tract, Zip |
| Count of naltrexone providers (bike) | NalCntBk60 | Average Count of naltrexone providers in 60 minute biking time threshold | 2025 | Zip |
| Count of naltrexone providers (bike) | NalCntBk30 | Average Count of naltrexone providers in 30 minute biking time threshold | 2025 | Zip |

#### County and State
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Count of tracts | TotTracts | Total number of tracts in county/state | 2025 | County, State |
| Count of tracts within 30-min buprenorphine driving range | BupCtTmDr | Number of tracts with buprenorphine provider within a 30-min driving range | 2025 | County, State |
| Count of tracts within 30-min buprenorphine biking range | BupCtTmBk | Number of tracts with buprenorphine provider within a 30-min biking range | 2025 | County, State |
| Count of tracts within 30-min buprenorphine walking range | BupCtTmWk | Number of tracts with buprenorphine provider within a 30-min walking range | 2025 | County, State |
| Count of tracts within 30-min methadone driving range | MetCtTmDr | Number of tracts with methadone provider within a 30-min driving range | 2025 | County, State |
| Count of tracts within 30-min methadone biking range | MetCtTmBk | Number of tracts with methadone provider within a 30-min biking range | 2025 | County, State |
| Count of tracts within 30-min methadone walking range | MetCtTmWk | Number of tracts with methadone provider within a 30-min walking range | 2025 | County, State |
| Count of tracts within 30-min naltrexone driving range | NalCtTmDr | Number of tracts with naltrexone provider within a 30-min driving range | 2025 | County, State |
| Count of tracts within 30-min naltrexone biking range | NalCtTmBk | Number of tracts with naltrexone provider within a 30-min biking range | 2025 | County, State |
| Count of tracts within 30-min naltrexone walking range | NalCtTmWk | Number of tracts with naltrexone provider within a 30-min walking range | 2025 | County, State |
| Average driving time to nearest buprenorphine provider | BupAvTmDr | Average driving time (minutes) across tracts in county/state to nearest buprenorphine provider | 2025 | County, State |
| Average biking time to nearest buprenorphine provider | BupAvTmBk | Average biking time (minutes) across tracts in county/state to nearest buprenorphine provider | 2025 | County, State |
| Average walking time to nearest buprenorphine provider | BupAvTmWk | Average walking time (minutes) across tracts in county/state to nearest buprenorphine provider | 2025 | County, State |
| Average driving time to nearest methadone provider | MetAvTmDr | Average driving time (minutes) across tracts in county/state to nearest methadone provider | 2025 | County, State |
| Average biking time to nearest methadone provider | MetAvTmBk | Average biking time (minutes) across tracts in county/state to nearest methadone provider | 2025 | County, State |
| Average walking time to nearest methadone provider | MetAvTmWk | Average walking time (minutes) across tracts in county/state to nearest methadone provider | 2025 | County, State |
| Average driving time to nearest naltrexone provider | NalAvTmDr | Average driving time (minutes) across tracts in county/state to nearest naltrexone provider | 2025 | County, State |
| Average biking time to nearest naltrexone provider | NalAvTmBk | Average biking time (minutes) across tracts in county/state to nearest naltrexone provider | 2025 | County, State |
| Average walking time to nearest naltrexone provider | NalAvTmWk | Average walking time (minutes) across tracts in county/state to nearest naltrexone provider | 2025 | County, State |
| Percent of tracts within 30-min buprenorphine driving range | BupTmDrP | Percent of tracts with buprenorphine provider within a 30-min driving range | 2025 | County, State |
| Percent of tracts within 30-min buprenorphine biking range | BupTmBkP | Percent of tracts with buprenorphine provider within a 30-min biking range | 2025 | County, State |
| Percent of tracts within 30-min buprenorphine walking range | BupTmWkP | Percent of tracts with buprenorphine provider within a 30-min walking range | 2025 | County, State |
| Percent of tracts within 30-min methadone driving range | MetTmDrP | Percent of tracts with methadone provider within a 30-min driving range | 2025 | County, State |
| Percent of tracts within 30-min methadone biking range | MetTmBkP | Percent of tracts with methadone provider within a 30-min biking range | 2025 | County, State |
| Percent of tracts within 30-min methadone walking range | MetTmWkP | Percent of tracts with methadone provider within a 30-min walking range | 2025 | County, State |
| Percent of tracts within 30-min naltrexone driving range | NalTmDrP | Percent of tracts with naltrexone provider within a 30-min driving range | 2025 | County, State |
| Percent of tracts within 30-min naltrexone biking range | NalTmBkP | Percent of tracts with naltrexone provider within a 30-min biking range | 2025 | County, State |
| Percent of tracts within 30-min naltrexone walking range | NalTmWkP | Percent of tracts with naltrexone provider within a 30-min walking range | 2025 | County, State |

### Data Limitations:
Access metrics are calculated for the continental U.S., and do not include Hawaii, Alaska, or U.S. territories. 

### Comments/Notes:
* All nearest distance calculations are in miles. 
* All nearest travel time calculations are in minutes.
* The access metrics for 2025 have been calculated using vintage travel metrics and geographic data.
