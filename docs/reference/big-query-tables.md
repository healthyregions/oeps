# Project Id: oeps-391119

2 datasets in this project: tabular, spatial

## tabular

39 tables in this dataset.

### county-2020

ID: `oeps-391119.tabular.county-2020`

74 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
TotPopHh|INTEGER|Total number of people in households|ACS 2018, 5-Year
TotVetPop|INTEGER|Total Veteran population|ACS 2018, 5-Year; ACS 2012, 5-Year
TotWrkE|INTEGER|Estimated count of working population|ACS 2018, 5-Year
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
VetP|NUMERIC|Percent of population that are veterans|ACS 2017, 5-Year; ACS 2012, 5-Year
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family|ACS 2018, 5-Year
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related|ACS 2018, 5-Year
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)|ACS 2018, 5-Year; ACS 2012, 5-Year
EduP|NUMERIC|Percentage of population employed in educational services industry|ACS 2018, 5-Year
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities|ACS 2018, 5-Year
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries|ACS 2018, 5-Year
RetailP|NUMERIC|Percentage of population employed in retail trade industry|ACS 2018, 5-Year
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.|ACS 2018, 5-Year
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures|ACS 2018, 5-Year
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago|ACS 2018, 5-Year
RentalP|NUMERIC|Percentage of occupied housing units that are rented|ACS 2018, 5-Year
UnitDens|NUMERIC|Number of housing units per square mile of land area|ACS 2018, 5-Year
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range|US Covid Atlas via HRSA, 2020
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center|US Covid Atlas via HRSA, 2020
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.|US Covid Atlas via HRSA, 2020
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range|CovidCareMap, 2020
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.|CovidCareMap, 2020
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range|CovidCareMap, 2020
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.|SAMHSA, 2020
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.|SAMHSA, 2020
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.|SAMHSA, 2020
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.|SAMHSA, 2020
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.|SAMHSA, 2020
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.|SAMHSA, 2020
OpRxRt|NUMERIC|Opioid prescription rate|HepVu, 2020
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020|HepVu, 2020
BupCtTmDr|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCtTmBk|INTEGER|Number of tracts with buprenorphine provider within a 30-min biking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCtTmWk|INTEGER|Number of tracts with buprenorphine provider within a 30-min walking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCtTmDr|INTEGER|Number of tracts with methadone provider within a 30-min driving range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCtTmBk|INTEGER|Number of tracts with methadone provider within a 30-min biking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCtTmWk|INTEGER|Number of tracts with methadone provider within a 30-min walking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCtTmDr|INTEGER|Number of tracts with naltrexone provider within a 30-min driving range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCtTmBk|INTEGER|Number of tracts with naltrexone provider within a 30-min biking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCtTmWk|INTEGER|Number of tracts with naltrexone provider within a 30-min walking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalAvTmDr|NUMERIC|Average driving time (minutes) across tracts in county to nearest naltrexone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalAvTmBk|NUMERIC|Average biking time (minutes) across tracts in county to nearest naltrexone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalAvTmWk|NUMERIC|Average walking time (minutes) across tracts in county to nearest naltrexone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupTmDrP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupTmBkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min biking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupTmWkP|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min walking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetTmDrP|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetTmBkP|NUMERIC|Percent of tracts with methadone provider within a 30-min biking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetTmWkP|NUMERIC|Percent of tracts with methadone provider within a 30-min walking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalTmDrP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalTmBkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min biking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalTmWkP|NUMERIC|Percent of tracts with naltrexone provider within a 30-min walking range|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020

### state-2017

ID: `oeps-391119.tabular.state-2017`

