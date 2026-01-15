# Project Id: oeps-391119

1 dataset in this project: tabular

## tabular

58 tables in this dataset.

### zcta-2021

ID: `oeps-391119.tabular.zcta-2021`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### state-2014

ID: `oeps-391119.tabular.state-2014`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
OdMortRt|NUMERIC|Overdose mortality rate
FlHcvD|INTEGER|Hepatitis C deaths among women
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations

### zcta-2025

ID: `oeps-391119.tabular.zcta-2025`

3 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### county-1990

ID: `oeps-391119.tabular.county-1990`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
Ovr16|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
HisP|NUMERIC|
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### state-2020

ID: `oeps-391119.tabular.state-2020`

66 columns in this table.

Name|Data Type|Description
-|-|-|-
HlthExp|INTEGER|Total expenditures on public health and hospitals
CntMetT|INTEGER|Number of tracts with methadone provider within a 30-min driving range
AvMetTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest methadone provider.
PctMetT|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
CrrctExp|INTEGER|Total expenditures on corrections system and operations
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
PrMsuseP|NUMERIC|Percent of persons who self-report misusing prescription pain relief medication in 2020.
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MlHcvD|INTEGER|Hepatitis C deaths among men
AsHcvD|NUMERIC|
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
PctBupT|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range
PctNaltT|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range
CntNaltT|INTEGER|Number of tracts within 30 -min of naltrexone driving range
WlfrExp|INTEGER|Total expenditures on public welfare programs
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AvBupTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest buprenorphine provider.
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
CntBupT|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MulHcvD|NUMERIC|
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
NhPiHcvD|NUMERIC|
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
OdMortRt|NUMERIC|Overdose mortality rate
AvNaltTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest naltrexone provider.
FlHcvD|INTEGER|Hepatitis C deaths among women
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
OpRxRt|NUMERIC|Opioid prescription rate
WhtHcvD|NUMERIC|
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.

### tract-2014

ID: `oeps-391119.tabular.tract-2014`

2 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### county-1980

ID: `oeps-391119.tabular.county-1980`

40 columns in this table.

Name|Data Type|Description
-|-|-|-
Ovr16|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
HisP|NUMERIC|
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### state-2025

ID: `oeps-391119.tabular.state-2025`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
SmokeP|NUMERIC|Percentage of Smoking Population
TotTracts|INTEGER|Total number of census tracts within the state.
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### state-2017

ID: `oeps-391119.tabular.state-2017`

53 columns in this table.

Name|Data Type|Description
-|-|-|-
AvAmInHcvD|NUMERIC|Mean yearly Hepatitis C deaths among American Indian population from 2013-2017
Un50Hcv|NUMERIC|Mean yearly Hepatatis C cases in people under 50 years of age from 2013-2016
AvMlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among men from 2013-2017
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
NonBlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations non-Black other race/ethnicity populations 2013-2016
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MlHcvD|INTEGER|Hepatitis C deaths among men
AvHspHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Hispanic populations from 2013-2017
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
MlHcv|NUMERIC|Mean yearly Hepatitis C cases in men from 2013-2016
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
A50_74Hcv|NUMERIC|Mean yearly Hepatitis C cases in people between 50 to 74 years of age from 2013-2016
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AvU50HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people under 50 years of age from 2013-2017
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
AvA50_74HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people between 50 and 74 years of age from 2013-2017, 2018-2022
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
AvO75HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people over 75 years of age
AvFlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among women from 2013-2017
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
AvBlkHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Black populations from 2013-2017
OdMortRt|NUMERIC|Overdose mortality rate
BlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations identified as non-hispanic Black alone across 2013-2016
FlHcvD|INTEGER|Hepatitis C deaths among women
TotHcv|NUMERIC|Mean total yearly Hepitatis C cases from 2013-2016
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
FmHcv|NUMERIC|Mean yearly Hepatitis C cases in women from 2013-2016
Ov75Hcv|NUMERIC|Mean yearly Hepatitis C cases in people over 75 years of age from 2013-2016
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
AvHcvD|NUMERIC|Mean total yearly Hepatitis C deaths from 2013-2017, 2018-2022
AvAsPiHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Asian and Pacific Islanders population from 2013-2017

### zcta-ruca-2010

ID: `oeps-391119.tabular.zcta-ruca-2010`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
Rurality|STRING|Urban/Suburban/Rural
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
Ruca2|STRING|Secondary RUCA Code
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ruca1|STRING|Primary RUCA Code

### zcta-2019

ID: `oeps-391119.tabular.zcta-2019`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
NoIntP|NUMERIC|Percentage of Households without Internet access
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold

### tract-2022

ID: `oeps-391119.tabular.tract-2022`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation

### tract-2018

