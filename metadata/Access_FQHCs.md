**Meta Data Name**: Access to Federal Qualified Health Centers (FQHCs)  
**Date Added**: January 5, 2021  
**Author**: Susan Paykin, Wataru Morioka, Mahjabin Kabir Adrita, Marynia Kolak  
**Date Last Modified**: December 23, 2025   
**Last Modified By**: Marynia Kolak

### Theme: 
Environment

### Data Source(s) Description:  

#### Resources
Locations of Federal Qualified Health Centers (FQHCs) were sourced from the [Health Resources and Services Administration](https://bphc.hrsa.gov/datareporting/index.html).

- For the 2021 measure, the original FQHC data was extracted, cleaned and geocoded for the [US COVID Atlas](https://theuscovidatlas.org/), and subsequently used for OEPS.
- For the 2025 measure, a copy of the original data used can be found at the [SDOH & Place Data Refuge](https://uofi.app.box.com/s/fqtslnfkpmgi32pb1cah1eyvmimvp740/folder/305426293733) for HRSA data downloaded on January 31, 2025. 

#### Street Network Topology & Travel Time Matrices
Data on street and pedestrian networks to calculate travel time metrics were sourced from multiple open source data portals. Street network topologies (including street orientations and speed/travel time) all derive from [OpenStreetMap](https://www.openstreetmap.org), also known as OSM.

- For 2019, the **travel time matrices** for driving, biking and walking were sourced from [Project OSRM](https://project-osrm.org/), calculated by Vidal Anguiano (University of Chicago), and are available at the Tract or ZCTA scales.
- For 2025, the **travel time matrices** for driving, biking and walking were sourced from OpenStreetMap using [OSMnx](https://osmnx.readthedocs.io/en/stable/) and [SPASTC](https://doi.org/10.1080/13658816.2024.2326445), calculated by [Alex Michels](https://alexandermichels.github.io/) (University of Texas at Dallas), and are available at the tract scales.

In our approach, a travel time is calculated from the center of each census tract, to the center of another census tract, up to 90 minutes away. These time tables are calculated for across the country, and can be referenced by tract FIPS (unique ID) code.

#### Geographic Boundaries
ZIP Code Tract Area (ZCTA) and Census Tract boundary files were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018, 2020](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html). 
A copy of the geographic boundary files used can be found at the [HEROP GeoData Web Archive](https://geodata.healthyregions.org/).

### Description of Data Processing: 

#### Tract and Zip Code

##### Minimum Distance
Data was cleaned and prepared for analysis. Centroids were calculated for ZCTA and Census Tract geometries. 
For the nearest resource analysis, Euclidean distance was calculated from the centroid of each tract/ZCTA to the 
nearest FQHC location. The original 2021 script is available in [code/access_FQHC.R](https://github.com/GeoDaCenter/opioid-policy-scan/blob/master/code/access_FQHC.R).

##### Travel Time and Count Within Threshold
We calculated travel-network access metrics for the driving travel time to the nearest FQHC location and count of FQHCs within a 30 minute driving threshold. We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. For *zip code tabulation areas*, overlapping tract-level measures were averaged, weighted by proportion of the overlapping tract, using the corresponding HUD tract-to-zip code crosswalks. 

This travel time analysis was conducted using a Python Computational notebook. 

- For 2021 measures, some of the scripts are available in [code/AccessMetrics - MOUDs.](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20MOUD).
- The updated 2025 notebook will be released in late January 2026, due to some refinements and updates.

In addition, an **impedance factor** was introduced in 2025 access metrics. Raw travel time measures assume pristine conditions in a best-case-scenario. 
An impedance approach instead multiples the estimated travel time by a factor, in this case a factor of 2, better approximating actual travel time due to traffic, congestion, etc.

#### County and State 
County and state-level variables include the **count** of Census tracts and the **percent** of Census tracts located within a 30 minute driving threshold of an FQHC, as well as the mean (average) driving time in minutes from Census tracts within the county or state. 

For 2025 measures, the tract to county conversion were completed using R code, and can be found
[scripts/fqhc-tract2county.R.](https://github.com/healthyregions/oeps/tree/main/scripts).

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

#### Tract and Zip Code
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------| 
| Distance to nearest FQHC | FqhcMinDis | Euclidean distance *from tract/zip centroid to nearest FQHC, in miles* | 2021, 2025 | Tract, Zip |
| Driving time to nearest FQHC | FqhcTmDr | Driving time from tract/zip origin centroid to the nearest tract FQHC destination centroid, in minutes | 2021, 2025 | Tract|
| Driving time to nearest FQHC, with Impedance | FqhcTmDr2 | Driving time from tract/zip origin centroid to the nearest tract FQHC destination centroid, with impedance factor, in minutes. | 2025 | Tract |
| Count of FQHCs | FqhcCntDr | Count of FQHCs within a 30-minute driving threshold | 2021, 2025 | Tract |
| Count of FQHCs, with Impedance | FqhcCntDr2 | Count of FQHCs within a 30-minute driving threshold, with impedance factor | 2025 | Tract |

#### County and State
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Count of tracts | TotTracts | Total number of tracts in county/state | 2021, 2025 | County, State |
| Count of tracts within 30-min driving range | FqhcCtTmDr | Number of tracts with FQHC within a 30-min driving range | 2021, 2025 | County, State |
| Count of tracts within 30-min driving range, with Impedance | FqhcCtTmDr2 | Number of tracts with FQHC within a 30-min driving range, with impedance factor | 2025 | County |
| Percent of tracts within 30-min driving range | FqhcTmDrP | Percent of tracts with FQHC within a 30-min driving range | 2021, 2025 | County, State |
| Percent of tracts within 30-min driving range, with Impedance | FqhcTmDrP2 | Percent of tracts with FQHC within a 30-min driving range, with impedance factor | 2025 | County |
| Average time drive to nearest FQHC | FqhcAvTmDr | Average driving time (minutes) across tracts in county/state to nearest FQHC | 2021, 2025 | County, State |
| Average time drive to nearest FQHC, with Impedance | FqhcAvTmDr2 | Average driving time (minutes) across tracts in county/state to nearest FQHC, with impedance factor | 2025 | County |

[Percent of tracts within 30-min driving range, with Impedance (FqhcTmDrP2)](/images/FqhcTmDrP2.png)

[Average time drive to nearest FQHC, with Impedance (FqhcAvTmDr2)](/images/FqhcAvTmDr2_2025.png)

### Data Limitations:
- Euclidean distance or straight-line distance is a simple approximation of distance or travel time from an origin centroid to the nearest health center. It is not a precise calculation of real travel times or distances. 
- The travel times are capped at a 90-minute threshold (or 180 minutes, with impedance factor) were not calculated, as they were deemed too far = no access. 
- Travel times are calculated from centroid to centroid of each census tract, meaning that the travel time will equal zero if there is a resource in the census tract. Thus, travel times must be considered approximations, and best suited for relative
understanding of potential spatial access. 
- Note that Alaska travel times may reflect the data technically, but due to the geographic complexities of the state, we don't recommend using measures for that state at this time. Tracts are very large, and while there may
be a FQHC location within the tract -- giving it a travel time of zero -- the physical size of the tract boundary makes that actual time a bit unreasonable. Please proceed with caution in frontier locations.

[Limitations of Alaska travel times due to tract boundary size and approach utilized](/images/FqhcAvTmDr2_Alaska_2025.png)

### Comments/Notes:
- All nearest distance calculations are in miles. 
- All nearest travel time calculations are in minutes.
- Null values correspond to the worst access, where travel takes over 90 minutes in optimal conditions, or 180 minutes in normal conditions.
- Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
- While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
- The zip code calculation was updated in 2025 to an average of overlapping tract-level metrics, rather than distance from the center of a zip code area. Because zip code areas are large, when compared to census tracts, distance from the geometric center was deemed less meaningful. A detailed notebook comparing the differences will be shared in 2026.
- During the crosswalk process, we used the total ratio from the HUD USPS Crosswalk Files. This ratio represents the proportion of total addresses in a given geographic unit (e.g., census tract) that fall within a corresponding target geographic unit (e.g., ZIP Code). The total ratio was used as a weighting factor to allocate counts and measures proportionally between geographies.


