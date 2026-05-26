# Project Id: oeps-391119

1 dataset in this project: tabular

## tabular

58 tables in this dataset.

### county-2022

ID: `oeps-391119.tabular.county-2022`

8 columns in this table.

Name|Data Type|Description
-|-|-|-
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking
OpRxRt|NUMERIC|Opioid prescription rate
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation

### state-2024

ID: `oeps-391119.tabular.state-2024`

9 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlPrPp|INTEGER|Total Prison Population Count
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MedPolP5Yr|NUMERIC|Proportion of the five-year period (ending in given year) for which Medicaid Expansion was implemented / in effect
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
EdBupPolP|NUMERIC|Proportion of Entire Data Period with State-Level Buprenorphine Policy in Effect
BupPolP|NUMERIC|Proportion of Year with State-Level Buprenorphine Policy in Effect
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
PerImpBupP|STRING|Periods of Implementation of State-Level Buprenorphine Policy (Associated Date Ranges)
TtlPrPpr|NUMERIC|Total Prison Population Rate

### state-2019

ID: `oeps-391119.tabular.state-2019`

54 columns in this table.

Name|Data Type|Description
-|-|-|-
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MulHcvD|NUMERIC|
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
FlHcvD|INTEGER|Hepatitis C deaths among women
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
NtPrFrDsSy|BOOLEAN|Dummy variable indicating whether the state law does not prohibit free distribution of syringes (0=no, 1=yes)
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
WhtHcvD|NUMERIC|
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MedPolP5Yr|NUMERIC|Proportion of the five-year period (ending in given year) for which Medicaid Expansion was implemented / in effect
WlfrExp|INTEGER|Total expenditures on public welfare programs
NoPrphLw|BOOLEAN|Dummy variable indicating whether the state has no state drug paraphernalia law (0=no, 1=yes)
NoIntP|NUMERIC|Percentage of Households without Internet access
NoLwRmUnc|BOOLEAN|Dummy variable indicating whether the state has no law removing barriers or uncertainty as to SSP legality (0=no, 1=yes)
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
MlHcvD|INTEGER|Hepatitis C deaths among men
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
PrNtRefInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law does not refer to objects used for injecting drugs (0=no, 1=yes)
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
PrExcInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law explicitly exludes objects used for injecting drugs (0=no, 1=yes)
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
HlthExp|INTEGER|Total expenditures on public health and hospitals
CrrctExp|INTEGER|Total expenditures on corrections system and operations
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
OdMortRt|NUMERIC|Overdose mortality rate
ExpSsp|BOOLEAN|Dummy variable indicating whether the state has law that explicitly authorizes Syringe Service Programs (0=no, 1=yes)
HcvD|INTEGER|Total Hepatitis C deaths
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AsHcvD|NUMERIC|
NhPiHcvD|NUMERIC|
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
MedcdExp|INTEGER|Total medicaid spending

### tract-2021

ID: `oeps-391119.tabular.tract-2021`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.

### county-2016

ID: `oeps-391119.tabular.county-2016`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlPrPp|INTEGER|Total Prison Population Count
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TtlPrAPp|INTEGER|Prison Prison Admissions Count
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
OdMortRt|NUMERIC|Overdose mortality rate
TtlPrPpr|NUMERIC|Total Prison Population Rate

### county-2010

ID: `oeps-391119.tabular.county-2010`

46 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
TotVetPop|INTEGER|Total Veteran population
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Age15_44|INTEGER|Total population between age 15-44
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
ChildrenP|NUMERIC|Percentage of population under age 18

### state-2023

ID: `oeps-391119.tabular.state-2023`

71 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
EngProf|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
Ovr16P|NUMERIC|
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
GradSclP|NUMERIC|
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
EduHsP|NUMERIC|
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
TradSttExp|INTEGER|Traditional medicaid - state spending
EdBupPolP|NUMERIC|Proportion of Entire Data Period with State-Level Buprenorphine Policy in Effect
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
TradFedExp|INTEGER|Traditional medicaid - federal spending
Ovr16|NUMERIC|
BupPolP|NUMERIC|Proportion of Year with State-Level Buprenorphine Policy in Effect
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
ExpnFedExp|INTEGER|Expansion Group - Federal Spending
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
Ovr21|NUMERIC|
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
Ovr18|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
PerImpBupP|STRING|Periods of Implementation of State-Level Buprenorphine Policy (Associated Date Ranges)
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
MedcdExp|INTEGER|Total medicaid spending
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
ExpnSttExp|INTEGER|Expansion Group - State Spending

### county-2017

ID: `oeps-391119.tabular.county-2017`

10 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
PrcNtvRsrv|NUMERIC|Percentage of county land area that belongs to Native American reservation(s)
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
OdMortRt|NUMERIC|Overdose mortality rate
TtlJlPrt|NUMERIC|Pretrial Jail Population Count

### county-2015

ID: `oeps-391119.tabular.county-2015`

4 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
DmySgrg|BOOLEAN|Dummy variable for whether county is part of a hypersegregated city or its metropolitan area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OdMortRt|NUMERIC|Overdose mortality rate

### state-2017

ID: `oeps-391119.tabular.state-2017`

53 columns in this table.