51 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
TotHcv|NUMERIC|Mean total yearly Hepitatis C cases from 2013-2016|HepVu, 2017
MlHcv|NUMERIC|Mean yearly Hepatitis C cases in men from 2013-2016|HepVu, 2017
FmHcv|NUMERIC|Mean yearly Hepatitis C cases in women from 2013-2016|HepVu, 2017
Un50Hcv|NUMERIC|Mean yearly Hepatatis C cases in people under 50 years of age from 2013-2016|HepVu, 2017
A50_74Hcv|NUMERIC|Mean yearly Hepatitis C cases in people between 50 to 74 years of age from 2013-2016|HepVu, 2017
Ov75Hcv|NUMERIC|Mean yearly Hepatitis C cases in people over 75 years of age from 2013-2016|HepVu, 2017
BlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations identified as non-hispanic Black alone across 2013-2016|HepVu, 2017
NonBlkHcv|NUMERIC|Mean yearly Hepatitis C cases in populations non-Black other race/ethnicity populations 2013-2016|HepVu, 2017
HcvD|INTEGER|Total Hepatitis C deaths|HepVu, 2017
MlHcvD|INTEGER|Hepatitis C deaths among men|HepVu, 2017
FlHcvD|INTEGER|Hepatitis C deaths among women|HepVu, 2017
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations|HepVu, 2017
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations|HepVu, 2017
BlkHcvD|INTEGER|Hepatitis C deaths among Black population|HepVu, 2017
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations|HepVu, 2017
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age|HepVu, 2017
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age|HepVu, 2017
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age|HepVu, 2017
AvHcvD|NUMERIC|Mean total yearly Hepatitis C deaths from 2013-2017|HepVu, 2017
AvMlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among men from 2013-2017|HepVu, 2017
AvFlHcvD|NUMERIC|Mean yearly Hepatitis C deaths among women from 2013-2017|HepVu, 2017
AvAmInHcvD|NUMERIC|Mean yearly Hepatitis C deaths among American Indian population from 2013-2017|HepVu, 2017
AvAsPiHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Asian and Pacific Islanders population from 2013-2017|HepVu, 2017
AvBlkHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Black populations from 2013-2017|HepVu, 2017
AvHspHcvD|NUMERIC|Mean yearly Hepatitis C deaths among Hispanic populations from 2013-2017|HepVu, 2017
AvU50HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people under 50 years of age from 2013-2017|HepVu, 2017
Av50_74HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people between 50 and 74 years of age from 2013-2017|HepVu, 2017
AvO75HcvD|NUMERIC|Mean yearly Hepatitis C deaths among people over 75 years of age|HepVu, 2017
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020
AnyPdmpFr|NUMERIC|Fraction of year that state has any prescription drug monitoring program operating.|OPTIC, 2017
AnyPdmphFr|NUMERIC|Fraction of year that state has prescription drug monitoring program enabling legislation for any type of prescription drug monitoring program in effect ,including paper-based systems (as determined by Horowitz et al., 2018) enacted|OPTIC, 2017
OpPdmpFr|NUMERIC|Fraction of year that state has a “modern system” operational and users could access (as determined by Horowitz et al., 2018).|OPTIC, 2017
MsAcPdmpFr|NUMERIC|Fraction of year that state has any legislation requiring Prescribers to access PDMP before prescribing (as interpreted by PDAPS) enacted.|OPTIC, 2017
ElcPdmpFr|NUMERIC|Fraction of year that state has an electronic PDMP system operating.|OPTIC, 2017
AnyPdmpDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: PDAPS for first PDMP laws passed after January 1, 1998; Info on laws prior to 1998 came from Brandeis TTAC.|OPTIC, 2017
AnyPdmphDt|DATE|Date when PDMP enabling legislation was first enacted for any type of PDMP in effect (including paper-based systems). Source: Horowitz et al., 2018, Table 2, column 1.|OPTIC, 2017
OpPdmpDt|DATE|Date when a “modern system” became operational and users could access. Source: Horowitz et al., 2018, Table 2, column 4. This definition includes specific caveats adopted by Horowitz et al., 2018, described further below in Notes.|OPTIC, 2017
MsAcPdmpDt|DATE|Date of legislation requiring Prescribers to access PDMP before prescribing as interpreted by PDAPS.|OPTIC, 2017
ElcPdmpDt|DATE|Date state began operating an electronic PDMP system.|OPTIC, 2017
AnyGslDt|DATE|Date (DMY) any type of GoodDate (DMY) any type of Good Samaritan Law is effective|OPTIC, 2017
GslArrDt|DATE|Date (DMY) that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective|OPTIC, 2017
AnyGslFr|NUMERIC|Fraction of year any type of Good Samaritan Law is effective|OPTIC, 2017
GslArrFr|NUMERIC|Fraction of year that Good Samaritan Law providing protection from arrest for controlled substance possession laws is effective|OPTIC, 2017
AnyNalDt|DATE|Date (MY) any type of Naloxone law effective|OPTIC, 2017
NalPrStDt|DATE|Date (MY) Naloxone law allowing distribution through a standing or protocol order effective|OPTIC, 2017
NalPresDt|DATE|Date (MY) Naloxone law allowing pharmacists prescriptive authority effective|OPTIC, 2017
AnyNalFr|NUMERIC|Fraction of year any type of Naloxone law is effective|OPTIC, 2017
NalPrStFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing distribution through a standing or protocol order|OPTIC, 2017
NalPresFr|NUMERIC|Fraction of year state has an effective Naloxone law allowing pharmacists prescriptive authority|OPTIC, 2017
MdMarijLaw|BOOLEAN|Dummy variable, indicating whether state has a law authorizing adults to use medical marijuana (0=no, 1=yes)|PDAPS, 2017

### tract-1980

ID: `oeps-391119.tabular.tract-1980`

32 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age45_54|INTEGER|Total population between age 45-54|IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)|

### county-2021

ID: `oeps-391119.tabular.county-2021`

4 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range|SAMSHA, 2021
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.|SAMSHA, 2021
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.|SAMSHA, 2021

### zcta-2020

ID: `oeps-391119.tabular.zcta-2020`

41 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest FQHC, in miles|US Covid Atlas via HRSA, 2020
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes|US Covid Atlas via HRSA, 2020
FqhcCntDr|INTEGER|Count of FQHCs within a 30-minute driving threshold|US Covid Atlas via HRSA, 2020
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles|CovidCareMap, 2020
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes|CovidCareMap, 2020
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold|CovidCareMap, 2020
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles|SAMHSA, 2020
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes|SAMHSA, 2020
MhCntDr|INTEGER|Count of MH providers within a 30-minute driving threshold|SAMHSA, 2020
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles|SAMHSA, 2020
SutTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip SUT destination centroid, in minutes|SAMHSA, 2020
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold|SAMHSA, 2020

### tract-2010

ID: `oeps-391119.tabular.tract-2010`

42 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
TotVetPop|INTEGER|Total Veteran population|ACS 2018, 5-Year; ACS 2012, 5-Year
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
VetP|NUMERIC|Percent of population that are veterans|ACS 2017, 5-Year; ACS 2012, 5-Year
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)|ACS 2018, 5-Year; ACS 2012, 5-Year
TotPcp|INTEGER|Number of primary care providers in area|Dartmouth Atlas, 2010
TotSp|INTEGER|Number of specialty physicians in area|Dartmouth Atlas, 2010
PcpPer100k|NUMERIC|PCPs per total Population X 100,000|Dartmouth Atlas, 2010
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000|Dartmouth Atlas, 2010
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)|

### zcta-2021

ID: `oeps-391119.tabular.zcta-2021`

4 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles|SAMSHA, 2021
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes|SAMSHA, 2021
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold|SAMSHA, 2021

### tract-1990

ID: `oeps-391119.tabular.tract-1990`

33 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)|

### state-1980

ID: `oeps-391119.tabular.state-1980`

29 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age45_54|INTEGER|Total population between age 45-54|IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer

### state-2016

ID: `oeps-391119.tabular.state-2016`

12 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
HcvD|INTEGER|Total Hepatitis C deaths|HepVu, 2017
MlHcvD|INTEGER|Hepatitis C deaths among men|HepVu, 2017
FlHcvD|INTEGER|Hepatitis C deaths among women|HepVu, 2017
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations|HepVu, 2017
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations|HepVu, 2017
BlkHcvD|INTEGER|Hepatitis C deaths among Black population|HepVu, 2017
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations|HepVu, 2017
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age|HepVu, 2017
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age|HepVu, 2017
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age|HepVu, 2017
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020

### state-2022

ID: `oeps-391119.tabular.state-2022`

3 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
ParkArea|NUMERIC|Area (in square meters) of park or green space in a state).|OSM
Cover|NUMERIC|Percent of state covered by park or green space|OSM

### tract-2020

ID: `oeps-391119.tabular.tract-2020`

