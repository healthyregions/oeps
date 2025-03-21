
# Set the working directory to the specified path
setwd("~/Box Sync/HEROP Lab/Active Funded Grants/Oeps Data/OEPS Data - Updates/Scripts")

# Load required libraries for spatial analysis, data manipulation, and accessing Census data
library(sf)
library(tidyverse)
library(tidycensus)

# Retrieve the Census API key from system environment
Sys.getenv("CENSUS_API_KEY")

# Get 2020 ACS data at the county level for total number of occupants in housing units
county20 <- get_acs(geography = 'county', variables = (Occupants = "B25014_001"),
                    year = 2010, geometry = FALSE)
# Display first few rows of the retrieved dataset
head(county20)

#################
# Get 2010 ACS data at the county level for various economic indicators
county18 <- get_acs(geography = 'county', variables = c(UnempP = "DP03_0005P",  # Unemployment rate
                                                        S2401_C01_011 = "S2401_C01_011",  # Industry employment
                                                        
                                                        # Employment status by various demographic categories
                                                        NMMLFU    = 'B12006_006',  NMMLF  = 'B12006_004',
                                                        NMFLFU    = 'B12006_011',  NMFLF  = 'B12006_009',
                                                        MMLFU     = 'B12006_017',  MMLF   = 'B12006_015',
                                                        MFLFU     = 'B12006_022',  MFLF   = 'B12006_020',
                                                        SMLFU     = 'B12006_028',  SMLF   = 'B12006_026',
                                                        SFLFU     = 'B12006_033',  SFLF   = 'B12006_031',
                                                        WMLFU     = 'B12006_039',  WMLF   = 'B12006_037',
                                                        WFLFU     = 'B12006_044',  WFLF   = 'B12006_042',
                                                        DMLFU     = 'B12006_050',  DMLF   = 'B12006_048',
                                                        DFLFU     = 'B12006_055',  DFLF   = 'B12006_053',
                                                        pci       = 'B19301_001',  # Per capita income
                                                        cntPov    = 'B06012_002',  # Population below poverty level
                                                        cntPovUni = 'B06012_001',  # Total population for poverty calculation
                                                        GiniCoeff = 'B19083_001',  # Gini coefficient for income inequality
                                                        MedInc    = 'B06011_001'), # Median income
                    year = 2010, geometry = FALSE) %>%
  select(GEOID, NAME, variable, estimate) %>%  # Select relevant columns
  spread(variable, estimate) %>%  # Reshape the data for better readability
  mutate(
    # Calculate alternative unemployment percentage
    unempP2 = round(100 * (NMMLFU + NMFLFU + MMLFU +  
                             MFLFU + SMLFU + SFLFU +  
                             WMLFU + WFLFU + DMLFU +  
                             DFLFU) / 
                      (NMMLFU + NMMLF + NMFLFU + NMFLF + 
                         SMLFU  + SMLF  + SFLFU  + SFLF + 
                         MMLFU  + MMLF  + MFLFU  + MFLF + 
                         WMLFU  + WMLF  + WFLFU  + WFLF + 
                         DMLFU  + DFLF  + DFLFU  + DFLF), 
                    2),
    # Calculate poverty percentage
    povP   = round(100 * cntPov / cntPovUni, 2)
  ) %>%
  select(GEOID, UnempP, unempP2, pci, povP, GiniCoeff, MedInc)  # Select final variables

# Display first few rows of the processed county dataset
head(county)
summary(county) 

# Create a histogram of the unemployment percentage
hist(county$UnempP)

# Save the processed county-level economic data to a CSV file
write.csv(county, "../data/economic_county10.csv")