Name|Data Type|Description
-|-|-|-
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
TotHcv|NUMERIC|Mean total yearly Hepitatis C cases from 2013-2016
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
AvAmInHcvD|NUMERIC|Mean yearly Hepatitis C deaths among American Indian population from 2013-2017
FlHcvD|INTEGER|Hepatitis C deaths among women
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
A50_74Hcv|NUMERIC|Mean yearly Hepatitis C cases in people between 50 to 74 years of age from 2013-2016
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
AvHspHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Hispanic populations from 2013-2017
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
AvAsPiHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Asian and Pacific Islanders population from 2013-2017
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ov75Hcv|NUMERIC|Mean yearly Hepatitis C cases in people over 75 years of age from 2013-2016
AvU50HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people under 50 years of age from 2013-2017
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
FmHcv|NUMERIC|Mean yearly Hepatitis C cases in women from 2013-2016
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
MlHcvD|INTEGER|Hepatitis C deaths among men
AvFlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among women from 2013-2017
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
BlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations identified as non-hispanic Black alone across 2013-2016
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
AvA50_74HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people between 50 and 74 years of age from 2013-2017, 2018-2022
Un50Hcv|NUMERIC|Mean yearly Hepatatis C cases in people under 50 years of age from 2013-2016
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
MlHcv|NUMERIC|Mean yearly Hepatitis C cases in men from 2013-2016
NonBlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations non-Black other race/ethnicity populations 2013-2016
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
OdMortRt|NUMERIC|Overdose mortality rate
HcvD|INTEGER|Total Hepatitis C deaths
AvBlkHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Black populations from 2013-2017
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AvMlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among men from 2013-2017
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
AvHcvD|NUMERIC|Mean total yearly Hepatitis C deaths from 2013-2017, 2018-2022
AvO75HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people over 75 years of age

### state-2025

ID: `oeps-391119.tabular.state-2025`

29 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpCtTmDr2|NUMERIC|Number of tracts with Opioid Treatment Provider within a 30-min driving range, with Impedance factor
BupAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest buprenorphine provider
SutCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
NaltAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest naltrexone provider
MetAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Methadone Provider(MET), with Impedance factor
SmokeP|NUMERIC|Percentage of Smoking Population
MetTmDrP2|NUMERIC|Percent of tracts with Methadone Providerwithin a 30-min driving range, with Impedance factor
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
OtpTmDrP2|NUMERIC|Percent of tracts with Opioid Treatment Provider within a 30-min driving range, with Impedance factor
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OtpAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Opioid Treatment Provider (Otp), with Impedance factor
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
SutCtTmDr2|NUMERIC|Number of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
TotTracts|INTEGER|Total number of census tracts within the state.
SutTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
BupAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Buprenorphine Provider (BUP), with Impedance factor
NaltCtTmDr2|NUMERIC|Number of tracts with Naltrexone Provider within a 30-min driving range, with Impedance factor
MetCtTmDr2|NUMERIC|Number of tracts with Methadone Providerwithin a 30-min driving range, with Impedance factor
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
NaltTmDrP2|NUMERIC|Percent of tracts with Naltrexone Provider within a 30-min driving range, with Impedance factor
SutAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
BupTmDrP2|NUMERIC|Percent of tracts with Buprenorphine Provider within a 30-min driving range, with Impedance factor
SutAvTmDr2|NUMERIC| Average driving time (minutes) across tracts in state to nearestSubstance Use Treatment Provider (Sut), with Impedance factor
SutTmDrP2|NUMERIC|Percent of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
MetAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest methadone provider
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
NaltAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Naltrexone Provider (NALT), with Impedance factor
BupCtTmDr2|NUMERIC|Number of tracts with Buprenorphine Provider within a 30-min driving range, with Impedance factor

### county-2019

ID: `oeps-391119.tabular.county-2019`

11 columns in this table.

Name|Data Type|Description
-|-|-|-
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
TtlPrPp|INTEGER|Total Prison Population Count
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
NoIntP|NUMERIC|Percentage of Households without Internet access
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
TtlPrAPp|INTEGER|Prison Prison Admissions Count
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
OdMortRt|NUMERIC|Overdose mortality rate
TtlPrPpr|NUMERIC|Total Prison Population Rate

### zcta-2023

ID: `oeps-391119.tabular.zcta-2023`

89 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
EngProf|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr62P|NUMERIC|
TotWrkE|INTEGER|Estimated count of working population
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
MrrdP|NUMERIC|
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HhldMA|NUMERIC|
HsdTypMC|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
HhldFA|NUMERIC|
OccupantP|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
MedAge|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
HsdTot|NUMERIC|
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
TotPopHh|INTEGER|Total number of people in households
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HsdTypCo|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
HhldMC|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HhldMS|NUMERIC|
RentalP|NUMERIC|Percentage of occupied housing units that are rented
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr16|NUMERIC|
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
DivrcdP|NUMERIC|
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
SepartedP|NUMERIC|
WidwdP|NUMERIC|
HisP|NUMERIC|
Und18P|NUMERIC|
HhldFS|NUMERIC|
HhldFC|NUMERIC|
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
CrowdHsng|NUMERIC|
NvMrrdP|NUMERIC|
HHSize|NUMERIC|
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
FamSize|NUMERIC|
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
HsdTypM|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.

### state-2020

ID: `oeps-391119.tabular.state-2020`

66 columns in this table.

