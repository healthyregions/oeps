# Set working directory
setwd("~/Code/oeps2/scripts")

# Load necessary libraries for data manipulation and analysis
library(sf)  # For working with spatial data
library(tidyverse)  # For data manipulation (dplyr, ggplot2, etc.)
library(tidycensus)  # For accessing US Census data

#census_api_key("ADD HERE", install = TRUE) # installs the key for future sessions. 

# Check for Census API key
Sys.getenv("CENSUS_API_KEY")

# 2023
# Selected Social Characteristics in the United States
# DP02_0153: Estimate!!COMPUTERS AND INTERNET USE!!Total households!!With a computer
# DP02_0153P: Percent!!COMPUTERS AND INTERNET USE!!Total households!!With a computer
# DP02_0154P: Percent!!COMPUTERS AND INTERNET USE!!Total households!!With a broadband Internet subscription

# Retrieve ACS data for 2023 at the tract level for the specified variable
tract <- get_acs(geography = 'tract', variables = c(CompHhlds = "DP02_0153",
                                                    CompHhldsP = "DP02_0153P", 
                                                    BbndInternetP = "DP02_0154P"),
                 year = 2023, geometry = FALSE, state = c(state.abb, "DC")) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate) %>% 
  select(GEOID,CompHhlds,CompHhldsP,BbndInternetP)

head(tract)

hist(tract$CompHhlds)
hist(tract$CompHhldsP)
hist(tract$BbndInternetP)
summary(tract) #84400


tract$HEROP_ID <- paste0("140US",tract$GEOID)
head(tract)

write.csv(tract, "../data_to_merge/internet_tract23.csv",row.names = FALSE)

# 2018
pVarNames <- load_variables(2018, "acs5/profile", cache = TRUE)
View(pVarNames)

# Selected Social Characteristics in the United States
# DP02_0151: Estimate!!COMPUTERS AND INTERNET USE!!Total households!!With a computer
# DP02_0151P: Percent!!COMPUTERS AND INTERNET USE!!Total households!!With a computer
# DP02_0152P: Percent!!COMPUTERS AND INTERNET USE!!Total households!!With a broadband Internet subscription

# Retrieve ACS data for 2018 at the tract level for the specified variable
tract <- get_acs(geography = 'tract', variables = c(CompHhlds = "DP02_0151",
                                                    CompHhldsP = "DP02_0151P", 
                                                    BbndInternetP = "DP02_0152P"),
                 year = 2018, geometry = FALSE, state = c(state.abb, "DC")) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate) %>% 
  select(GEOID,CompHhlds,CompHhldsP,BbndInternetP)

head(tract)

hist(tract$CompHhlds)
hist(tract$CompHhldsP)
hist(tract$BbndInternetP)
summary(tract) #73056


tract$HEROP_ID <- paste0("140US",tract$GEOID)
head(tract)

write.csv(tract, "../data_to_merge/internet_tract18.csv",row.names = FALSE)


###### Zip

# Retrieve ACS data for 2018 at the zcta level for the specified variable
zcta <- get_acs(geography = 'zcta', variables = c(CompHhlds = "DP02_0151",
                                                  CompHhldsP = "DP02_0151P", 
                                                  BbndInternetP = "DP02_0152P"),
                year = 2018, geometry = FALSE, state = c(state.abb, "DC")) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate) %>% 
  select(GEOID,CompHhlds,CompHhldsP,BbndInternetP)

head(zcta)

hist(zcta$CompHhlds)
hist(zcta$CompHhldsP)
hist(zcta$BbndInternetP)
summary(zcta) #32989


zcta$HEROP_ID <- paste0("860US",zcta$GEOID)
head(zcta)

write.csv(zcta, "../data_to_merge/internet_zcta18.csv",row.names = FALSE)

#zcta not available after 2019
