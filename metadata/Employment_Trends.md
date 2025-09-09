**Meta Data Name**: Employment Trends
**Date Added**: October 22, 2020  
**Author**: Adam Cox, Marynia Kolak, Wataru Morioka, Moksha Menghaney & Qinyun Lin
**Date Last Modified**: September 9, 2025
**Last Modified By**: Adam Cox

### Theme:
Economic

### Data Location: 
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.

### Data Source(s) Description:  
Variables were obtained from the multiple periods of the [American Community Survey (ACS)](https://data.census.gov) at State, County, Tract and ZIP Code Tabulation Area (ZCTA) levels.

The definition of **"essential jobs"** included in this dataset comes from [Chicago Metropolitan Agency for Planning (CMAP)](https://github.com/CMAP-REPOS/essentialworkers). 

### Description of Data Source Tables:

- **Table S2401**: Occupation by sex for the civilian employed population 16 years and over
- **Table DP03**: Selected Economic Characteristics
- **Table S2403**: Industry by sex for the civilian employed population 16 years and over

### Description of Data Processing: 

#### Unemployment Definition
The following variables were included from **DP03**:
  * **Percent estimate; Unemployment Rate**. The unemployment rate represents the number of unemployed individuals as a percentage of the civilian labor force. 

#### Essential Workers Definition
All essential worker variables were included from S2401. The following variables were identified as essential workers for 2018 as our baseline, then replicated in subsequent time periods:  

S2401_C01_011, S2401_C01_016, S2401_C01_017, S2401_C01_019, S2401_C01_021, S2401_C01_022, S2401_C01_023, S2401_C01_024, S2401_C01_030, S2401_C01_031, S2401_C01_032, S2401_C01_034, S2401_C01_035, S2401_C01_036

See [CMAP](https://github.com/CMAP-REPOS/essentialworkers) for a more detailed description of essential jobs. 

----------

* Percentage of population employed in Essential Jobs was calculated as:  

	*Sum of the workers employed in (<br> 
                 - Community and social service occupations, <br>
                 - Health diagnosing and treating practitioners, Health technologists and technicians, and other technical occupations,<br>
                 - Healthcare support occupations,<br>
                 - Protective service occupations,<br>
                 - Food preparation and serving related occupations,<br>
                 - Building and grounds cleaning and maintenance occupations,<br>
                 - Farming, fishing, and forestry occupations,<br>
                 - Construction and extraction occupations,<br>
                 - Installation, maintenance, and repair occupations,<br>
                 - Production, <br>
                 - Transportation and material moving occupations) / (Total Civilian employed population 16 years and over)*

#### Jobs by Industry Definition

All variables were included from S2403 (2018):

* High risk of injury jobs - S2403_C01_003, S2403_C01_004, S2403_C01_005, S2403_C01_006, and S2403_C01_011  
* Education jobs - S2403_C01_021 
* Health care jobs - S2403_C01_022  
* Retail jobs - S2403_C01_008  

----------
* Percentage of population employed in High Risk of Injury Jobs was calculated as : 
*Sum of the workers employed in (<br> 
		- Agriculture, forestry, fishing and hunting, <br>
		- Mining, quarrying, and oil and gas extraction,<br>
		- Construction,<br>
		- Manufacturing,<br>
		- Utilities) / (Total Civilian employed population 16 years and over)*

* Percentage of population employed in Educations Jobs was calculated as : <br>
*Sum of the workers employed in Educational services / (Total Civilian employed population 16 years and over)*
	
* Percentage of population employed in HealthCare Jobs was calculated as : <br>
*Sum of the workers employed in Health care and social assistance/ (Total Civilian employed population 16 years and over)*

* Percentage of population employed in Retail Jobs was calculated as : <br>
*Sum of the workers employed in Retail trade / (Total Civilian employed population 16 years and over)* 

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Unemployment Rate | UnempP | The number of unemployed individuals as a percentage of the civilian labor force | 1980, 1990, 2000, 2010, 2018, 2023 | Tract, Zip* County, State |
| Count of Essential Workers | EssnWrkE | Estimated count of Population Employed in Essential Occupations (outlined above) | 2018, 2023 | Tract, Zip, County, State |
| % Essential Workers  | EssnWrkP | Percentage of Population Employed in Essential Occupations (outlined above) | 2018, 2023 | Tract, Zip, County, State |
| Total Count of Workers | TotWrkE | Estimated count of working population | 2018, 2023 | Tract, Zip, County, State |
| % Education Jobs  | EduP | Percentage of population employed in educational services industry | 2018, 2023 | Tract, Zip, County, State |
| % High Risk of Injury Jobs  | HghRskP | Percentage of population employed in following industries: agriculture, forestry, fishing and hunting, mining, quarrying,  oil and gas extraction, construction, manufacturing, utilities | 2018, 2023 | Tract, Zip, County, State |
| % Health Care Jobs | HltCrP | Percentage of population employed in health care and social assistance industries | 2018, 2023 | Tract, Zip, County, State |
| % Retail Jobs  | RetailP | Percentage of population employed in retail trade industry | 2018, 2023 | Tract, Zip, County, State |

### Data Limitations:
Please note this dataset uses "occupation" and "industry" as classifiers and does not include any information about the occupation or industry to which a job belongs. This can lead to an overestimation of Essential Workers and High Risk to Injury categories.

### Comments/Notes:

**Note on missing data:** Missing and/or unavailable data are coded as blank/empty cells.
