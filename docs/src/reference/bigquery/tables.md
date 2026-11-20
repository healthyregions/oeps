# Project Id: oeps-391119

1 dataset in this project: tabular

## tabular

60 tables in this dataset.

### zcta-2021

ID: `oeps-391119.tabular.zcta-2021`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.

### tract-2025

ID: `oeps-391119.tabular.tract-2025`

95 columns in this table.

Name|Data Type|Description
-|-|-|-
NaltRm30|NUMERIC|Naltrexone access 30 minutes (RAAM)
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
BupCntDr60|NUMERIC|Count of buprenorphine providers in 60 minute drive time threshold
HcvTmDr|NUMERIC|Driving time from origin to nearest HCV testing provider (minutes)
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
OtpRm60|NUMERIC|Opioid Treatment Provider access 60 minutes (RAAM)
FqhcTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes, with Impedance factor
OtpTmDr2|NUMERIC|Driving time in minutes from the tract centroid to the nearest opioid treatment program, using impedance-adjusted travel time.
NaltRm60|NUMERIC|Naltrexone access 60 minutes (RAAM)
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
SspTmDr2|NUMERIC|Driving time in minutes from origin census tract centroid to census tract centroid of nearest SSP and back to origin census tract centroid
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
HcvTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip HCV Testing Facility with impedance destination centroid, in minutes
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
MhTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid with impedance, in minutes
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
MoudTyp|INTEGER|Count (0-3) of distinct MOUD provider types (buprenorphine, methadone, naltrexone) within a 30-minute impedance-adjusted driving time.
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
MetCntDr60|NUMERIC|Count of methadone providers in 60 minute drive time threshold
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
BupTmDr2|NUMERIC|Driving time (minutes) from the tract centroid to the nearest buprenorphine provider, with the impedance factor applied.
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
HospTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes with Impedance factor
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
MhCntDr|INTEGER|Count of mental health providers within a 30-minute driving threshold
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
HivTmDr|NUMERIC|Driving time from origin to nearest HIV testing provider (minutes)
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
TlBupCntDr30|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 30-minute driving time threshold
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
RxTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid with impedance factor, in minutes
NaltTmDr2|NUMERIC|Driving time in minutes from the tract centroid to the nearest naltrexone provider, with the impedance factor applied.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
SspTmDr|NUMERIC|Driving time in minutes from origin census tract centroid to census tract centroid of nearest SSP
HcvMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest HCV testing provider (miles)
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
OtpFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to opioid treatment programs within a 30-minute drive
BupFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Buprenorphine within a 30-minute drive
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
SutTmDr|NUMERIC|Driving time (min) to nearest  Substance Use Treatment (SUT) facility
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
OtpFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to opioid treatment programs within a 60-minute drive
TlBupCntWk30|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 30-minute walking time threshold
TlBupMinDis|NUMERIC|Euclidean distance (in miles) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
BupRm60|NUMERIC|Buprenorphine access 60 minutes (RAAM)
TlBupCntBk30|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 30-minute biking time threshold
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
TlBupTmDr|NUMERIC|Estimated driving time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
NaltCntDr60|NUMERIC|Count of naltrexone providers in 60 minute drive time threshold
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
NaltFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Naltrexone within a 30-minute drive
TlBupCntDr60|INTEGER|Total number of providers offering buprenorphine treatment via telemedicine/telehealth located within a 60-minute driving time threshold
NaltFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Naltrexone within a 60-minute drive
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
HivTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip HIV Testing Facility with impedance destination centroid, in minutes
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
MetFca60|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Methadone within a 60-minute drive
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
BupRm30|NUMERIC|Buprenorphine access 30 minutes (RAAM)
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
HivCntDr|INTEGER|Number of HIV testing providers within a 30-minute drive
BupFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Buprenorphine within a 30-minute drive
SutTmDr2|NUMERIC|Driving time (minutes) from the tract/zip centroid to the nearest Substance Use Treatment provider, with the impedance factor applied.
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
OtpRm30|NUMERIC|Opioid Treatment Provider access 30 minutes (RAAM)
HivMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest HIV testing provider (miles)
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
MetTmDr2|NUMERIC|Driving time in minutes from the tract centroid to the nearest methadone provider, with the impedance factor applied.
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
HcvCntDr|INTEGER|Number of HCV testing providers within a 30-minute drive
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
MetFca30|NUMERIC|Two-step floating catchment area (2SFCA) measure of access to Methadone within a 30-minute drive

### tract-2023

ID: `oeps-391119.tabular.tract-2023`

85 columns in this table.

Name|Data Type|Description
-|-|-|-
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFA|NUMERIC|Percent female householder with no spouse/partner living alone
NvMrrdP|NUMERIC|Percent males aged 15 or older who never got married
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|Percent males aged 15 or older who are married and living with their spouse
LibPerCap|NUMERIC|Libraries per capita by census tract
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
HsdTypMC|NUMERIC|Percent married-couple household With children under 18 years
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
SepartedP|NUMERIC|Percent males aged 15 years and over who are separated from their spouse
CrowdHsng|NUMERIC|Proportion of occupied housing units that are considered crowded (more than 1 person per room)
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
VetP|NUMERIC|Percent of population that are veterans
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
TotVetPop|INTEGER|Total Veteran population
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
TotPopHh|INTEGER|Total number of people in households
HhldMA|NUMERIC|Percent male householder with no spouse/partner living alone
HhldMC|NUMERIC|Percent married-couple household With children under 18 years
Und18P|NUMERIC|Percent of population under age 18
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
HhldMS|NUMERIC|Percent male householder 65 years and over living alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
HhldFC|NUMERIC|Percent female householder with no spouse/partner living with children under 18 years
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
SocCapInd|NUMERIC|Composite index of LngTermP, LibPerCap, RlgPerCap
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
HhldFS|NUMERIC|Percent female householder 65 years and over living alone
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
WidwdP|NUMERIC|Percent male population aged 15 and over who are widowed
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OccupantP|NUMERIC|Percent occupied housing units
HHSize|NUMERIC|Average number of persons per household
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HsdTot|NUMERIC|Total households
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
FamSize|NUMERIC|Average number of persons per family
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
HsdTypCo|NUMERIC|Percent cohabiting couple household
MedAge|NUMERIC|
MaleP|NUMERIC|Percent of population that is male
HsdTypM|NUMERIC|Percent married-couple household
MedHsgTen|STRING|Median time period occupant moved into housing unit by tract
Ovr16P|NUMERIC|Percent of population over age 16
TotWrkE|INTEGER|Estimated count of working population
Ovr62P|NUMERIC|Percent of population over age 62
RentalP|NUMERIC|Percentage of occupied housing units that are rented
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
DivrcdP|NUMERIC|Percent males 15 years and over who are divorced
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
RlgPerCap|NUMERIC|Religious institutions per capita by census tract
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### zcta-2022

ID: `oeps-391119.tabular.zcta-2022`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
SviSmryRnk|NUMERIC|Overall summary ranking
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation

### tract-ruca-2010

ID: `oeps-391119.tabular.tract-ruca-2010`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
Ruca1|STRING|Primary RUCA Code
Rurality|STRING|Urban/Suburban/Rural
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ruca2|STRING|Secondary RUCA Code

### tract-2000

ID: `oeps-391119.tabular.tract-2000`

46 columns in this table.

Name|Data Type|Description
-|-|-|-
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### state-2023

ID: `oeps-391119.tabular.state-2023`

71 columns in this table.

