# Project Id: oeps-391119

1 dataset in this project: tabular

## tabular

58 tables in this dataset.

### state-2010

ID: `oeps-391119.tabular.state-2010`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
TwoRaceP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
TotVetPop|INTEGER|Total Veteran population
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
EduNoHsP|NUMERIC|
Ovr18P|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### state-2015

ID: `oeps-391119.tabular.state-2015`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
FlHcvD|INTEGER|Hepatitis C deaths among women
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
OdMortRt|NUMERIC|Overdose mortality rate
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
HcvD|INTEGER|Total Hepatitis C deaths
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### county-providers-2010

ID: `oeps-391119.tabular.county-providers-2010`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
TotPcp|INTEGER|Number of primary care providers in area
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PcpPer100k|NUMERIC|PCPs per total Population X 100,000
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotSp|INTEGER|Number of specialty physicians in area
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000

### county-2024

ID: `oeps-391119.tabular.county-2024`

8 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate

### tract-2021

ID: `oeps-391119.tabular.tract-2021`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.

### tract-2022

ID: `oeps-391119.tabular.tract-2022`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking

### county-2019

ID: `oeps-391119.tabular.county-2019`

11 columns in this table.

Name|Data Type|Description
-|-|-|-
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
TtlPrPpr|NUMERIC|Total Prison Population Rate
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
TtlPrAPp|INTEGER|Prison Prison Admissions Count
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
NoIntP|NUMERIC|Percentage of Households without Internet access
TtlPrPp|INTEGER|Total Prison Population Count

### county-2016

ID: `oeps-391119.tabular.county-2016`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlPrPpr|NUMERIC|Total Prison Population Rate
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
TtlPrAPp|INTEGER|Prison Prison Admissions Count
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlPrPp|INTEGER|Total Prison Population Count

### tract-2025

ID: `oeps-391119.tabular.tract-2025`

90 columns in this table.

Name|Data Type|Description
-|-|-|-
NaltCntDr60|NUMERIC|Count of naltrexone providers in 60 minute drive time threshold
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
SutTmDr|NUMERIC|Driving time (min) to nearest  Substance Use Treatment (SUT) facility
RxTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid with impedance factor, in minutes
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
HcvCntDr|INTEGER|Number of HCV testing providers within a 30-minute drive
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
HivTmDr|NUMERIC|Driving time from origin to nearest HIV testing provider (minutes)
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
TlBupTmDr|NUMERIC|Estimated driving time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
MhCntDr|INTEGER|Count of mental health providers within a 30-minute driving threshold
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
NaltFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Naltrexone within a 60-minute drive
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
HospTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes with Impedance factor
TlBupCntWk30|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 30-minute walking time threshold
BupRm30|NUMERIC|Buprenorphine access 30 minutes (RAAM)
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
BupRm60|NUMERIC|Buprenorphine access 60 minutes (RAAM)
TlBupMinDis|NUMERIC|Euclidean distance (in miles) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
NaltFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Naltrexone within a 30-minute drive
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
BupFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Buprenorphine within a 30-minute drive
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
MetFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Methadone within a 60-minute drive
MetFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Methadone within a 30-minute drive
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
FqhcTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes, with Impedance factor
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
TlBupCntDr30|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 30-minute driving time threshold
MhTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip Mental Health Provider with impedance destination centroid, in minutes
MetCntDr60|NUMERIC|Count of methadone providers in 60 minute drive time threshold
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
BupCntDr60|NUMERIC|Count of buprenorphine providers in 60 minute drive time threshold
SutTmDr2|NUMERIC|Driving time (minutes) from the tract centroid to the nearest Substance Use Treatment provider, with the impedance factor applied.
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OtpFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to opioid treatment programs within a 30-minute drive
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
OtpRm60|NUMERIC|Opioid Treatment Provider access 60 minutes (RAAM)
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
HcvTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip HCV Testing Facility with impedance destination centroid, in minutes
SspTmDr|NUMERIC|Driving time in minutes from origin census tract centroid to census tract centroid of nearest SSP
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
TlBupCntDr60|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 60-minute driving time threshold
HcvMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest HCV testing provider (miles)
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
TlBupCntBk30|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 30-minute biking time threshold
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
SspTmDr2|NUMERIC|Driving time in minutes from origin census tract centroid to census tract centroid of nearest SSP and back to origin census tract centroid
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
BupFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Buprenorphine within a 30-minute drive
NaltRm60|NUMERIC|Naltrexone access 60 minutes (RAAM)
OtpRm30|NUMERIC|Opioid Treatment Provider access 30 minutes (RAAM)
HcvTmDr|NUMERIC|Driving time from origin to nearest HCV testing provider (minutes)
HivMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest HIV testing provider (miles)
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
HivCntDr|INTEGER|Number of HIV testing providers within a 30-minute drive
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes
HivTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip HIV Testing Facility with impedance destination centroid, in minutes
NaltRm30|NUMERIC|Naltrexone access 30 minutes (RAAM)
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
OtpFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to opioid treatment programs within a 60-minute drive

### state-2000

ID: `oeps-391119.tabular.state-2000`

43 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
HisP|NUMERIC|
Ovr18P|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### tract-1990

ID: `oeps-391119.tabular.tract-1990`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
Ovr16|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
HisP|NUMERIC|
Ovr18P|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### state-2014

ID: `oeps-391119.tabular.state-2014`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
FlHcvD|INTEGER|Hepatitis C deaths among women
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
OdMortRt|NUMERIC|Overdose mortality rate
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
HcvD|INTEGER|Total Hepatitis C deaths
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### county-2000

ID: `oeps-391119.tabular.county-2000`

44 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
HisP|NUMERIC|
DmyBlckBlt|BOOLEAN|Dummy variable for whether county is in the Southern Black Belt region
Ovr18P|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### state-1990

ID: `oeps-391119.tabular.state-1990`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
HisP|NUMERIC|
Ovr18P|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### state-2023

ID: `oeps-391119.tabular.state-2023`

71 columns in this table.

