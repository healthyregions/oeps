**Meta Data Name**: Access to MOUDs  
**Date Added**: February 1, 2021  
**Author**: Marynia Kolak, Mahjabin Kabir Adrita, Wataru Morioka, Susan Paykin, Yilin Lyu, Mallikarjun Bhusnoor   
**Date Last Modified**: January 24, 2026   
**Last Modified By**: Mallikarjun Bhusnoor

### Data Source(s) Description:

#### Medications for Opioid Overuse Disorder (MOUDs)
Data on providers prescribing Medications for Opioid Overuse Disorder (MOUDs) and their locations were sourced from the [U.S. Substance Abuse and Mental Health Services Administration (SAMHSA) Treatment Locator](https://findtreatment.samhsa.gov/locator) for all time periods. 

We extracted the following from SAMSHA’s Treatment Locator Service in September 2020:

- **Buprenorphine**: All prescribers listed. 
- **Methadone**: All providers tagged as providing “methadone maintenance.”
- **OTP**: All providers tagged as “opioid treatment providers.”
- **Naltrexone**: All providers tagged as providing “naltrexone.”

Naltrexone provider data from SAMHSA in 2019 was supplemented by provider data from Vivitrol.com, with duplicates removed.

The following was extracted in May 2025 from SAMSHA’s Treatment Locator Service:

 - **Buprenorphine**: All prescribers listed.
 - **Telehealth**: All providers offering buprenorphine treatment via "telemedicine/telehealth" services.
 - **Methadone**: Methadone: All providers tagged as providing “methadone.” The term methadone maintenance was no longer visible as a feature in the locator service.
 - **OTP**: All providers tagged as “opioid treatment providers.”
 - **Naltrexone**: All providers tagged as providing “naltrexone.”

 For Opioid Treatment Programs, measures for all years were extracted from the U.S. Substance Abuse and Mental Health Services Administration (SAMHSA) [Opioid Treatment Program (OTP) Directory](https://dpt2.samhsa.gov/treatment/directory.aspx). The OTPs represented in this set are those certified, either fully or provisionally by SAMHSA. Certification is required for MOUD, but these programs can offer other types of treatment, including counseling and other behavioral therapies. Raw data can be found [here](https://dpt2.samhsa.gov/treatment/directory.aspx) and more information can be found [here](https://www.samhsa.gov/medication-assisted-treatment/become-accredited-opioid-treatment-program).


#### Street Network Topology & Travel Time Matrices
Data on street and pedestrian networks to calculate travel time metrics were sourced from multiple open source data portals. Street network topologies (including street orientations and speed/travel time) all derive from [OpenStreetMap](https://www.openstreetmap.org), also known as OSM.

- For 2019, the **travel time matrices** for driving, biking and walking were sourced from [Project OSRM](https://project-osrm.org/), calculated by Vidal Anguiano (University of Chicago), and are available at the Tract or ZCTA scales.
- For 2025, the **travel time matrices** for driving were sourced from OpenStreetMap using [OSMnx](https://osmnx.readthedocs.io/en/stable/) and [SPASTC](https://doi.org/10.1080/13658816.2024.2326445), calculated by [Alex Michels](https://alexandermichels.github.io/) (University of Texas at Dallas), and are available at the tract scales.

In our approach, a travel time is calculated from the center of each census tract, to the center of another census tract, up to 90 minutes away. These time tables are calculated for across the country, and can be referenced by tract FIPS (unique ID) code.

### Description of Data Processing: 
Data was identified, wrangled, cleaned, and prepared for analysis. For 2019 locations that needed geocoding, we used the [tidygeocoder](https://cran.r-project.org/web/packages/tidygeocoder/vignettes/tidygeocoder.html) package in R, as well as supplemental geocoding through University of Chicago Library GIS services. Data extracted in 2025 was already complete with spatial coordinate information.

#### Tract and ZIP Code

##### Distance
We conducted the nearest resource analysis from geography centroid to MOUD provider location by type (buprenorphine, methadone, naltrexone) to calculate the nearest Euclidean distance (i.e. straight line distance) for each MOUD. This analysis was conducted in R. Some of the scripts are available in [code/access_MOUDs.R](https://github.com/GeoDaCenter/opioid-policy-scan/blob/v1.0/code/access_MOUDs.R), and will be updated by 2026 with standardized codebooks.

##### Travel Time and Count Within Threshold

We calculated travel-network access metrics for every census tract centroid to the census tract centroid of nearest provider type, up to 90 minutes away. For *zip code tabulation areas*, overlapping tract-level measures were averaged, weighted by proportion of the overlapping tract, using the corresponding HUD tract-to-zip code crosswalks. 

Count of providers within a travel threshold (30 minutes and/or 60 minutes) were also calculated for three modes of transit: driving, walking, and biking at the tract level, with corresponding average of overlapping tracts at the ZCTA scale. 

This analysis was conducted in Python. The scripts are available in code/AccessMetrics - MOUDs. Some of the scripts are available in [code/AccessMetrics - MOUDs.](https://github.com/GeoDaCenter/opioid-policy-scan/tree/fc3d94053dd1941a96a5945d73cc6f4845453484/code/Access%20Metrics%20-%20MOUD), with complete computational notebooks which can be found in [scripts/Calculate_Access_Metrics (2).ipynb] (https://github.com/healthyregions/oeps/blob/270-MOUD-2025-Update-(-BUP%2C-MET%2C-NAL-%2C-OTP-%2C-Near-by-MOUD)/scripts/Calculate_Access_Metrics%20(2).ipynb) 

#### County and State 
County and state-level variables include the **count** of Census tracts and the **percent** of Census tracts located within a 30 minute driving threshold of an MOUD type, as well as the mean (average) driving time in minutes from Census tracts within the county or state. 

### Data Limitations:
All access metrics should be considered approximations, as estimates are calculated from locations within administrative units. Furthermore, resource data only represents *potential* access or spatial availability, reflecting resources made available on a publicly available website. Much research has shown that data on SAMHSA does not represent actual availability, as not all providers may in fact prescribe MOUD medications, some providers may not be accepting new patients, and multiple  factors such as access to insurance, policy matters, and stigma may serve as additional barriers to MOUDs. 

### Comments/Notes:
* All nearest distance calculations are in miles. 
* All nearest travel time calculations are in minutes.
* Not all metrics are available for U.S. places beyond the continental States; we recommend exploring the data on the OEPS Explorer web map to examine in more depth.
* While a different time travel calculation was performed in 2025, the street network topology original source (Open Street Map) remained the same.
* The zip code calculation was updated in 2025 to an average of overlapping tract-level metrics, rather than distance from the center of a zip code area. Because zip code areas are large, when compared to census tracts, distance from the geometric center was deemed less meaningful. A detailed notebook comparing the differences will be shared in 2026.
* During the crosswalk process, we used the total ratio from the HUD USPS Crosswalk Files. This ratio represents the proportion of total addresses in a given geographic unit (e.g., census tract) that fall within a corresponding target geographic unit (e.g., ZIP Code). The total ratio was used as a weighting factor to allocate counts and measures proportionally between geographies.
