**Meta Data Name**: Prison Incarceration Variables  
**Date Added**: September 11, 2020  
**Author**: Marynia Kolak, Qinyun Lin, Yilin Lyu  
**Date Last Modified**: February 12, 2026  
**Last Modified By**: Yilin Lyu  

### Data Source(s) Description:  

#### Resources
Prison incarceration variables were obtained from the Vera Institute of Justice, which maintains the Incarceration Trends dataset documenting prison and jail populations across the United States.

Raw data and documentation are publicly available through the Vera Institute’s GitHub repository. OEPS uses Version 1 of the Vera data for county-level prison measures beginning in 2017. As of May 2025, updated county- and state-level prison data through 2024 are available at [Vera Institute's Github Page](https://github.com/vera-institute/incarceration-trends). 

#### Geographic Boundaries
ZIP Code Tract Area (ZCTA) and Census Tract boundary files were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018, 2020](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html). 
A copy of the geographic boundary files used can be found at the [HEROP GeoData Web Archive](https://geodata.healthyregions.org/).

### Description of Data Processing: 
The Vera Institute prison dataset includes annual state-level and county-level measures derived from administrative correctional records. The following prison-related variables are included in OEPS:
1. Total prison population rate
2. Total prison admission rate
3. Total prison population count
4. Total prison admission count

Rates are calculated by the Vera Institute using the county population aged 15–64 as the denominator. This age range is used because populations under 15 and over 64 have a very low risk of incarceration, and their proportions vary substantially across counties.


State Map:

<img width="778" height="487" alt="State Map_Prison_2024_Natural Break" src="https://github.com/user-attachments/assets/12fb953b-3906-404e-901e-41058d2d4310" />

County Map:

<img width="778" height="487" alt="County Map_Prison_2019_Natural Break" src="https://github.com/user-attachments/assets/dfc70206-e6f7-4a81-b034-bbe7428eabaa" />

### Data Limitations:
- There are missing data in many counties. Prison admission data are not available after 2020.
- Some states (e.g., Alaska) do not report prison data by county of commitment, so the same statewide prison population count and rate has been assigned to every county. These identical values reflect missing county-level detail, not real uniformity.
- Some prison counts are estimates or filled using linear interpolation, which can produce fractional values instead of whole numbers. These decimals reflect estimation methods, not actual observed counts.

### Comments/Notes:
- County-level data are reported annually.
- This dataset includes year from 2016 to 2024, please see the Vera Institute’s raw data and documentation for data before that.
- Some prison counts are estimates or filled using linear interpolation, which can produce fractional values instead of whole numbers. These decimals reflect estimation methods, not actual observed counts.