51 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
MoudMinDis|NUMERIC|Euclidean distance (miles) to nearest MOUD (all types)|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupMinDis|NUMERIC|Euclidean distance (miles) to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupTmDr|NUMERIC|Driving time (minutes) to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetMinDis|NUMERIC|Euclidean distance (miles) to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetTmDr|NUMERIC|Driving time (minutes) to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntDr30|INTEGER|Count of methadone providers in 30 minute drive time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalMinDis|NUMERIC|Euclidean distance (miles) to nearest naltrexone/Vivitrol provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalTmDr|NUMERIC|Driving time (minutes) to nearest naltrexone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntDr30|INTEGER|Count of naltrexone providers in 30 minute drive time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupTmWk|NUMERIC|Walking time (minutes) to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntWk60|INTEGER|Count of buprenorphine providers in 60 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntWk30|INTEGER|Count of buprenorphine providers in 30 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetTmWk|NUMERIC|Walking time (minutes) to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntWk30|INTEGER|Count of methadone providers in 60 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntWk60|INTEGER|Count of methadone providers in 30 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalTmWk|NUMERIC|Walking time (minutes) to nearest naltrexone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntWk60|INTEGER|Count of naltrexone providers in 60 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntWk30|INTEGER|Count of naltrexone providers in 30 minute walking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupTmBk|NUMERIC|Biking time (minutes) to nearest buprenorphine provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntBk60|INTEGER|Count of buprenorphine providers in 60 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
BupCntBk30|INTEGER|Count of buprenorphine providers in 30 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetTmBk|NUMERIC|Biking time (minutes) to nearest methadone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntBk60|INTEGER|Count of methadone providers in 60 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
MetCntBk30|INTEGER|Count of methadone providers in 30 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalTmBk|NUMERIC|Biking time (minutes) to nearest naltrexone provider|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntBk60|INTEGER|Count of naltrexone providers in 60 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
NalCntBk30|INTEGER|Count of naltrexone providers in 30 minute biking time threshold|SAMHSA, 2019; Vivitrol, 2020; OSRM, 2020
FqhcMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest FQHC, in miles|US Covid Atlas via HRSA, 2020
FqhcTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip FQHC destination centroid, in minutes|US Covid Atlas via HRSA, 2020
FqhcCntDr|INTEGER|Count of FQHCs within a 30-minute driving threshold|US Covid Atlas via HRSA, 2020
HospMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest hospital, in miles|CovidCareMap, 2020
HospTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip hospital destination centroid, in minutes|CovidCareMap, 2020
HospCntDr|INTEGER|Count of hospitals within a 30-minute driving threshold|CovidCareMap, 2020
MhMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest mental health provider, in miles|SAMHSA, 2020
MhTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip mental health provider destination centroid, in minutes|SAMHSA, 2020
MhCntDr|INTEGER|Count of MH providers within a 30-minute driving threshold|SAMHSA, 2020
SutMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest SUT service location, in miles|SAMHSA, 2020
SutTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip SUT destination centroid, in minutes|SAMHSA, 2020
SutCntDr|INTEGER|Count of SUT services within a 30-minute driving threshold|SAMHSA, 2020
NeighbTyp|STRING|Categorical, one of seven neighborhood (tract-level) typologies: 1 = Rural Affordable; 2 = Suburban Affluent; 3 = Suburban Affordable; 4 = Extreme Poverty; 5 = Multilingual Working; 6 = Urban Core Opportunity; 7 = Sparse Areas|Kolak et al., 2020
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)|
NalRm30|NUMERIC|Naltrexone access 30 minutes (RAAM)|
NalRm60|NUMERIC|Naltrexone access 60 minutes (RAAM)|
NalRm90|NUMERIC|Naltrexone access 90 minutes (RAAM)|
BupRm30|NUMERIC|Buprenorphine access 30 minutes (RAAM)|
BupRm60|NUMERIC|Buprenorphine access 60 minutes (RAAM)|
BupRm90|NUMERIC|Buprenorphine access 90 minutes (RAAM)|

### state-1990

ID: `oeps-391119.tabular.state-1990`

30 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS

### state-2019

ID: `oeps-391119.tabular.state-2019`

13 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
NoIntP|NUMERIC|Percentage of Households without Internet access|ACS, 2019
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range|InfoGroup, 2019
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.|InfoGroup, 2019
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range|InfoGroup, 2019
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020
MedcdExp|INTEGER|Total medicaid spending|KFF, 2019
ExpSsp|BOOLEAN|Dummy variable indicating whether the state has law that explicitly authorizes Syringe Service Programs (0=no, 1=yes)|LawAtlas, 2019
NoPrphLw|BOOLEAN|Dummy variable indicating whether the state has no state drug paraphernalia law (0=no, 1=yes)|LawAtlas, 2019
NtPrFrDsSy|BOOLEAN|Dummy variable indicating whether the state law does not prohibit free distribution of syringes (0=no, 1=yes)|LawAtlas, 2019
PrExcInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law explicitly exludes objects used for injecting drugs (0=no, 1=yes)|LawAtlas, 2019
PrNtRefInj|BOOLEAN|Dummy variable indicating whether the paraphernalia definition in the state law does not refer to objects used for injecting drugs (0=no, 1=yes)|LawAtlas, 2019
NoLwRmUnc|BOOLEAN|Dummy variable indicating whether the state has no law removing barriers or uncertainty as to SSP legality (0=no, 1=yes)|LawAtlas, 2019

### tract-2021

ID: `oeps-391119.tabular.tract-2021`

4 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
OtpMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest OTP service location, in miles|SAMSHA, 2021
OtpTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip OTP destination centroid, in minutes|SAMSHA, 2021
OtpCntDr|INTEGER|Count of OTPs within a 30-minute driving threshold|SAMSHA, 2021

### county-1980

ID: `oeps-391119.tabular.county-1980`

29 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age45_54|INTEGER|Total population between age 45-54|IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer

### tract-2018

ID: `oeps-391119.tabular.tract-2018`

