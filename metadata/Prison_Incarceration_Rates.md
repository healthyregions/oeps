**Meta Data Name**: Prison Incarceration Variables  
**Date Added**: September 11, 2020  
**Author**: Marynia Kolak, Qinyun Lin, Yilin Lyu  
**Date Last Modified**: October 23, 2025  
**Last Modified By**: Yilin Lyu  

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

### Data Limitations:
- There are missing data in many counties. Prison admission data are not available after 2020.
- Some states (e.g., Alaska) do not report prison data by county of commitment, so the same statewide prison population count and rate has been assigned to every county. These identical values reflect missing county-level detail, not real uniformity.
- Some prison counts are estimates or filled using linear interpolation, which can produce fractional values instead of whole numbers. These decimals reflect estimation methods, not actual observed counts.

### Comments/Notes:
- County-level data are reported annually.
- This dataset includes year from 2016 to 2024, please see the Vera Institute’s raw data and documentation for data before that.
- Some prison counts are estimates or filled using linear interpolation, which can produce fractional values instead of whole numbers. These decimals reflect estimation methods, not actual observed counts.