Name|Data Type|Description
-|-|-|-
BupPolP|NUMERIC|Proportion of Year with State-Level Buprenorphine Policy in Effect
MedcdExp|INTEGER|Total medicaid spending
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
PerImpBupP|STRING|Periods of Implementation of State-Level Buprenorphine Policy (Associated Date Ranges)
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
FemP|NUMERIC|Percent of population that is female
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
ExpnFedExp|INTEGER|Expansion Group - Federal Spending
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TradSttExp|INTEGER|Traditional medicaid - state spending
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
Ovr21|NUMERIC|
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
SRatio|NUMERIC|
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
MaleP|NUMERIC|Percent of population that is male
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
Ovr16P|NUMERIC|Percent of population over age 16
ExpnSttExp|INTEGER|Expansion Group - State Spending
TradFedExp|INTEGER|Traditional medicaid - federal spending
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
EdBupPolP|NUMERIC|Proportion of Entire Data Period with State-Level Buprenorphine Policy in Effect
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents

### zcta-2023

ID: `oeps-391119.tabular.zcta-2023`

89 columns in this table.

Name|Data Type|Description
-|-|-|-
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFA|NUMERIC|Percent female householder with no spouse/partner living alone
NvMrrdP|NUMERIC|Percent males aged 15 or older who never got married
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|Percent males aged 15 or older who are married and living with their spouse
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
HsdTypMC|NUMERIC|Percent married-couple household With children under 18 years
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
SepartedP|NUMERIC|Percent males aged 15 years and over who are separated from their spouse
CrowdHsng|NUMERIC|Proportion of occupied housing units that are considered crowded (more than 1 person per room)
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
VetP|NUMERIC|Percent of population that are veterans
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
TotVetPop|INTEGER|Total Veteran population
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
TotPopHh|INTEGER|Total number of people in households
HhldMA|NUMERIC|Percent male householder with no spouse/partner living alone
HhldMC|NUMERIC|Percent married-couple household With children under 18 years
Und18P|NUMERIC|Percent of population under age 18
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
HhldMS|NUMERIC|Percent male householder 65 years and over living alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
HhldFC|NUMERIC|Percent female householder with no spouse/partner living with children under 18 years
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
FemP|NUMERIC|Percent of population that is female
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
HhldFS|NUMERIC|Percent female householder 65 years and over living alone
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
WidwdP|NUMERIC|Percent male population aged 15 and over who are widowed
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
OccupantP|NUMERIC|Percent occupied housing units
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
HHSize|NUMERIC|Average number of persons per household
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HsdTot|NUMERIC|Total households
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
FamSize|NUMERIC|Average number of persons per family
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
HsdTypCo|NUMERIC|Percent cohabiting couple household
MedAge|NUMERIC|
MaleP|NUMERIC|Percent of population that is male
HsdTypM|NUMERIC|Percent married-couple household
Ovr16P|NUMERIC|Percent of population over age 16
TotWrkE|INTEGER|Estimated count of working population
Ovr62P|NUMERIC|Percent of population over age 62
RentalP|NUMERIC|Percentage of occupied housing units that are rented
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
DivrcdP|NUMERIC|Percent males 15 years and over who are divorced
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents

### state-2015

ID: `oeps-391119.tabular.state-2015`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
FlHcvD|INTEGER|Hepatitis C deaths among women
HcvD|INTEGER|Total Hepatitis C deaths
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
MlHcvD|INTEGER|Hepatitis C deaths among men
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age

### state-2020

ID: `oeps-391119.tabular.state-2020`

66 columns in this table.

Name|Data Type|Description
-|-|-|-
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
AvMetTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest methadone provider.
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
PctBupT|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MulHcvD|NUMERIC|
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider
CrrctExp|INTEGER|Total expenditures on corrections system and operations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
AvBupTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest buprenorphine provider.
OpRxRt|NUMERIC|Opioid prescription rate
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
CntBupT|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
NhPiHcvD|NUMERIC|
PctMetT|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020
FlHcvD|INTEGER|Hepatitis C deaths among women
HcvD|INTEGER|Total Hepatitis C deaths
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
PrMsuseP|NUMERIC|Percent of persons who self-report misusing prescription pain relief medication in 2020.
PctNaltT|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
CntNaltT|INTEGER|Number of tracts within 30 -min of naltrexone driving range
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
OdMortRt|NUMERIC|Overdose mortality rate
HlthExp|INTEGER|Total expenditures on public health and hospitals
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
AsHcvD|NUMERIC|
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-min driving range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
AvNaltTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest naltrexone provider.
WhtHcvD|NUMERIC|
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
CntMetT|INTEGER|Number of tracts with methadone provider within a 30-min driving range
MlHcvD|INTEGER|Hepatitis C deaths among men
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
WlfrExp|INTEGER|Total expenditures on public welfare programs

### state-2021

ID: `oeps-391119.tabular.state-2021`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MulHcvD|NUMERIC|
CrrctExp|INTEGER|Total expenditures on corrections system and operations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
NhPiHcvD|NUMERIC|
FlHcvD|INTEGER|Hepatitis C deaths among women
HcvD|INTEGER|Total Hepatitis C deaths
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
OdMortRt|NUMERIC|Overdose mortality rate
HlthExp|INTEGER|Total expenditures on public health and hospitals
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
AsHcvD|NUMERIC|
WhtHcvD|NUMERIC|
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
MlHcvD|INTEGER|Hepatitis C deaths among men
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
WlfrExp|INTEGER|Total expenditures on public welfare programs

### state-2010

ID: `oeps-391119.tabular.state-2010`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
VetP|NUMERIC|Percent of population that are veterans
TotVetPop|INTEGER|Total Veteran population
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### state-1990

ID: `oeps-391119.tabular.state-1990`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### county-2020

ID: `oeps-391119.tabular.county-2020`

116 columns in this table.

Name|Data Type|Description
-|-|-|-
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFA|NUMERIC|Percent female householder with no spouse/partner living alone
MetCtTmBk|INTEGER|Number of tracts with methadone provider within a 30-min biking range
NvMrrdP|NUMERIC|Percent males aged 15 or older who never got married
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|Percent males aged 15 or older who are married and living with their spouse
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
HsdTypMC|NUMERIC|Percent married-couple household With children under 18 years
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
SepartedP|NUMERIC|Percent males aged 15 years and over who are separated from their spouse
CrowdHsng|NUMERIC|Proportion of occupied housing units that are considered crowded (more than 1 person per room)
MetAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest methadone provider
BupAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest buprenorphine provider
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
BupTmWkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min walking range
VetP|NUMERIC|Percent of population that are veterans
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider
NaltAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest naltrexone provider
TotVetPop|INTEGER|Total Veteran population
BupAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest buprenorphine provider
OpRxRt|NUMERIC|Opioid prescription rate
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
MetTmDrP|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range
NaltTmDrP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
TotPopHh|INTEGER|Total number of people in households
HhldMA|NUMERIC|Percent male householder with no spouse/partner living alone
HhldMC|NUMERIC|Percent married-couple household With children under 18 years
Und18P|NUMERIC|Percent of population under age 18
BupAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest buprenorphine provider
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
MetAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest methadone provider
SviSmryRnk|NUMERIC|Overall summary ranking
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
HhldMS|NUMERIC|Percent male householder 65 years and over living alone
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
BupCtTmDr|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range
SRatio65|NUMERIC|
NaltCtTmDr|INTEGER|Number of tracts with naltrexone provider within a 30-min driving range
NaltAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest naltrexone provider
HhldFC|NUMERIC|Percent female householder with no spouse/partner living with children under 18 years
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
NaltCtTmWk|INTEGER|Number of tracts with naltrexone provider within a 30-min walking range
VacantP|NUMERIC|Percentage of vacant housing units
MetCtTmWk|INTEGER|Number of tracts with methadone provider within a 30-min walking range
BupCtTmWk|INTEGER|Number of tracts with buprenorphine provider within a 30-min walking range
FemP|NUMERIC|Percent of population that is female
MetTmWkP|NUMERIC|Percent of tracts with methadone provider within a 30-min walking range
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
HhldFS|NUMERIC|Percent female householder 65 years and over living alone
Ovr21P|NUMERIC|Percent of population over age 21
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
WidwdP|NUMERIC|Percent male population aged 15 and over who are widowed
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
MetTmBkP|NUMERIC|Percent of tracts with methadone provider within a 30-min biking range
MetAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest methadone provider
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OccupantP|NUMERIC|Percent occupied housing units
HHSize|NUMERIC|Average number of persons per household
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
NaltAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest naltrexone provider
HsdTot|NUMERIC|Total households
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
FamSize|NUMERIC|Average number of persons per family
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
OdMortRt|NUMERIC|Overdose mortality rate
HsdTypCo|NUMERIC|Percent cohabiting couple household
MedAge|NUMERIC|
MaleP|NUMERIC|Percent of population that is male
HsdTypM|NUMERIC|Percent married-couple household
Ovr16P|NUMERIC|Percent of population over age 16
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-min driving range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
TotWrkE|INTEGER|Estimated count of working population
Ovr62P|NUMERIC|Percent of population over age 62
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
BupTmDrP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range
NaltTmWkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min walking range
RentalP|NUMERIC|Percentage of occupied housing units that are rented
MetCtTmDr|INTEGER|Number of tracts with methadone provider within a 30-min driving range
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
DivrcdP|NUMERIC|Percent males 15 years and over who are divorced
BupCtTmBk|INTEGER|Number of tracts with buprenorphine provider within a 30-min biking range
BupTmBkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min biking range
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
NaltTmBkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min biking range
NaltCtTmBk|INTEGER|Number of tracts with naltrexone provider within a 30-min biking range
TotPop|INTEGER|Total population
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### state-2018