65 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
TotPopHh|INTEGER|Total number of people in households|ACS 2018, 5-Year
TotVetPop|INTEGER|Total Veteran population|ACS 2018, 5-Year; ACS 2012, 5-Year
TotWrkE|INTEGER|Estimated count of working population|ACS 2018, 5-Year
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
AgeOv18|NUMERIC|Total population at or over age 18|ACS 2018, 5-Year; 2010 Decennial Census
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
VetP|NUMERIC|Percent of population that are veterans|ACS 2017, 5-Year; ACS 2012, 5-Year
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family|ACS 2018, 5-Year
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related|ACS 2018, 5-Year
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession|HUD, 2018
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession|HUD, 2018
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)|ACS 2018, 5-Year; ACS 2012, 5-Year
EduP|NUMERIC|Percentage of population employed in educational services industry|ACS 2018, 5-Year
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities|ACS 2018, 5-Year
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries|ACS 2018, 5-Year
RetailP|NUMERIC|Percentage of population employed in retail trade industry|ACS 2018, 5-Year
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.|ACS 2018, 5-Year
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.|ACS 2018, 5-Year
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures|ACS 2018, 5-Year
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago|ACS 2018, 5-Year
RentalP|NUMERIC|Percentage of occupied housing units that are rented|ACS 2018, 5-Year
UnitDens|NUMERIC|Number of housing units per square mile of land area|ACS 2018, 5-Year
AreaSqMi|NUMERIC|Land area of geography in sq miles|InfoGroup, 2018
AlcTot|INTEGER|Total number of alcohol outlets|InfoGroup, 2018
AlcDens|NUMERIC|Number of alcohol outlets per square mile|InfoGroup, 2018
AlcPerCap|NUMERIC|Number of alcohol outlets per capita|InfoGroup, 2018
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract|Sentinel-2 MSI, 2018
Ruca1|STRING|Primary RUCA Code|USDA-ERS 2010 & ACS 2018 5-Year
Ruca2|STRING|Secondary RUCA Code|USDA-ERS 2010 & ACS 2018 5-Year
Rurality|STRING|Urban/Suburban/Rural|USDA-ERS 2010 & ACS 2018 5-Year
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic|CDC, 2018
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability|CDC, 2018
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language|CDC, 2018
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation|CDC, 2018
SviSmryRnk|NUMERIC|Overall summary ranking|CDC, 2018

### tract-2019

ID: `oeps-391119.tabular.tract-2019`

5 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
NoIntP|NUMERIC|Percentage of Households without Internet access|ACS, 2019
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles|InfoGroup, 2019
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes|InfoGroup, 2019
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold|InfoGroup, 2019

### county-1990

ID: `oeps-391119.tabular.county-1990`

30 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS

### state-2010

ID: `oeps-391119.tabular.state-2010`

37 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
TotVetPop|INTEGER|Total Veteran population|ACS 2018, 5-Year; ACS 2012, 5-Year
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
AgeOv18|NUMERIC|Total population at or over age 18|ACS 2018, 5-Year; 2010 Decennial Census
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
VetP|NUMERIC|Percent of population that are veterans|ACS 2017, 5-Year; ACS 2012, 5-Year
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)|ACS 2018, 5-Year; ACS 2012, 5-Year
TotPcp|INTEGER|Number of primary care providers in area|Dartmouth Atlas, 2010
TotSp|INTEGER|Number of specialty physicians in area|Dartmouth Atlas, 2010

### county-2015

ID: `oeps-391119.tabular.county-2015`

3 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020
DmySgrg|BOOLEAN|Dummy variable for whether county is part of a hypersegregated city or its metropolitan area|Massey et al, 2015

### county-2019

ID: `oeps-391119.tabular.county-2019`

6 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
NoIntP|NUMERIC|Percentage of Households without Internet access|ACS, 2019
RxCtTmDr|INTEGER|Number of tracts with pharmacy within a 30-min driving range|InfoGroup, 2019
RxAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest pharmacy.|InfoGroup, 2019
RxTmDrP|NUMERIC|Percent of tracts with pharmacy within a 30-min driving range|InfoGroup, 2019
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020

### county-2014

ID: `oeps-391119.tabular.county-2014`

2 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020

### state-2015

ID: `oeps-391119.tabular.state-2015`

12 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
HcvD|INTEGER|Total Hepatitis C deaths|HepVu, 2017
MlHcvD|INTEGER|Hepatitis C deaths among men|HepVu, 2017
FlHcvD|INTEGER|Hepatitis C deaths among women|HepVu, 2017
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations|HepVu, 2017
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations|HepVu, 2017
BlkHcvD|INTEGER|Hepatitis C deaths among Black population|HepVu, 2017
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations|HepVu, 2017
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age|HepVu, 2017
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age|HepVu, 2017
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age|HepVu, 2017
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020

### tract-2000

ID: `oeps-391119.tabular.tract-2000`

34 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
MetRm30|NUMERIC|Methadone access 30 minutes (RAAM)|
MetRm60|NUMERIC|Methadone access 60 minutes (RAAM)|
MetRm90|NUMERIC|Methadone access 90 minutes (RAAM)|

### county-2018

ID: `oeps-391119.tabular.county-2018`