#####################
# Retrieve 2010 ACS data at the ZIP Code Tabulation Area (ZCTA) level
zcta <- get_acs(geography = 'zcta', variables = c(UnempP = "DP03_0005P", 
                                                  S2401_C01_011 = "S2401_C01_011",
                                                  NMMLFU    = 'B12006_006',  NMMLF  = 'B12006_004',
                                                  NMFLFU    = 'B12006_011',  NMFLF  = 'B12006_009',
                                                  MMLFU     = 'B12006_017',  MMLF   = 'B12006_015',
                                                  MFLFU     = 'B12006_022',  MFLF   = 'B12006_020',
                                                  SMLFU     = 'B12006_028',  SMLF   = 'B12006_026',
                                                  SFLFU     = 'B12006_033',  SFLF   = 'B12006_031',
                                                  WMLFU     = 'B12006_039',  WMLF   = 'B12006_037',
                                                  WFLFU     = 'B12006_044',  WFLF   = 'B12006_042',
                                                  DMLFU     = 'B12006_050',  DMLF   = 'B12006_048',
                                                  DFLFU     = 'B12006_055',  DFLF   = 'B12006_053',
                                                  pci       = 'B19301_001',  cntPov = 'B06012_002', 
                                                  cntPovUni = 'B06012_001',
                                                  GiniCoeff = 'B19083_001',
                                                  MedInc    = 'B06011_001'), 
                year = 2010, geometry = FALSE) %>%
  select(GEOID, NAME, variable, estimate) %>%
  spread(variable, estimate) %>%
  mutate(
    unempP2 = round(100 * (NMMLFU + NMFLFU + MMLFU +  
                             MFLFU + SMLFU + SFLFU +  
                             WMLFU + WFLFU + DMLFU +  
                             DFLFU) / 
                      (NMMLFU + NMMLF + NMFLFU + NMFLF + 
                         SMLFU  + SMLF  + SFLFU  + SFLF + 
                         MMLFU  + MMLF  + MFLFU  + MFLF + 
                         WMLFU  + WMLF  + WFLFU  + WFLF + 
                         DMLFU  + DFLF  + DFLFU  + DFLF), 
                    2),
    povP   = round(100 * cntPov / cntPovUni, 2)
  ) %>%
  select(GEOID, UnempP, unempP2, pci, povP, GiniCoeff, MedInc)

head(zcta)
summary(zcta) 

# Create histogram for unemployment percentage at ZCTA level
hist(zcta$UnempP)

# Save the ZCTA-level economic data to a CSV file
write.csv(zcta, "../data/economic_zcta15.csv")

#####################
# Retrieve 2010 ACS data at the census tract level
tracts <- get_acs(geography = 'tract', variables = c(UnempP = "DP03_0005P", 
                                                     S2401_C01_011 = "S2401_C01_011",
                                                     pci       = 'B19301_001',  
                                                     cntPov    = 'B06012_002',  
                                                     cntPovUni = 'B06012_001',
                                                     GiniCoeff = 'B19083_001',
                                                     MedInc    = 'B06011_001'), 
                  year = 2010, state = c(state.abb, "DC"), geometry = FALSE) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate)

head(tracts)
summary(tracts) 

# Create histogram for unemployment percentage at tract level
hist(tracts$UnempP)

# Save the tract-level economic data to a CSV file
write.csv(tracts, "../data/economic_tract10.csv")



# ACS Table: S0501 - Selected Characteristics of the Native and Foreign-Born Populations
# Employment Status Variables (Population 16 years and over)

48  S0501_C01_048  
# Total population 16 years and over - This includes everyone in the specified age group.

49  S0501_C01_049  
# Population 16 years and over who are in the labor force - This includes both employed and unemployed individuals.

50  S0501_C01_050  
# Civilian labor force - This excludes military personnel and focuses on civilians who are either employed or seeking employment.

51  S0501_C01_051  
# Employed civilians - This represents individuals within the civilian labor force who have jobs.

52  S0501_C01_052  
# Unemployed civilians - This represents individuals within the civilian labor force who are actively looking for jobs.

53  S0501_C01_053  
# Unemployment rate - Percentage of the civilian labor force that is unemployed.

54  S0501_C01_054  
# Armed Forces - Individuals serving in the military, counted separately from the civilian labor force.

55  S0501_C01_055  
# Not in the labor force - Individuals who are not seeking work, such as retirees, students, or those unable to work.

