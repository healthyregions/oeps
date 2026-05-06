**Meta Data Name**: Bup Policy Proportion  
**Date Added**: November 05, 2025  
**Author**: Saket Pochiraju  
**Date Last Modified**: December 12, 2025      
**Last Modified By**: Saket Pochiraju    

### Theme: 
Policy

### Data Source(s) Description:  

**State Buprenorphine Policies**

Data were acquired from [Law Atlas](https://lawatlas.org/datasets/buprenorphine-prescribing-requirements-and-limitations) on state-level policies with prescribing requirements and limitations for Buprenorphine. This is a longitudinal dataset created and maintained by the Center for Public Health Law Research and Vital Strategies that captures the laws in effect between March 1, 2023, and September 1, 2024, across all 50 states and the District of Columbia. Data was most recently accessed in December 2025.

Important to note is that the dataset does not include laws or policies that regulate buprenorphine prescribing exclusively within state Medicaid programs. Additional information on the scope of state laws that this dataset captures is available in their [Research Protocol document](https://lawatlas.org/sites/default/files/2025-03/Buprenorphine%20Rx_Codebook%203.4.25.pdf), and the coding forms used for variables are available in [this Codebook](https://lawatlas.org/sites/default/files/2025-03/Buprenorphine%20Rx_Codebook%203.4.25.pdf).

The data used for this analysis is a variable encoded as BRx_oud, a binary variable that answers the following question: 
- "Does the state explicitly regulate buprenorphine prescribing 
for opioid use disorder (OUD)?"
- 0 represents No and 1 represents Yes

This data is available to download and work with at [this link](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Flawatlas.org%2Fsites%2Fdefault%2Ffiles%2F2025-03%2FBuprenorphine_Prescribing_Data_3.4.25.xlsx&wdOrigin=BROWSELINK).

For each state during the time period of data coverage, March 1st, 2023 to September 1st, 2024, any changes to the state policy landscape regarding buprenorphine were represented as a new policy and entered as a new row in the spreadsheet with the associated dates - 'Effective Date' and 'Valid Through Date' - for that policy. These dates reflect the date that the policy coded was put into effect and the last date the policy was in effect, respectively. While this was the entire time period for certain policies in some jurisdictions (states), other states had multiple different policies implemented within the period of data coverage.

### Description of Data Processing: 

The policy variables here were created by calculating the proportion of a) the year and b) the entire data coverage period for which policies explicity regulating buprenorphine prescription for opioid use disorder (OUD) - as captured by a value of 1 for the BRx_oud variable - were in effect. 

As a third variable, associated date ranges for periods of policy implementation are stored and provided as well. If a state had no relevant policy implemented in the given year, the value of this variable is left blank.

 These calculations were done in Excel and followed the basic formulas of:
 
a) ('Valid Through Date' - 'Effective Date') / (latest data available for year: 12/31/2023 or 9/1/2024 minus earliest date available for year: 3/1/2023 or 1/1/2024) (given year timespan) for the first variable 

and 

b) ('Valid Through Date' - 'Effective Date') / (9/1/2024 - 3/1/2023) (period of entire data coverage) for the second variable. 
 
In states where multiple policies regulating buprenorphine went into effect, the overall sum period of regulation (across which all policies had a value of 1 for BRx_oud) was taken and used in the calculation.

### Data Limitations:

- Data was only available through this source between March 2023 and September 2024. As such, the proportions are calculated to reflect this specifically and policies prescribing requirements/limitations may have been in effect during other parts of the given years that were not captured in the data used to provide the 'Periods of Buprenorphine Policy Implementation' variable.

### Comments/Notes:
Calculated proportions were rounded to three decimal places.

A paper whose data and methodology may be helpful to capture state-level buprenorphine policy in earlier years could be [Stein et al. (2023)](https://jamanetwork.com/journals/jama-health-forum/fullarticle/2805495), who used 6 selected policies to study the association between state policies and buprenorphine dispensing from 2006 to 2018.

Dataset citation:
Temple University Center for Public Health Law Research &amp; Vital Strategies
																		(March 26, 2025). “Buprenorphine Prescribing Regulations and Limitations”.
																		LawAtlas.org.
																		https://doi.org/10.60541/snt6-m904