ID: `oeps-391119.tabular.state-2018`

120 columns in this table.

Name|Data Type|Description
-|-|-|-
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
MedcdExp|INTEGER|Total medicaid spending
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
MulHcvD|NUMERIC|
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
AlcDens|NUMERIC|Number of alcohol outlets per square mile
VetP|NUMERIC|Percent of population that are veterans
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
TotVetPop|INTEGER|Total Veteran population
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
TotPopHh|INTEGER|Total number of people in households
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
AlcTot|INTEGER|Total number of alcohol outlets
TotTracts|INTEGER|Total number of census tracts within the state.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
NhPiHcvD|NUMERIC|
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
ExpnFedExp|INTEGER|Expansion Group - Federal Spending
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
AreaSqMi|NUMERIC|Land area of geography in sq miles
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
FlHcvD|INTEGER|Hepatitis C deaths among women
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
HcvD|INTEGER|Total Hepatitis C deaths
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
TradSttExp|INTEGER|Traditional medicaid - state spending
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
Ovr21|NUMERIC|
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
StateArea|NUMERIC|Area (in square meters) of state
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
OdMortRt|NUMERIC|Overdose mortality rate
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
AsHcvD|NUMERIC|
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
TotWrkE|INTEGER|Estimated count of working population
ExpnSttExp|INTEGER|Expansion Group - State Spending
RentalP|NUMERIC|Percentage of occupied housing units that are rented
TradFedExp|INTEGER|Traditional medicaid - federal spending
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
WhtHcvD|NUMERIC|
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
MlHcvD|INTEGER|Hepatitis C deaths among men
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### county-2000

ID: `oeps-391119.tabular.county-2000`

44 columns in this table.

Name|Data Type|Description
-|-|-|-
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
DmyBlckBlt|BOOLEAN|Dummy variable for whether county is in the Southern Black Belt region
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### county-2017

ID: `oeps-391119.tabular.county-2017`

10 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PrcNtvRsrv|NUMERIC|Percentage of county land area that belongs to Native American reservation(s)
OdMortRt|NUMERIC|Overdose mortality rate
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data

### state-2016

ID: `oeps-391119.tabular.state-2016`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
FlHcvD|INTEGER|Hepatitis C deaths among women
HcvD|INTEGER|Total Hepatitis C deaths
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
MlHcvD|INTEGER|Hepatitis C deaths among men
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age

### state-1980

ID: `oeps-391119.tabular.state-1980`

40 columns in this table.

Name|Data Type|Description
-|-|-|-
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### county-2019

ID: `oeps-391119.tabular.county-2019`

11 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlPrPpr|NUMERIC|Total Prison Population Rate
TtlPrAPp|INTEGER|Prison Prison Admissions Count
TtlPrPp|INTEGER|Total Prison Population Count
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
NoIntP|NUMERIC|Percentage of Households without Internet access

### tract-2020

ID: `oeps-391119.tabular.tract-2020`

123 columns in this table.

Name|Data Type|Description
-|-|-|-
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFA|NUMERIC|Percent female householder with no spouse/partner living alone
BupRm90|NUMERIC|Buprenorphine access 90 minutes (RAAM)
NaltRm30|NUMERIC|Naltrexone access 30 minutes (RAAM)
NvMrrdP|NUMERIC|Percent males aged 15 or older who never got married
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|Percent males aged 15 or older who are married and living with their spouse
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
HsdTypMC|NUMERIC|Percent married-couple household With children under 18 years
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
SepartedP|NUMERIC|Percent males aged 15 years and over who are separated from their spouse
CrowdHsng|NUMERIC|Proportion of occupied housing units that are considered crowded (more than 1 person per room)
NaltRm90|NUMERIC|Naltrexone access 90 minutes (RAAM)
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
VetP|NUMERIC|Percent of population that are veterans
NaltRm60|NUMERIC|Naltrexone access 60 minutes (RAAM)
TotVetPop|INTEGER|Total Veteran population
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
TotPopHh|INTEGER|Total number of people in households
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
HhldMA|NUMERIC|Percent male householder with no spouse/partner living alone
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
HhldMC|NUMERIC|Percent married-couple household With children under 18 years
Und18P|NUMERIC|Percent of population under age 18
SviSmryRnk|NUMERIC|Overall summary ranking
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
HhldMS|NUMERIC|Percent male householder 65 years and over living alone
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
SRatio65|NUMERIC|
HhldFC|NUMERIC|Percent female householder with no spouse/partner living with children under 18 years
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
VacantP|NUMERIC|Percentage of vacant housing units
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
HhldFS|NUMERIC|Percent female householder 65 years and over living alone
Ovr21P|NUMERIC|Percent of population over age 21
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
MhCntDr|INTEGER|Count of mental health providers within a 30-minute driving threshold
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
WidwdP|NUMERIC|Percent male population aged 15 and over who are widowed
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OccupantP|NUMERIC|Percent occupied housing units
HHSize|NUMERIC|Average number of persons per household
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HsdTot|NUMERIC|Total households
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
SutTmDr|NUMERIC|Driving time (min) to nearest  Substance Use Treatment (SUT) facility
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
FamSize|NUMERIC|Average number of persons per family
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
BupRm60|NUMERIC|Buprenorphine access 60 minutes (RAAM)
HsdTypCo|NUMERIC|Percent cohabiting couple household
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
MedAge|NUMERIC|
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
MaleP|NUMERIC|Percent of population that is male
HsdTypM|NUMERIC|Percent married-couple household
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
Ovr16P|NUMERIC|Percent of population over age 16
TotWrkE|INTEGER|Estimated count of working population
Ovr62P|NUMERIC|Percent of population over age 62
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
RentalP|NUMERIC|Percentage of occupied housing units that are rented
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
DivrcdP|NUMERIC|Percent males 15 years and over who are divorced
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
BupRm30|NUMERIC|Buprenorphine access 30 minutes (RAAM)
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
TotPop|INTEGER|Total population
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### county-2016