Name|Data Type|Description
-|-|-|-
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
MulHcvD|NUMERIC|
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
PctBupT|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
FlHcvD|INTEGER|Hepatitis C deaths among women
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
CntNaltT|INTEGER|Number of tracts within 30 -min of naltrexone driving range
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
PctMetT|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
WhtHcvD|NUMERIC|
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
WlfrExp|INTEGER|Total expenditures on public welfare programs
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
MlHcvD|INTEGER|Hepatitis C deaths among men
PctNaltT|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
AvBupTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest buprenorphine provider.
AvMetTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest methadone provider.
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
OpRxRt|NUMERIC|Opioid prescription rate
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
HlthExp|INTEGER|Total expenditures on public health and hospitals
CrrctExp|INTEGER|Total expenditures on corrections system and operations
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
CntMetT|INTEGER|Number of tracts with methadone provider within a 30-min driving range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
OdMortRt|NUMERIC|Overdose mortality rate
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range
HcvD|INTEGER|Total Hepatitis C deaths
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AsHcvD|NUMERIC|
AvNaltTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest naltrexone provider.
NhPiHcvD|NUMERIC|
PrMsuseP|NUMERIC|Percent of persons who self-report misusing prescription pain relief medication in 2020.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.
CntBupT|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range

### county-2023

ID: `oeps-391119.tabular.county-2023`

115 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
EngProf|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr62P|NUMERIC|
TotWrkE|INTEGER|Estimated count of working population
TtlJlPrtrQ4|NUMERIC|Pretrial Jail Population Rate (Q4)
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
MrrdP|NUMERIC|
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
TtlJlPpQ3|NUMERIC|Total Jail Population Count (Q3), ASJ/COJ Data
TtlJlPprQ2|NUMERIC|Total Jail Population Rate (Q2), ASJ/COJ Data
TtlJlPrtrQ1|NUMERIC|Pretrial Jail Population Rate (Q1)
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TtlJlAdmQ1|NUMERIC|Total Jail Admissions Count (Q1), ASJ/COJ Data
TtlJlPrtrQ2|NUMERIC|Pretrial Jail Population Rate (Q2)
HhldMA|NUMERIC|
HsdTypMC|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
HhldFA|NUMERIC|
OccupantP|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
TtlJlPrtQ4|NUMERIC|Pretrial Jail Population Count (Q4)
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
MedAge|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
TtlJlPrtQ1|NUMERIC|Pretrial Jail Population Count (Q1)
HsdTot|NUMERIC|
TtlJlPprQ1|NUMERIC|Total Jail Population Rate (Q1), ASJ/COJ Data
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
TtlJlPprQ3|NUMERIC|Total Jail Population Rate (Q3), ASJ/COJ Data
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
TtlJlPpQ2|NUMERIC|Total Jail Population Count (Q2), ASJ/COJ Data
TtlJlAdmrQ4|NUMERIC|Total Jail Admissions Rate (Q4), ASJ/COJ Data
TtlJlAdmQ4|NUMERIC|Total Jail Admissions Count (Q4), ASJ/COJ Data
TotPopHh|INTEGER|Total number of people in households
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
TtlJlPpQ1|NUMERIC|Total Jail Population Count (Q1), ASJ/COJ Data
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HsdTypCo|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
HhldMC|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
TtlJlAdmQ3|NUMERIC|Total Jail Admissions Count (Q3), ASJ/COJ Data
HhldMS|NUMERIC|
TtlJlPrtQ3|NUMERIC|Pretrial Jail Population Count (Q3)
TtlJlPpQ4|NUMERIC|Total Jail Population Count (Q4), ASJ/COJ Data
RentalP|NUMERIC|Percentage of occupied housing units that are rented
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
TtlJlAdmrQ1|NUMERIC|Total Jail Admissions Rate (Q1), ASJ/COJ Data
TtlJlAdmrQ3|NUMERIC|Total Jail Admissions Rate (Q3), ASJ/COJ Data
Ovr16|NUMERIC|
DivrcdP|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
SepartedP|NUMERIC|
WidwdP|NUMERIC|
HisP|NUMERIC|
Und18P|NUMERIC|
TtlJlPprQ4|NUMERIC|Total Jail Population Rate (Q4), ASJ/COJ Data
RspRt|NUMERIC|Percent of units interviewed from total units intended for interview
TtlJlAdmrQ2|NUMERIC|Total Jail Admissions Rate (Q2), ASJ/COJ Data
HhldFS|NUMERIC|
HhldFC|NUMERIC|
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
TtlJlPrtrQ3|NUMERIC|Pretrial Jail Population Rate (Q3)
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
CrowdHsng|NUMERIC|
NvMrrdP|NUMERIC|
TtlJlPrtQ2|NUMERIC|Pretrial Jail Population Count (Q2)
HHSize|NUMERIC|
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
FamSize|NUMERIC|
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
HsdTypM|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TtlJlAdmQ2|NUMERIC|Total Jail Admissions Count (Q2), ASJ/COJ Data

### tract-2022

ID: `oeps-391119.tabular.tract-2022`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation

### tract-ruca-2010

ID: `oeps-391119.tabular.tract-ruca-2010`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Rurality|STRING|Urban/Suburban/Rural
Ruca2|STRING|Secondary RUCA Code
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ruca1|STRING|Primary RUCA Code

### state-1980

ID: `oeps-391119.tabular.state-1980`

40 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
ChildrenP|NUMERIC|Percentage of population under age 18

### tract-2023

ID: `oeps-391119.tabular.tract-2023`

