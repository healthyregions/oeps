**Meta Data Name**: Naloxone Policy Variables  
**Date Added**: January 8, 2021  
**Author**: Qinyun Lin, Wataru Morioka, Mahjabin Kabir Adrita  
**Date Last Modified**: May 12, 2025  
**Last Modified By**: Wataru Morioka, Mahjabin Kabir Adrita  

### Theme: 
Policy

### Data Location: 
You can find the variables described in this document in the CSV files [here](../full_tables).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  
Note: Every variable can be found in the **Latest** files.

### Data Source(s) Description:  
Variables were obtained from RAND-USC Schaeffer Opioid Policy Tools and Information Center, [OPTIC-Vetted Naloxone Policy Dat](https://www.rand.org/health-care/centers/optic/resources/datasets.html), accessed on Jan 7th, 2021. Raw data is downloaded in the folder of [data_raw](https://github.com/GeoDaCenter/opioid-policy-scan/tree/v1.0/data_raw), named as *WEB_NAL.xlsx*. 

### Description of Data Processing: 
The following variables were included from the source data:
1. Any Naloxone law effective date;
2. Naloxone law allowing distribution through a standing or protocal order effective date;
3. Naloxone law allowing pharmacists prescriptive authority effective date; 
4. Fraction of year with any Naloxone law effective;
5. Fraction of year with Naloxone law allowing distribution through a standing or protocal order effective;
6. Fraction of year with Naloxone law allowing pharmacists prescriptive authority effective. 

Fractions are calculated based on the number of months out of 12 that a law is effective. A law is considered effective for a given month if a law becomes effective by the 7th for January, or if a law becomes effective by the 3rd for February – December.

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Any Naloxone law effective date | AnyNalxDt | Date (MY) any type of Naloxone law effective | 2017, 2022 | State |
| Naloxone law allowing distribution through a standing or protocal order effective date | NalxPrStDt | Date (MY) Naloxone law allowing distribution through a standing or protocol order effective | 2017, 2022 | State |
| Naloxone law allowing pharmacists prescriptive authority effective date | NalxPresDt | Date (MY) Naloxone law allowing pharmacists prescriptive authority effective | 2017, 2022 | State |
| Fraction of year with any Naloxone law effective | AnyNalxFr | Fraction of year any type of Naloxone law is effective | 2017, 2022 | State |
| Fraction of year with Naloxone law allowing distribution through a standing or protocal order effective | NalxPrStFr | Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order | 2017, 2022 | State |
| Fraction of year with Naloxone law allowing pharmacists prescriptive authority effective |  NalxPresFr | Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority | 2017, 2022 | State |

### Data Limitations:
N/A.

### Comments/Notes:
1. Specific dimensions of Naloxone policy data included in this public version of the data are based on a review of relevant protections granted through different variations of these laws as described in:
* Davis, C. S., & Carr, D. (2015). Legal changes to increase access to naloxone for opioid overdose
reversal in the United States. *Drug and alcohol dependence*, *157*, 112-120.
* Davis, C., & Carr, D. (2017). State legal innovations to encourage naloxone dispensing. *Journal of the American Pharmacists Association*, *57*(2), S180-S184. 
2. Notes on effective dates:
* In Iowa, the legislature adopted two different bills (one house bill and one senate bill) regarding this section, both with an effective date of May 27, 2016. However, one amended the section and made those amendments retroactive to April 6, 2016. However, given no action could be taken on the retroactive date, we assume the PDAPS effective date of 5/27/2016 – thus, it is coded as June 2016.
* In Jan 2008, California piloted naloxone programs in several counties (including the most populous LA and SF). However, this was not expanded statewide until January 2014. PDAPS uses the pilot date for the first law (2008), which is what we use here for "any NAL." However, one could make the argument that the 2014 date is preferable.