ID: `oeps-391119.tabular.county-2016`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlPrPpr|NUMERIC|Total Prison Population Rate
TtlPrAPp|INTEGER|Prison Prison Admissions Count
TtlPrPp|INTEGER|Total Prison Population Count
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate

### zcta-ruca-2010

ID: `oeps-391119.tabular.zcta-ruca-2010`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
Ruca1|STRING|Primary RUCA Code
Rurality|STRING|Urban/Suburban/Rural
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ruca2|STRING|Secondary RUCA Code
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.

### county-2025

ID: `oeps-391119.tabular.county-2025`

79 columns in this table.

Name|Data Type|Description
-|-|-|-
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
HospCtTmDr2|NUMERIC|Number of tracts with hospitals within a 30-min driving range, with impedance
BupTmDrP2|NUMERIC|Percent of tracts with Buprenorphine Provider within a 30-min driving range, with Impedance factor
HcvCtTmDr|INTEGER|Number of tracts with an HCV testing provider within a 30-minute driving range
HivCtTmDr2|NUMERIC|Number of tracts with HIV Testing Facility within a 30-min driving range, with impedance
HospTmDrP2|NUMERIC|Percent of tracts with hospital within a 30-min driving range with impedance factor
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
RxTmDrP2|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range with impedance factor
MhCtTmDr2|NUMERIC|Number of tracts with mental health provider within a 30-min driving range, with impedance
MetAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest methadone provider
BupAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest buprenorphine provider
OtpCtTmDr2|NUMERIC|Number of tracts with Opioid Treatment Provider within a 30-min driving range, with Impedance factor
HivAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HIV Testing Facility, with impedance
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider
MetTmDrP|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range
NaltTmDrP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
SmokeP|NUMERIC|Percentage of Smoking Population
HcvCtTmDr2|NUMERIC|Number of tracts with HCV Testing Facility within a 30-min driving range, with impedance
NaltTmDrP2|NUMERIC|Percent of tracts with Naltrexone Provider within a 30-min driving range, with Impedance factor
HivTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HIV testing provider
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.
BupCtTmDr|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range
NaltCtTmDr|INTEGER|Number of tracts with naltrexone provider within a 30-min driving range
OtpAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Opioid Treatment Provider (Otp), with Impedance factor
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
MetCtTmDr2|NUMERIC|Number of tracts with Methadone Providerwithin a 30-min driving range, with Impedance factor
SutCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
TotTracts|INTEGER|Total number of census tracts within the state.
HcvTmDrP2|NUMERIC|Percent of tracts with HCV Testing Facility within a 30-mini driving range, with impedance
BupAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Buprenorphine Provider (BUP), with Impedance factor
HivAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HIV testing provider
SutTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
HcvTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HCV testing provider
HospAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital with Impedance factor
OtpTmDrP2|NUMERIC|Percent of tracts with Opioid Treatment Provider within a 30-min driving range, with Impedance factor
HcvAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HCV Testing Facility, with impedance
SutCtTmDr2|NUMERIC|Number of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
HivTmDrP2|NUMERIC|Percent of tracts with HIV Testing Facility within a 30-mini driving range, with impedance
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
RxAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy with Impedance Factor
FqhcCtTmDr2|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SutAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
RxCtTmDr2|INTEGER|Number of tracts with pharmacy within a 30-min driving range with impedance factor
FqhcTmDrP2|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
SutTmDrP2|NUMERIC|Percent of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
NaltAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest naltrexone provider
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
BupCtTmDr2|NUMERIC|Number of tracts with Buprenorphine Provider within a 30-min driving range, with Impedance factor
HcvAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HCV testing provider
TlBupMinDis|NUMERIC|Euclidean distance (in miles) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
HivCtTmDr|INTEGER|Number of tracts with an HIV testing provider within a 30-minute driving range
FqhcAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center, with Impedance factor
MetAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Methadone Provider(MET), with Impedance factor
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-min driving range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
BupTmDrP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range
MetCtTmDr|INTEGER|Number of tracts with methadone provider within a 30-min driving range
MetTmDrP2|NUMERIC|Percent of tracts with Methadone Providerwithin a 30-min driving range, with Impedance factor
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
NaltAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Naltrexone Provider (NALT), with Impedance factor
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
NaltCtTmDr2|NUMERIC|Number of tracts with Naltrexone Provider within a 30-min driving range, with Impedance factor
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
MhAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider, with impedance
MhTmDrP2|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range, with impedance
SutAvTmDr2|NUMERIC| Average driving time (minutes) across tracts in state to nearestSubstance Use Treatment Provider (Sut), with Impedance factor

### county-1980

ID: `oeps-391119.tabular.county-1980`

40 columns in this table.

Name|Data Type|Description
-|-|-|-
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### tract-2010

ID: `oeps-391119.tabular.tract-2010`

48 columns in this table.

Name|Data Type|Description
-|-|-|-
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
VetP|NUMERIC|Percent of population that are veterans
TotVetPop|INTEGER|Total Veteran population
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
VacantP|NUMERIC|Percentage of vacant housing units
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
TotPop|INTEGER|Total population
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### county-providers-2010

ID: `oeps-391119.tabular.county-providers-2010`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
PcpPer100k|NUMERIC|PCPs per total Population X 100,000
TotPcp|INTEGER|Number of primary care providers in area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TotSp|INTEGER|Number of specialty physicians in area
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000

### tract-2014

ID: `oeps-391119.tabular.tract-2014`

2 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### zcta-2019

ID: `oeps-391119.tabular.zcta-2019`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
NoIntP|NUMERIC|Percentage of Households without Internet access

### state-2024

ID: `oeps-391119.tabular.state-2024`

9 columns in this table.

Name|Data Type|Description
-|-|-|-
BupPolP|NUMERIC|Proportion of Year with State-Level Buprenorphine Policy in Effect
TtlPrPpr|NUMERIC|Total Prison Population Rate
MedPolP5Yr|NUMERIC|Proportion of the five-year period (ending in given year) for which Medicaid Expansion was implemented / in effect
PerImpBupP|STRING|Periods of Implementation of State-Level Buprenorphine Policy (Associated Date Ranges)
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
TtlPrPp|INTEGER|Total Prison Population Count
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
EdBupPolP|NUMERIC|Proportion of Entire Data Period with State-Level Buprenorphine Policy in Effect

### county-2015

ID: `oeps-391119.tabular.county-2015`

4 columns in this table.

Name|Data Type|Description
-|-|-|-
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
DmySgrg|BOOLEAN|Dummy variable for whether county is part of a hypersegregated city or its metropolitan area
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

### county-2018

ID: `oeps-391119.tabular.county-2018`

91 columns in this table.

Name|Data Type|Description
-|-|-|-
RcaSubrbP|NUMERIC|Percent census tracts in the county classified as Suburban using RUCA codes
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
RcaRuralP|NUMERIC|Percent census tracts in the county classified as Rural using RUCA codes
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
AlcDens|NUMERIC|Number of alcohol outlets per square mile
VetP|NUMERIC|Percent of population that are veterans
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
CenFlags|STRING|Three different values indicating three things:
1 - Revised count, so urban and rural components will not add to total. 
2 - Geography name and FIPS code were changed since 2010. Shannon County, Sotuh Dakota name changed to Oglala Lakota County, new FIPS 46102. Wade Hampton Census Area, Alaska, name changed to Kusilvak CEnsus Area, nwe FIPS 02158
3 - Bedford City, Virginia, was consolidated with Bedford County, Virginia (FIPS 51019) since 2010.
TotVetPop|INTEGER|Total Veteran population
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TotPopHh|INTEGER|Total number of people in households
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SviSmryRnk|NUMERIC|Overall summary ranking
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
RspRt|NUMERIC|Percent of units interviewed from total units intended for interview
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
AlcTot|INTEGER|Total number of alcohol outlets
TotTracts|INTEGER|Total number of census tracts within the state.
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
AreaSqMi|NUMERIC|Land area of geography in sq miles
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
RcaUrbanP|NUMERIC|Percent census tracts in the county classified as Urban using RUCA codes
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
OdMortRt|NUMERIC|Overdose mortality rate
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
TotWrkE|INTEGER|Estimated count of working population
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
RentalP|NUMERIC|Percentage of occupied housing units that are rented
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### tract-1980