85 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
EngProf|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr62P|NUMERIC|
TotWrkE|INTEGER|Estimated count of working population
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
MrrdP|NUMERIC|
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HhldMA|NUMERIC|
HsdTypMC|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
HhldFA|NUMERIC|
OccupantP|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
LibPerCap|NUMERIC|Libraries per capita by census tract
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
MedAge|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
HsdTot|NUMERIC|
TotPopHh|INTEGER|Total number of people in households
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HsdTypCo|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
HhldMC|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HhldMS|NUMERIC|
RentalP|NUMERIC|Percentage of occupied housing units that are rented
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
SocCapInd|NUMERIC|Composite index of LngTermP, LibPerCap, RlgPerCap
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr16|NUMERIC|
RlgPerCap|NUMERIC|Religious institutions per capita by census tract
DivrcdP|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
SepartedP|NUMERIC|
WidwdP|NUMERIC|
HisP|NUMERIC|
Und18P|NUMERIC|
HhldFS|NUMERIC|
HhldFC|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
CrowdHsng|NUMERIC|
NvMrrdP|NUMERIC|
HHSize|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
MedHsgTen|STRING|Median time period occupant moved into housing unit by tract
FamSize|NUMERIC|
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
HsdTypM|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.

### county-2021

ID: `oeps-391119.tabular.county-2021`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OdMortRt|NUMERIC|Overdose mortality rate

### county-2024

ID: `oeps-391119.tabular.county-2024`

8 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
TtlJlPrt|NUMERIC|Pretrial Jail Population Count

### state-1990

ID: `oeps-391119.tabular.state-1990`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
GradSclP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
ChildrenP|NUMERIC|Percentage of population under age 18

### tract-providers-2010

ID: `oeps-391119.tabular.tract-providers-2010`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TotPcp|INTEGER|Number of primary care providers in area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000
TotSp|INTEGER|Number of specialty physicians in area
PcpPer100k|NUMERIC|PCPs per total Population X 100,000

### county-2000

ID: `oeps-391119.tabular.county-2000`

44 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
DmyBlckBlt|BOOLEAN|Dummy variable for whether county is in the Southern Black Belt region
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
ChildrenP|NUMERIC|Percentage of population under age 18

### state-2010

ID: `oeps-391119.tabular.state-2010`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
TotVetPop|INTEGER|Total Veteran population
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Age15_44|INTEGER|Total population between age 15-44
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.

### zcta-ruca-2010

ID: `oeps-391119.tabular.zcta-ruca-2010`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Rurality|STRING|Urban/Suburban/Rural
Ruca2|STRING|Secondary RUCA Code
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
Ruca1|STRING|Primary RUCA Code

### state-2022

ID: `oeps-391119.tabular.state-2022`

64 columns in this table.

Name|Data Type|Description
-|-|-|-
MulHcvD|NUMERIC|
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
AvNhPiHcvD|NUMERIC|
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
AvAmInHcvD|NUMERIC|Mean yearly Hepatitis C deaths among American Indian population from 2013-2017
FlHcvD|INTEGER|Hepatitis C deaths among women
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
AvHspHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Hispanic populations from 2013-2017
TtlPrPp|INTEGER|Total Prison Population Count
AvMulHcvD|NUMERIC|
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
WhtHcvD|NUMERIC|
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AvWhHcvD|NUMERIC|Mean yearly Hepatitis C deaths among White populations from 2018-2022
AvAsHcvD|NUMERIC|
WlfrExp|INTEGER|Total expenditures on public welfare programs
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
AvU50HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people under 50 years of age from 2013-2017
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
MlHcvD|INTEGER|Hepatitis C deaths among men
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
AvFlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among women from 2013-2017
TtlPrAPp|INTEGER|Prison Prison Admissions Count
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
AvA50_74HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people between 50 and 74 years of age from 2013-2017, 2018-2022
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
OpRxRt|NUMERIC|Opioid prescription rate
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
HlthExp|INTEGER|Total expenditures on public health and hospitals
CrrctExp|INTEGER|Total expenditures on corrections system and operations
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
OdMortRt|NUMERIC|Overdose mortality rate
ParkArea|NUMERIC|Area (in square meters) of park or green space in a state).
HcvD|INTEGER|Total Hepatitis C deaths
AvBlkHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Black populations from 2013-2017
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AvMlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among men from 2013-2017
AsHcvD|NUMERIC|
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
TtlPrPpr|NUMERIC|Total Prison Population Rate
NhPiHcvD|NUMERIC|
PrMsuseP|NUMERIC|Percent of persons who self-report misusing prescription pain relief medication in 2020.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
AvHcvD|NUMERIC|Mean total yearly Hepatitis C deaths from 2013-2017, 2018-2022
AvO75HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people over 75 years of age

### county-2025

ID: `oeps-391119.tabular.county-2025`

55 columns in this table.

Name|Data Type|Description
-|-|-|-
HcvCtTmDr2|NUMERIC|Number of tracts with HCV Testing Facility within a 30-min driving range, with impedance
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
SmokeP|NUMERIC|Percentage of Smoking Population
HivTmDrP2|NUMERIC|Percent of tracts with HIV Testing Facility within a 30-mini driving range, with impedance
HcvAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HCV Testing Facility, with impedance
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
HivTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HIV testing provider
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
MhCtTmDr2|NUMERIC|Number of tracts with Mental Health Provider within a 30-min driving range, with impedance
MhTmDrP2|NUMERIC|Percent of tracts with Mental Health Provider within a 30-mini driving range, with impedence
HcvTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HCV testing provider
MhAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Mental Health Provider, with impedance
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
FqhcAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center, with Impedance factor
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
HivAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HIV Testing Facility, with impedance
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
HivAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HIV testing provider
HcvAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HCV testing provider
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FqhcCtTmDr2|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
RxTmDrP2|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range with impedance factor
HcvTmDrP2|NUMERIC|Percent of tracts with HCV Testing Facility within a 30-mini driving range, with impedance
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
TlBupMinDis|NUMERIC|Euclidean distance (in miles) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
TotTracts|INTEGER|Total number of census tracts within the state.
HivCtTmDr2|NUMERIC|Number of tracts with HIV Testing Facility within a 30-min driving range, with impedance
RxAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy with Impedance Factor
HospAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital with Impedance factor
HospCtTmDr2|NUMERIC|Number of tracts with Hospitals within a 30-min driving range, with impedance
HospTmDrP2|NUMERIC|Percent of tracts with hospital within a 30-mini driving range with Impedance Factor
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
TlBupTmDr|NUMERIC|Estimated driving time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
FqhcTmDrP2|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
HcvCtTmDr|INTEGER|Number of tracts with an HCV testing provider within a 30-minute driving range
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range
RxCtTmDr2|INTEGER|Number of tracts with pharmacy within a 30-min driving range with impedance factor
HivCtTmDr|INTEGER|Number of tracts with an HIV testing provider within a 30-minute driving range
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider

