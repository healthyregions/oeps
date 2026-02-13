**Meta Data Name**: Jail Incarceration Variables  
**Date Added**: September 11, 2020  
**Author**: Marynia Kolak, Qinyun Lin, Yilin Lyu  
**Date Last Modified**: February 12, 2026  
**Last Modified By**: Yilin Lyu  

### Data Source(s) Description:  

#### Resources
Jail incarceration variables were obtained from the Vera Institute of Justice, which maintains the Incarceration Trends dataset documenting prison and jail populations across the United States.

Raw data and documentation are publicly available through the Vera Institute’s GitHub repository. OEPS uses Version 1 of the Vera data for county-level prison measures beginning in 2017. As of May 2025, updated county- and state-level prison data through 2024 are available at  [Vera Institute's Github Page](https://github.com/vera-institute/incarceration-trends). 

#### Geographic Boundaries
ZIP Code Tract Area (ZCTA) and Census Tract boundary files were sourced from the [US Census Bureau, TIGER/Line Shapefiles 2018, 2020](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html). 
A copy of the geographic boundary files used can be found at the [HEROP GeoData Web Archive](https://geodata.healthyregions.org/).

### Description of Data Processing: 
The Vera Institute prison dataset includes annual state-level and county-level measures derived from administrative correctional records. The following prison-related variables are included in OEPS:
1. Total jail population rate;
2. Total jail admission rate;
3. Pretrial jail population rate;
4. Total jail population count;
5. Total jail admission count;
6. Pretrial jail population count. 
 
Rates are calculated by the Vera Institute using the county population aged 15–64 as the denominator. This age range is used because populations under 15 and over 64 have a very low risk of incarceration, and their proportions vary substantially across counties.

Note that these rates are jail population relative to the total county population. For example, the female jail population rate is calculated as the jail female population divided by the female population (aged 15–64) in that county (multiplied by 100,000).


State Map:

<img width="778" height="487" alt="State Map_Jail_2023_Natural Break" src="https://github.com/user-attachments/assets/2cf23d18-5007-4786-8efc-7f663ad9b315" />

County Map:

<img width="778" height="487" alt="County Map_Jail_2024Q1_Natural Break" src="https://github.com/user-attachments/assets/3d27ed20-044d-426e-8b53-ec5f26ae4a10" />

### Data Limitations:
- There is missing data in many counties.
- County-level data are reported quarterly, with estimates provided for four reference dates each year (March 31, June 30, September 30, and December 31). The latest county-level data extend to 2024, but it only includes Quarter 1.
- Pretrial jail population rate and count are largely unavailable; only some counties in Virginia and West Virginia report them.
- Many states use regional or multi-county jail systems (e.g., WV statewide system, VA regional jails), so counties sharing the same jail receive identical jail population values. These repeated values reflect jail system structure, not actual similarities across counties.
- Some jail counts may be fractional because linear interpolation has been used to replace missing data and apportions regional jail populations across counties based on population share. These estimation steps naturally create non-integer counts.

### Comments/Notes:
- This dataset includes year from 2017 to 2024, please see the Vera Institute’s raw data and documentation for data before that.