Name|Data Type|Description
-|-|-|-
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
GradSclP|NUMERIC|
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
TwoRaceP|NUMERIC|
ExpnFedExp|INTEGER|Expansion Group - Federal Spending
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
EdBupPolP|NUMERIC|Proportion of Entire Data Period with State-Level Buprenorphine Policy in Effect
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
TradFedExp|INTEGER|Traditional medicaid - federal spending
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
FemP|NUMERIC|
ExpnSttExp|INTEGER|Expansion Group - State Spending
SRatio|NUMERIC|
EngProf|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
TradSttExp|INTEGER|Traditional medicaid - state spending
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
SRatio18|NUMERIC|
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
Ovr16|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
Ovr65P|NUMERIC|Percentage of population over 65
PerImpBupP|STRING|Periods of Implementation of State-Level Buprenorphine Policy (Associated Date Ranges)
SomeCollegeP|NUMERIC|
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
Ovr18|NUMERIC|
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
HisP|NUMERIC|
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
Ovr18P|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
BupPolP|NUMERIC|Proportion of Year with State-Level Buprenorphine Policy in Effect
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotPop|INTEGER|Total population
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
EduHsP|NUMERIC|
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
MedcdExp|INTEGER|Total medicaid spending
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### state-2022

ID: `oeps-391119.tabular.state-2022`

64 columns in this table.

Name|Data Type|Description
-|-|-|-
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
OpRxRt|NUMERIC|Opioid prescription rate
NhPiHcvD|NUMERIC|
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
AvA50_74HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people between 50 and 74 years of age from 2013-2017, 2018-2022
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
HlthExp|INTEGER|Total expenditures on public health and hospitals
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
AvBlkHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Black populations from 2013-2017
CrrctExp|INTEGER|Total expenditures on corrections system and operations
WlfrExp|INTEGER|Total expenditures on public welfare programs
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
WhtHcvD|NUMERIC|
MulHcvD|NUMERIC|
AvO75HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people over 75 years of age
AvHspHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Hispanic populations from 2013-2017
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AsHcvD|NUMERIC|
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
AvAsHcvD|NUMERIC|
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
ParkArea|NUMERIC|Area (in square meters) of park or green space in a state).
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
AvHcvD|NUMERIC|Mean total yearly Hepatitis C deaths from 2013-2017, 2018-2022
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AvU50HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people under 50 years of age from 2013-2017
PrMsuseP|NUMERIC|Percent of persons who self-report misusing prescription pain relief medication in 2020.
TtlPrPpr|NUMERIC|Total Prison Population Rate
FlHcvD|INTEGER|Hepatitis C deaths among women
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
MlHcvD|INTEGER|Hepatitis C deaths among men
AvMlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among men from 2013-2017
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
OdMortRt|NUMERIC|Overdose mortality rate
AvAmInHcvD|NUMERIC|Mean yearly Hepatitis C deaths among American Indian population from 2013-2017
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
TtlPrAPp|INTEGER|Prison Prison Admissions Count
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
AvNhPiHcvD|NUMERIC|
AvMulHcvD|NUMERIC|
HcvD|INTEGER|Total Hepatitis C deaths
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
AvWhHcvD|NUMERIC|Mean yearly Hepatitis C deaths among White populations from 2018-2022
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AvFlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among women from 2013-2017
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
TtlPrPp|INTEGER|Total Prison Population Count

### state-2013

ID: `oeps-391119.tabular.state-2013`

12 columns in this table.

Name|Data Type|Description
-|-|-|-
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
FlHcvD|INTEGER|Hepatitis C deaths among women
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
HcvD|INTEGER|Total Hepatitis C deaths
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### county-1980

ID: `oeps-391119.tabular.county-1980`

40 columns in this table.

Name|Data Type|Description
-|-|-|-
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
HisP|NUMERIC|
Ovr18P|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### zcta-2023

ID: `oeps-391119.tabular.zcta-2023`

89 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
GradSclP|NUMERIC|
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
TwoRaceP|NUMERIC|
HsdTot|NUMERIC|
SepartedP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
RentalP|NUMERIC|Percentage of occupied housing units that are rented
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
CrowdHsng|NUMERIC|
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|
TotVetPop|INTEGER|Total Veteran population
FemP|NUMERIC|
SRatio|NUMERIC|
EngProf|NUMERIC|
HhldFC|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
HhldFA|NUMERIC|
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
SomeCollegeP|NUMERIC|
MedAge|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HsdTypM|NUMERIC|
HhldFS|NUMERIC|
HhldMA|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
Ovr18|NUMERIC|
OccupantP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
FamSize|NUMERIC|
HisP|NUMERIC|
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr18P|NUMERIC|
TotPopHh|INTEGER|Total number of people in households
HHSize|NUMERIC|
NvMrrdP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
HhldMC|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
HsdTypCo|NUMERIC|
Ovr21P|NUMERIC|
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
DivrcdP|NUMERIC|
TotPop|INTEGER|Total population
Und18P|NUMERIC|
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
Ovr62P|NUMERIC|
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HhldMS|NUMERIC|
WidwdP|NUMERIC|
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
TotWrkE|INTEGER|Estimated count of working population
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
HsdTypMC|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### county-2018

ID: `oeps-391119.tabular.county-2018`

91 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
RentalP|NUMERIC|Percentage of occupied housing units that are rented
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
TotVetPop|INTEGER|Total Veteran population
FemP|NUMERIC|
RspRt|NUMERIC|Percent of units interviewed from total units intended for interview
SRatio|NUMERIC|
EngProf|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AreaSqMi|NUMERIC|Land area of geography in sq miles
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
Ovr65P|NUMERIC|Percentage of population over 65
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
Age15_44|INTEGER|Total population between age 15-44
RcaUrbanP|NUMERIC|Percent census tracts in the county classified as Urban using RUCA codes
SomeCollegeP|NUMERIC|
TotTracts|INTEGER|Total number of census tracts within the state.
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
AlcDens|NUMERIC|Number of alcohol outlets per square mile
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
Ovr18|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
OdMortRt|NUMERIC|Overdose mortality rate
RcaRuralP|NUMERIC|Percent census tracts in the county classified as Rural using RUCA codes
RcaSubrbP|NUMERIC|Percent census tracts in the county classified as Suburban using RUCA codes
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr18P|NUMERIC|
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
TotPopHh|INTEGER|Total number of people in households
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
CenFlags|STRING|Three different values indicating three things:
1 - Revised count, so urban and rural components will not add to total. 
2 - Geography name and FIPS code were changed since 2010. Shannon County, Sotuh Dakota name changed to Oglala Lakota County, new FIPS 46102. Wade Hampton Census Area, Alaska, name changed to Kusilvak CEnsus Area, nwe FIPS 02158
3 - Bedford City, Virginia, was consolidated with Bedford County, Virginia (FIPS 51019) since 2010.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotPop|INTEGER|Total population
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
SviSmryRnk|NUMERIC|Overall summary ranking
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
AlcTot|INTEGER|Total number of alcohol outlets
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
TotWrkE|INTEGER|Estimated count of working population
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### state-2025