### tract-1990

ID: `oeps-391119.tabular.tract-1990`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
GradSclP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
ChildrenP|NUMERIC|Percentage of population under age 18

### state-2018

ID: `oeps-391119.tabular.state-2018`

120 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
EngProf|NUMERIC|
MulHcvD|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
VacantP|NUMERIC|Percentage of vacant housing units
UnitDens|NUMERIC|Number of housing units per square mile of land area
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotWrkE|INTEGER|Estimated count of working population
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
FlHcvD|INTEGER|Hepatitis C deaths among women
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
AlcTot|INTEGER|Total number of alcohol outlets
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
WhtHcvD|NUMERIC|
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
TotPopHh|INTEGER|Total number of people in households
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
MlHcvD|INTEGER|Hepatitis C deaths among men
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
TradSttExp|INTEGER|Traditional medicaid - state spending
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
TotTracts|INTEGER|Total number of census tracts within the state.
RentalP|NUMERIC|Percentage of occupied housing units that are rented
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
TradFedExp|INTEGER|Traditional medicaid - federal spending
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
StateArea|NUMERIC|Area (in square meters) of state
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
ExpnFedExp|INTEGER|Expansion Group - Federal Spending
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
AreaSqMi|NUMERIC|Land area of geography in sq miles
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
OdMortRt|NUMERIC|Overdose mortality rate
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
HcvD|INTEGER|Total Hepatitis C deaths
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
AsHcvD|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
NhPiHcvD|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
AlcDens|NUMERIC|Number of alcohol outlets per square mile
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
MedcdExp|INTEGER|Total medicaid spending
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
ChildrenP|NUMERIC|Percentage of population under age 18
ExpnSttExp|INTEGER|Expansion Group - State Spending

### state-2021

ID: `oeps-391119.tabular.state-2021`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MulHcvD|NUMERIC|
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
FlHcvD|INTEGER|Hepatitis C deaths among women
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
WhtHcvD|NUMERIC|
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
WlfrExp|INTEGER|Total expenditures on public welfare programs
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
MlHcvD|INTEGER|Hepatitis C deaths among men
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
HlthExp|INTEGER|Total expenditures on public health and hospitals
CrrctExp|INTEGER|Total expenditures on corrections system and operations
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
OdMortRt|NUMERIC|Overdose mortality rate
HcvD|INTEGER|Total Hepatitis C deaths
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AsHcvD|NUMERIC|
NhPiHcvD|NUMERIC|
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### county-1990

ID: `oeps-391119.tabular.county-1990`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
GradSclP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
ChildrenP|NUMERIC|Percentage of population under age 18

### state-2015

ID: `oeps-391119.tabular.state-2015`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
FlHcvD|INTEGER|Hepatitis C deaths among women
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MlHcvD|INTEGER|Hepatitis C deaths among men
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
OdMortRt|NUMERIC|Overdose mortality rate
HcvD|INTEGER|Total Hepatitis C deaths
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### tract-2000

ID: `oeps-391119.tabular.tract-2000`

46 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
ChildrenP|NUMERIC|Percentage of population under age 18

### tract-2020

ID: `oeps-391119.tabular.tract-2020`

123 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
EngProf|NUMERIC|
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
VacantP|NUMERIC|Percentage of vacant housing units
UnitDens|NUMERIC|Number of housing units per square mile of land area
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
Ovr62P|NUMERIC|
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
TotWrkE|INTEGER|Estimated count of working population
NaltRm60|NUMERIC|Naltrexone access 60 minutes (RAAM)
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
MrrdP|NUMERIC|
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
MhCntDr|INTEGER|Count of MH providers within a 30-minute driving threshold
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HhldMA|NUMERIC|
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
HsdTypMC|NUMERIC|
NaltRm30|NUMERIC|Naltrexone access 30 minutes (RAAM)
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
HhldFA|NUMERIC|
OccupantP|NUMERIC|
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
GradSclP|NUMERIC|
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
MedAge|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
HsdTot|NUMERIC|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
NaltRm90|NUMERIC|Naltrexone access 90 minutes (RAAM)
TotPopHh|INTEGER|Total number of people in households
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
TotUnits|INTEGER|Count of total occupied housing units
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
EduHsP|NUMERIC|
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
SomeCollegeP|NUMERIC|
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HsdTypCo|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
HhldMC|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HhldMS|NUMERIC|
RentalP|NUMERIC|Percentage of occupied housing units that are rented
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
SutTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip SUT destination centroid, in minutes
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
BupRm90|NUMERIC|Buprenorphine access 90 minutes (RAAM)
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
BupRm30|NUMERIC|Buprenorphine access 30 minutes (RAAM)
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
DivrcdP|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
SRatio|NUMERIC|
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
Ovr21P|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
SepartedP|NUMERIC|
WidwdP|NUMERIC|
HisP|NUMERIC|
Und18P|NUMERIC|
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
HhldFS|NUMERIC|
HhldFC|NUMERIC|
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
BupRm60|NUMERIC|Buprenorphine access 60 minutes (RAAM)
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
CrowdHsng|NUMERIC|
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
NvMrrdP|NUMERIC|
HHSize|NUMERIC|
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
FamSize|NUMERIC|
WhiteP|NUMERIC|Percentage of population with race identified as white alone
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
SRatio18|NUMERIC|
HsdTypM|NUMERIC|
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider

