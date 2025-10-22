**Meta Data Name**: Prison Incarceration Variables  
**Date Added**: September 11, 2020  
**Author**: Marynia Kolak, Qinyun Lin, Yilin Lyu  
**Date Last Modified**: October 21, 2025  
**Last Modified By**: Yilin Lyu  

### Theme:
Policy

### Data Location: 
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  
Note: Every variable can be found in the **Latest** files.

### Data Source(s) Description:  
Variables were obtained from the Vera Institute of Justice. Raw data and more details can be found at https://github.com/vera-institute/incarceration_trends. Raw data is downloaded in the folder of data_raw, named "incarceration_trends.xlsx". 

OEPS includes version 1 of Vera Institute's data, or county-level measures available from 2017. As of May 2025, an updated version
of the data at county and state level is available for 2024 at [Vera Institute's Github Page](https://github.com/vera-institute/incarceration-trends). 
This will be updated in OEPS by fall 2025.

### Description of Data Processing: 
The following variables were included from the source data:
 1. Total prison population rate;
 2. Total prison admission rate;
 3. Total prison population count;
 4. Total prison admission count;

These rates were calculated using base rate of county population aged 15-64. They argue that "youth under age 15 and adults over 64 are age groups at very low risk of jail incarceration and because the proportion of these groups varies greatly by county." 

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

#### County
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Total prison population rate | TtlPrPpr | Total Prison Population Rate | 1983-2019 | County |
| Total prison admission rate | TtlPrAPpr | Prison Prison Admissions Rate | 1983-2019 | County |
| Total prison population count | TtlPrPp | Total Prison Population Count| 1983-2019 | County |
| Total prison admission count | TtlPrAPp | Prison Prison Admissions Count | 1983-2019 | County |

#### State
| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Total prison population rate | TtlPrPpr | Total Prison Population Rate | 1969-2024 | State |
| Total prison admission rate | TtlPrAPpr | Prison Prison Admissions Rate | 1978-2022 | State |
| Total prison population count | TtlPrPp | Total Prison Population Count| 1950-2024 | State |
| Total prison admission count | TtlPrAPp | Prison Prison Admissions Count | 1978-2022 | State |

### Data Limitations:
There are missing data in many counties. 

### Comments/Notes:
- Most state-level data are available for consistent ranges as shown above, but some states differ. The federal system (FED) only includes 2005 data for total prison population rate and admission rate, covers 1978–2024 for total prison population count, and 1978–1989 and 1993–2022 for total prison admission count. Georgia (GA) has data from 1970–2022 for total prison admission rate and admission count. The District of Columbia (DC) is missing 2001–2011 and 2024 for total prison population rate and count, and 2001–2003 and 2019–2022 for total prison admission rate and count. Alaska (AK) is missing 1994 and 2006 data for total prison admission rate and count.