ID: `oeps-391119.tabular.tract-2018`

79 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
GradSclP|NUMERIC|
Ovr16|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
TotPopHh|INTEGER|Total number of people in households
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SocCapInd|NUMERIC|Composite index of LngTermP, LibPerCap, RlgPerCap
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotWrkE|INTEGER|Estimated count of working population
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
SRatio18|NUMERIC|
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
MedHsgTen|STRING|Median time period occupant moved into housing unit by tract
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
SviSmryRnk|NUMERIC|Overall summary ranking
RentalP|NUMERIC|Percentage of occupied housing units that are rented
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr21P|NUMERIC|
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
AlcTot|INTEGER|Total number of alcohol outlets
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
RlgPerCap|NUMERIC|Religious institutions per capita by census tract
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
AreaSqMi|NUMERIC|Land area of geography in sq miles
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
AlcDens|NUMERIC|Number of alcohol outlets per square mile
ChildrenP|NUMERIC|Percentage of population under age 18
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
MaleP|NUMERIC|
LibPerCap|NUMERIC|Libraries per capita by census tract
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
EngProf|NUMERIC|

### state-2021

ID: `oeps-391119.tabular.state-2021`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
HlthExp|INTEGER|Total expenditures on public health and hospitals
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
CrrctExp|INTEGER|Total expenditures on corrections system and operations
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MlHcvD|INTEGER|Hepatitis C deaths among men
AsHcvD|NUMERIC|
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
WlfrExp|INTEGER|Total expenditures on public welfare programs
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MulHcvD|NUMERIC|
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
NhPiHcvD|NUMERIC|
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
OdMortRt|NUMERIC|Overdose mortality rate
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
FlHcvD|INTEGER|Hepatitis C deaths among women
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
WhtHcvD|NUMERIC|

### county-2010

ID: `oeps-391119.tabular.county-2010`

46 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
GradSclP|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
TwoRaceP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### county-2021

ID: `oeps-391119.tabular.county-2021`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.

### tract-providers-2010

ID: `oeps-391119.tabular.tract-providers-2010`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
TotPcp|INTEGER|Number of primary care providers in area
TotSp|INTEGER|Number of specialty physicians in area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
PcpPer100k|NUMERIC|PCPs per total Population X 100,000
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### state-1980

ID: `oeps-391119.tabular.state-1980`

40 columns in this table.

Name|Data Type|Description
-|-|-|-
Ovr16|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
HisP|NUMERIC|
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### zcta-2023

ID: `oeps-391119.tabular.zcta-2023`

89 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
GradSclP|NUMERIC|
Ovr16|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
TotPopHh|INTEGER|Total number of people in households
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HisP|NUMERIC|
MedAge|NUMERIC|
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
HHSize|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotWrkE|INTEGER|Estimated count of working population
SRatio18|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
HsdTot|NUMERIC|
RentalP|NUMERIC|Percentage of occupied housing units that are rented
HhldMS|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
Ovr18P|NUMERIC|
WidwdP|NUMERIC|
HsdTypCo|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFC|NUMERIC|
Ovr21P|NUMERIC|
DivrcdP|NUMERIC|
CrowdHsng|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
SepartedP|NUMERIC|
HhldFS|NUMERIC|
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HhldFA|NUMERIC|
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
FamSize|NUMERIC|
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MrrdP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
HhldMA|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr62P|NUMERIC|
HsdTypMC|NUMERIC|
MaleP|NUMERIC|
HhldMC|NUMERIC|
NvMrrdP|NUMERIC|
TwoRaceP|NUMERIC|
HsdTypM|NUMERIC|
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
Ovr16P|NUMERIC|
Und18P|NUMERIC|
OccupantP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
EngProf|NUMERIC|

### state-2023

ID: `oeps-391119.tabular.state-2023`

71 columns in this table.

Name|Data Type|Description
-|-|-|-
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
GradSclP|NUMERIC|
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
Ovr16|NUMERIC|
EdBupPolP|NUMERIC|Proportion of Entire Data Period with State-Level Buprenorphine Policy in Effect
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
HisP|NUMERIC|
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
SRatio18|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
TradFedExp|INTEGER|Traditional medicaid - federal spending
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
TradSttExp|INTEGER|Traditional medicaid - state spending
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
MedcdExp|INTEGER|Total medicaid spending
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
PerImpBupP|STRING|Periods of Implementation of State-Level Buprenorphine Policy (Associated Date Ranges)
Ovr21P|NUMERIC|
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
ExpnSttExp|INTEGER|Expansion Group - State Spending
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
BupPolP|NUMERIC|Proportion of Year with State-Level Buprenorphine Policy in Effect
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
MaleP|NUMERIC|
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
TwoRaceP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
ExpnFedExp|INTEGER|Expansion Group - Federal Spending
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
EngProf|NUMERIC|