78 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
TotPopHh|INTEGER|Total number of people in households|ACS 2018, 5-Year
TotVetPop|INTEGER|Total Veteran population|ACS 2018, 5-Year; ACS 2012, 5-Year
TotWrkE|INTEGER|Estimated count of working population|ACS 2018, 5-Year
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
AgeOv18|NUMERIC|Total population at or over age 18|ACS 2018, 5-Year; 2010 Decennial Census
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
VetP|NUMERIC|Percent of population that are veterans|ACS 2017, 5-Year; ACS 2012, 5-Year
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family|ACS 2018, 5-Year
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related|ACS 2018, 5-Year
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession|HUD, 2018
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession|HUD, 2018
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)|ACS 2018, 5-Year; ACS 2012, 5-Year
EduP|NUMERIC|Percentage of population employed in educational services industry|ACS 2018, 5-Year
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities|ACS 2018, 5-Year
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries|ACS 2018, 5-Year
RetailP|NUMERIC|Percentage of population employed in retail trade industry|ACS 2018, 5-Year
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.|ACS 2018, 5-Year
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.|ACS 2018, 5-Year
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures|ACS 2018, 5-Year
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago|ACS 2018, 5-Year
RentalP|NUMERIC|Percentage of occupied housing units that are rented|ACS 2018, 5-Year
UnitDens|NUMERIC|Number of housing units per square mile of land area|ACS 2018, 5-Year
AreaSqMi|NUMERIC|Land area of geography in sq miles|InfoGroup, 2018
AlcTot|INTEGER|Total number of alcohol outlets|InfoGroup, 2018
AlcDens|NUMERIC|Number of alcohol outlets per square mile|InfoGroup, 2018
AlcPerCap|NUMERIC|Number of alcohol outlets per capita|InfoGroup, 2018
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents|ACS 2018, 5-Year
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents|ACS 2018, 5-Year
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents|ACS 2018, 5-Year
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents|ACS 2018, 5-Year
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents|ACS 2018, 5-Year
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents|ACS 2018, 5-Year
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents|ACS 2018, 5-Year
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).|ACS 2018, 5-Year
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents|ACS 2018, 5-Year
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract|Sentinel-2 MSI, 2018
TotTracts|INTEGER|Total number of census tracts within the state.|Tiger/Line 2018
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic|CDC, 2018
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability|CDC, 2018
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language|CDC, 2018
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation|CDC, 2018
SviSmryRnk|NUMERIC|Overall summary ranking|CDC, 2018
RcaUrbanP|NUMERIC|Percent census tracts in the county classified as Urban using RUCA codes|USDA-ERS 2010 & ACS 2018 5-Year
RcaSubrbP|NUMERIC|Percent census tracts in the county classified as Suburban using RUCA codes|USDA-ERS 2010 & ACS 2018 5-Year
RcaRuralP|NUMERIC|Percent census tracts in the county classified as Rural using RUCA codes|USDA-ERS 2010 & ACS 2018 5-Year
CenFlags|STRING|Three different values indicating three things:
1 - Revised count, so urban and rural components will not add to total. 
2 - Geography name and FIPS code were changed since 2010. Shannon County, Sotuh Dakota name changed to Oglala Lakota County, new FIPS 46102. Wade Hampton Census Area, Alaska, name changed to Kusilvak CEnsus Area, nwe FIPS 02158
3 - Bedford City, Virginia, was consolidated with Bedford County, Virginia (FIPS 51019) since 2010.|USDA-ERS 2010 & ACS 2018 5-Year
CenRuralP|NUMERIC|% of 2010 Population living in non urban areas, as defined by Census Bureau|USDA-ERS 2010 & ACS 2018 5-Year

### county-2016

ID: `oeps-391119.tabular.county-2016`

6 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020
TtlPrPpr|NUMERIC|Total Prison Population Rate|Vera Institute of Justice, 2016
TtlPrAPpr|NUMERIC|Prison Prison Admissions Rate|Vera Institute of Justice, 2016
TtlPrPp|INTEGER|Total Prison Population Count|Vera Institute of Justice, 2016
TtlPrAPp|INTEGER|Prison Prison Admissions Count|Vera Institute of Justice, 2016

### state-2020

ID: `oeps-391119.tabular.state-2020`

26 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
CntBupT|INTEGER|Number of tracts with buprenorphine provider within a 30-min driving range|SAMSHA, 2019; Vivitrol, 2020; OSRM, 2020
CntMetT|INTEGER|Number of tracts with methadone provider within a 30-min driving range|SAMSHA, 2019; Vivitrol, 2020; OSRM, 2020
CntNalT|INTEGER|Number of tracts within 30 -min of naltrexone driving range|SAMSHA, 2019; Vivitrol, 2020; OSRM, 2020
AvBupTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest buprenorphine provider.|SAMSHA, 2019; Vivitrol, 2020; OSRM, 2020
AvMetTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest methadone provider.|SAMSHA, 2019; Vivitrol, 2020; OSRM, 2020
AvNalTime|NUMERIC|Average driving time (minutes) across tracts in state to nearest naltrexone provider.|SAMSHA, 2019; Vivitrol, 2020; OSRM, 2020
PctBupT|NUMERIC|Percent of tracts with buprenorphine provider within a 30-min driving range|SAMSHA, 2019; Vivitrol, 2020; OSRM, 2020
PctMetT|NUMERIC|Percent of tracts with methadone provider within a 30-min driving range|SAMSHA, 2019; Vivitrol, 2020; OSRM, 2020
PctNalT|NUMERIC|Percent of tracts with naltrexone provider within a 30-min driving range|SAMSHA, 2019; Vivitrol, 2020; OSRM, 2020
FqhcCtTmDr|INTEGER|Number of tracts with Federally Qualified Health Center within a 30-min driving range|US Covid Atlas via HRSA, 2020
FqhcAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Federally Qualified Health Center|US Covid Atlas via HRSA, 2020
FqhcTmDrP|NUMERIC|Percent of tracts with Federally Qualified Health Center within a 30-min driving range.|US Covid Atlas via HRSA, 2020
HospCtTmDr|INTEGER|Number of tracts with hospital within a 30-min driving range|CovidCareMap, 2020
HospAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest hospital.|CovidCareMap, 2020
HospTmDrP|NUMERIC|Percent of tracts with hospital within a 30-mini driving range|CovidCareMap, 2020
MhCtTmDr|INTEGER|Number of tracts with a mental health provider within a 30-min driving range.|SAMHSA, 2020
MhAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest mental health provider.|SAMHSA, 2020
MhTmDrP|NUMERIC|Percent of tracts with a mental health provider within a 30-min driving range.|SAMHSA, 2020
SutpCtTmDr|INTEGER|Number of tracts with Substance Use Treatment within a 30-min driving range.|SAMHSA, 2020
SutpAvTmDr|NUMERIC|Average driving time (minutes) across tracts in state to nearest Substance Use Treatment program.|SAMHSA, 2020
SutpTmDrP|NUMERIC|Percent of tracts with Substance Use Treatment program within a 30-minute driving range.|SAMHSA, 2020
OpRxRt|NUMERIC|Opioid prescription rate|HepVu, 2020
PrMsuseP|NUMERIC|Percent of persons who self-report misusing prescription pain relief medication in 2020.|HepVu, 2020
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020
OdMortRtAv|NUMERIC|Average overdose mortality rate from 2016-2020|HepVu, 2020

### county-2017

ID: `oeps-391119.tabular.county-2017`

