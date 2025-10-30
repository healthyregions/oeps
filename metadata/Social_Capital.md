**Metadata Name**:   Social Capital Index

**Date Added**:   October 30, 2025

**Author**: Catherine Discenza  

**Last Modified By**: Catherine Discenza

**Date Last Modified**: October 30, 2025

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

- Response rate reported as a percent
- Libraries calculated per capita at tract level
- Religious institutions calculated per capita at tract level
- Median housing tenure calculated at tract level and reported as a time period of 10 or fewer years

### Key Variables and Definitions

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable | Variable ID | Description | Years Available | Spatial Scale |
|:--|:--|:--|:--|:--|
| Housing Tenure | MedianHt | Median time period householder moved into unit by tract | 2018, 2023 | Tract |
| Libraries | Libpercap | Libraries per capita | 2025 | Tract |
| Religious Institutions| Relgpercap | Religious institutions per capita | 2025 | Tract |
| Response Rate| Resprate | Ratio of units interviewed to units intended for interview | 2018, 2023 | County |


### Data Limitations

- The ACS does not gather information in the U.S. territories American Samoa, Guam, Northern Mariana Islands and U.S. Virgin Islands. It does include information for Puerto Rico & Washington, D.C.
- Overture Maps Foundation began data releases in 2024, no data specific to 2018 and 2023 is available. 2025 data was extracted for completeness.
- 
### Comments/Notes