### state-1990

ID: `oeps-391119.tabular.state-1990`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
Ovr16|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
HisP|NUMERIC|
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### state-2024

ID: `oeps-391119.tabular.state-2024`

9 columns in this table.

Name|Data Type|Description
-|-|-|-
EdBupPolP|NUMERIC|Proportion of Entire Data Period with State-Level Buprenorphine Policy in Effect
TtlPrPpr|NUMERIC|Total Prison Population Rate
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlPrPp|INTEGER|Total Prison Population Count
PerImpBupP|STRING|Periods of Implementation of State-Level Buprenorphine Policy (Associated Date Ranges)
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
BupPolP|NUMERIC|Proportion of Year with State-Level Buprenorphine Policy in Effect
MedPolP5Yr|NUMERIC|Proportion of the five-year period (ending in given year) for which Medicaid Expansion was implemented / in effect

### state-2015

ID: `oeps-391119.tabular.state-2015`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
OdMortRt|NUMERIC|Overdose mortality rate
FlHcvD|INTEGER|Hepatitis C deaths among women
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations

### zcta-2022

ID: `oeps-391119.tabular.zcta-2022`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
SviSmryRnk|NUMERIC|Overall summary ranking
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation

### county-providers-2010

ID: `oeps-391119.tabular.county-providers-2010`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
TotPcp|INTEGER|Number of primary care providers in area
TotSp|INTEGER|Number of specialty physicians in area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
PcpPer100k|NUMERIC|PCPs per total Population X 100,000
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### tract-2021

ID: `oeps-391119.tabular.tract-2021`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### county-2022

ID: `oeps-391119.tabular.county-2022`

8 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
OpRxRt|NUMERIC|Opioid prescription rate
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation

### tract-sdoh-2014