9 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020
PrcNtvRsrv|NUMERIC|Percentage of county land area that belongs to Native American reservation(s)|TIGER/Line 2017
TtlJlPpr|NUMERIC|Total Jail Population Rate, ASJ/COJ Data|Vera Institute of Justice, 2017
TtlJlAdmr|NUMERIC|Total Jail Admissions Rate, ASJ/COJ Data|Vera Institute of Justice, 2017
TtlJlPrtr|NUMERIC|Pretrial Jail Population Rate|Vera Institute of Justice, 2017
TtlJlPp|NUMERIC|Total Jail Population Count, ASJ/COJ Data|Vera Institute of Justice, 2017
TtlJlAdm|NUMERIC|Total Jail Admissions Count, ASJ/COJ Data|Vera Institute of Justice, 2017
TtlJlPrt|NUMERIC|Pretrial Jail Population Count|Vera Institute of Justice, 2017

### state-2000

ID: `oeps-391119.tabular.state-2000`

31 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year

### state-2021

ID: `oeps-391119.tabular.state-2021`

4 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
OtpCtTmDr|INTEGER|Number of tracts within 30-min of opioid treatment program driving range|SAMSHA, 2021
OtpAvTmDr|NUMERIC|Average driving time (minutes) across tracts to nearest opioid treatment program.|SAMSHA, 2021
OtpTmDrP|NUMERIC|Percent of tracts within a 30-minute drive time of an opioid treatment program.|SAMSHA, 2021

### zcta-2018

ID: `oeps-391119.tabular.zcta-2018`

72 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
TotPopHh|INTEGER|Total number of people in households|ACS 2018, 5-Year
TotVetPop|INTEGER|Total Veteran population|ACS 2018, 5-Year; ACS 2012, 5-Year
TotWrkE|INTEGER|Estimated count of working population|ACS 2018, 5-Year
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
AgeOv18|NUMERIC|Total population at or over age 18|ACS 2018, 5-Year; 2010 Decennial Census
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
VetP|NUMERIC|Percent of population that are veterans|ACS 2017, 5-Year; ACS 2012, 5-Year
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family|ACS 2018, 5-Year
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related|ACS 2018, 5-Year
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)|ACS 2018, 5-Year; ACS 2012, 5-Year
EduP|NUMERIC|Percentage of population employed in educational services industry|ACS 2018, 5-Year
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities|ACS 2018, 5-Year
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries|ACS 2018, 5-Year
RetailP|NUMERIC|Percentage of population employed in retail trade industry|ACS 2018, 5-Year
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.|ACS 2018, 5-Year
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.|ACS 2018, 5-Year
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures|ACS 2018, 5-Year
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago|ACS 2018, 5-Year
RentalP|NUMERIC|Percentage of occupied housing units that are rented|ACS 2018, 5-Year
UnitDens|NUMERIC|Number of housing units per square mile of land area|ACS 2018, 5-Year
AreaSqMi|NUMERIC|Land area of geography in sq miles|InfoGroup, 2018
AlcTot|INTEGER|Total number of alcohol outlets|InfoGroup, 2018
AlcDens|NUMERIC|Number of alcohol outlets per square mile|InfoGroup, 2018
AlcPerCap|NUMERIC|Number of alcohol outlets per capita|InfoGroup, 2018
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents|ACS 2018, 5-Year
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents|ACS 2018, 5-Year
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents|ACS 2018, 5-Year
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents|ACS 2018, 5-Year
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents|ACS 2018, 5-Year
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents|ACS 2018, 5-Year
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents|ACS 2018, 5-Year
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).|ACS 2018, 5-Year
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents|ACS 2018, 5-Year
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract|Sentinel-2 MSI, 2018
Ruca1|STRING|Primary RUCA Code|USDA-ERS 2010 & ACS 2018 5-Year
Ruca2|STRING|Secondary RUCA Code|USDA-ERS 2010 & ACS 2018 5-Year
Rurality|STRING|Urban/Suburban/Rural|USDA-ERS 2010 & ACS 2018 5-Year
SviTh1|NUMERIC|SVI Ranking, Theme 1: Socioeconomic|CDC, 2018
SviTh2|NUMERIC|SVI Ranking, Theme 2: Household Composition & Disability|CDC, 2018
SviTh3|NUMERIC|SVI Ranking, Theme 3: Minority Status & Language|CDC, 2018
SviTh4|NUMERIC|SVI Ranking, Theme 4: Housing Type & Transportation|CDC, 2018
SviSmryRnk|NUMERIC|Overall summary ranking|CDC, 2018
A15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS

### county-2010

ID: `oeps-391119.tabular.county-2010`

43 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
TotVetPop|INTEGER|Total Veteran population|ACS 2018, 5-Year; ACS 2012, 5-Year
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
VetP|NUMERIC|Percent of population that are veterans|ACS 2017, 5-Year; ACS 2012, 5-Year
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)|ACS 2018, 5-Year; ACS 2012, 5-Year
TotPcp|INTEGER|Number of primary care providers in area|Dartmouth Atlas, 2010
TotSp|INTEGER|Number of specialty physicians in area|Dartmouth Atlas, 2010
PcpPer100k|NUMERIC|PCPs per total Population X 100,000|Dartmouth Atlas, 2010
SpPer100k|NUMERIC|Specialty Physicians per total Population X 100,000|Dartmouth Atlas, 2010
TotPop10|INTEGER|2010 total population|USDA-ERS 2010 & ACS 2018 5-Year
UrbPop|INTEGER|2010 Population living in urban areas, as defined by Census Bureau|USDA-ERS 2010 & ACS 2018 5-Year
RuralPop|INTEGER|2010 Population living in non urban areas, as defined by Census Bureau|USDA-ERS 2010 & ACS 2018 5-Year

### state-2018

ID: `oeps-391119.tabular.state-2018`

