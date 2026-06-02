**Meta Data Name**: Access to Mental Health Providers  
**Date Added**: January 9, 2021  
**Author**: Mahjabin Kabir Adrita, Wataru Morioka, Susan Paykin  
**Date Last Modified**: June 2, 2026  
**Last Modified By**: Marynia Kolak

### Data Source(s) Description:  
Mental health provider data was sourced from [Substance Abuse and Mental Health Services Administration (SAMSHA)](https://www.samhsa.gov/) through its [Treatment Services Locator Tool](https://findtreatment.samhsa.gov/locator). 

ZIP Code Tract Area (ZCTA) and Census Tract files were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html). 

### Description of Data Source Tables: 
The source SAMSHA mental health provider dataset includes provider name, location (address, city, state, zip, county, latitude and longitude), and contact information (website, phone number).

### Description of Data Processing: 
Data was scraped from the SAMSHA Treatment Locator tool, filtered for mental health providers, cleaned, and then converted to spatial data. 

#### Tract and Zip Code

##### Distance
Next, we conducted the nearest resource analysis using minimum Euclidean distance as a proxy variable for access. This analysis included calculating centroids for all census tracts and ZCTAs, identifying the nearest mental health (MH) provider to each centroid, and calculating the distance in miles. 

##### Travel Time and Count Within Threshold
We calculated travel-network access metrics for the driving travel time to the nearest mental health (MH) provider location and count of MH providers within a 30 minute driving threshold. We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type. For *zip code tabulation areas*, overlapping tract-level measures were averaged, weighted by proportion of the overlapping tract, using the corresponding HUD tract-to-zip code crosswalks. 

Count of providers within a travel threshold (30 minutes and/or 60 minutes) were also calculated for three modes of transit: driving, walking, and biking at the tract level, with corresponding average of overlapping tracts at the ZCTA scale. This analysis was conducted in Python.

In addition, an impedance factor was introduced in 2025 access metrics. Raw travel time measures assume pristine conditions in a best-case-scenario. An impedance approach instead multiples the estimated travel time by a factor, in this case a factor of 2, better approximating actual travel time due to traffic, congestion, etc.

#### County and State 
County and state-level variables include the **count** of Census tracts and the **percent** of Census tracts located within a 30-minute driving threshold of a mental health provider, as well as the mean (average) driving time in minutes from Census tracts within the county or state. 

For 2025 measures, the tract to county and state conversions were completed using R code, and can be found in the corresponding [scripts](https://github.com/healthyregions/oeps/tree/main/scripts) folder on our Github Repository.

### Data Limitations:
*Euclidean or straight-line distance is a simple approximation of access or travel from an origin centroid to the nearest hospital. It is not a precise calculation of real travel times or distances. The travel times are capped at a 90-minute threshold; any data exceeding this limit is left blank. 

### Comments/Notes:
* All nearest distance calculations are in miles. 
* All nearest travel time calculations are in minutes.
* Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
* While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
* The zip code calculation was updated in 2025 to an average of overlapping tract-level metrics, rather than distance from the center of a zip code area. Because zip code areas are large, when compared to census tracts, distance from the geometric center was deemed less meaningful. A detailed notebook comparing the differences will be shared in 2026.
* During the crosswalk process, we used the total ratio from the HUD USPS Crosswalk Files. This ratio represents the proportion of total addresses in a given geographic unit (e.g., census tract) that fall within a corresponding target geographic unit (e.g., ZIP Code). The total ratio was used as a weighting factor to allocate counts and measures proportionally between geographies.