ID: `oeps-391119.tabular.tract-1980`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### county-2022

ID: `oeps-391119.tabular.county-2022`

8 columns in this table.

Name|Data Type|Description
-|-|-|-
OpRxRt|NUMERIC|Opioid prescription rate
SviSmryRnk|NUMERIC|Overall summary ranking
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation

### state-2025

ID: `oeps-391119.tabular.state-2025`

65 columns in this table.

Name|Data Type|Description
-|-|-|-
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range
HospCtTmDr2|NUMERIC|Number of tracts with hospitals within a 30-min driving range, with impedance
BupTmDrP2|NUMERIC|Percent of tracts with Buprenorphine Provider within a 30-min driving range, with Impedance factor
HcvCtTmDr|INTEGER|Number of tracts with an HCV testing provider within a 30-minute driving range
HivCtTmDr2|NUMERIC|Number of tracts with HIV Testing Facility within a 30-min driving range, with impedance
HospTmDrP2|NUMERIC|Percent of tracts with hospital within a 30-min driving range with impedance factor
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.
RxTmDrP2|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range with impedance factor
MhCtTmDr2|NUMERIC|Number of tracts with mental health provider within a 30-min driving range, with impedance
MetAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest methadone provider
BupAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest buprenorphine provider
OtpCtTmDr2|NUMERIC|Number of tracts with Opioid Treatment Provider within a 30-min driving range, with Impedance factor
HivAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HIV Testing Facility, with impedance
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.
SmokeP|NUMERIC|Percentage of Smoking Population
HcvCtTmDr2|NUMERIC|Number of tracts with HCV Testing Facility within a 30-min driving range, with impedance
NaltTmDrP2|NUMERIC|Percent of tracts with Naltrexone Provider within a 30-min driving range, with Impedance factor
HivTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HIV testing provider
OtpAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Opioid Treatment Provider (Otp), with Impedance factor
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
MetCtTmDr2|NUMERIC|Number of tracts with Methadone Providerwithin a 30-min driving range, with Impedance factor
SutCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
TotTracts|INTEGER|Total number of census tracts within the state.
HcvTmDrP2|NUMERIC|Percent of tracts with HCV Testing Facility within a 30-mini driving range, with impedance
BupAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Buprenorphine Provider (BUP), with Impedance factor
HivAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HIV testing provider
SutTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
HcvTmDrP|NUMERIC|Percent of tracts within 30-minute drive to an HCV testing provider
HospAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital with Impedance factor
OtpTmDrP2|NUMERIC|Percent of tracts with Opioid Treatment Provider within a 30-min driving range, with Impedance factor
HcvAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest HCV Testing Facility, with impedance
SutCtTmDr2|NUMERIC|Number of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
HivTmDrP2|NUMERIC|Percent of tracts with HIV Testing Facility within a 30-mini driving range, with impedance
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
RxAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy with Impedance Factor
FqhcCtTmDr2|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SutAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.
RxCtTmDr2|INTEGER|Number of tracts with pharmacy within a 30-min driving range with impedance factor
FqhcTmDrP2|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range, with Impedance factor
SutTmDrP2|NUMERIC|Percent of tracts with Substance Use Treatment Provider within a 30-min driving range, with Impedance factor
NaltAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest naltrexone provider
BupCtTmDr2|NUMERIC|Number of tracts with Buprenorphine Provider within a 30-min driving range, with Impedance factor
HcvAvTmDr|NUMERIC|Mean driving time (minutes) from tracts to nearest HCV testing provider
HivCtTmDr|INTEGER|Number of tracts with an HIV testing provider within a 30-minute driving range
FqhcAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center, with Impedance factor
MetAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Methadone Provider(MET), with Impedance factor
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-min driving range
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range
MetTmDrP2|NUMERIC|Percent of tracts with Methadone Providerwithin a 30-min driving range, with Impedance factor
NaltAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest Naltrexone Provider (NALT), with Impedance factor
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.
TlBupTmWk|NUMERIC|Estimated walking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
NaltCtTmDr2|NUMERIC|Number of tracts with Naltrexone Provider within a 30-min driving range, with Impedance factor
TlBupTmBk|NUMERIC|Estimated biking time (in minutes) to the nearest provider offering buprenorphine treatment via telemedicine/telehealth services
MhAvTmDr2|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider, with impedance
MhTmDrP2|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range, with impedance
SutAvTmDr2|NUMERIC| Average driving time (minutes) across tracts in state to nearestSubstance Use Treatment Provider (Sut), with Impedance factor

### county-2023

ID: `oeps-391119.tabular.county-2023`

115 columns in this table.

Name|Data Type|Description
-|-|-|-
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFA|NUMERIC|Percent female householder with no spouse/partner living alone
NvMrrdP|NUMERIC|Percent males aged 15 or older who never got married
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|Percent males aged 15 or older who are married and living with their spouse
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
TtlJlPrtQ4|NUMERIC|Pretrial Jail Population Count (Q4)
TtlJlPprQ2|NUMERIC|Total Jail Population Rate (Q2), ASJ/COJ Data
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
HsdTypMC|NUMERIC|Percent married-couple household With children under 18 years
TtlJlPprQ3|NUMERIC|Total Jail Population Rate (Q3), ASJ/COJ Data
TtlJlPpQ3|NUMERIC|Total Jail Population Count (Q3), ASJ/COJ Data
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
SepartedP|NUMERIC|Percent males aged 15 years and over who are separated from their spouse
CrowdHsng|NUMERIC|Proportion of occupied housing units that are considered crowded (more than 1 person per room)
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
VetP|NUMERIC|Percent of population that are veterans
TtlJlPrtQ3|NUMERIC|Pretrial Jail Population Count (Q3)
TtlJlAdmrQ1|NUMERIC|Total Jail Admissions Rate (Q1), ASJ/COJ Data
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
TtlJlAdmrQ2|NUMERIC|Total Jail Admissions Rate (Q2), ASJ/COJ Data
TotVetPop|INTEGER|Total Veteran population
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TtlJlPpQ2|NUMERIC|Total Jail Population Count (Q2), ASJ/COJ Data
TtlJlPrtrQ3|NUMERIC|Pretrial Jail Population Rate (Q3)
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
TotPopHh|INTEGER|Total number of people in households
HhldMA|NUMERIC|Percent male householder with no spouse/partner living alone
HhldMC|NUMERIC|Percent married-couple household With children under 18 years
TtlJlAdmQ4|NUMERIC|Total Jail Admissions Count (Q4), ASJ/COJ Data
Und18P|NUMERIC|Percent of population under age 18
TtlJlPpQ4|NUMERIC|Total Jail Population Count (Q4), ASJ/COJ Data
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
HhldMS|NUMERIC|Percent male householder 65 years and over living alone
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
HhldFC|NUMERIC|Percent female householder with no spouse/partner living with children under 18 years
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
RspRt|NUMERIC|Percent of units interviewed from total units intended for interview
TtlJlPrtQ2|NUMERIC|Pretrial Jail Population Count (Q2)
FemP|NUMERIC|Percent of population that is female
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
TtlJlAdmrQ3|NUMERIC|Total Jail Admissions Rate (Q3), ASJ/COJ Data
TtlJlAdmrQ4|NUMERIC|Total Jail Admissions Rate (Q4), ASJ/COJ Data
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
HhldFS|NUMERIC|Percent female householder 65 years and over living alone
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
WidwdP|NUMERIC|Percent male population aged 15 and over who are widowed
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
TtlJlPrtrQ1|NUMERIC|Pretrial Jail Population Rate (Q1)
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
TtlJlPprQ1|NUMERIC|Total Jail Population Rate (Q1), ASJ/COJ Data
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OccupantP|NUMERIC|Percent occupied housing units
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
HHSize|NUMERIC|Average number of persons per household
TtlJlPprQ4|NUMERIC|Total Jail Population Rate (Q4), ASJ/COJ Data
TtlJlPpQ1|NUMERIC|Total Jail Population Count (Q1), ASJ/COJ Data
Ovr21|NUMERIC|
TtlJlPrtrQ2|NUMERIC|Pretrial Jail Population Rate (Q2)
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
TtlJlPrtrQ4|NUMERIC|Pretrial Jail Population Rate (Q4)
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TtlJlPrtQ1|NUMERIC|Pretrial Jail Population Count (Q1)
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HsdTot|NUMERIC|Total households
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
FamSize|NUMERIC|Average number of persons per family
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
HsdTypCo|NUMERIC|Percent cohabiting couple household
TtlJlAdmQ2|NUMERIC|Total Jail Admissions Count (Q2), ASJ/COJ Data
MedAge|NUMERIC|
MaleP|NUMERIC|Percent of population that is male
HsdTypM|NUMERIC|Percent married-couple household
Ovr16P|NUMERIC|Percent of population over age 16
TotWrkE|INTEGER|Estimated count of working population
Ovr62P|NUMERIC|Percent of population over age 62
RentalP|NUMERIC|Percentage of occupied housing units that are rented
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
DivrcdP|NUMERIC|Percent males 15 years and over who are divorced
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
TtlJlAdmQ3|NUMERIC|Total Jail Admissions Count (Q3), ASJ/COJ Data
TtlJlAdmQ1|NUMERIC|Total Jail Admissions Count (Q1), ASJ/COJ Data
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents

### zcta-2025

ID: `oeps-391119.tabular.zcta-2025`

46 columns in this table.

Name|Data Type|Description
-|-|-|-
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
HcvTmDr|NUMERIC|Driving time from origin to nearest HCV testing provider (minutes)
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
FqhcTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes, with Impedance factor
OtpTmDr2|NUMERIC|Driving time in minutes from the tract centroid to the nearest opioid treatment program, using impedance-adjusted travel time.
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes
HcvTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip HCV Testing Facility with impedance destination centroid, in minutes
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
MhTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid with impedance, in minutes
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
BupTmDr2|NUMERIC|Driving time (minutes) from the tract centroid to the nearest buprenorphine provider, with the impedance factor applied.
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
HospTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes with Impedance factor
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
MhCntDr|INTEGER|Count of mental health providers within a 30-minute driving threshold
HivTmDr|NUMERIC|Driving time from origin to nearest HIV testing provider (minutes)
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
RxTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid with impedance factor, in minutes
NaltTmDr2|NUMERIC|Driving time in minutes from the tract centroid to the nearest naltrexone provider, with the impedance factor applied.
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
HcvMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest HCV testing provider (miles)
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
SutTmDr|NUMERIC|Driving time (min) to nearest  Substance Use Treatment (SUT) facility
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
HivTmDr2|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip HIV Testing Facility with impedance destination centroid, in minutes
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
HivCntDr|INTEGER|Number of HIV testing providers within a 30-minute drive
SutTmDr2|NUMERIC|Driving time (minutes) from the tract/zip centroid to the nearest Substance Use Treatment provider, with the impedance factor applied.
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
HivMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest HIV testing provider (miles)
MetTmDr2|NUMERIC|Driving time in minutes from the tract centroid to the nearest methadone provider, with the impedance factor applied.
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
HcvCntDr|INTEGER|Number of HCV testing providers within a 30-minute drive

### state-2013

ID: `oeps-391119.tabular.state-2013`

12 columns in this table.

Name|Data Type|Description
-|-|-|-
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
FlHcvD|INTEGER|Hepatitis C deaths among women
HcvD|INTEGER|Total Hepatitis C deaths
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MlHcvD|INTEGER|Hepatitis C deaths among men
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age

### tract-2019

ID: `oeps-391119.tabular.tract-2019`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles
NoIntP|NUMERIC|Percentage of Households without Internet access

### state-2022

ID: `oeps-391119.tabular.state-2022`

64 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
TtlPrPpr|NUMERIC|Total Prison Population Rate
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
AvMlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among men from 2013-2017
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MulHcvD|NUMERIC|
CrrctExp|INTEGER|Total expenditures on corrections system and operations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
OpRxRt|NUMERIC|Opioid prescription rate
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
AvAmInHcvD|NUMERIC|Mean yearly Hepatitis C deaths among American Indian population from 2013-2017
AvNhPiHcvD|NUMERIC|
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
TtlPrAPp|INTEGER|Prison Prison Admissions Count
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
AvHcvD|NUMERIC|Mean total yearly Hepatitis C deaths from 2013-2017, 2018-2022
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
AvAsHcvD|NUMERIC|
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
AvWhHcvD|NUMERIC|Mean yearly Hepatitis C deaths among White populations from 2018-2022
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
TtlPrPp|INTEGER|Total Prison Population Count
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
AvMulHcvD|NUMERIC|
AvU50HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people under 50 years of age from 2013-2017
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
NhPiHcvD|NUMERIC|
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
FlHcvD|INTEGER|Hepatitis C deaths among women
HcvD|INTEGER|Total Hepatitis C deaths
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AvO75HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people over 75 years of age
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate
PrMsuseP|NUMERIC|Percent of persons who self-report misusing prescription pain relief medication in 2020.
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
AvBlkHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Black populations from 2013-2017
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AvA50_74HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people between 50 and 74 years of age from 2013-2017, 2018-2022
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
OdMortRt|NUMERIC|Overdose mortality rate
HlthExp|INTEGER|Total expenditures on public health and hospitals
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
ParkArea|NUMERIC|Area (in square meters) of park or green space in a state).
AsHcvD|NUMERIC|
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data
WhtHcvD|NUMERIC|
AvFlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among women from 2013-2017
MlHcvD|INTEGER|Hepatitis C deaths among men
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
AvHspHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Hispanic populations from 2013-2017
WlfrExp|INTEGER|Total expenditures on public welfare programs

### tract-1990

ID: `oeps-391119.tabular.tract-1990`

45 columns in this table.

Name|Data Type|Description
-|-|-|-
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### tract-2021

ID: `oeps-391119.tabular.tract-2021`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### tract-ruca-2020

ID: `oeps-391119.tabular.tract-ruca-2020`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
Ruca1|STRING|Primary RUCA Code
Rurality|STRING|Urban/Suburban/Rural
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
Ruca2|STRING|Secondary RUCA Code

### state-2019

ID: `oeps-391119.tabular.state-2019`

54 columns in this table.