86 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
TotPopHh|INTEGER|Total number of people in households|ACS 2018, 5-Year
TotVetPop|INTEGER|Total Veteran population|ACS 2018, 5-Year; ACS 2012, 5-Year
TotWrkE|INTEGER|Estimated count of working population|ACS 2018, 5-Year
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
AgeOv18|NUMERIC|Total population at or over age 18|ACS 2018, 5-Year; 2010 Decennial Census
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
VetP|NUMERIC|Percent of population that are veterans|ACS 2017, 5-Year; ACS 2012, 5-Year
NonRelFhhP|NUMERIC|Percent of people living in family households that are not related to family|ACS 2018, 5-Year
NonRelNfhhP|NUMERIC|Percent of people living in non-family households that are not related|ACS 2018, 5-Year
MedInc|INTEGER|Median income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
PciE|INTEGER|Per capita income for individuals in the past 12 months (in 2018 inflation-adjusted dollars)|ACS 2018, 5-Year; ACS 2012, 5-Year
ForDqP|NUMERIC|Estimated percent of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession|HUD, 2018
ForDqTot|NUMERIC|Estimated number of mortgages to start foreclosure process or be seriously delinquent during the 2008 Recession|HUD, 2018
GiniCoeff|NUMERIC|Income Inequality (Gini Coefficient)|ACS 2018, 5-Year; ACS 2012, 5-Year
EduP|NUMERIC|Percentage of population employed in educational services industry|ACS 2018, 5-Year
HghRskP|NUMERIC|Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying, oil and gas extraction, construction, manufacturing, utilities|ACS 2018, 5-Year
HltCrP|NUMERIC|Percentage of population employed in health care and social assistance industries|ACS 2018, 5-Year
RetailP|NUMERIC|Percentage of population employed in retail trade industry|ACS 2018, 5-Year
EssnWrkE|INTEGER|Estimated count of population employed in essential occupations.|ACS 2018, 5-Year
EssnWrkP|NUMERIC|Percentage of population employed in essential occupations.|ACS 2018, 5-Year
MobileP|NUMERIC|Percentage of total housing units categorized as mobile housing structures|ACS 2018, 5-Year
LngTermP|NUMERIC|Percentage of population who moved into their current housing more than 20 years ago|ACS 2018, 5-Year
RentalP|NUMERIC|Percentage of occupied housing units that are rented|ACS 2018, 5-Year
UnitDens|NUMERIC|Number of housing units per square mile of land area|ACS 2018, 5-Year
AreaSqMi|NUMERIC|Land area of geography in sq miles|InfoGroup, 2018
AlcTot|INTEGER|Total number of alcohol outlets|InfoGroup, 2018
AlcDens|NUMERIC|Number of alcohol outlets per square mile|InfoGroup, 2018
AlcPerCap|NUMERIC|Number of alcohol outlets per capita|InfoGroup, 2018
DsmBlk|NUMERIC|Dissimilarity index for Black and non-Hispanic White residents|ACS 2018, 5-Year
IntrBlkWht|NUMERIC|Interaction index for Black and non-Hispanic White residents|ACS 2018, 5-Year
IsoBlk|NUMERIC|Isolation index for Black and non-Hispanic White residents|ACS 2018, 5-Year
DsmHsp|NUMERIC|Dissimilarity index for Hispanic and non-Hispanic White residents|ACS 2018, 5-Year
IntrHspWht|NUMERIC|Interaction index for Hispanic and non-Hispanic White residents|ACS 2018, 5-Year
IsoHsp|NUMERIC|Isolation index for Hispanic and non-Hispanic White residents|ACS 2018, 5-Year
DsmAs|NUMERIC|Dissimilarity index for Asian and non-Hispanic White residents|ACS 2018, 5-Year
IntrAsWht|NUMERIC|Area (in square meters) of park or green space in a state).|ACS 2018, 5-Year
IsoAs|NUMERIC|Isolation index for Asian and non-Hispanic White residents|ACS 2018, 5-Year
Ndvi|NUMERIC|Average normalized difference vegetation index, a measure of greenness used to determine the amount of vegetation in an area, value from all pixel values in each Census tract|Sentinel-2 MSI, 2018
StateArea|NUMERIC|Area (in square meters) of state|Tiger/Line 2018
TotTracts|INTEGER|Total number of census tracts within the state.|Tiger/Line 2018
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020
MedcdExp|INTEGER|Total medicaid spending|KFF, 2019
TradFedExp|INTEGER|Traditional medicaid - federal spending|KFF, 2018
TradSttExp|INTEGER|Traditional medicaid - state spending|KFF, 2018
ExpnFedExp|INTEGER|Expansion Group - Federal Spending|KFF, 2018
ExpnSttExp|INTEGER|Expansion Group - State Spending|KFF, 2018
CrrctExpS|INTEGER|Expenditures on corrections system and operation by the State alone|US Census, 2018
PlcFyrExpS|INTEGER|Expenditures on police and fire protection by the State alone|US Census, 2018
HlthExpS|INTEGER|Expenditures on public health and hospitals by the State alone|US Census, 2018
WlfrExpS|INTEGER|Expenditures on public welfare progrmas by the State alone|US Census, 2018
CrrctExpL|INTEGER|Expenditures on corrections system and operation by local governments alone|US Census, 2018
PlcFyrExpL|INTEGER|Expenditures on police and fire protection by the local government alone|US Census, 2018
HlthExpL|INTEGER|Expenditures on public health and hospitals by the local government alone|US Census, 2018
WlfrExpL|INTEGER|Expenditures on public welfare progrmas by the local government alone|US Census, 2018
CrrctExpT|INTEGER|Total expenditures on corrections system and operations|US Census, 2018
PlcFyrExpT|INTEGER|Total expenditures on police and fire protection|US Census, 2018
HlthExpT|INTEGER|Total expenditures on public health and welfare|US Census, 2018
WlfrExpT|INTEGER|Total expenditures on public welfare programs|US Census, 2018

### state-2013

ID: `oeps-391119.tabular.state-2013`

11 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
HcvD|INTEGER|Total Hepatitis C deaths|HepVu, 2017
MlHcvD|INTEGER|Hepatitis C deaths among men|HepVu, 2017
FlHcvD|INTEGER|Hepatitis C deaths among women|HepVu, 2017
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations|HepVu, 2017
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations|HepVu, 2017
BlkHcvD|INTEGER|Hepatitis C deaths among Black population|HepVu, 2017
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations|HepVu, 2017
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age|HepVu, 2017
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age|HepVu, 2017
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age|HepVu, 2017

### state-2014

ID: `oeps-391119.tabular.state-2014`

