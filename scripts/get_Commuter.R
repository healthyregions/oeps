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

# Concept: Household Size by Vehicles Available
# B08201_001 Estimate!!Total:
# B08201_002 Estimate!!Total:!!No vehicle available

# Retrieve ACS data for 2018 at the tract level for the specified variable
tract <- get_acs(geography = 'tract', variables = c(TotalPop = "B08201_001", 
                                                    NoVehTotal = "B08201_002"),
                 year = 2018, geometry = FALSE, state = c(state.abb, "DC")) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate) %>% 
  mutate( NoVehHHld = NoVehTotal/TotalPop*100) %>%
  select(GEOID,NoVehHHld)

head(tract)

hist(tract$NoVehHHld)
summary(tract) #73056

# Means of Transportation to Work by Age
# B08101_001: Estimate!!Total:
# B08101_025: Estimate!!Total:!!Public transportation (excluding taxicab):
# B08101_033: Estimate!!Total:!!Walked:


tract2 <- get_acs(geography = 'tract', 
                  variables = c(TotalPop = "B08101_001", 
                                CommTransitTotal = "B08101_025",
                                CommWalkingTotal = "B08101_033"),
                 year = 2018, geometry = FALSE, state = c(state.abb, "DC")) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate) %>% 
  mutate( CommTransit = CommTransitTotal/TotalPop*100,
          CommWalking = CommWalkingTotal/TotalPop*100) %>%
  select(GEOID,CommTransit,CommWalking)

head(tract2)

hist(tract2$CommTransit)
hist(tract2$CommWalking)

summary(tract2) #73056

final <- merge(tract,tract2,by="GEOID")

# Format specific columns (e.g., 'var1' and 'var2') to 2 decimal places
final_rounded <- final %>%
  mutate(across(where(is.numeric), round, 2))

head(final_rounded)

final_rounded$HEROP_ID <- paste0("140US",final_rounded$GEOID)

head(final_rounded)

write.csv(final_rounded, "../data_to_merge/commuting_tract18.csv",row.names = FALSE)