ID: `oeps-391119.tabular.state-2025`

65 columns in this table.

Name|Data Type|Description
-|-|-|-
SutAvTmDr2|NUMERIC| Average driving time (minutes) across tracts in state to nearestSubstance Use Treatment Provider (Sut), with Impedance factor
OtpAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Opioid Treatment Provider (Otp), with Impedance factor
MetCtTmDr2|NUMERIC|Number of tracts with Methadone Providerwithin a 30-min driving range, with Impedance factor
FqhcAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center, with Impedance factor
OtpTmDrP2|NUMERIC|Percent of tracts with Opioid Treatment Provider within a 30-min driving range, with Impedance factor
NaltCtTmDr2|NUMERIC|Number of tracts with Naltrexone Provider within a 30-min driving range, with Impedance factor
MetAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest methadone provider
HivAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HIV Testing Facility, with impedance
MhCtTmDr2|NUMERIC|Number of tracts with Mental Health Provider within a 30-min driving range, with impedance
HivCtTmDr2|NUMERIC|Number of tracts with HIV Testing Facility within a 30-min driving range, with impedance
BupTmDrP2|NUMERIC|Percent of tracts with Buprenorphine Provider within a 30-min driving range, with Impedance factor
HcvTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HCV testing provider
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
HcvTmDrP2|NUMERIC|Percent of tracts with HCV Testing Facility within a 30-mini driving range, with impedance
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
MhTmDrP2|NUMERIC|Percent of tracts with Mental Health Provider within a 30-mini driving range, with impedence
RxAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy with Impedance Factor
FqhcTmDrP2|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.
HcvCtTmDr|INTEGER|Number of tracts with an HCV testing provider within a 30-minute driving range
SmokeP|NUMERIC|Percentage of Smoking Population
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
SutTmDrP2|NUMERIC|Percent of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
SutTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
HcvAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HCV testing provider
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
MhAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Mental Health Provider, with impedance
TotTracts|INTEGER|Total number of census tracts within the state.
OtpCtTmDr2|NUMERIC|Number of tracts with Opioid Treatment Provider within a 30-min driving range, with Impedance factor
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
HospTmDrP2|NUMERIC|Percent of tracts with hospital within a 30-mini driving range with Impedance Factor
HivAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HIV testing provider
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
HivTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HIV testing provider
HivCtTmDr|INTEGER|Number of tracts with an HIV testing provider within a 30-minute driving range
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range
BupCtTmDr2|NUMERIC|Number of tracts with Buprenorphine Provider within a 30-min driving range, with Impedance factor
HcvAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HCV Testing Facility, with impedance
RxCtTmDr2|INTEGER|Number of tracts with pharmacy within a 30-min driving range with impedance factor
MetTmDrP2|NUMERIC|Percent of tracts with Methadone Providerwithin a 30-min driving range, with Impedance factor
RxTmDrP2|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range with impedance factor
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
SutCtTmDr2|NUMERIC|Number of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
SutCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
FqhcCtTmDr2|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
HospAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital with Impedance factor
NaltAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest naltrexone provider
HcvCtTmDr2|NUMERIC|Number of tracts with HCV Testing Facility within a 30-min driving range, with impedance
BupAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Buprenorphine Provider (BUP), with Impedance factor
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
NaltAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Naltrexone Provider (NALT), with Impedance factor
MetAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Methadone Provider(MET), with Impedance factor
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
BupAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest buprenorphine provider
HivTmDrP2|NUMERIC|Percent of tracts with HIV Testing Facility within a 30-mini driving range, with impedance
SutAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
NaltTmDrP2|NUMERIC|Percent of tracts with Naltrexone Provider within a 30-min driving range, with Impedance factor
HospCtTmDr2|NUMERIC|Number of tracts with Hospitals within a 30-min driving range, with impedance
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range

### zcta-2022

ID: `oeps-391119.tabular.zcta-2022`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
SviSmryRnk|NUMERIC|Overall summary ranking

### tract-sdoh-2014