### zcta-2020

ID: `oeps-391119.tabular.zcta-2020`

109 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
EngProf|NUMERIC|
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
VacantP|NUMERIC|Percentage of vacant housing units
UnitDens|NUMERIC|Number of housing units per square mile of land area
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
Ovr62P|NUMERIC|
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
TotWrkE|INTEGER|Estimated count of working population
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
MrrdP|NUMERIC|
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
MhCntDr|INTEGER|Count of MH providers within a 30-minute driving threshold
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HhldMA|NUMERIC|
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
HsdTypMC|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
HhldFA|NUMERIC|
OccupantP|NUMERIC|
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
GradSclP|NUMERIC|
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
MedAge|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
HsdTot|NUMERIC|
TotPopHh|INTEGER|Total number of people in households
TotUnits|INTEGER|Count of total occupied housing units
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
EduHsP|NUMERIC|
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
SomeCollegeP|NUMERIC|
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HsdTypCo|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
HhldMC|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HhldMS|NUMERIC|
RentalP|NUMERIC|Percentage of occupied housing units that are rented
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
SutTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip SUT destination centroid, in minutes
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
DivrcdP|NUMERIC|
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
SRatio|NUMERIC|
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
Ovr21P|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
SepartedP|NUMERIC|
WidwdP|NUMERIC|
HisP|NUMERIC|
Und18P|NUMERIC|
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
HhldFS|NUMERIC|
HhldFC|NUMERIC|
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
CrowdHsng|NUMERIC|
NvMrrdP|NUMERIC|
HHSize|NUMERIC|
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
FamSize|NUMERIC|
WhiteP|NUMERIC|Percentage of population with race identified as white alone
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
SRatio18|NUMERIC|
HsdTypM|NUMERIC|
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider

### zcta-2022

ID: `oeps-391119.tabular.zcta-2022`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
SviSmryRnk|NUMERIC|Overall summary ranking
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation

### tract-2025

ID: `oeps-391119.tabular.tract-2025`

88 columns in this table.

Name|Data Type|Description
-|-|-|-
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
BupFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Buprenorphine within a 30-minute drive
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
TlBupCntBk30|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 30-minute biking time threshold
NaltRm60|NUMERIC|Naltrexone access 60 minutes (RAAM)
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
MhCntDr|INTEGER|Count of MH providers within a 30-minute driving threshold
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
NaltCntDr60|NUMERIC|Count of naltrexone providers in 60 minute drive time threshold
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
NaltRm30|NUMERIC|Naltrexone access 30 minutes (RAAM)
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
BupFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Buprenorphine within a 30-minute drive
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
MetCntDr60|NUMERIC|Count of methadone providers in 60 minute drive time threshold
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
OtpFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to opioid treatment programs within a 30-minute drive
HivCntDr|INTEGER|Number of HIV testing providers within a 30-minute drive
HivTmDr|NUMERIC|Driving time from origin to nearest HIV testing provider (minutes)
HivTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip HIV Testing Facility with impedance destination centroid, in minutes
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
HospTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes with Impedance factor
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
MetFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Methadone within a 30-minute drive
TlBupCntDr30|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 30-minute driving time threshold
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
OtpRm30|NUMERIC|Opioid Treatment Provider access 30 minutes (RAAM)
HivMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest HIV testing provider (miles)
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
TlBupMinDis|NUMERIC|Euclidean distance (in miles) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
NaltFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Naltrexone within a 60-minute drive
OtpRm60|NUMERIC|Opioid Treatment Provider access 60 minutes (RAAM)
OtpFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to opioid treatment programs within a 60-minute drive
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
SutTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip SUT destination centroid, in minutes
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
NaltFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Naltrexone within a 30-minute drive
BupRm30|NUMERIC|Buprenorphine access 30 minutes (RAAM)
TlBupCntDr60|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 60-minute driving time threshold
RxTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid with impedance factor, in minutes
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
BupCntDr60|NUMERIC|Count of buprenorphine providers in 60 minute drive time threshold
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
TlBupTmDr|NUMERIC|Estimated driving time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
MetFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Methadone within a 60-minute drive
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
HcvTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip HCV Testing Facility with impedance destination centroid, in minutes
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
SspTmDr|NUMERIC|Driving time in minutes from origin census tract centroid to census tract centroid of nearest SSP
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
BupRm60|NUMERIC|Buprenorphine access 60 minutes (RAAM)
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
FqhcTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes, with Impedance factor
HcvMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest HCV testing provider (miles)
SspTmDr2|NUMERIC|Driving time in minutes from origin census tract centroid to census tract centroid of nearest SSP and back to origin census tract centroid
HcvCntDr|INTEGER|Number of HCV testing providers within a 30-minute drive
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
TlBupCntWk30|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 30-minute walking time threshold
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
HcvTmDr|NUMERIC|Driving time from origin to nearest HCV testing provider (minutes)
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
MhTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip Mental Health Provider with impedance destination centroid, in minutes

