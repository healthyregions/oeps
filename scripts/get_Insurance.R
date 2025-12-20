# Set working directory
setwd("~/Code/oeps2/scripts")

# Load necessary libraries for data manipulation and analysis
library(sf)  # For working with spatial data
library(tidyverse)  # For data manipulation (dplyr, ggplot2, etc.)
library(tidycensus)  # For accessing US Census data

#census_api_key("ADD HERE", install = TRUE) # installs the key for future sessions. 

# Check for Census API key
Sys.getenv("CENSUS_API_KEY")

sVarNames <- load_variables(2023, "acs5/subject", cache = TRUE)
pVarNames <- load_variables(2023, "acs5/profile", cache = TRUE)
otherVarNames <- load_variables(2023, "acs5", cache = TRUE)

head(pVarNames)

# Selected Economic Characteristics
# DP03_0096: Estimate!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage
# DP03_0096P: Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage
# DP03_0097P: Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage!!With private health insurance
# DP03_0098P: Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage!!With public coverage

# Retrieve ACS data for 2023 at the tract level for the specified variable
tract <- get_acs(geography = 'tract', variables = c(InsuredPop = "DP03_0096",
                                                    InsuredPopP = "DP03_0096P", 
                                                    PrivateInsP = "DP03_0097P",
                                                    PublicInsP = "DP03_0098P"),
                 year = 2018, geometry = FALSE, state = c(state.abb, "DC")) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate) %>% 
  select(GEOID,InsuredPop,InsuredPopP,PrivateInsP,PublicInsP)

head(tract)

hist(tract$InsuredPop)
hist(tract$InsuredPopP)
hist(tract$PrivateInsP)
hist(tract$PublicInsP)
summary(tract) #73056


tract$HEROP_ID <- paste0("140US",tract$GEOID)
head(tract)

write.csv(tract, "../data_to_merge/insurance_tract18.csv",row.names = FALSE)
