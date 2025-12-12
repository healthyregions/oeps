**Meta Data Name**: Medicaid Policy Proportion  
**Date Added**: November 05, 2025  
**Author**: Saket Pochiraju  
**Date Last Modified**: December 12, 2025      
**Last Modified By**: Saket Pochiraju    

### Theme: 
Policy

### Data Location: 
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  

### Data Source(s) Description:  

Variables were obtained for 2014 through 2024 from the ['Status of State Action on the Medicaid Expansion Decision' dataset / indicator](https://www.kff.org/affordable-care-act/state-indicator/state-activity-around-expanding-medicaid-under-the-affordable-care-act/) maintained by KFF, a health policy organization, through their tracking and analysis of state executive activity. The source data was updated most recently in September 2025 and accessed in December 2025.

The dataset includes the Expansion Implementation Date as applicable for each state, based on which our calculation of proportions are done; an indicator variable (as described below) for Status of Medicaid Expansion Decision; and additional variables on whether (& when) Expansion was adopted through a Ballot Initiative and whether there is a Trigger Law in place.

### Description of Data Processing: 
The following variables were included from the source data:

1. Status of Medicaid Expansion Decision, a dummy variable indicating whether a state has adopted state-level policy action on the Medicaid Expansion decision ("Adopted") or not ("Not Adopted")

Our first variable, Medicaid Policy Proportion, was calculated as a proportion of each year from 2014 to 2024 for which Medicaid Expansion was adopted / in effect in a state. For example, if Alaska adopted Medicaid Expansion on 9/1/2015, their proportion should be 0 for 2014, 0.333 (as Medicaid Expansion was adopted for four months -> 1/3rd of that calendar year) for 2015, and 1 for each year afterwards through 2024.  

Two broader five-year variables (2014 - 2019 Medicaid Expansion Proportion and 2020 - 2024 Medicaid Expansion Proportion) were also created to capture the proportion of the periods 2014 - 2019 and 2020 - 2024 for which Medicaid Expansion was implemented in a state.

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Medicaid Expansion Proportion | MedPolProp | Proportion of given year for which Medicaid Expansion was implemented / in effect | 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | State |
| 2014 - 2019 Medicaid Expansion Proportion | 14to19MedPolProp | Proportion of the period from 2014 - 2019 for which Medicaid Expansion was implemented / in effect | 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | State | 
| 2020 - 2024 Expansion Proportion | 20to24MedPolProp | Proportion of the period from 2020 - 2024 for which Medicaid Expansion was implemented / in effect | 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024 | State | 

### Data Limitations / Additional Information:
See source documentation for details. Additional information, such as a downloadable map and a detailed table of the state actions adopting Medicaid expansion, can be accessed [here](https://www.kff.org/medicaid/status-of-state-medicaid-expansion-decisions/).

### Comments/Notes: 
Calculations of proportions were rounded to three decimal places. 

Also, rather than accounting for the specific number of days in each month, proportions calculation was done in terms of months (e.g. New Hampshire's implementation date of 8/15/14 was the 227th day of that year, meaning the policy was in effect for 139 out of 365 days or roughly 38.082% of the year. However, the calculation currently accounts for it as 4.5 months of Medicaid expansion in effect during 2014 after that date, making that percentage of the year 37.5% and the proportion ultimately used 0.375).