### county-2020

ID: `oeps-391119.tabular.county-2020`

116 columns in this table.

Name|Data Type|Description
-|-|-|-
BupAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest buprenorphine provider
FemP|NUMERIC|
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
EngProf|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
NaltAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest naltrexone provider
VacantP|NUMERIC|Percentage of vacant housing units
UnitDens|NUMERIC|Number of housing units per square mile of land area
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020
BupAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest buprenorphine provider
Ovr62P|NUMERIC|
TotWrkE|INTEGER|Estimated count of working population
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
MrrdP|NUMERIC|
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
MetTmBkP|NUMERIC|Percent of tracts with methadone provider within a 30-min biking range
MetTmWkP|NUMERIC|Percent of tracts with methadone provider within a 30-min walking range
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
BupCtTmWk|INTEGER|Number of tracts with buprenorphine provider within a 30-min walking range
BupTmBkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min biking range
HhldMA|NUMERIC|
HsdTypMC|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
BupTmWkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min walking range
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
HhldFA|NUMERIC|
OccupantP|NUMERIC|
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
GradSclP|NUMERIC|
MetCtTmBk|INTEGER|Number of tracts with methadone provider within a 30-min biking range
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
MedAge|NUMERIC|
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
BupTmDrP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
HsdTot|NUMERIC|
TotPopHh|INTEGER|Total number of people in households
TotUnits|INTEGER|Count of total occupied housing units
NaltAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest naltrexone provider
EduHsP|NUMERIC|
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
SomeCollegeP|NUMERIC|
NaltTmDrP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HsdTypCo|NUMERIC|
NaltAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest naltrexone provider
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
HhldMC|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HhldMS|NUMERIC|
MetTmDrP|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range
RentalP|NUMERIC|Percentage of occupied housing units that are rented
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MetAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest methadone provider
MetCtTmWk|INTEGER|Number of tracts with methadone provider within a 30-min walking range
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MetAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest methadone provider
NaltCtTmDr|INTEGER|Number of tracts with naltrexone provider within a 30-min driving range
DivrcdP|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking
SRatio|NUMERIC|
Ovr21P|NUMERIC|
OpRxRt|NUMERIC|Opioid prescription rate
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
SepartedP|NUMERIC|
WidwdP|NUMERIC|
HisP|NUMERIC|
Und18P|NUMERIC|
HhldFS|NUMERIC|
HhldFC|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
NaltCtTmWk|INTEGER|Number of tracts with naltrexone provider within a 30-min walking range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
OdMortRt|NUMERIC|Overdose mortality rate
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
CrowdHsng|NUMERIC|
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
NaltCtTmBk|INTEGER|Number of tracts with naltrexone provider within a 30-min biking range
NvMrrdP|NUMERIC|
BupCtTmDr|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range
BupCtTmBk|INTEGER|Number of tracts with buprenorphine provider within a 30-min biking range
HHSize|NUMERIC|
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
MetAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest methadone provider
MetCtTmDr|INTEGER|Number of tracts with methadone provider within a 30-min driving range
NaltTmWkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min walking range
FamSize|NUMERIC|
NaltTmBkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min biking range
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
HsdTypM|NUMERIC|
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
BupAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest buprenorphine provider

### county-1980

ID: `oeps-391119.tabular.county-1980`

40 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
ChildrenP|NUMERIC|Percentage of population under age 18

### tract-2010

ID: `oeps-391119.tabular.tract-2010`

48 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
TwoRaceP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
TotVetPop|INTEGER|Total Veteran population
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Age15_44|INTEGER|Total population between age 15-44
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.

### tract-1980

ID: `oeps-391119.tabular.tract-1980`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
ChildrenP|NUMERIC|Percentage of population under age 18

### zcta-2018

ID: `oeps-391119.tabular.zcta-2018`

82 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
EngProf|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
UnitDens|NUMERIC|Number of housing units per square mile of land area
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotWrkE|INTEGER|Estimated count of working population
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduNoHsP|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
AlcTot|INTEGER|Total number of alcohol outlets
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
GradSclP|NUMERIC|
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
TotPopHh|INTEGER|Total number of people in households
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
RentalP|NUMERIC|Percentage of occupied housing units that are rented
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
SviSmryRnk|NUMERIC|Overall summary ranking
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
AreaSqMi|NUMERIC|Land area of geography in sq miles
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
AlcDens|NUMERIC|Number of alcohol outlets per square mile
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
ChildrenP|NUMERIC|Percentage of population under age 18

### zcta-2021

ID: `oeps-391119.tabular.zcta-2021`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.

### state-2013

ID: `oeps-391119.tabular.state-2013`

12 columns in this table.

Name|Data Type|Description
-|-|-|-
FlHcvD|INTEGER|Hepatitis C deaths among women
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MlHcvD|INTEGER|Hepatitis C deaths among men
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
HcvD|INTEGER|Total Hepatitis C deaths
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### tract-2014

ID: `oeps-391119.tabular.tract-2014`

2 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.

### state-providers-2010

ID: `oeps-391119.tabular.state-providers-2010`

4 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TotPcp|INTEGER|Number of primary care providers in area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotSp|INTEGER|Number of specialty physicians in area

### zcta-2025

ID: `oeps-391119.tabular.zcta-2025`

3 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold

### tract-2019

ID: `oeps-391119.tabular.tract-2019`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
NoIntP|NUMERIC|Percentage of Households without Internet access
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes

### state-2014

