**Meta Data Name**: Jail Incarceration Variables  
**Date Added**: September 11, 2020  
**Author**: Marynia Kolak, Qinyun Lin, Yilin Lyu  
**Date Last Modified**: October 23, 2025  
**Last Modified By**: Yilin Lyu  

### Theme: 
Social  

### Data Location: 
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  

### Data Source(s) Description:  
Variables were obtained from the Vera Institute of Justice. Raw data and more details can be found at https://github.com/vera-institute/incarceration_trends. Raw data is downloaded in the folder of data_raw, named "incarceration_trends.xlsx". 

OEPS includes version 1 of Vera Institute's data, or county-level measures available from 2017. As of May 2025, an updated version
of the data at county and state level is available for 2024 at [Vera Institute's Github Page](https://github.com/vera-institute/incarceration-trends). 
This will be updated in OEPS by fall 2025.

### Description of Data Processing: 
The following variables were included from the source data:
1. Total jail population rate;
2. Total jail admission rate;
3. Pretrial jail population rate;
4. Total jail population count;
5. Total jail admission count;
6. Pretrial jail population count. 
 
These rates were calculated using base rate of county population aged 15-64 and the unit is per 100K people. They argue that "youth under age 15 and adults over 64 are age groups at very low risk of jail incarceration and because the proportion of these groups varies greatly by county." Also, note that these rates are jail population relative to the total county population. For example, the female jail population rate is calculated as the jail female population divided by the female population (aged 15–64) in that county (multiplied by 100,000). 

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

#### County
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Total jail population rate | TtlJlPpr | Total Jail Population Rate, ASJ/COJ Data | 1970-2024 | County |
| Total jail admission rate | TtlJlAdmr | Total Jail Admissions Rate, ASJ/COJ Data | 1970-2024 | County |
| Pretrial jail population rate | TtlJlPrtr | Pretrial Jail Population Rate | 1970-2024 | County |
| Total jail population count | TtlJlPp | Total Jail Population Count, ASJ/COJ Data | 1970-2024 | County |
| Total jail admission count | TtlJlAdm | Total Jail Admissions Count, ASJ/COJ Data | 1970-2024 | County |
| Pretrial jail population count | TtlJlPrt | Pretrial Jail Population Count | 1970-2024 | County |

#### State
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Total jail population rate | TtlJlPpr | Total Jail Population Rate, ASJ/COJ Data | 1970-2023 | State |
| Total jail admission rate | TtlJlAdmr | Total Jail Admissions Rate, ASJ/COJ Data | 1978-2022 | State |
| Pretrial jail population rate | TtlJlPrtr | Pretrial Jail Population Rate | 1970-2023 | State |
| Total jail population count | TtlJlPp | Total Jail Population Count, ASJ/COJ Data | 1970-2023 | State |
| Total jail admission count | TtlJlAdm | Total Jail Admissions Count, ASJ/COJ Data | 1978-2022 | State |
| Pretrial jail population count | TtlJlPrt | Pretrial Jail Population Count | 1970-2023 | State |

### Data Limitations:
- There is missing data in many counties.
- Most state-level data are available for consistent ranges as shown above, but some states differ. Alaska (AK), Connecticut (CT), Delaware (DE), Rhode Island (RI) miss data from 1970-1977. Hawaii (HI) and Vermont (VT) miss data from 1971-1977.
- See the Vera Insitute's documentation for details on additional limitations.

### Comments/Notes:
- The latest county-level data extend to 2024, but it only includes Quarter 1. Also, pretrial jail population rate and count are largely unavailable; only some counties in Virginia and West Virginia report them.
- County-level data are reported quarterly, with estimates provided for four reference dates each year (March 31, June 30, September 30, and December 31).
- Many states use regional or multi-county jail systems (e.g., WV statewide system, VA regional jails), so counties sharing the same jail receive identical jail population values. These repeated values reflect jail system structure, not actual similarities across counties.
- Some jail counts may be fractional because linear interpolation has been used to replace missing data and apportions regional jail populations across counties based on population share. These estimation steps naturally create non-integer counts.