ID: `oeps-391119.tabular.tract-sdoh-2014`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
NeighbTyp|STRING|Categorical, one of seven neighborhood (tract-level) typologies: 1 = Rural Affordable; 2 = Suburban Affluent; 3 = Suburban Affordable; 4 = Extreme Poverty; 5 = Multilingual Working; 6 = Urban Core Opportunity; 7 = Sparse Areas
UrbCoreInd|NUMERIC|Raw Urban Core Opportunity Index (https://sdohatlas.github.io/)
LimMobInd|NUMERIC|Raw Limited Mobility Index (https://sdohatlas.github.io/)
SocEcAdvIn|NUMERIC|Raw Socioeconomic Advantage Index (https://sdohatlas.github.io/)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
MicaInd|NUMERIC|Raw Mixed Immigrant Cohesion and Accessibility (MICA) Index (https://sdohatlas.github.io/)

### county-1990

ID: `oeps-391119.tabular.county-1990`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
HisP|NUMERIC|
Ovr18P|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### state-2016

ID: `oeps-391119.tabular.state-2016`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
FlHcvD|INTEGER|Hepatitis C deaths among women
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
OdMortRt|NUMERIC|Overdose mortality rate
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
HcvD|INTEGER|Total Hepatitis C deaths
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### state-2018

ID: `oeps-391119.tabular.state-2018`

120 columns in this table.

Name|Data Type|Description
-|-|-|-
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
GradSclP|NUMERIC|
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
NhPiHcvD|NUMERIC|
TwoRaceP|NUMERIC|
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
ExpnFedExp|INTEGER|Expansion Group - Federal Spending
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
StateArea|NUMERIC|Area (in square meters) of state
RentalP|NUMERIC|Percentage of occupied housing units that are rented
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
WhtHcvD|NUMERIC|
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
MulHcvD|NUMERIC|
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
TradFedExp|INTEGER|Traditional medicaid - federal spending
AsHcvD|NUMERIC|
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
TotVetPop|INTEGER|Total Veteran population
FemP|NUMERIC|
ExpnSttExp|INTEGER|Expansion Group - State Spending
SRatio|NUMERIC|
EngProf|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
TradSttExp|INTEGER|Traditional medicaid - state spending
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
AreaSqMi|NUMERIC|Land area of geography in sq miles
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
Ovr16|NUMERIC|
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
Ovr65P|NUMERIC|Percentage of population over 65
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
TotTracts|INTEGER|Total number of census tracts within the state.
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
FlHcvD|INTEGER|Hepatitis C deaths among women
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
AlcDens|NUMERIC|Number of alcohol outlets per square mile
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
Ovr18|NUMERIC|
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
OdMortRt|NUMERIC|Overdose mortality rate
HisP|NUMERIC|
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr18P|NUMERIC|
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
TotPopHh|INTEGER|Total number of people in households
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
HcvD|INTEGER|Total Hepatitis C deaths
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotPop|INTEGER|Total population
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
AlcTot|INTEGER|Total number of alcohol outlets
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
TotWrkE|INTEGER|Estimated count of working population
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
MedcdExp|INTEGER|Total medicaid spending
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### county-2025

ID: `oeps-391119.tabular.county-2025`

61 columns in this table.

Name|Data Type|Description
-|-|-|-
SutAvTmDr2|NUMERIC| Average driving time (minutes) across tracts in state to nearestSubstance Use Treatment Provider (Sut), with Impedance factor
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
FqhcAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center, with Impedance factor
TlBupTmDr|NUMERIC|Estimated driving time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
HivAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HIV Testing Facility, with impedance
MhCtTmDr2|NUMERIC|Number of tracts with Mental Health Provider within a 30-min driving range, with impedance
HivCtTmDr2|NUMERIC|Number of tracts with HIV Testing Facility within a 30-min driving range, with impedance
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
HcvTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HCV testing provider
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
HcvTmDrP2|NUMERIC|Percent of tracts with HCV Testing Facility within a 30-mini driving range, with impedance
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
MhTmDrP2|NUMERIC|Percent of tracts with Mental Health Provider within a 30-mini driving range, with impedence
RxAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy with Impedance Factor
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
FqhcTmDrP2|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
TlBupMinDis|NUMERIC|Euclidean distance (in miles) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.
HcvCtTmDr|INTEGER|Number of tracts with an HCV testing provider within a 30-minute driving range
SmokeP|NUMERIC|Percentage of Smoking Population
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
SutTmDrP2|NUMERIC|Percent of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
SutTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
HcvAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HCV testing provider
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
MhAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Mental Health Provider, with impedance
TotTracts|INTEGER|Total number of census tracts within the state.
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
HospTmDrP2|NUMERIC|Percent of tracts with hospital within a 30-mini driving range with Impedance Factor
HivAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HIV testing provider
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
HivTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HIV testing provider
HivCtTmDr|INTEGER|Number of tracts with an HIV testing provider within a 30-minute driving range
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range
HcvAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HCV Testing Facility, with impedance
RxCtTmDr2|INTEGER|Number of tracts with pharmacy within a 30-min driving range with impedance factor
RxTmDrP2|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range with impedance factor
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
SutCtTmDr2|NUMERIC|Number of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
SutCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
FqhcCtTmDr2|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
HospAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital with Impedance factor
HcvCtTmDr2|NUMERIC|Number of tracts with HCV Testing Facility within a 30-min driving range, with impedance
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
HivTmDrP2|NUMERIC|Percent of tracts with HIV Testing Facility within a 30-mini driving range, with impedance
SutAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
HospCtTmDr2|NUMERIC|Number of tracts with Hospitals within a 30-min driving range, with impedance
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range

### county-2015

ID: `oeps-391119.tabular.county-2015`

4 columns in this table.

Name|Data Type|Description
-|-|-|-
DmySgrg|BOOLEAN|Dummy variable for whether county is part of a hypersegregated city or its metropolitan area
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.

### tract-2023

ID: `oeps-391119.tabular.tract-2023`

85 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
TwoRaceP|NUMERIC|
HsdTot|NUMERIC|
SepartedP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
RentalP|NUMERIC|Percentage of occupied housing units that are rented
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
CrowdHsng|NUMERIC|
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|
TotVetPop|INTEGER|Total Veteran population
FemP|NUMERIC|
SRatio|NUMERIC|
EngProf|NUMERIC|
HhldFC|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
HhldFA|NUMERIC|
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
LibPerCap|NUMERIC|Libraries per capita by census tract
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
MedHsgTen|STRING|Median time period occupant moved into housing unit by tract
SomeCollegeP|NUMERIC|
MedAge|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HsdTypM|NUMERIC|
HhldFS|NUMERIC|
HhldMA|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
SocCapInd|NUMERIC|Composite index of LngTermP, LibPerCap, RlgPerCap
RlgPerCap|NUMERIC|Religious institutions per capita by census tract
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
OccupantP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
FamSize|NUMERIC|
HisP|NUMERIC|
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr18P|NUMERIC|
TotPopHh|INTEGER|Total number of people in households
HHSize|NUMERIC|
NvMrrdP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
HhldMC|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
HsdTypCo|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
DivrcdP|NUMERIC|
TotPop|INTEGER|Total population
Und18P|NUMERIC|
Ovr62P|NUMERIC|
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HhldMS|NUMERIC|
WidwdP|NUMERIC|
TotWrkE|INTEGER|Estimated count of working population
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
HsdTypMC|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### zcta-2025

ID: `oeps-391119.tabular.zcta-2025`

3 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### county-2023

ID: `oeps-391119.tabular.county-2023`

115 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlJlAdmQ1|NUMERIC|Total Jail Admissions Count (Q1), ASJ/COJ Data
TtlJlAdmQ3|NUMERIC|Total Jail Admissions Count (Q3), ASJ/COJ Data
GradSclP|NUMERIC|
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
TwoRaceP|NUMERIC|
HsdTot|NUMERIC|
TtlJlPrtrQ4|NUMERIC|Pretrial Jail Population Rate (Q4)
SepartedP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
TtlJlPrtQ1|NUMERIC|Pretrial Jail Population Count (Q1)
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
TtlJlPprQ3|NUMERIC|Total Jail Population Rate (Q3), ASJ/COJ Data
RentalP|NUMERIC|Percentage of occupied housing units that are rented
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
TtlJlPprQ4|NUMERIC|Total Jail Population Rate (Q4), ASJ/COJ Data
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
CrowdHsng|NUMERIC|
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|
TtlJlPrtrQ1|NUMERIC|Pretrial Jail Population Rate (Q1)
TotVetPop|INTEGER|Total Veteran population
TtlJlAdmrQ4|NUMERIC|Total Jail Admissions Rate (Q4), ASJ/COJ Data
FemP|NUMERIC|
RspRt|NUMERIC|Percent of units interviewed from total units intended for interview
SRatio|NUMERIC|
EngProf|NUMERIC|
TtlJlAdmQ2|NUMERIC|Total Jail Admissions Count (Q2), ASJ/COJ Data
HhldFC|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
TtlJlPpQ3|NUMERIC|Total Jail Population Count (Q3), ASJ/COJ Data
HhldFA|NUMERIC|
RetailP|NUMERIC|Percentage of population employed in retail trade industry
TtlJlPpQ4|NUMERIC|Total Jail Population Count (Q4), ASJ/COJ Data
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
TtlJlPrtQ2|NUMERIC|Pretrial Jail Population Count (Q2)
TtlJlPrtQ3|NUMERIC|Pretrial Jail Population Count (Q3)
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TtlJlAdmrQ2|NUMERIC|Total Jail Admissions Rate (Q2), ASJ/COJ Data
SomeCollegeP|NUMERIC|
MedAge|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HsdTypM|NUMERIC|
HhldFS|NUMERIC|
TtlJlAdmrQ3|NUMERIC|Total Jail Admissions Rate (Q3), ASJ/COJ Data
HhldMA|NUMERIC|
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
Ovr18|NUMERIC|
OccupantP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
FamSize|NUMERIC|
HisP|NUMERIC|
TtlJlPrtrQ3|NUMERIC|Pretrial Jail Population Rate (Q3)
TtlJlPpQ1|NUMERIC|Total Jail Population Count (Q1), ASJ/COJ Data
UnitDens|NUMERIC|Number of housing units per square mile of land area
TtlJlPrtQ4|NUMERIC|Pretrial Jail Population Count (Q4)
Ovr18P|NUMERIC|
TotPopHh|INTEGER|Total number of people in households
HHSize|NUMERIC|
NvMrrdP|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
HhldMC|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
HsdTypCo|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
DivrcdP|NUMERIC|
TotPop|INTEGER|Total population
Und18P|NUMERIC|
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
TtlJlPpQ2|NUMERIC|Total Jail Population Count (Q2), ASJ/COJ Data
TtlJlPrtrQ2|NUMERIC|Pretrial Jail Population Rate (Q2)
Ovr62P|NUMERIC|
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HhldMS|NUMERIC|
WidwdP|NUMERIC|
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
TotWrkE|INTEGER|Estimated count of working population
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
TtlJlPprQ2|NUMERIC|Total Jail Population Rate (Q2), ASJ/COJ Data
TtlJlAdmQ4|NUMERIC|Total Jail Admissions Count (Q4), ASJ/COJ Data
TtlJlAdmrQ1|NUMERIC|Total Jail Admissions Rate (Q1), ASJ/COJ Data
HsdTypMC|NUMERIC|
TtlJlPprQ1|NUMERIC|Total Jail Population Rate (Q1), ASJ/COJ Data
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### state-2017

ID: `oeps-391119.tabular.state-2017`

53 columns in this table.

Name|Data Type|Description
-|-|-|-
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
A50_74Hcv|NUMERIC|Mean yearly Hepatitis C cases in people between 50 to 74 years of age from 2013-2016
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
AvA50_74HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people between 50 and 74 years of age from 2013-2017, 2018-2022
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
AvBlkHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Black populations from 2013-2017
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
AvO75HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people over 75 years of age
AvHspHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Hispanic populations from 2013-2017
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AvAsPiHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Asian and Pacific Islanders population from 2013-2017
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
TotHcv|NUMERIC|Mean total yearly Hepitatis C cases from 2013-2016
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
Un50Hcv|NUMERIC|Mean yearly Hepatatis C cases in people under 50 years of age from 2013-2016
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
AvHcvD|NUMERIC|Mean total yearly Hepatitis C deaths from 2013-2017, 2018-2022
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
AvU50HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people under 50 years of age from 2013-2017
Ov75Hcv|NUMERIC|Mean yearly Hepatitis C cases in people over 75 years of age from 2013-2016
FlHcvD|INTEGER|Hepatitis C deaths among women
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
AvMlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among men from 2013-2017
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
OdMortRt|NUMERIC|Overdose mortality rate
AvAmInHcvD|NUMERIC|Mean yearly Hepatitis C deaths among American Indian population from 2013-2017
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
NonBlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations non-Black other race/ethnicity populations 2013-2016
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
HcvD|INTEGER|Total Hepatitis C deaths
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
FmHcv|NUMERIC|Mean yearly Hepatitis C cases in women from 2013-2016
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
BlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations identified as non-hispanic Black alone across 2013-2016
MlHcv|NUMERIC|Mean yearly Hepatitis C cases in men from 2013-2016
AvFlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among women from 2013-2017
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### county-2020

ID: `oeps-391119.tabular.county-2020`

116 columns in this table.

Name|Data Type|Description
-|-|-|-
MetCtTmBk|INTEGER|Number of tracts with methadone provider within a 30-min biking range
GradSclP|NUMERIC|
OpRxRt|NUMERIC|Opioid prescription rate
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
TwoRaceP|NUMERIC|
HsdTot|NUMERIC|
SepartedP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
MetAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest methadone provider
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
RentalP|NUMERIC|Percentage of occupied housing units that are rented
NaltAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest naltrexone provider
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
BupTmDrP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
NaltTmBkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min biking range
CrowdHsng|NUMERIC|
MetTmWkP|NUMERIC|Percent of tracts with methadone provider within a 30-min walking range
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|
TotVetPop|INTEGER|Total Veteran population
BupCtTmWk|INTEGER|Number of tracts with buprenorphine provider within a 30-min walking range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
FemP|NUMERIC|
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.
MetAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest methadone provider
SRatio|NUMERIC|
EngProf|NUMERIC|
HhldFC|NUMERIC|
NaltCtTmBk|INTEGER|Number of tracts with naltrexone provider within a 30-min biking range
MetTmBkP|NUMERIC|Percent of tracts with methadone provider within a 30-min biking range
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
NaltCtTmDr|INTEGER|Number of tracts with naltrexone provider within a 30-min driving range
HhldFA|NUMERIC|
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SRatio18|NUMERIC|
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
MetAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest methadone provider
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
SomeCollegeP|NUMERIC|
MedAge|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HsdTypM|NUMERIC|
HhldFS|NUMERIC|
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
MetCtTmWk|INTEGER|Number of tracts with methadone provider within a 30-min walking range
MetTmDrP|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range
NaltTmWkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min walking range
HhldMA|NUMERIC|
BupAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest buprenorphine provider
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
NaltTmDrP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OccupantP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range
MetCtTmDr|INTEGER|Number of tracts with methadone provider within a 30-min driving range
EduNoHsP|NUMERIC|
FamSize|NUMERIC|
OdMortRt|NUMERIC|Overdose mortality rate
HisP|NUMERIC|
BupCtTmDr|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr18P|NUMERIC|
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
TotPopHh|INTEGER|Total number of people in households
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
HHSize|NUMERIC|
NvMrrdP|NUMERIC|
HhldMC|NUMERIC|
NaltCtTmWk|INTEGER|Number of tracts with naltrexone provider within a 30-min walking range
BupAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest buprenorphine provider
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
NaltAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest naltrexone provider
HsdTypCo|NUMERIC|
BupTmBkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min biking range
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
NaltAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest naltrexone provider
DivrcdP|NUMERIC|
TotPop|INTEGER|Total population
Und18P|NUMERIC|
BupCtTmBk|INTEGER|Number of tracts with buprenorphine provider within a 30-min biking range
SviSmryRnk|NUMERIC|Overall summary ranking
Ovr62P|NUMERIC|
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
HhldMS|NUMERIC|
BupAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest buprenorphine provider
WidwdP|NUMERIC|
TotWrkE|INTEGER|Estimated count of working population
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
BupTmWkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min walking range
HsdTypMC|NUMERIC|

### tract-2020

ID: `oeps-391119.tabular.tract-2020`

123 columns in this table.

Name|Data Type|Description
-|-|-|-
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
GradSclP|NUMERIC|
SutTmDr|NUMERIC|Driving time (min) to nearest  Substance Use Treatment (SUT) facility
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
TwoRaceP|NUMERIC|
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
HsdTot|NUMERIC|
SepartedP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
MhCntDr|INTEGER|Count of mental health providers within a 30-minute driving threshold
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
RentalP|NUMERIC|Percentage of occupied housing units that are rented
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
BupRm30|NUMERIC|Buprenorphine access 30 minutes (RAAM)
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
CrowdHsng|NUMERIC|
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
BupRm60|NUMERIC|Buprenorphine access 60 minutes (RAAM)
TotVetPop|INTEGER|Total Veteran population
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
FemP|NUMERIC|
SRatio|NUMERIC|
EngProf|NUMERIC|
HhldFC|NUMERIC|
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
NaltRm90|NUMERIC|Naltrexone access 90 minutes (RAAM)
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
HhldFA|NUMERIC|
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SRatio18|NUMERIC|
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
VetP|NUMERIC|Percent of population that are veterans
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
SomeCollegeP|NUMERIC|
MedAge|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HsdTypM|NUMERIC|
HhldFS|NUMERIC|
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
HhldMA|NUMERIC|
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OccupantP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
EduNoHsP|NUMERIC|
FamSize|NUMERIC|
HisP|NUMERIC|
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr18P|NUMERIC|
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
TotPopHh|INTEGER|Total number of people in households
HHSize|NUMERIC|
NvMrrdP|NUMERIC|
HhldMC|NUMERIC|
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
HsdTypCo|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
BupRm90|NUMERIC|Buprenorphine access 90 minutes (RAAM)
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
DivrcdP|NUMERIC|
TotPop|INTEGER|Total population
Und18P|NUMERIC|
SviSmryRnk|NUMERIC|Overall summary ranking
NaltRm60|NUMERIC|Naltrexone access 60 minutes (RAAM)
Ovr62P|NUMERIC|
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HhldMS|NUMERIC|
WidwdP|NUMERIC|
TotWrkE|INTEGER|Estimated count of working population
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
NaltRm30|NUMERIC|Naltrexone access 30 minutes (RAAM)
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
HsdTypMC|NUMERIC|

### state-1980

ID: `oeps-391119.tabular.state-1980`

40 columns in this table.

Name|Data Type|Description
-|-|-|-
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
HisP|NUMERIC|
Ovr18P|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### zcta-2021

ID: `oeps-391119.tabular.zcta-2021`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes

### tract-2010

ID: `oeps-391119.tabular.tract-2010`

48 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
TwoRaceP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
TotVetPop|INTEGER|Total Veteran population
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
EduNoHsP|NUMERIC|
Ovr18P|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### zcta-2018

ID: `oeps-391119.tabular.zcta-2018`

82 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
GradSclP|NUMERIC|
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
RentalP|NUMERIC|Percentage of occupied housing units that are rented
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
TotVetPop|INTEGER|Total Veteran population
FemP|NUMERIC|
SRatio|NUMERIC|
EngProf|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AreaSqMi|NUMERIC|Land area of geography in sq miles
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
Ovr65P|NUMERIC|Percentage of population over 65
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
AlcDens|NUMERIC|Number of alcohol outlets per square mile
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
Ovr18|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr18P|NUMERIC|
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
TotPopHh|INTEGER|Total number of people in households
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotPop|INTEGER|Total population
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
SviSmryRnk|NUMERIC|Overall summary ranking
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
AlcTot|INTEGER|Total number of alcohol outlets
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
TotWrkE|INTEGER|Estimated count of working population
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### zcta-2019

ID: `oeps-391119.tabular.zcta-2019`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
NoIntP|NUMERIC|Percentage of Households without Internet access
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes

### county-2021

ID: `oeps-391119.tabular.county-2021`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.
OdMortRt|NUMERIC|Overdose mortality rate
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range

### tract-providers-2010

ID: `oeps-391119.tabular.tract-providers-2010`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
TotPcp|INTEGER|Number of primary care providers in area
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PcpPer100k|NUMERIC|PCPs per total Population X 100,000
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotSp|INTEGER|Number of specialty physicians in area
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000

### county-2017

ID: `oeps-391119.tabular.county-2017`

10 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
PrcNtvRsrv|NUMERIC|Percentage of county land area that belongs to Native American reservation(s)
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate

### tract-ruca-2010

ID: `oeps-391119.tabular.tract-ruca-2010`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
Rurality|STRING|Urban/Suburban/Rural
Ruca2|STRING|Secondary RUCA Code
Ruca1|STRING|Primary RUCA Code
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.

### zcta-ruca-2010

ID: `oeps-391119.tabular.zcta-ruca-2010`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
Rurality|STRING|Urban/Suburban/Rural
Ruca2|STRING|Secondary RUCA Code
Ruca1|STRING|Primary RUCA Code
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### state-2020

ID: `oeps-391119.tabular.state-2020`

66 columns in this table.

Name|Data Type|Description
-|-|-|-
CntNaltT|INTEGER|Number of tracts within 30 -min of naltrexone driving range
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
OpRxRt|NUMERIC|Opioid prescription rate
CntMetT|INTEGER|Number of tracts with methadone provider within a 30-min driving range
NhPiHcvD|NUMERIC|
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020
HlthExp|INTEGER|Total expenditures on public health and hospitals
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
CrrctExp|INTEGER|Total expenditures on corrections system and operations
WlfrExp|INTEGER|Total expenditures on public welfare programs
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
WhtHcvD|NUMERIC|
MulHcvD|NUMERIC|
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AsHcvD|NUMERIC|
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
PctBupT|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.
AvNaltTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest naltrexone provider.
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
CntBupT|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range
PctMetT|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
PrMsuseP|NUMERIC|Percent of persons who self-report misusing prescription pain relief medication in 2020.
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
FlHcvD|INTEGER|Hepatitis C deaths among women
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
OdMortRt|NUMERIC|Overdose mortality rate
AvBupTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest buprenorphine provider.
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
AvMetTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest methadone provider.
HcvD|INTEGER|Total Hepatitis C deaths
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
PctNaltT|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### state-2019

ID: `oeps-391119.tabular.state-2019`

54 columns in this table.

Name|Data Type|Description
-|-|-|-
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
NoLwRmUnc|BOOLEAN|Dummy variable indicating whether the state has no law removing barriers or uncertainty as to SSP legality (0=no, 1=yes)
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NhPiHcvD|NUMERIC|
NoPrphLw|BOOLEAN|Dummy variable indicating whether the state has no state drug paraphernalia law (0=no, 1=yes)
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
ExpSsp|BOOLEAN|Dummy variable indicating whether the state has law that explicitly authorizes Syringe Service Programs (0=no, 1=yes)
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
MedPolP5Yr|NUMERIC|Proportion of the five-year period (ending in given year) for which Medicaid Expansion was implemented / in effect
HlthExp|INTEGER|Total expenditures on public health and hospitals
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
CrrctExp|INTEGER|Total expenditures on corrections system and operations
WlfrExp|INTEGER|Total expenditures on public welfare programs
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
WhtHcvD|NUMERIC|
MulHcvD|NUMERIC|
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
PrNtRefInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law does not refer to objects used for injecting drugs (0=no, 1=yes)
AsHcvD|NUMERIC|
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
PrExcInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law explicitly exludes objects used for injecting drugs (0=no, 1=yes)
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
FlHcvD|INTEGER|Hepatitis C deaths among women
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
OdMortRt|NUMERIC|Overdose mortality rate
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
HcvD|INTEGER|Total Hepatitis C deaths
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
NoIntP|NUMERIC|Percentage of Households without Internet access
NtPrFrDsSy|BOOLEAN|Dummy variable indicating whether the state law does not prohibit free distribution of syringes (0=no, 1=yes)
MedcdExp|INTEGER|Total medicaid spending
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### state-2021

ID: `oeps-391119.tabular.state-2021`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NhPiHcvD|NUMERIC|
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
HlthExp|INTEGER|Total expenditures on public health and hospitals
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
CrrctExp|INTEGER|Total expenditures on corrections system and operations
WlfrExp|INTEGER|Total expenditures on public welfare programs
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
WhtHcvD|NUMERIC|
MulHcvD|NUMERIC|
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AsHcvD|NUMERIC|
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
FlHcvD|INTEGER|Hepatitis C deaths among women
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
MlHcvD|INTEGER|Hepatitis C deaths among men
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
OdMortRt|NUMERIC|Overdose mortality rate
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
HcvD|INTEGER|Total Hepatitis C deaths
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
BlkHcvD|INTEGER|Hepatitis C deaths among Black population

### tract-2019

ID: `oeps-391119.tabular.tract-2019`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
NoIntP|NUMERIC|Percentage of Households without Internet access
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes

### state-providers-2010

ID: `oeps-391119.tabular.state-providers-2010`

4 columns in this table.

Name|Data Type|Description
-|-|-|-
TotPcp|INTEGER|Number of primary care providers in area
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotSp|INTEGER|Number of specialty physicians in area

### tract-2018

ID: `oeps-391119.tabular.tract-2018`

79 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
RentalP|NUMERIC|Percentage of occupied housing units that are rented
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
TotVetPop|INTEGER|Total Veteran population
FemP|NUMERIC|
SRatio|NUMERIC|
EngProf|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AreaSqMi|NUMERIC|Land area of geography in sq miles
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr16|NUMERIC|
LibPerCap|NUMERIC|Libraries per capita by census tract
Ovr65P|NUMERIC|Percentage of population over 65
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
Age15_44|INTEGER|Total population between age 15-44
MedHsgTen|STRING|Median time period occupant moved into housing unit by tract
SomeCollegeP|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
AlcDens|NUMERIC|Number of alcohol outlets per square mile
SocCapInd|NUMERIC|Composite index of LngTermP, LibPerCap, RlgPerCap
RlgPerCap|NUMERIC|Religious institutions per capita by census tract
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr18P|NUMERIC|
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
TotPopHh|INTEGER|Total number of people in households
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotPop|INTEGER|Total population
SviSmryRnk|NUMERIC|Overall summary ranking
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
AlcTot|INTEGER|Total number of alcohol outlets
TotWrkE|INTEGER|Estimated count of working population
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### zcta-2020

ID: `oeps-391119.tabular.zcta-2020`

109 columns in this table.

Name|Data Type|Description
-|-|-|-
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
GradSclP|NUMERIC|
SutTmDr|NUMERIC|Driving time (min) to nearest  Substance Use Treatment (SUT) facility
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
TwoRaceP|NUMERIC|
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
HsdTot|NUMERIC|
SepartedP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
MhCntDr|INTEGER|Count of mental health providers within a 30-minute driving threshold
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
RentalP|NUMERIC|Percentage of occupied housing units that are rented
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
CrowdHsng|NUMERIC|
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
TotVetPop|INTEGER|Total Veteran population
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
FemP|NUMERIC|
SRatio|NUMERIC|
EngProf|NUMERIC|
HhldFC|NUMERIC|
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
HhldFA|NUMERIC|
RetailP|NUMERIC|Percentage of population employed in retail trade industry
SRatio18|NUMERIC|
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
VetP|NUMERIC|Percent of population that are veterans
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
Ovr65P|NUMERIC|Percentage of population over 65
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
SomeCollegeP|NUMERIC|
MedAge|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HsdTypM|NUMERIC|
HhldFS|NUMERIC|
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
HhldMA|NUMERIC|
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OccupantP|NUMERIC|
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
EduNoHsP|NUMERIC|
FamSize|NUMERIC|
HisP|NUMERIC|
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
UnitDens|NUMERIC|Number of housing units per square mile of land area
Ovr18P|NUMERIC|
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
TotPopHh|INTEGER|Total number of people in households
HHSize|NUMERIC|
NvMrrdP|NUMERIC|
HhldMC|NUMERIC|
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
HsdTypCo|NUMERIC|
Ovr21P|NUMERIC|
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
DivrcdP|NUMERIC|
TotPop|INTEGER|Total population
Und18P|NUMERIC|
Ovr62P|NUMERIC|
VacantP|NUMERIC|Percentage of vacant housing units
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
HhldMS|NUMERIC|
WidwdP|NUMERIC|
TotWrkE|INTEGER|Estimated count of working population
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
EduHsP|NUMERIC|
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
HsdTypMC|NUMERIC|

### county-2022

ID: `oeps-391119.tabular.county-2022`

8 columns in this table.

Name|Data Type|Description
-|-|-|-
OpRxRt|NUMERIC|Opioid prescription rate
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
SviSmryRnk|NUMERIC|Overall summary ranking

### tract-2014

ID: `oeps-391119.tabular.tract-2014`

2 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.

### county-2010

ID: `oeps-391119.tabular.county-2010`

46 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
TwoRaceP|NUMERIC|
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
ChildrenP|NUMERIC|Percentage of population under age 18
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
TotVetPop|INTEGER|Total Veteran population
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
VetP|NUMERIC|Percent of population that are veterans
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
EduNoHsP|NUMERIC|
Ovr18P|NUMERIC|
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### tract-1980

ID: `oeps-391119.tabular.tract-1980`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
Ovr16|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
Ovr18P|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

### county-2014

ID: `oeps-391119.tabular.county-2014`

3 columns in this table.

Name|Data Type|Description
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.

### state-2024

ID: `oeps-391119.tabular.state-2024`

9 columns in this table.

Name|Data Type|Description
-|-|-|-
MedPolP5Yr|NUMERIC|Proportion of the five-year period (ending in given year) for which Medicaid Expansion was implemented / in effect
EdBupPolP|NUMERIC|Proportion of Entire Data Period with State-Level Buprenorphine Policy in Effect
PerImpBupP|STRING|Periods of Implementation of State-Level Buprenorphine Policy (Associated Date Ranges)
TtlPrPpr|NUMERIC|Total Prison Population Rate
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
BupPolP|NUMERIC|Proportion of Year with State-Level Buprenorphine Policy in Effect
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlPrPp|INTEGER|Total Prison Population Count

### tract-2000

ID: `oeps-391119.tabular.tract-2000`

46 columns in this table.

Name|Data Type|Description
-|-|-|-
GradSclP|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
BachelorsP|NUMERIC|
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
Age15_44P|NUMERIC|Percentage of population below 45 years of age
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
WhiteP|NUMERIC|Percentage of population with race identified as white alone
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
Ovr16P|NUMERIC|
SRatio65|NUMERIC|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|
SRatio|NUMERIC|
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SRatio18|NUMERIC|
Ovr21|NUMERIC|
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
Ovr16|NUMERIC|
Ovr65P|NUMERIC|Percentage of population over 65
Age15_44|INTEGER|Total population between age 15-44
SomeCollegeP|NUMERIC|
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ovr18|NUMERIC|
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
EduNoHsP|NUMERIC|
HisP|NUMERIC|
Ovr18P|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MaleP|NUMERIC|
Ovr21P|NUMERIC|
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TotPop|INTEGER|Total population
VacantP|NUMERIC|Percentage of vacant housing units
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
EduHsP|NUMERIC|
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.