ID: `oeps-391119.tabular.state-2014`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
FlHcvD|INTEGER|Hepatitis C deaths among women
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MlHcvD|INTEGER|Hepatitis C deaths among men
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
OdMortRt|NUMERIC|Overdose mortality rate
HcvD|INTEGER|Total Hepatitis C deaths
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### county-2018

ID: `oeps-391119.tabular.county-2018`

91 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
EngProf|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
CenFlags|STRING|Three different values indicating three things:
1 - Revised count, so urban and rural components will not add to total. 
2 - Geography name and FIPS code were changed since 2010. Shannon County, Sotuh Dakota name changed to Oglala Lakota County, new FIPS 46102. Wade Hampton Census Area, Alaska, name changed to Kusilvak CEnsus Area, nwe FIPS 02158
3 - Bedford City, Virginia, was consolidated with Bedford County, Virginia (FIPS 51019) since 2010.
UnitDens|NUMERIC|Number of housing units per square mile of land area
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotWrkE|INTEGER|Estimated count of working population
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduNoHsP|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
AlcTot|INTEGER|Total number of alcohol outlets
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
GradSclP|NUMERIC|
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
TotPopHh|INTEGER|Total number of people in households
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
TotTracts|INTEGER|Total number of census tracts within the state.
RentalP|NUMERIC|Percentage of occupied housing units that are rented
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
RcaRuralP|NUMERIC|Percent census tracts in the county classified as Rural using RUCA codes
RcaUrbanP|NUMERIC|Percent census tracts in the county classified as Urban using RUCA codes
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
RcaSubrbP|NUMERIC|Percent census tracts in the county classified as Suburban using RUCA codes
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
RspRt|NUMERIC|Percent of units interviewed from total units intended for interview
AreaSqMi|NUMERIC|Land area of geography in sq miles
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
OdMortRt|NUMERIC|Overdose mortality rate
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
AlcDens|NUMERIC|Number of alcohol outlets per square mile
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
ChildrenP|NUMERIC|Percentage of population under age 18

### county-2014

ID: `oeps-391119.tabular.county-2014`

3 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OdMortRt|NUMERIC|Overdose mortality rate

### zcta-2019

ID: `oeps-391119.tabular.zcta-2019`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
NoIntP|NUMERIC|Percentage of Households without Internet access
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes

### tract-sdoh-2014

ID: `oeps-391119.tabular.tract-sdoh-2014`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SocEcAdvIn|NUMERIC|Raw Socioeconomic Advantage Index (https://sdohatlas.github.io/)
LimMobInd|NUMERIC|Raw Limited Mobility Index (https://sdohatlas.github.io/)
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
MicaInd|NUMERIC|Raw Mixed Immigrant Cohesion and Accessibility (MICA) Index (https://sdohatlas.github.io/)
UrbCoreInd|NUMERIC|Raw Urban Core Opportunity Index (https://sdohatlas.github.io/)
NeighbTyp|STRING|Categorical, one of seven neighborhood (tract-level) typologies: 1 = Rural Affordable; 2 = Suburban Affluent; 3 = Suburban Affordable; 4 = Extreme Poverty; 5 = Multilingual Working; 6 = Urban Core Opportunity; 7 = Sparse Areas

### tract-2018

ID: `oeps-391119.tabular.tract-2018`

79 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
EngProf|NUMERIC|
BachelorsP|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
UnitDens|NUMERIC|Number of housing units per square mile of land area
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotWrkE|INTEGER|Estimated count of working population
TotPop|INTEGER|Total population
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduNoHsP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr16P|NUMERIC|
AlcTot|INTEGER|Total number of alcohol outlets
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
GradSclP|NUMERIC|
LibPerCap|NUMERIC|Libraries per capita by census tract
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
TotPopHh|INTEGER|Total number of people in households
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
RentalP|NUMERIC|Percentage of occupied housing units that are rented
TotVetPop|INTEGER|Total Veteran population
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
SocCapInd|NUMERIC|Composite index of LngTermP, LibPerCap, RlgPerCap
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
RlgPerCap|NUMERIC|Religious institutions per capita by census tract
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
AreaSqMi|NUMERIC|Land area of geography in sq miles
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
MedHsgTen|STRING|Median time period occupant moved into housing unit by tract
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
AlcDens|NUMERIC|Number of alcohol outlets per square mile
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
ChildrenP|NUMERIC|Percentage of population under age 18

### state-2000

ID: `oeps-391119.tabular.state-2000`

43 columns in this table.

Name|Data Type|Description
-|-|-|-
FemP|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
VacantP|NUMERIC|Percentage of vacant housing units
Age15_44P|NUMERIC|Percentage of population below 45 years of age
TotPop|INTEGER|Total population
EduNoHsP|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16P|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
GradSclP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SRatio65|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduHsP|NUMERIC|
SomeCollegeP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
Age15_44|INTEGER|Total population between age 15-44
Ovr16|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
Ovr21|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HisP|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
Ovr18|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|
MaleP|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
ChildrenP|NUMERIC|Percentage of population under age 18

### state-2016

ID: `oeps-391119.tabular.state-2016`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
FlHcvD|INTEGER|Hepatitis C deaths among women
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MlHcvD|INTEGER|Hepatitis C deaths among men
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
OdMortRt|NUMERIC|Overdose mortality rate
HcvD|INTEGER|Total Hepatitis C deaths
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### county-providers-2010

ID: `oeps-391119.tabular.county-providers-2010`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TotPcp|INTEGER|Number of primary care providers in area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000
TotSp|INTEGER|Number of specialty physicians in area
PcpPer100k|NUMERIC|PCPs per total Population X 100,000

