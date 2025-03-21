# Set working directory to the location where the scripts are stored
setwd("~/Box Sync/HEROP Lab/Active Funded Grants/Oeps Data/OEPS Data - Updates/Scripts")

# Load necessary libraries
library(sf)          # For handling spatial data
library(tidyverse)   # For data wrangling and visualization
library(tidycensus)  # For accessing U.S. Census Bureau data

# Check if Census API key is set
Sys.getenv("CENSUS_API_KEY")

# Retrieve 2020 county-level ACS data for total number of occupants in housing units
county10 <- get_acs(geography = 'county', variables = (Occupants = "B25014_001"),
                    year = 2010, geometry = FALSE)
head(county10)  # Display first few rows of the dataset

# The following variables are related to household types and marital status 
# in the American Community Survey (ACS) dataset.

# Household type-related variables:
# - DP02_0001: Total households
# - DP02_0002P: Percentage of married-couple households
# - DP02_0003P: Percentage of married-couple households with children under 18
# - DP02_0004P: Percentage of cohabiting couple households
# - DP02_0016: Average household size
# - DP02_0017: Average family size

# Marital status-related variables:
# - DP02_0026P: Percentage of males (15+) never married
# - DP02_0027P: Percentage of males (15+) married
# - DP02_0028P: Percentage of males (15+) separated
# - DP02_0029P: Percentage of males (15+) widowed
# - DP02_0030P: Percentage of males (15+) divorced

# Additional household characteristics:
# - DP02_0011P: Percentage of female householders with children under 18
# - DP02_0012P: Percentage of female householders living alone
# - DP02_0013P: Percentage of female householders living alone, aged 65+
# - DP02_0007P: Percentage of male householders with children under 18
# - DP02_0008P: Percentage of male householders living alone
# - DP02_0009P: Percentage of male householders living alone, aged 65+

# Retrieve 2010 county-level ACS data for selected demographic and household variables
county10 <- get_acs(geography = 'county', variables = c(HsdTot = "DP02_0001",
                                                        HsdTypM = "DP02_0002P",
                                                        HsdTypMC = "DP02_0003P",
                                                        HsdTypCo = "DP02_0004P",
                                                        HHSize = "DP02_0016",
                                                        FamSize = "DP02_0017",
                                                        NvMrrdP = "DP02_0026P",
                                                        MrrdP = "DP02_0027P",
                                                        DivrcdP = "DP02_0030P",
                                                        SepartedP = "DP02_0028P",
                                                        WidwdP = "DP02_0029P",
                                                        HhldFC= "DP02_0011P",
                                                        HhldFA = "DP02_0012P",
                                                        HhldFS = "DP02_0013P",
                                                        HhldMC= "DP02_0007P",
                                                        HhldMA = "DP02_0008P",
                                                        HhldMS = "DP02_0009P"
), 
year = 2010, geometry = FALSE) %>%
  select(GEOID, NAME, variable, estimate) %>%  # Select relevant columns
  spread(variable, estimate)  %>%  # Convert long format to wide format
  select(GEOID,HsdTot,HsdTypM,HsdTypMC,HsdTypCo,HHSize,FamSize,NvMrrdP,MrrdP,DivrcdP,SepartedP,WidwdP,HhldFC,HhldFA,HhldFS,HhldMC,HhldMA,HhldMS)

# Display summary statistics and distributions
head(county10)
glimpse(county10)
summary(county10) 

# Generate histogram for percentage of never married males
hist(county10$NvMrrdP)

# Save county-level data to CSV
write.csv(county10, "../data/interpersonal_county10.csv")

#####################

# Retrieve 2010 ZCTA (ZIP Code Tabulation Area) level ACS data
zcta <- get_acs(geography = 'zcta', variables = c(HsdTot = "DP02_0001",
                                                  HsdTypM = "DP02_0002P",
                                                  HsdTypMC = "DP02_0003P",
                                                  HsdTypCo = "DP02_0004P",
                                                  HHSize = "DP02_0016",
                                                  FamSize = "DP02_0017",
                                                  NvMrrdP = "DP02_0026P",
                                                  MrrdP = "DP02_0027P",
                                                  DivrcdP = "DP02_0030P",
                                                  SepartedP = "DP02_0028P",
                                                  WidwdP = "DP02_0029P",
                                                  HhldFC= "DP02_0011P",
                                                  HhldFA = "DP02_0012P",
                                                  HhldFS = "DP02_0013P",
                                                  HhldMC= "DP02_0007P",
                                                  HhldMA = "DP02_0008P",
                                                  HhldMS = "DP02_0009P"
), 
year = 2010, geometry = FALSE) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate)  %>% 
  select(GEOID,HsdTot,HsdTypM,HsdTypMC,HsdTypCo,HHSize,FamSize,NvMrrdP,MrrdP,DivrcdP,SepartedP,WidwdP,HhldFC,HhldFA,HhldFS,HhldMC,HhldMA,HhldMS)

# Display summary statistics and histogram for never married males
summary(zcta) 
hist(zcta$NvMrrdP)

# Save ZCTA-level data to CSV
write.csv(zcta, "../data/interpersonal_zcta10.csv")

#####################

# Retrieve 2010 census tract-level ACS data for selected demographic and household variables
tract10 <- get_acs(geography = 'tract', variables = c(HsdTot = "DP02_0001",
                                                      HsdTypM = "DP02_0002P",
                                                      HsdTypMC = "DP02_0003P",
                                                      HsdTypCo = "DP02_0004P",
                                                      HHSize = "DP02_0016",
                                                      FamSize = "DP02_0017",
                                                      NvMrrdP = "DP02_0026P",
                                                      MrrdP = "DP02_0027P",
                                                      DivrcdP = "DP02_0030P",
                                                      SepartedP = "DP02_0028P",
                                                      WidwdP = "DP02_0029P",
                                                      HhldFC= "DP02_0011P",
                                                      HhldFA = "DP02_0012P",
                                                      HhldFS = "DP02_0013P",
                                                      HhldMC= "DP02_0007P",
                                                      HhldMA = "DP02_0008P",
                                                      HhldMS = "DP02_0009P"
), 
year = 2010, geometry = FALSE, state = c(state.abb, "DC")) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate)  %>% 
  select(GEOID,HsdTot,HsdTypM,HsdTypMC,HsdTypCo,HHSize,FamSize,NvMrrdP,MrrdP,DivrcdP,SepartedP,WidwdP,HhldFC,HhldFA,HhldFS,HhldMC,HhldMA,HhldMS)

# Display tract-level data summary and histogram for never married males
head(tract10)
glimpse(tract10)
summary(tract10) 

hist(tract10$NvMrrdP)

# Save tract-level data to CSV
write.csv(tract10, "../data/interpersonal_tract10.csv")

