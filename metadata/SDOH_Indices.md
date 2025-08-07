**Meta Data Name**: Social Determinants of Health (SDOH) Multivariate Estimates 
**Date Added**: March 4, 2021  
**Author**: Marynia Kolak, Qinyun Lin  
**Date Last Modified**: August 5, 2025
**Last Modified By**: Marynia Kolak

### Theme: 
Composite

### Data Location: 
You can find the variables described in this document in the CSV files [here](https://oeps.healthyregions.org/download).  

CSV files are organized by **year** and **spatial scale**. For example, county-level variables from 2000 will be found in C_2000.csv.  
Note: Every variable can be found in the **Latest** files.

### Data Source(s) Description:  
Original measures were from the 2014 5-Yr ACS Estimates, including fourteen factors of SDOH. Explore the paper for more details: 
Kolak, Marynia, Bhatt, Jay, Park, Yoon Hong, Padron, Norma, and Molefe, Ayrin. "Quantification of Neighborhood-Level Social Determinants of Health in the Continental United States." *JAMA Network Open.* 2020;3(1):e1919928. doi:10.1001/jamanetworkopen.2019.19928 

### Description of Data Processing: 
Measures were estimated for populated census tract for the continental U.S.. Final indices were generated using a principal component analysis; the typology was estimated with a K-Means Clustering Analysis. The full description of data analyses can be found in the linked paper above.

### Key Variable and Definitions:

- **Variable** -- title of variable
- **Variable ID** -- exact name of variable in datasets
- **Description** -- Short description of variable
- **Years Available** -- years for which data exists for this variable
- **Spatial Scale** -- the variable exists for these levels of spatial scale

| Variable | Variable ID in .csv | Description | Years Available | Spatial Scale |
|:---------|:--------------------|:------------|:----------------|:--------------|
| Socioeconomic Advantage Index | SocEcAdvIn | Driven by classic measures of socioeconomic advantage, like poverty, minority status, health insurance status, single parent households, and educational level. The strong correlation between minority status and poverty may reflect the role that racial segregation has played in perpetuating environments that are associated with health disparities. Lower values have more disadvantage; high values have more advantage. Lower values have more disadvantage; high values have more advantage. | 2014 | Tract |
| Limited Mobility Index | LimMobInd | Driven by areas with high proportions of seniors and persons with disabilities, and fewer children Reduced mobility issues are factors in both resource accessibility and social isolation needs, and reflect complex interactions between aging, disability, and transit. Ongoing research seeks to identify areas with a high concentration of older populations to improve transportation policy, social service facilities, and planning. Lower values have less mobility; high values have more mobility. | 2014 | Tract |
| Urban Core Opportunity Index | UrbCoreInd | Dominated by population-dense areas with higher per capita income, more renters, higher rent burden, households without a vehicle, and fewer children. Characterized by compact geographies, dense urban centers, and strong economies. May be highly walkable and diverse, but higher cost of living may impact the vulnerable disportionately. Lower values have less opportunity; high values have more opportunity. | 2014 | Tract |
| Mixed Immigrant Cohesion & Accessibility | MicaInd | Mostly immigrant or multilingual groups with traditional family structures and multiple accessibility stressors. Dominated by higher proportions of families with limited English proficiency, older adults and crowded housing, lack of health insurance, lower educational attainment, and fewer single parent households. Lower values have more multilingual families, traditional family structures, and/or accessibility stressors. | 2014 | Tract |
| SDOH Neighborhood Typology | NeighbTyp | Categorical, one of seven neighborhood (tract-level) typologies: 1 = Rural Affordable; 2 = Suburban Affluent; 3 = Suburban Affordable; 4 = Extreme Poverty; 5 = Multilingual Working; 6 = Urban Core Opportunity; 7 = Sparse Areas | 2014 | Tract |


### Data Limitations:
Measures are only provided for populated census tracts with all original measures provided, for the continental U.S. See original paper for details.

### Comments/Notes:
* See Kolak, Marynia, Bhatt, Jay, Park, Yoon Hong, Padron, Norma, and Molefe, Ayrin. "Quantification of Neighborhood-Level Social Determinants of Health in the Continental United States." *JAMA Network Open.* 2020;3(1):e1919928. doi:10.1001/jamanetworkopen.2019.19928 for more detailed information. 
* See [SDOH Atlas](https://sdohatlas.github.io/) for visualizations.  
* **Note on missing data:** Missing and/or unavailable data are represented as blank cells or _NA._
