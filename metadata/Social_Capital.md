**Metadata Name**:   Social Capital Index
**Date Added**:   October 30, 2025
**Author**: Catherine Discenza  
**Last Modified By**: Catherine Discenza
**Date Last Modified**: December 8, 2025

### Data Source(s) Description

Population and housing variables were obtained from 2018 and 2023 5-year American Community Survey (ACS) at County and/or Tract levels.

Library and religious institution data were obtained from Overture Maps Foundation. 

### Description of Data Source Tables

**ACS**

**Table B25026**: Total population in occupied housing units by tenue by year householder moved into unit

**Overture**

**Libraries**: library

**Religious Instituions**: anglican_church; baptist_church; catholic_church; church_cathedral; episcopal_church; evangelical_church; pentecostal_church; buddhist_temple; hindu_temple; sikh_temple; religious_destination; religious_items; religious_organization; religious_school; jehovahs_witness_kingdom_hall; mosque; synagogue

### Description of Data Processing
 
The following variables were included from **2018 5-year ACS B25026**:
  1. Estimate; Total population in occupied housing units
  3. Estimate; Owner occupied: Moved in 2017 or later
  4. Estimate; Owner occupied: Moved in 2015 to 2016
  5. Estimate; Owner occupied: Moved in 2010 to 2014
  6. Estimate; Owner occupied: Moved in 2000 to 2009
  7. Estimate; Owner occupied: Moved in 1990 to 1999
  8. Estimate; Owner occupied: Moved in 1989 or earlier
  10. Estimate; Renter occupied: Moved in 2017 or later
  11. Estimate; Renter occupied: Moved in 2015 to 2016
  12. Estimate; Renter occupied: Moved in 2010 to 2014
  13. Estimate; Renter occupied: Moved in 2000 to 2009
  14. Estimate; Renter occupied: Moved in 1990 to 1999
  15. Estimate; Renter occupied: Moved in 1989 or earlier

The following variables were included from **2023 5-year ACS B25026**:
  1. Estimate; Total population in occupied housing units
  3. Estimate; Owner occupied: Moved in 2021 or later
  4. Estimate; Owner occupied: Moved in 2018 to 2020
  5. Estimate; Owner occupied: Moved in 2010 to 2017
  6. Estimate; Owner occupied: Moved in 2000 to 2009
  7. Estimate; Owner occupied: Moved in 1990 to 1999
  8. Estimate; Owner occupied: Moved in 1989 or earlier
  10. Estimate; Renter occupied: Moved in 2021 or later
  11. Estimate; Renter occupied: Moved in 2018 to 2020
  12. Estimate; Renter occupied: Moved in 2010 to 2017
  13. Estimate; Renter occupied: Moved in 2000 to 2009
  14. Estimate; Renter occupied: Moved in 1990 to 1999
  15. Estimate; Renter occupied: Moved in 1989 or earlier

---------- 

* **Long-term occupancy rate** was calculated as : *(Owner & renter populations moved in before 1989 + Owner & renter population moved in between 1990 & 1999) / (Total population in owner & renter occupied units) * 100*

* **2018 5-year ACS Median occupancy rate** was calculated as : *=IF((Owner  & renter populations moved in 2017 or later)>=(Total population in occupied housing units/2),THEN(Moved in 2017 or later),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016)>=(Total population in occupied housing units/2),THEN(Moved in 2015 to 2016),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016 + Owner & renter populations moved in 2010 to 2014)>=(Total population in occupied housing units/2),THEN(Moved in 2010 to 2014),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016 + Owner & renter populations moved in 2010 to 2014 + Owner & renter populations moved in 2000 to 2009)>=(Total population in occupied housing units/2),THEN(Moved in 2000 to 2009),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016 + Owner & renter populations moved in 2010 to 2014 + Owner & renter populations moved in 2000 to 2009 + Owner & renter populations moved in 1990 to 1999)>=(Total population in occupied housing units/2),THEN(Moved in 1990 to 1999),IF((Owner  & renter populations moved in 2017 or later + Owner  & renter populations moved in 2015 to 2016 + Owner & renter populations moved in 2010 to 2014 + Owner & renter populations moved in 2000 to 2009 + Owner & renter populations moved in 1990 to 1999 + Ownder & renter populaiton moved in before 1989)>=(Total population in occupied housing units/2),THEN(Moved in 1989 or earlier)))))))*

* **2023 5-year ACS Median occupancy rate** was calculated as : *=IF((Owner  & renter populations moved in 2021 or later)>=(Total population in occupied housing units/2),THEN(Moved in 2021 or later),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020)>=(Total population in occupied housing units/2),THEN(Moved in 2018 to 2020),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020 + Owner & renter populations moved in 2010 to 2017)>=(Total population in occupied housing units/2),THEN(Moved in 2010 to 2017),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020 + Owner & renter populations moved in 2010 to 2017 + Owner & renter populations moved in 2000 to 2009)>=(Total population in occupied housing units/2),THEN(Moved in 2000 to 2009),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020 + Owner & renter populations moved in 2010 to 2017 + Owner & renter populations moved in 2000 to 2009 + Owner & renter populations moved in 1990 to 1999)>=(Total population in occupied housing units/2),THEN(Moved in 1990 to 1999),IF((Owner  & renter populations moved in 2021 or later + Owner  & renter populations moved in 2018 to 2020 + Owner & renter populations moved in 2010 to 2017 + Owner & renter populations moved in 2000 to 2009 + Owner & renter populations moved in 1990 to 1999 + Ownder & renter populaiton moved in before 1989)>=(Total population in occupied housing units/2),THEN(Moved in 1989 or earlier)))))))*

* **Libraries per capita** was calculated as : *(Number of libraries in tract) / (Total population in owner & renter occupied units)*

* **Religious institutions per capita** was calculated as : *(Number of religious institutions in tract) / (Total population in owner & renter occupied units)*

* **Social Capital Index** was calculated as : LngTermP, LibPerCap, RlgPerCap all standardized to a z-score, equally weighted and summed *=0.33(LngTermPZ) + 0.33(LibPerCapZ) + 0.33RlgPerCapZ)*

Note: Unpopulated census tracts removed from dataset.

### Data Limitations

- The ACS does not gather information in the U.S. territories American Samoa, Guam, Northern Mariana Islands and U.S. Virgin Islands. It does include information for Puerto Rico & Washington, D.C.
- Overture Maps Foundation began data releases in 2024, no data specific to 2018 and 2023 is available. 2025 data was extracted for completeness and applied to both 2018 and 2023 data.
  
### Comments/Notes

- Unpopulated census tracts removed from dataset


