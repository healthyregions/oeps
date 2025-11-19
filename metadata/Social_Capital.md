**Metadata Name**:   Social Capital Index

**Date Added**:   October 30, 2025

**Author**: Catherine Discenza  

**Last Modified By**: Catherine Discenza

**Date Last Modified**: November 19, 2025

### Theme

Social

### Data Location

You can find the variables described in this document in the CSV files [here](/data_final/full_tables). CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2018 will be found in C_2000.csv.

### Data Source(s) Description

Population and housing variables were obtained from 2018 and 2023 5-year American Community Survey (ACS) at County and/or Tract levels.

Library and religious institution data were obtained from Overture Maps Foundation. 

### Description of Data Source Tables

**ACS**

**Table B25026**: Total population in occupied housing units by tenue by year householder moved into unit

**Table B98021**: Housing unit response and nonresponse rates with reasons for noninterviews (Data for nation, state, and county levels only)

**Overture**

**Libraries**: library

**Religious Instituions**: anglican_church; baptist_church; catholic_church; church_cathedral; episcopal_church; evangelical_church; pentecostal_church; buddhist_temple; hindu_temple; sikh_temple; religious_destination; religious_items; religious_organization; religious_school; jehovahs_witness_kingdom_hall; mosque; synagogue

### Description of Data Processing
 
The following variables were included from **B98021**:
  1. Estimate; Response Rate
 
The following variables were included from **2018 5-year ACS B25026**:
  1. Estimate; Total population in occupied housing units
  3. Estimate; Owner occupied: Moved in 2017 or later
  4. Estimate; Owner occupied: Moved in 2015 to 2016
  5. Estimate; Owner occupied: Moved in 2010 to 2014
  6. Estimate; Owner occupied: Moved in 2000 to 2009
  7. Estimate; Owner occupied: Moved in 1990 to 1999
  8. Estimate; Owner occupied: Moved in 1989 or earlier
  10. Estimate; Renter occupied: Moved in 2017 or later
  11. Estimate; Renter occupied: Moved in 2015 to 2016
  12. Estimate; Renter occupied: Moved in 2010 to 2014
  13. Estimate; Renter occupied: Moved in 2000 to 2009
  14. Estimate; Renter occupied: Moved in 1990 to 1999
  15. Estimate; Renter occupied: Moved in 1989 or earlier

The following variables were included from **2023 5-year ACS B25026**:
  1. Estimate; Total population in occupied housing units
  3. Estimate; Owner occupied: Moved in 2021 or later
  4. Estimate; Owner occupied: Moved in 2018 to 2020
  5. Estimate; Owner occupied: Moved in 2010 to 2017
  6. Estimate; Owner occupied: Moved in 2000 to 2009
  7. Estimate; Owner occupied: Moved in 1990 to 1999
  8. Estimate; Owner occupied: Moved in 1989 or earlier
  10. Estimate; Renter occupied: Moved in 2021 or later
  11. Estimate; Renter occupied: Moved in 2018 to 2020
  12. Estimate; Renter occupied: Moved in 2010 to 2017
  13. Estimate; Renter occupied: Moved in 2000 to 2009
  14. Estimate; Renter occupied: Moved in 1990 to 1999
  15. Estimate; Renter occupied: Moved in 1989 or earlier

---------- 

* **Long-term occupancy rate** was calculated as : *(Owner & renter populations moved in before 1989 + Owner & renter population moved in between 1990 & 1999) / (Total population in owner & renter occupied units)*

* **2018 5-year ACS Median occupancy rate** was calculated as : *=IF((Owner  & renter populations moved in 2017 or later)>=(Total population in occupied housing units/2),THEN(Moved in 2017 or later),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016)>=(Total population in occupied housing units/2),THEN(Moved in 2015 to 2016),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016 + Owner & renter populations moved in 2010 to 2014)>=(Total population in occupied housing units/2),THEN(Moved in 2010 to 2014),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016 + Owner & renter populations moved in 2010 to 2014 + Owner & renter populations moved in 2000 to 2009)>=(Total population in occupied housing units/2),THEN(Moved in 2000 to 2009),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016 + Owner & renter populations moved in 2010 to 2014 + Owner & renter populations moved in 2000 to 2009 + Owner & renter populations moved in 1990 to 1999)>=(Total population in occupied housing units/2),THEN(Moved in 1990 to 1999),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016 + Owner & renter populations moved in 2010 to 2014 + Owner & renter populations moved in 2000 to 2009 + Owner & renter populations moved in 1990 to 1999 + Ownder & renter populaiton moved in before 1989)>=(Total population in occupied housing units/2),THEN(Moved in 1989 or earlier)))))))*

* **2023 5-year ACS Median occupancy rate** was calculated as : *=IF((Owner  & renter populations moved in 2021 or later)>=(Total population in occupied housing units/2),THEN(Moved in 2021 or later),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020)>=(Total population in occupied housing units/2),THEN(Moved in 2018 to 2020),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020 + Owner & renter populations moved in 2010 to 2017)>=(Total population in occupied housing units/2),THEN(Moved in 2010 to 2017),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020 + Owner & renter populations moved in 2010 to 2017 + Owner & renter populations moved in 2000 to 2009)>=(Total population in occupied housing units/2),THEN(Moved in 2000 to 2009),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020 + Owner & renter populations moved in 2010 to 2017 + Owner & renter populations moved in 2000 to 2009 + Owner & renter populations moved in 1990 to 1999)>=(Total population in occupied housing units/2),THEN(Moved in 1990 to 1999),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020 + Owner & renter populations moved in 2010 to 2017 + Owner & renter populations moved in 2000 to 2009 + Owner & renter populations moved in 1990 to 1999 + Ownder & renter populaiton moved in before 1989)>=(Total population in occupied housing units/2),THEN(Moved in 1989 or earlier)))))))*

* **Libraries per capita** was calculated as : *(Number of libraries in tract) / (Total population in owner & renter occupied units)*

* **Religious institutions per capita** was calculated as : *(Number of religious institutions in tract) / (Total population in owner & renter occupied units)*

Note: Unpopulated census tracts removed from dataset.

### Key Variables and Definitions

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable | Variable ID | Description | Years Available | Spatial Scale |
|:--|:--|:--|:--|:--|
| Housing Tenure | MedHsgTen | Median time period occupant moved into housing unit by tract | 2018, 2023 | Tract |
| Long-Term Occupancy | LngTermP | Percentage of population who moved into their current housing approximately more than 20 years ago | 2018, 2023 | Tract|
| Libraries per Capita | LibPerCap | Libraries per capita | 2025 | Tract |
| Religious Institutions per Capita| RlgPerCap | Religious institutions per capita | 2025 | Tract |
| Response Rate| RspRt | Percent of units interviewed from total units intended for interview | 2018, 2023 | County |


### Data Limitations

- The ACS does not gather information in the U.S. territories American Samoa, Guam, Northern Mariana Islands and U.S. Virgin Islands. It does include information for Puerto Rico & Washington, D.C.
- Overture Maps Foundation began data releases in 2024, no data specific to 2018 and 2023 is available. 2025 data was extracted for completeness and applied to both 2018 and 2023 data.
- 
### Comments/Notes