Name|Data Type|Description
-|-|-|-
NoPrphLw|BOOLEAN|Dummy variable indicating whether the state has no state drug paraphernalia law (0=no, 1=yes)
NoLwRmUnc|BOOLEAN|Dummy variable indicating whether the state has no law removing barriers or uncertainty as to SSP legality (0=no, 1=yes)
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
MedcdExp|INTEGER|Total medicaid spending
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
MedPolP5Yr|NUMERIC|Proportion of the five-year period (ending in given year) for which Medicaid Expansion was implemented / in effect
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
MulHcvD|NUMERIC|
CrrctExp|INTEGER|Total expenditures on corrections system and operations
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
NtPrFrDsSy|BOOLEAN|Dummy variable indicating whether the state law does not prohibit free distribution of syringes (0=no, 1=yes)
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
ExpSsp|BOOLEAN|Dummy variable indicating whether the state has law that explicitly authorizes Syringe Service Programs (0=no, 1=yes)
PrNtRefInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law does not refer to objects used for injecting drugs (0=no, 1=yes)
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
NhPiHcvD|NUMERIC|
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.
FlHcvD|INTEGER|Hepatitis C deaths among women
HcvD|INTEGER|Total Hepatitis C deaths
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
PlcFyrExp|INTEGER|Total expenditures on police and fire protection
OdMortRt|NUMERIC|Overdose mortality rate
HlthExp|INTEGER|Total expenditures on public health and hospitals
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
AsHcvD|NUMERIC|
WhtHcvD|NUMERIC|
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
MlHcvD|INTEGER|Hepatitis C deaths among men
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
NoIntP|NUMERIC|Percentage of Households without Internet access
PrExcInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law explicitly exludes objects used for injecting drugs (0=no, 1=yes)
WlfrExp|INTEGER|Total expenditures on public welfare programs

### tract-sdoh-2014