ID: `oeps-391119.tabular.tract-sdoh-2014`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
UrbCoreInd|NUMERIC|Raw Urban Core Opportunity Index (https://sdohatlas.github.io/)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
LimMobInd|NUMERIC|Raw Limited Mobility Index (https://sdohatlas.github.io/)
SocEcAdvIn|NUMERIC|Raw Socioeconomic Advantage Index (https://sdohatlas.github.io/)
MicaInd|NUMERIC|Raw Mixed Immigrant Cohesion and Accessibility (MICA) Index (https://sdohatlas.github.io/)
NeighbTyp|STRING|Categorical, one of seven neighborhood (tract-level) typologies: 1 = Rural Affordable; 2 = Suburban Affluent; 3 = Suburban Affordable; 4 = Extreme Poverty; 5 = Multilingual Working; 6 = Urban Core Opportunity; 7 = Sparse Areas

### tract-2020

ID: `oeps-391119.tabular.tract-2020`

123 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
GradSclP|NUMERIC|
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
NaltRm30|NUMERIC|Naltrexone access 30 minutes (RAAM)
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
TotPopHh|INTEGER|Total number of people in households
NaltRm60|NUMERIC|Naltrexone access 60 minutes (RAAM)
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HisP|NUMERIC|
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
MedAge|NUMERIC|
HHSize|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotWrkE|INTEGER|Estimated count of working population
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
SRatio18|NUMERIC|
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
HsdTot|NUMERIC|
SviSmryRnk|NUMERIC|Overall summary ranking
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
RentalP|NUMERIC|Percentage of occupied housing units that are rented
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
HhldMS|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
VacantP|NUMERIC|Percentage of vacant housing units
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
Ovr18P|NUMERIC|
BupCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
WidwdP|NUMERIC|
HsdTypCo|NUMERIC|
BachelorsP|NUMERIC|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
SRatio|NUMERIC|
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFC|NUMERIC|
Ovr21P|NUMERIC|
SutTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip SUT destination centroid, in minutes
DivrcdP|NUMERIC|
CrowdHsng|NUMERIC|
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
SepartedP|NUMERIC|
BupRm30|NUMERIC|Buprenorphine access 30 minutes (RAAM)
HhldFS|NUMERIC|
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
NaltRm90|NUMERIC|Naltrexone access 90 minutes (RAAM)
HhldFA|NUMERIC|
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
FamSize|NUMERIC|
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MrrdP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
HhldMA|NUMERIC|
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
MhCntDr|INTEGER|Count of MH providers within a 30-minute driving threshold
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
BupRm60|NUMERIC|Buprenorphine access 60 minutes (RAAM)
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr62P|NUMERIC|
HsdTypMC|NUMERIC|
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
MaleP|NUMERIC|
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
HhldMC|NUMERIC|
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
NvMrrdP|NUMERIC|
TwoRaceP|NUMERIC|
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
HsdTypM|NUMERIC|
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
Ovr16P|NUMERIC|
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
Und18P|NUMERIC|
OccupantP|NUMERIC|
FemP|NUMERIC|
BupRm90|NUMERIC|Buprenorphine access 90 minutes (RAAM)
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
EngProf|NUMERIC|

### county-2025

ID: `oeps-391119.tabular.county-2025`

12 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
FqhcAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center, with Impedance factor
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
SmokeP|NUMERIC|Percentage of Smoking Population
TotTracts|INTEGER|Total number of census tracts within the state.
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
FqhcCtTmDr2|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
FqhcTmDrP2|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor

### state-2022

ID: `oeps-391119.tabular.state-2022`

64 columns in this table.

Name|Data Type|Description
-|-|-|-
AvAmInHcvD|NUMERIC|Mean yearly Hepatitis C deaths among American Indian population from 2013-2017
HlthExp|INTEGER|Total expenditures on public health and hospitals
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
AvMlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among men from 2013-2017
TtlPrPpr|NUMERIC|Total Prison Population Rate
AvNhPiHcvD|NUMERIC|
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
CrrctExp|INTEGER|Total expenditures on corrections system and operations
AvAsHcvD|NUMERIC|
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
PrMsuseP|NUMERIC|Percent of persons who self-report misusing prescription pain relief medication in 2020.
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
MlHcvD|INTEGER|Hepatitis C deaths among men
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
AvHspHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Hispanic populations from 2013-2017
AsHcvD|NUMERIC|
WlfrExp|INTEGER|Total expenditures on public welfare programs
TtlPrPp|INTEGER|Total Prison Population Count
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
TtlPrAPp|INTEGER|Prison Prison Admissions Count
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
AvU50HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people under 50 years of age from 2013-2017
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MulHcvD|NUMERIC|
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AvMulHcvD|NUMERIC|
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
AvA50_74HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people between 50 and 74 years of age from 2013-2017, 2018-2022
NhPiHcvD|NUMERIC|
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
AvO75HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people over 75 years of age
AvFlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among women from 2013-2017
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
AvBlkHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Black populations from 2013-2017
OdMortRt|NUMERIC|Overdose mortality rate
AvWhHcvD|NUMERIC|Mean yearly Hepatitis C deaths among White populations from 2018-2022
FlHcvD|INTEGER|Hepatitis C deaths among women
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
OpRxRt|NUMERIC|Opioid prescription rate
ParkArea|NUMERIC|Area (in square meters) of park or green space in a state).
WhtHcvD|NUMERIC|
AvHcvD|NUMERIC|Mean total yearly Hepatitis C deaths from 2013-2017, 2018-2022

### tract-1990

ID: `oeps-391119.tabular.tract-1990`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
Ovr16|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
HisP|NUMERIC|
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### state-providers-2010

ID: `oeps-391119.tabular.state-providers-2010`

4 columns in this table.

Name|Data Type|Description
-|-|-|-
TotPcp|INTEGER|Number of primary care providers in area
TotSp|INTEGER|Number of specialty physicians in area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### county-2020

ID: `oeps-391119.tabular.county-2020`

116 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
GradSclP|NUMERIC|
MetAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest methadone provider
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
BupAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest buprenorphine provider
TotPopHh|INTEGER|Total number of people in households
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
MetTmBkP|NUMERIC|Percent of tracts with methadone provider within a 30-min biking range
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HisP|NUMERIC|
NaltTmWkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min walking range
MedAge|NUMERIC|
NaltAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest naltrexone provider
HHSize|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotWrkE|INTEGER|Estimated count of working population
SRatio18|NUMERIC|
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
NaltCtTmWk|INTEGER|Number of tracts with naltrexone provider within a 30-min walking range
BupTmWkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min walking range
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
HsdTot|NUMERIC|
SviSmryRnk|NUMERIC|Overall summary ranking
RentalP|NUMERIC|Percentage of occupied housing units that are rented
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
HhldMS|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
VacantP|NUMERIC|Percentage of vacant housing units
NaltCtTmBk|INTEGER|Number of tracts with naltrexone provider within a 30-min biking range
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
Ovr18P|NUMERIC|
MetTmDrP|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range
WidwdP|NUMERIC|
HsdTypCo|NUMERIC|
NaltAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest naltrexone provider
BachelorsP|NUMERIC|
BupTmDrP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
BupCtTmWk|INTEGER|Number of tracts with buprenorphine provider within a 30-min walking range
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range
SRatio|NUMERIC|
NaltTmDrP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFC|NUMERIC|
Ovr21P|NUMERIC|
DivrcdP|NUMERIC|
CrowdHsng|NUMERIC|
BupAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest buprenorphine provider
SepartedP|NUMERIC|
HhldFS|NUMERIC|
NaltTmBkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min biking range
TotUnits|INTEGER|Count of total occupied housing units
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HhldFA|NUMERIC|
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
MetCtTmDr|INTEGER|Number of tracts with methadone provider within a 30-min driving range
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
MetTmWkP|NUMERIC|Percent of tracts with methadone provider within a 30-min walking range
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
FamSize|NUMERIC|
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MrrdP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
HhldMA|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
NaltAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest naltrexone provider
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr62P|NUMERIC|
OdMortRt|NUMERIC|Overdose mortality rate
HsdTypMC|NUMERIC|
MetCtTmBk|INTEGER|Number of tracts with methadone provider within a 30-min biking range
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
MaleP|NUMERIC|
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020
BupCtTmDr|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range
MetAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest methadone provider
MetCtTmWk|INTEGER|Number of tracts with methadone provider within a 30-min walking range
HhldMC|NUMERIC|
BupCtTmBk|INTEGER|Number of tracts with buprenorphine provider within a 30-min biking range
NaltCtTmDr|INTEGER|Number of tracts with naltrexone provider within a 30-min driving range
NvMrrdP|NUMERIC|
TwoRaceP|NUMERIC|
BupTmBkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min biking range
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.
HsdTypM|NUMERIC|
Ovr16P|NUMERIC|
Und18P|NUMERIC|
OccupantP|NUMERIC|
FemP|NUMERIC|
OpRxRt|NUMERIC|Opioid prescription rate
BupAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest buprenorphine provider
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
MetAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest methadone provider
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
EngProf|NUMERIC|

### county-2017

ID: `oeps-391119.tabular.county-2017`

10 columns in this table.

Name|Data Type|Description
-|-|-|-
PrcNtvRsrv|NUMERIC|Percentage of county land area that belongs to Native American reservation(s)
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
OdMortRt|NUMERIC|Overdose mortality rate

### county-2000

ID: `oeps-391119.tabular.county-2000`

44 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
Ovr16|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
HisP|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
DmyBlckBlt|BOOLEAN|Dummy variable for whether county is in the Southern Black Belt region
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### county-2018

ID: `oeps-391119.tabular.county-2018`

91 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
GradSclP|NUMERIC|
Ovr16|NUMERIC|
RspRt|NUMERIC|Percent of units interviewed from total units intended for interview
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
CenFlags|STRING|Three different values indicating three things:
1 - Revised count, so urban and rural components will not add to total. 
2 - Geography name and FIPS code were changed since 2010. Shannon County, Sotuh Dakota name changed to Oglala Lakota County, new FIPS 46102. Wade Hampton Census Area, Alaska, name changed to Kusilvak CEnsus Area, nwe FIPS 02158
3 - Bedford City, Virginia, was consolidated with Bedford County, Virginia (FIPS 51019) since 2010.
TotPopHh|INTEGER|Total number of people in households
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
RetailP|NUMERIC|Percentage of population employed in retail trade industry
RcaRuralP|NUMERIC|Percent census tracts in the county classified as Rural using RUCA codes
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotWrkE|INTEGER|Estimated count of working population
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
SRatio18|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
SviSmryRnk|NUMERIC|Overall summary ranking
RentalP|NUMERIC|Percentage of occupied housing units that are rented
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
TotTracts|INTEGER|Total number of census tracts within the state.
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr21P|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
AlcTot|INTEGER|Total number of alcohol outlets
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
AreaSqMi|NUMERIC|Land area of geography in sq miles
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
OdMortRt|NUMERIC|Overdose mortality rate
AlcDens|NUMERIC|Number of alcohol outlets per square mile
ChildrenP|NUMERIC|Percentage of population under age 18
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
MaleP|NUMERIC|
RcaSubrbP|NUMERIC|Percent census tracts in the county classified as Suburban using RUCA codes
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
RcaUrbanP|NUMERIC|Percent census tracts in the county classified as Urban using RUCA codes
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
EngProf|NUMERIC|

### tract-2025

ID: `oeps-391119.tabular.tract-2025`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
FqhcTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes, with Impedance factor
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### tract-ruca-2010

ID: `oeps-391119.tabular.tract-ruca-2010`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
Rurality|STRING|Urban/Suburban/Rural
Ruca2|STRING|Secondary RUCA Code
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ruca1|STRING|Primary RUCA Code

### county-2019

ID: `oeps-391119.tabular.county-2019`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
NoIntP|NUMERIC|Percentage of Households without Internet access
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate

### county-2014

ID: `oeps-391119.tabular.county-2014`

3 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate

### tract-1980

ID: `oeps-391119.tabular.tract-1980`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
Ovr16|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### tract-2019

ID: `oeps-391119.tabular.tract-2019`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
NoIntP|NUMERIC|Percentage of Households without Internet access
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold

### state-2016

ID: `oeps-391119.tabular.state-2016`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
OdMortRt|NUMERIC|Overdose mortality rate
FlHcvD|INTEGER|Hepatitis C deaths among women
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations

### county-2015

ID: `oeps-391119.tabular.county-2015`

4 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
DmySgrg|BOOLEAN|Dummy variable for whether county is part of a hypersegregated city or its metropolitan area
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate

### state-2019

ID: `oeps-391119.tabular.state-2019`

54 columns in this table.

Name|Data Type|Description
-|-|-|-
HlthExp|INTEGER|Total expenditures on public health and hospitals
PrExcInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law explicitly exludes objects used for injecting drugs (0=no, 1=yes)
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
CrrctExp|INTEGER|Total expenditures on corrections system and operations
NoLwRmUnc|BOOLEAN|Dummy variable indicating whether the state has no law removing barriers or uncertainty as to SSP legality (0=no, 1=yes)
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
ExpSsp|BOOLEAN|Dummy variable indicating whether the state has law that explicitly authorizes Syringe Service Programs (0=no, 1=yes)
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
NtPrFrDsSy|BOOLEAN|Dummy variable indicating whether the state law does not prohibit free distribution of syringes (0=no, 1=yes)
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MlHcvD|INTEGER|Hepatitis C deaths among men
AsHcvD|NUMERIC|
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
NoIntP|NUMERIC|Percentage of Households without Internet access
WlfrExp|INTEGER|Total expenditures on public welfare programs
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
MedcdExp|INTEGER|Total medicaid spending
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
NoPrphLw|BOOLEAN|Dummy variable indicating whether the state has no state drug paraphernalia law (0=no, 1=yes)
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MulHcvD|NUMERIC|
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
NhPiHcvD|NUMERIC|
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
OdMortRt|NUMERIC|Overdose mortality rate
MedPolP5Yr|NUMERIC|Proportion of the five-year period (ending in given year) for which Medicaid Expansion was implemented / in effect
FlHcvD|INTEGER|Hepatitis C deaths among women
PrNtRefInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law does not refer to objects used for injecting drugs (0=no, 1=yes)
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
WhtHcvD|NUMERIC|

### state-2018

ID: `oeps-391119.tabular.state-2018`

120 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
GradSclP|NUMERIC|
Ovr16|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
TotPopHh|INTEGER|Total number of people in households
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
HisP|NUMERIC|
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
TotWrkE|INTEGER|Estimated count of working population
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
SRatio18|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
TradFedExp|INTEGER|Traditional medicaid - federal spending
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
StateArea|NUMERIC|Area (in square meters) of state
MlHcvD|INTEGER|Hepatitis C deaths among men
RentalP|NUMERIC|Percentage of occupied housing units that are rented
TradSttExp|INTEGER|Traditional medicaid - state spending
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
TotTracts|INTEGER|Total number of census tracts within the state.
AsHcvD|NUMERIC|
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
MedcdExp|INTEGER|Total medicaid spending
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
Ovr21P|NUMERIC|
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
ExpnSttExp|INTEGER|Expansion Group - State Spending
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
AlcTot|INTEGER|Total number of alcohol outlets
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MulHcvD|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
Age15_44|INTEGER|Total population between age 15-44
NhPiHcvD|NUMERIC|
AreaSqMi|NUMERIC|Land area of geography in sq miles
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
OdMortRt|NUMERIC|Overdose mortality rate
AlcDens|NUMERIC|Number of alcohol outlets per square mile
FlHcvD|INTEGER|Hepatitis C deaths among women
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
TwoRaceP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
ExpnFedExp|INTEGER|Expansion Group - Federal Spending
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
WhtHcvD|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
EngProf|NUMERIC|

### zcta-2018

ID: `oeps-391119.tabular.zcta-2018`

82 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
GradSclP|NUMERIC|
Ovr16|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
TotPopHh|INTEGER|Total number of people in households
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
RetailP|NUMERIC|Percentage of population employed in retail trade industry
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotWrkE|INTEGER|Estimated count of working population
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
SRatio18|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
SviSmryRnk|NUMERIC|Overall summary ranking
RentalP|NUMERIC|Percentage of occupied housing units that are rented
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
Ovr21P|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
AlcTot|INTEGER|Total number of alcohol outlets
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
AreaSqMi|NUMERIC|Land area of geography in sq miles
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
AlcDens|NUMERIC|Number of alcohol outlets per square mile
ChildrenP|NUMERIC|Percentage of population under age 18
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
EngProf|NUMERIC|

### tract-2023

ID: `oeps-391119.tabular.tract-2023`

85 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
GradSclP|NUMERIC|
Ovr16|NUMERIC|
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
TotPopHh|INTEGER|Total number of people in households
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HisP|NUMERIC|
MedAge|NUMERIC|
SocCapInd|NUMERIC|Composite index of LngTermP, LibPerCap, RlgPerCap
HHSize|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotWrkE|INTEGER|Estimated count of working population
SRatio18|NUMERIC|
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
MedHsgTen|STRING|Median time period occupant moved into housing unit by tract
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
HsdTot|NUMERIC|
RentalP|NUMERIC|Percentage of occupied housing units that are rented
HhldMS|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
WidwdP|NUMERIC|
HsdTypCo|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFC|NUMERIC|
Ovr21P|NUMERIC|
DivrcdP|NUMERIC|
CrowdHsng|NUMERIC|
SepartedP|NUMERIC|
HhldFS|NUMERIC|
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HhldFA|NUMERIC|
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
RlgPerCap|NUMERIC|Religious institutions per capita by census tract
FamSize|NUMERIC|
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MrrdP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
HhldMA|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr62P|NUMERIC|
HsdTypMC|NUMERIC|
MaleP|NUMERIC|
HhldMC|NUMERIC|
LibPerCap|NUMERIC|Libraries per capita by census tract
NvMrrdP|NUMERIC|
TwoRaceP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
HsdTypM|NUMERIC|
Ovr16P|NUMERIC|
Und18P|NUMERIC|
OccupantP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
EngProf|NUMERIC|

### county-2024

ID: `oeps-391119.tabular.county-2024`

8 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data

### state-2013

ID: `oeps-391119.tabular.state-2013`

12 columns in this table.

Name|Data Type|Description
-|-|-|-
HcvD|INTEGER|Total Hepatitis C deaths
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
FlHcvD|INTEGER|Hepatitis C deaths among women
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations

### state-2010

ID: `oeps-391119.tabular.state-2010`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
GradSclP|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
MaleP|NUMERIC|
TwoRaceP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### state-2000

ID: `oeps-391119.tabular.state-2000`

43 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
Ovr16|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
HisP|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### zcta-2020

ID: `oeps-391119.tabular.zcta-2020`

109 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
GradSclP|NUMERIC|
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
TotPopHh|INTEGER|Total number of people in households
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HisP|NUMERIC|
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
MedAge|NUMERIC|
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
HHSize|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotWrkE|INTEGER|Estimated count of working population
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
SRatio18|NUMERIC|
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
HsdTot|NUMERIC|
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
RentalP|NUMERIC|Percentage of occupied housing units that are rented
HhldMS|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BupCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
WidwdP|NUMERIC|
HsdTypCo|NUMERIC|
BachelorsP|NUMERIC|
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
SRatio|NUMERIC|
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFC|NUMERIC|
Ovr21P|NUMERIC|
SutTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip SUT destination centroid, in minutes
DivrcdP|NUMERIC|
CrowdHsng|NUMERIC|
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
SepartedP|NUMERIC|
HhldFS|NUMERIC|
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HhldFA|NUMERIC|
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
FamSize|NUMERIC|
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MrrdP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
HhldMA|NUMERIC|
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
MhCntDr|INTEGER|Count of MH providers within a 30-minute driving threshold
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr62P|NUMERIC|
HsdTypMC|NUMERIC|
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
MaleP|NUMERIC|
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
HhldMC|NUMERIC|
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
NvMrrdP|NUMERIC|
TwoRaceP|NUMERIC|
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
HsdTypM|NUMERIC|
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
Ovr16P|NUMERIC|
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
Und18P|NUMERIC|
OccupantP|NUMERIC|
FemP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
EngProf|NUMERIC|

### county-2016

ID: `oeps-391119.tabular.county-2016`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlPrPpr|NUMERIC|Total Prison Population Rate
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlPrPp|INTEGER|Total Prison Population Count
TtlPrAPp|INTEGER|Prison Prison Admissions Count
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate

### county-2023

ID: `oeps-391119.tabular.county-2023`

115 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
GradSclP|NUMERIC|
Ovr16|NUMERIC|
RspRt|NUMERIC|Percent of units interviewed from total units intended for interview
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
TotPopHh|INTEGER|Total number of people in households
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
RetailP|NUMERIC|Percentage of population employed in retail trade industry
HisP|NUMERIC|
MedAge|NUMERIC|
HHSize|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotWrkE|INTEGER|Estimated count of working population
SRatio18|NUMERIC|
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TtlJlPrtQ4|NUMERIC|Pretrial Jail Population Count (Q4)
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
TtlJlPrtrQ3|NUMERIC|Pretrial Jail Population Rate (Q3)
HsdTot|NUMERIC|
RentalP|NUMERIC|Percentage of occupied housing units that are rented
HhldMS|NUMERIC|
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
TtlJlPprQ2|NUMERIC|Total Jail Population Rate (Q2), ASJ/COJ Data
TtlJlPprQ1|NUMERIC|Total Jail Population Rate (Q1), ASJ/COJ Data
TtlJlAdmrQ1|NUMERIC|Total Jail Admissions Rate (Q1), ASJ/COJ Data
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
Ovr18P|NUMERIC|
TtlJlAdmrQ4|NUMERIC|Total Jail Admissions Rate (Q4), ASJ/COJ Data
TtlJlAdmrQ2|NUMERIC|Total Jail Admissions Rate (Q2), ASJ/COJ Data
WidwdP|NUMERIC|
HsdTypCo|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
TtlJlPrtrQ2|NUMERIC|Pretrial Jail Population Rate (Q2)
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
TtlJlPrtrQ1|NUMERIC|Pretrial Jail Population Rate (Q1)
HhldFC|NUMERIC|
Ovr21P|NUMERIC|
DivrcdP|NUMERIC|
TtlJlPrtQ3|NUMERIC|Pretrial Jail Population Count (Q3)
CrowdHsng|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
SepartedP|NUMERIC|
TtlJlPpQ3|NUMERIC|Total Jail Population Count (Q3), ASJ/COJ Data
HhldFS|NUMERIC|
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
HhldFA|NUMERIC|
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
TtlJlPrtQ1|NUMERIC|Pretrial Jail Population Count (Q1)
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
FamSize|NUMERIC|
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
TtlJlPrtQ2|NUMERIC|Pretrial Jail Population Count (Q2)
MrrdP|NUMERIC|
TtlJlPprQ4|NUMERIC|Total Jail Population Rate (Q4), ASJ/COJ Data
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
TtlJlPpQ2|NUMERIC|Total Jail Population Count (Q2), ASJ/COJ Data
TtlJlAdmrQ3|NUMERIC|Total Jail Admissions Rate (Q3), ASJ/COJ Data
Ovr21|NUMERIC|
TtlJlAdmQ4|NUMERIC|Total Jail Admissions Count (Q4), ASJ/COJ Data
TtlJlPrtrQ4|NUMERIC|Pretrial Jail Population Rate (Q4)
TtlJlPpQ4|NUMERIC|Total Jail Population Count (Q4), ASJ/COJ Data
HhldMA|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr62P|NUMERIC|
HsdTypMC|NUMERIC|
TtlJlAdmQ3|NUMERIC|Total Jail Admissions Count (Q3), ASJ/COJ Data
MaleP|NUMERIC|
TtlJlAdmQ2|NUMERIC|Total Jail Admissions Count (Q2), ASJ/COJ Data
TtlJlAdmQ1|NUMERIC|Total Jail Admissions Count (Q1), ASJ/COJ Data
HhldMC|NUMERIC|
NvMrrdP|NUMERIC|
TwoRaceP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
HsdTypM|NUMERIC|
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
Ovr16P|NUMERIC|
Und18P|NUMERIC|
OccupantP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TtlJlPprQ3|NUMERIC|Total Jail Population Rate (Q3), ASJ/COJ Data
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
TtlJlPpQ1|NUMERIC|Total Jail Population Count (Q1), ASJ/COJ Data
EngProf|NUMERIC|

### tract-2010

ID: `oeps-391119.tabular.tract-2010`

48 columns in this table.

Name|Data Type|Description
-|-|-|-
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
GradSclP|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
TotVetPop|INTEGER|Total Veteran population
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
VetP|NUMERIC|Percent of population that are veterans
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
MaleP|NUMERIC|
TwoRaceP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

### tract-2000

ID: `oeps-391119.tabular.tract-2000`

46 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
Ovr16|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
HisP|NUMERIC|
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SRatio18|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EduHsP|NUMERIC|
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
VacantP|NUMERIC|Percentage of vacant housing units
Ovr18P|NUMERIC|
BachelorsP|NUMERIC|
Ovr18|NUMERIC|
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
SRatio|NUMERIC|
Ovr21P|NUMERIC|
TotUnits|INTEGER|Count of total occupied housing units
EduNoHsP|NUMERIC|
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
Ovr65P|NUMERIC|Percentage of population over 65
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SomeCollegeP|NUMERIC|
Ovr21|NUMERIC|
Age15_44|INTEGER|Total population between age 15-44
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TotPop|INTEGER|Total population
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ChildrenP|NUMERIC|Percentage of population under age 18
MaleP|NUMERIC|
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
Ovr16P|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
FemP|NUMERIC|
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population