12 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
HcvD|INTEGER|Total Hepatitis C deaths|HepVu, 2017
MlHcvD|INTEGER|Hepatitis C deaths among men|HepVu, 2017
FlHcvD|INTEGER|Hepatitis C deaths among women|HepVu, 2017
AmInHcvD|INTEGER|Hepatitis C deaths among American Indian populations|HepVu, 2017
AsPiHcvD|INTEGER|Hepatitis C deaths among Asian and Pacific Islander populations|HepVu, 2017
BlkHcvD|INTEGER|Hepatitis C deaths among Black population|HepVu, 2017
HspHcvD|INTEGER|Hepatitis C deaths among hispanic populations|HepVu, 2017
U50HcvD|INTEGER|Hepatitis C deaths in populations under 50 years of age|HepVu, 2017
A50_74HcvD|INTEGER|Hepatitis C deaths among populations between 50 and 74 years of age|HepVu, 2017
O75HcvD|INTEGER|Hepatitis C deaths among populations over 75 years of age|HepVu, 2017
OdMortRt|NUMERIC|Overdose mortality rate|HepVu, 2020

### zcta-2019

ID: `oeps-391119.tabular.zcta-2019`

5 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
NoIntP|NUMERIC|Percentage of Households without Internet access|ACS, 2019
RxMinDis|NUMERIC|Euclidean distance* from tract/zip centroid to nearest pharmacy, in miles|InfoGroup, 2019
RxTmDr|NUMERIC|Driving time from tract/zip origin centroid to the nearest tract/zip pharmacy destination centroid, in minutes|InfoGroup, 2019
RxCntDr|INTEGER|Count of pharmacies within a 30-minute driving threshold|InfoGroup, 2019

### tract-2014

ID: `oeps-391119.tabular.tract-2014`

5 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
SocEcAdvIn|NUMERIC|Raw Socioeconomic Advantage Index (https://sdohatlas.github.io/)|GeoDa Data and Lab; SDOH Atlas
LimMobInd|NUMERIC|Raw Limited Mobility Index (https://sdohatlas.github.io/)|GeoDa Data and Lab; SDOH Atlas
UrbCoreInd|NUMERIC|Raw Urban Core Opportunity Index (https://sdohatlas.github.io/)|GeoDa Data and Lab; SDOH Atlas
MicaInd|NUMERIC|Raw Mixed Immigrant Cohesion and Accessibility (MICA) Index (https://sdohatlas.github.io/)|GeoDa Data and Lab; SDOH Atlas

### county-2000

ID: `oeps-391119.tabular.county-2000`

32 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|A derived unique id corresponding to the relevant geographic unit.|Healthy Regions & Policies Lab, UIUC
GEOID|STRING|Unique identifer for the geography unit to which this value should be attached|Tiger/Line 2018; Tiger/Line 2010
TotPop|INTEGER|Total population|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
TotUnits|INTEGER|Count of total occupied housing units|ACS 2018, 5-Year; Census 2010; Social Explorer
Age18_64|INTEGER|Total adult population under age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age0_4|INTEGER|Total population between age 0-4|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age5_14|INTEGER|Total population between age 5-14|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_19|INTEGER|Total population between age 15-19|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age20_24|INTEGER|Total population between age 20-24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_44|INTEGER|Total population between age 15-44|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age55_59|INTEGER|Total population between age 55-59|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age60_64|INTEGER|Total population between age 60-64|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AgeOv65|INTEGER|Total population at or over age 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Age15_24P|NUMERIC|Percentage of population between ages of 15 & 24|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Und45P|NUMERIC|	Percentage of population below 45 years of age|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
Ovr65P|NUMERIC|Percentage of population over 65|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
WhiteP|NUMERIC|Percentage of population with race identified as white alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
BlackP|NUMERIC|Percentage of population with race identified as Black or African American alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
HispP|NUMERIC|Percentage of population with ethnicity identified as of Hispanic or Latinx origin|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AmIndP|NUMERIC|Percentage of population with race identified as Native American or Alaska Native alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
AsianP|NUMERIC|Percentage of population with race identified as Asian alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PacIsP|NUMERIC|Percentage of population with race identified as Native Hawaiian and Other Pacific Islander alone|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
OtherP|NUMERIC|Percentage of Population with race not mentioned in any of the options above (includes two race or more races)|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
NoHsP|NUMERIC|Percentage of population 25 years and over, less than a high school degree|ACS 2018, 5-Year; ACS 2012, 5-Year; IPUMS NHGIS
ChildrenP|NUMERIC|Percentage of population under age 18|ACS 2018, 5-Year; Census 2010; IPUMS NHGIS
PovP|NUMERIC|Number of individuals earning below the poverty income threshold as a percentage of the total population|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
UnempP|NUMERIC|The number of unemployed individuals as a percentage of the civilian labor force|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
VacantP|NUMERIC|Percentage of vacant housing units|ACS 2018, 5-Year; ACS 2012, 5-Year; Social Explorer
Age45_49|INTEGER|Total population between age 45-49|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
Age50_54|NUMERIC|Total population between age 50-54|ACS 2018, 5-Year; 2010 Decennial Census; IPUMS NHGIS
DisbP|NUMERIC|Percentage of civilian non institutionalized population with a disability|ACS 2018, 5-Year; ACS 2012, 5-Year
DmyBlckBlt|BOOLEAN|Dummy variable for whether county is in the Southern Black Belt region|US Census, 2000

## spatial

7 tables in this dataset.

### counties2010

ID: `oeps-391119.spatial.counties2010`

2 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|None|None
name|STRING|None|None

### states2018

ID: `oeps-391119.spatial.states2018`

2 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|None|None
name|STRING|None|None

### zctas2018

ID: `oeps-391119.spatial.zctas2018`

1 column in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|None|None

### states2010

ID: `oeps-391119.spatial.states2010`

2 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|None|None
name|STRING|None|None

### tracts2010

ID: `oeps-391119.spatial.tracts2010`

1 column in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|None|None

### counties2018

ID: `oeps-391119.spatial.counties2018`

2 columns in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|None|None
name|STRING|None|None

### tracts2018

ID: `oeps-391119.spatial.tracts2018`

1 column in this table.

Name|Data Type|Description|Source
-|-|-|-
HEROP_ID|STRING|None|None