ID: `oeps-391119.tabular.tract-sdoh-2014`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
MicaInd|NUMERIC|Raw Mixed Immigrant Cohesion and Accessibility (MICA) Index (https://sdohatlas.github.io/)
NeighbTyp|STRING|Categorical, one of seven neighborhood (tract-level) typologies: 1 = Rural Affordable; 2 = Suburban Affluent; 3 = Suburban Affordable; 4 = Extreme Poverty; 5 = Multilingual Working; 6 = Urban Core Opportunity; 7 = Sparse Areas
LimMobInd|NUMERIC|Raw Limited Mobility Index (https://sdohatlas.github.io/)
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
UrbCoreInd|NUMERIC|Raw Urban Core Opportunity Index (https://sdohatlas.github.io/)
SocEcAdvIn|NUMERIC|Raw Socioeconomic Advantage Index (https://sdohatlas.github.io/)

### county-2010

ID: `oeps-391119.tabular.county-2010`

46 columns in this table.

Name|Data Type|Description
-|-|-|-
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
VetP|NUMERIC|Percent of population that are veterans
TotVetPop|INTEGER|Total Veteran population
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### county-2021

ID: `oeps-391119.tabular.county-2021`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate

### county-1990

ID: `oeps-391119.tabular.county-1990`

42 columns in this table.

Name|Data Type|Description
-|-|-|-
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### tract-2022

ID: `oeps-391119.tabular.tract-2022`

7 columns in this table.

Name|Data Type|Description
-|-|-|-
SviSmryRnk|NUMERIC|Overall summary ranking
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation

### state-2014

ID: `oeps-391119.tabular.state-2014`

14 columns in this table.

Name|Data Type|Description
-|-|-|-
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
FlHcvD|INTEGER|Hepatitis C deaths among women
HcvD|INTEGER|Total Hepatitis C deaths
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
OdMortRt|NUMERIC|Overdose mortality rate
MlHcvD|INTEGER|Hepatitis C deaths among men
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age

### state-providers-2010

ID: `oeps-391119.tabular.state-providers-2010`

4 columns in this table.

Name|Data Type|Description
-|-|-|-
TotPcp|INTEGER|Number of primary care providers in area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TotSp|INTEGER|Number of specialty physicians in area

### state-2000

ID: `oeps-391119.tabular.state-2000`

43 columns in this table.

Name|Data Type|Description
-|-|-|-
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
SRatio|NUMERIC|
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### county-2024

ID: `oeps-391119.tabular.county-2024`

8 columns in this table.

Name|Data Type|Description
-|-|-|-
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data
TtlJlPrt|NUMERIC|Pretrial Jail Population Count
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data

### county-ruca-2020

ID: `oeps-391119.tabular.county-ruca-2020`

5 columns in this table.

Name|Data Type|Description
-|-|-|-
RcaSubrbP|NUMERIC|Percent census tracts in the county classified as Suburban using RUCA codes
RcaRuralP|NUMERIC|Percent census tracts in the county classified as Rural using RUCA codes
RcaUrbanP|NUMERIC|Percent census tracts in the county classified as Urban using RUCA codes
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.

### zcta-2020

ID: `oeps-391119.tabular.zcta-2020`

109 columns in this table.

Name|Data Type|Description
-|-|-|-
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
HhldFA|NUMERIC|Percent female householder with no spouse/partner living alone
NvMrrdP|NUMERIC|Percent males aged 15 or older who never got married
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
MrrdP|NUMERIC|Percent males aged 15 or older who are married and living with their spouse
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider
NaltCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
HsdTypMC|NUMERIC|Percent married-couple household With children under 18 years
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
SepartedP|NUMERIC|Percent males aged 15 years and over who are separated from their spouse
CrowdHsng|NUMERIC|Proportion of occupied housing units that are considered crowded (more than 1 person per room)
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
VetP|NUMERIC|Percent of population that are veterans
TotVetPop|INTEGER|Total Veteran population
BupCntDr30|INTEGER|Count of Buprenorphine providers in 30 minute drive time threshold
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
TwoRaceP|NUMERIC|Percent of population identifying as two or more races
TotPopHh|INTEGER|Total number of people in households
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold
HhldMA|NUMERIC|Percent male householder with no spouse/partner living alone
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles
NaltTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider
HhldMC|NUMERIC|Percent married-couple household With children under 18 years
Und18P|NUMERIC|Percent of population under age 18
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider
HhldMS|NUMERIC|Percent male householder 65 years and over living alone
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
NaltMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider
SRatio65|NUMERIC|
HhldFC|NUMERIC|Percent female householder with no spouse/partner living with children under 18 years
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold
VacantP|NUMERIC|Percentage of vacant housing units
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
HhldFS|NUMERIC|Percent female householder 65 years and over living alone
Ovr21P|NUMERIC|Percent of population over age 21
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
MhCntDr|INTEGER|Count of mental health providers within a 30-minute driving threshold
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold
WidwdP|NUMERIC|Percent male population aged 15 and over who are widowed
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
OccupantP|NUMERIC|Percent occupied housing units
HHSize|NUMERIC|Average number of persons per household
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
NaltCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
HsdTot|NUMERIC|Total households
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest Federally Qualified Health Centers (FQHC), in miles
SutTmDr|NUMERIC|Driving time (min) to nearest  Substance Use Treatment (SUT) facility
NaltTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
FamSize|NUMERIC|Average number of persons per family
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
FqhcCntDr|INTEGER|Count of Federally Qualified Health Centers (FQHCs) within a 30-minute driving threshold
HsdTypCo|NUMERIC|Percent cohabiting couple household
NaltCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold
MedAge|NUMERIC|
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes
MaleP|NUMERIC|Percent of population that is male
HsdTypM|NUMERIC|Percent married-couple household
NaltCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold
Ovr16P|NUMERIC|Percent of population over age 16
TotWrkE|INTEGER|Estimated count of working population
Ovr62P|NUMERIC|Percent of population over age 62
RentalP|NUMERIC|Percentage of occupied housing units that are rented
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold
DivrcdP|NUMERIC|Percent males 15 years and over who are divorced
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider
NaltTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes
NaltCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold
HisP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### tract-2018

ID: `oeps-391119.tabular.tract-2018`

79 columns in this table.

Name|Data Type|Description
-|-|-|-
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
LibPerCap|NUMERIC|Libraries per capita by census tract
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
AlcDens|NUMERIC|Number of alcohol outlets per square mile
VetP|NUMERIC|Percent of population that are veterans
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
TotVetPop|INTEGER|Total Veteran population
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TotPopHh|INTEGER|Total number of people in households
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SviSmryRnk|NUMERIC|Overall summary ranking
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
AlcTot|INTEGER|Total number of alcohol outlets
SocCapInd|NUMERIC|Composite index of LngTermP, LibPerCap, RlgPerCap
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
AreaSqMi|NUMERIC|Land area of geography in sq miles
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
MaleP|NUMERIC|Percent of population that is male
MedHsgTen|STRING|Median time period occupant moved into housing unit by tract
Ovr16P|NUMERIC|Percent of population over age 16
TotWrkE|INTEGER|Estimated count of working population
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
RentalP|NUMERIC|Percentage of occupied housing units that are rented
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
RlgPerCap|NUMERIC|Religious institutions per capita by census tract
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### zcta-2018

ID: `oeps-391119.tabular.zcta-2018`

82 columns in this table.

Name|Data Type|Description
-|-|-|-
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).
AsianP|NUMERIC|Percentage of population with race identified as Asian alone
EduNoHsP|NUMERIC|Percent population aged 25 years and over with less than a high school diploma
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)
AlcDens|NUMERIC|Number of alcohol outlets per square mile
VetP|NUMERIC|Percent of population that are veterans
Ovr65|NUMERIC|Percentage of population between ages of 15 & 24
TotVetPop|INTEGER|Total Veteran population
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities
WhiteE|NUMERIC|Count persons with race identified as white alone. Estimated count in non-decennial years.
TotPopHh|INTEGER|Total number of people in households
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract
HisE|NUMERIC|Count persons with ethnicity identified as of Hispanic or Latinx origin. Estimated count in non-decennial years.
BlackE|NUMERIC|Count population with race identified as Black or African American alone. Estimated count in non-decennial years.
SviSmryRnk|NUMERIC|Overall summary ranking
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family
AmIndE|NUMERIC|Count population with race identified as Native American or Alaska Native alone. Estimated count in non-decennial years.
EduHsP|NUMERIC|	Percent population aged 25 years and over whose highest educational attainment is a high school diploma (or equivalent)
SRatio65|NUMERIC|
Age15_44P|NUMERIC|Percentage of population below 45 years of age
SomeCollegeP|NUMERIC|Percent population 25 years and over with some college, but no degree
VacantP|NUMERIC|Percentage of vacant housing units
ChildrenP|NUMERIC|Percentage of population under age 18
FemP|NUMERIC|Percent of population that is female
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents
GradSclP|NUMERIC|Percent population aged 25 years and over with a graduate or professional degree
AlcTot|INTEGER|Total number of alcohol outlets
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone
Ovr65P|NUMERIC|Percentage of population over 65
Ovr18|NUMERIC|
Ovr21P|NUMERIC|Percent of population over age 21
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries
UnitDens|NUMERIC|Number of housing units per square mile of land area
WhiteP|NUMERIC|Percentage of population with race identified as white alone
SRatio18|NUMERIC|
AreaSqMi|NUMERIC|Land area of geography in sq miles
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.
Ovr18P|NUMERIC|Percent of population over age 18
TotUnits|INTEGER|Count of total occupied housing units
PacIsE|NUMERIC|Count population with race identified as Native Hawaiian and Other Pacific Islander alone. Estimated count in non-decennial years.
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents
Ovr21|NUMERIC|
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone
OtherE|NUMERIC|Count of Population with race not mentioned in any of the options above (includes two race or more races). Estimated count in non-decennial years.
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related
SRatio|NUMERIC|
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents
RetailP|NUMERIC|Percentage of population employed in retail trade industry
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone
EngProf|NUMERIC|Proportion of the population aged 18+ who speak a language other than English at home but are proficient in English
TwoRaceE|NUMERIC|Count persons identifying as two or more races. Estimated count in non-decennial years.
MaleP|NUMERIC|Percent of population that is male
Ovr16P|NUMERIC|Percent of population over age 16
TotWrkE|INTEGER|Estimated count of working population
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic
RentalP|NUMERIC|Percentage of occupied housing units that are rented
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)
BachelorsP|NUMERIC|Percent persons aged 25 years and over with a bachelor’s degree as their highest level of education
AsianE|NUMERIC|Count population with race identified as Asian alone. Estimated count in non-decennial years.
Age15_44|INTEGER|Total population between age 15-44
ZCTA5|STRING|Census Bureau designated zip code tabulation area, or the rough area that contains five digit zip codes.
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability
TotPop|INTEGER|Total population
Ovr16|NUMERIC|
AlcPerCap|NUMERIC|Number of alcohol outlets per capita
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin

### state-2017

ID: `oeps-391119.tabular.state-2017`

53 columns in this table.

Name|Data Type|Description
-|-|-|-
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age
BlkHcvD|INTEGER|Hepatitis C deaths among Black population
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.
NonBlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations non-Black other race/ethnicity populations 2013-2016
AvMlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among men from 2013-2017
AnyNalxFr|NUMERIC|Fraction of year any type of Naloxone law is effective
Un50Hcv|NUMERIC|Mean yearly Hepatatis C cases in people under 50 years of age from 2013-2016
Ov75Hcv|NUMERIC|Mean yearly Hepatitis C cases in people over 75 years of age from 2013-2016
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted
A50_74Hcv|NUMERIC|Mean yearly Hepatitis C cases in people between 50 to 74 years of age from 2013-2016
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.
AvAmInHcvD|NUMERIC|Mean yearly Hepatitis C deaths among American Indian population from 2013-2017
MedPolProp|NUMERIC|Proportion of given year for which Medicaid Expansion was implemented / in effect
MlHcv|NUMERIC|Mean yearly Hepatitis C cases in men from 2013-2016
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.
AvHcvD|NUMERIC|Mean total yearly Hepatitis C deaths from 2013-2017, 2018-2022
FmHcv|NUMERIC|Mean yearly Hepatitis C cases in women from 2013-2016
TotHcv|NUMERIC|Mean total yearly Hepitatis C cases from 2013-2016
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
NalxPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective
NalxPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order
NalxPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective
AvU50HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people under 50 years of age from 2013-2017
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.
AvAsPiHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Asian and Pacific Islanders population from 2013-2017
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations
FlHcvD|INTEGER|Hepatitis C deaths among women
HcvD|INTEGER|Total Hepatitis C deaths
NalxPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations
AvO75HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people over 75 years of age
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations
AvBlkHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Black populations from 2013-2017
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
AvA50_74HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people between 50 and 74 years of age from 2013-2017, 2018-2022
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)
OdMortRt|NUMERIC|Overdose mortality rate
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.
BlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations identified as non-hispanic Black alone across 2013-2016
AvFlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among women from 2013-2017
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective
MlHcvD|INTEGER|Hepatitis C deaths among men
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age
AnyNalxDt|DATE|Date (MY) any type of Naloxone law effective
AvHspHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Hispanic populations from 2013-2017

### tract-providers-2010

ID: `oeps-391119.tabular.tract-providers-2010`

6 columns in this table.

Name|Data Type|Description
-|-|-|-
PcpPer100k|NUMERIC|PCPs per total Population X 100,000
TotPcp|INTEGER|Number of primary care providers in area
FIPS|STRING|Federal Information Processing Standard code designated by the NIST; is two digits for states, five digits for counties, eleven digits for tracts.
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.
TotSp|INTEGER|Number of specialty physicians in area
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000

