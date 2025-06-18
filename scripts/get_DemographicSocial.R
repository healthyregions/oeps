# Set working directory
setwd("~/Box Sync/HEROP Lab/Active Funded Grants/Oeps Data/OEPS Data - Updates/Scripts")

# Load necessary libraries for data manipulation and analysis
library(sf)  # For working with spatial data
library(tidyverse)  # For data manipulation (dplyr, ggplot2, etc.)
library(tidycensus)  # For accessing US Census data

# Check for Census API key
Sys.getenv("CENSUS_API_KEY")

# Retrieve ACS data for 2020 at the county level for the specified variable (Occupants)
county20 <- get_acs(geography = 'county', variables = (Occupants = "B25014_001"),
                    year = 2020, geometry = FALSE)
head(county20)

## Codebook reference for variable details

# Retrieve ACS data for 2018 at the county level with multiple demographic variables
county18 <- get_acs(geography = 'county', variables = c(TotalPop ="DP05_0001",
                                                        MaleP = "DP05_0002P",
                                                        FemP = "DP05_0003P",
                                                        SRatio = "DP05_0004",
                                                        SRatio18 ="DP05_0028P",
                                                        SRatio65 = "DP05_0032P",
                                                        Under5P = "DP05_0005P",
                                                        Over16P = "DP05_0020P",
                                                        Under18P = "DP05_0019P",
                                                        Over18P = "DP05_0021P",
                                                        Over21P = "DP05_0022P",
                                                        Over25P = "DP02_0059P",
                                                        Over65P = "DP05_0024P",
                                                        MedAge = "DP05_0018",
                                                        WhiteNHE = "DP05_0082",
                                                        WhiteNHP = "DP05_0082P",
                                                        BlackNHE = "DP05_0083",
                                                        BlackNHP = "DP05_0083P",
                                                        AIANNHE = "DP05_0084",
                                                        AIANNHP = "DP05_0084P",
                                                        AsianNHE = "DP05_0085",
                                                        AsianNHP = "DP05_0085P",
                                                        NAPINHE = "DP05_0086",
                                                        NAPINHP = "DP05_0086P",
                                                        HispLatE = "DP05_0076",
                                                        HispLatP = "DP05_0076P",
                                                        OthrNH = "DP05_0087",
                                                        OthrNHP = "DP05_0087P",
                                                        TwoNH = "DP05_0088",
                                                        TwoNHP = "DP05_0088P",
                                                        below9 = "DP02_0060P",
                                                        noHS = "DP02_0061P",
                                                        eduHS = "DP02_0062P",
                                                        someCollege = "DP02_0063P",
                                                        Bachelors = "DP02_0065P",
                                                        GradScl = "DP02_0066P",
                                                        CivilnPop = "DP02_0069",
                                                        VetP = "DP02_0070P", 
                                                        DisabP = "DP02_0071P"),
                    year = 2018, geometry = FALSE) %>%
  select(GEOID, NAME, variable, estimate) %>%  # Select relevant columns
  spread(variable, estimate) %>%  # Spread data so each variable is a separate column
  mutate( eduNoHS = below9+noHS) %>%  # Calculate the total population with less than high school education
  select(GEOID,TotalPop,MaleP,FemP,SRatio,SRatio18,SRatio65,
         Under5P,Over16P,Under18P,Over18P,Over21P,Over25P,Over65P,MedAge,WhiteNHE,
         WhiteNHP,BlackNHE,BlackNHP,AIANNHE,AIANNHP,
         AsianNHE,AsianNHP,NAPINHE,NAPINHP,HispLatE,HispLatP,OthrNH,OthrNHP,
         OthrNHP,TwoNH,TwoNHP,eduNoHS,eduHS,someCollege,Bachelors,GradScl,CivilnPop,VetP,DisabP)

# View first few rows of the data
head(county18)
# Glimpse to see the structure of the dataset
glimpse(county18)
# Summary statistics of the dataset
summary(county18) 

# Plot histogram of Veterans percentage
hist(county18$VetP)

# Write the data to a CSV file
write.csv(county18, "../data/social_county18.csv")

# Repeat similar process for county data from 2015 with a different set of variables
county18 <- get_acs(geography = 'county', variables = c(TotalPop ="DP05_0001",
                                                        MaleP = "DP05_0002P",
                                                        FemP = "DP05_0003P",
                                                        SRatio = "DP05_0004",
                                                        SRatio18 ="DP05_0028P",
                                                        SRatio65 = "DP05_0032P",
                                                        Under5P = "DP05_0005P",
                                                        Over16P = "DP05_0020P",
                                                        Under18P = "DP05_0019P",
                                                        Over18P = "DP05_0021P",
                                                        Over21P = "DP05_0022P",
                                                        Over25P = "DP02_0059P",
                                                        Over65P = "DP05_0024P",
                                                        MedAge = "DP05_0018",
                                                        WhiteNHE = "DP05_0082",
                                                        WhiteNHP = "DP05_0082P",
                                                        BlackNHE = "DP05_0083",
                                                        BlackNHP = "DP05_0083P",
                                                        AIANNHE = "DP05_0084",
                                                        AIANNHP = "DP05_0084P",
                                                        HispLatE = "DP05_0076",
                                                        HispLatP = "DP05_0076P",
                                                        below9 = "DP02_0060P",
                                                        noHS = "DP02_0061P",
                                                        eduHS = "DP02_0062P",
                                                        someCollege = "DP02_0063P",
                                                        Bachelors = "DP02_0065P",
                                                        GradScl = "DP02_0066P",
                                                        CivilnPop = "DP02_0069",
                                                        VetP = "DP02_0069P", 
                                                        DisabP = "DP02_0071P"),
                    year = 2015, geometry = FALSE) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate) %>% 
  mutate( eduNoHS = below9+noHS) %>%
  select(GEOID,TotalPop,MaleP,FemP,SRatio,SRatio18,SRatio65,
         Under5P,Over16P,Under18P,Over18P,Over21P,Over25P,Over65P,MedAge,WhiteNHE,
         WhiteNHP,BlackNHE,BlackNHP,
         HispLatE,HispLatP,
         eduNoHS,eduHS,someCollege,Bachelors,GradScl,CivilnPop,VetP,DisabP)

# Handle unavailable variables for 2015 data
head(county18)
glimpse(county18)
summary(county18) 

# Plot histogram of Veterans percentage
hist(county18$VetP)

# Write the data to a CSV file
write.csv(county18, "../data/social_county15.csv")

# Repeat similar process for tract-level data for different years
tract <- get_acs(geography = 'tract', variables = c(TotalPop ="DP05_0001",
                                                    MaleP = "DP05_0002P",
                                                    FemP = "DP05_0003P",
                                                    SRatio = "DP05_0004",
                                                    SRatio18 ="DP05_0028P",
                                                    SRatio65 = "DP05_0032P",
                                                    Under5P = "DP05_0005P",
                                                    Over16P = "DP05_0020P",
                                                    Under18P = "DP05_0019P",
                                                    Over18P = "DP05_0021P",
                                                    Over21P = "DP05_0022P",
                                                    Over25P = "DP02_0059P",
                                                    Over65P = "DP05_0024P",
                                                    MedAge = "DP05_0018",
                                                    WhiteNHE = "DP05_0082",
                                                    WhiteNHP = "DP05_0082P",
                                                    BlackNHE = "DP05_0083",
                                                    BlackNHP = "DP05_0083P",
                                                    AIANNHE = "DP05_0084",
                                                    AIANNHP = "DP05_0084P",
                                                    AsianNHE = "DP05_0085",
                                                    AsianNHP = "DP05_0085P",
                                                    NAPINHE = "DP05_0086",
                                                    NAPINHP = "DP05_0086P",
                                                    HispLatE = "DP05_0076",
                                                    HispLatP = "DP05_0076P",
                                                    OthrNH = "DP05_0087",
                                                    OthrNHP = "DP05_0087P",
                                                    TwoNH = "DP05_0088",
                                                    TwoNHP = "DP05_0088P",
                                                    below9 = "DP02_0060P",
                                                    noHS = "DP02_0061P",
                                                    eduHS = "DP02_0062P",
                                                    someCollege = "DP02_0063P",
                                                    Bachelors = "DP02_0065P",
                                                    GradScl = "DP02_0066P",
                                                    CivilnPop = "DP02_0069",
                                                    VetP = "DP02_0070P", 
                                                    DisabP = "DP02_0071P"),
                 year = 2023, geometry = FALSE, state = c(state.abb, "DC")) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate) %>% 
  mutate( eduNoHS = below9+noHS) %>%
  select(GEOID,TotalPop,MaleP,FemP,SRatio,SRatio18,SRatio65,
         Under5P,Over16P,Under18P,Over18P,Over21P,Over25P,Over65P,MedAge,WhiteNHE,
         WhiteNHP,BlackNHE,BlackNHP,AIANNHE,AIANNHP,
         AsianNHE,AsianNHP,NAPINHE,NAPINHP,HispLatE,HispLatP,OthrNH,OthrNHP,
         OthrNHP,TwoNH,TwoNHP,eduNoHS,eduHS,someCollege,Bachelors,GradScl,CivilnPop,VetP,DisabP)

# View first few rows of the tract data
head(tract)
# Glimpse to see the structure of the tract dataset
glimpse(tract)
# Summary statistics of the dataset
summary(tract) 

# Plot histogram of Veterans percentage for tracts
hist(tract$VetP)

# Write the tract data to a CSV file
write.csv(tract, "../data/social_tract23.csv")

# Repeat for other tract-level data from previous years
# Continue similarly for different years and regions
write.csv(zip, "../data/social_zcta18.csv")

##################
# The following block of code is for working with data from different geographic levels (county, tract, and zip) using the American Community Survey (ACS)
# The ACS data is being pulled for various demographic variables and then transformed, such as creating a new column for the percentage of population with no high school diploma (eduNoHS).

# For ZIP Code Tabulation Areas (ZCTA) for the year 2020, a similar process can be repeated as done for county and tract data.

zip20 <- get_acs(geography = 'zcta', variables = c(TotalPop = "DP05_0001",
                                                   MaleP = "DP05_0002P",
                                                   FemP = "DP05_0003P",
                                                   SRatio = "DP05_0004",
                                                   SRatio18 = "DP05_0028P",
                                                   SRatio65 = "DP05_0032P",
                                                   Under5P = "DP05_0005P",
                                                   Over16P = "DP05_0020P",
                                                   Under18P = "DP05_0019P",
                                                   Over18P = "DP05_0021P",
                                                   Over21P = "DP05_0022P",
                                                   Over25P = "DP02_0059P",
                                                   Over65P = "DP05_0024P",
                                                   MedAge = "DP05_0018",
                                                   WhiteNHE = "DP05_0082",
                                                   WhiteNHP = "DP05_0082P",
                                                   BlackNHE = "DP05_0083",
                                                   BlackNHP = "DP05_0083P",
                                                   AIANNHE = "DP05_0084",
                                                   AIANNHP = "DP05_0084P",
                                                   AsianNHE = "DP05_0085",
                                                   AsianNHP = "DP05_0085P",
                                                   NAPINHE = "DP05_0086",
                                                   NAPINHP = "DP05_0086P",
                                                   HispLatE = "DP05_0076",
                                                   HispLatP = "DP05_0076P",
                                                   OthrNH = "DP05_0087",
                                                   OthrNHP = "DP05_0087P",
                                                   TwoNH = "DP05_0088",
                                                   TwoNHP = "DP05_0088P",
                                                   below9 = "DP02_0060P",
                                                   noHS = "DP02_0061P",
                                                   eduHS = "DP02_0062P",
                                                   someCollege = "DP02_0063P",
                                                   Bachelors = "DP02_0065P",
                                                   GradScl = "DP02_0066P",
                                                   CivilnPop = "DP02_0069",
                                                   VetP = "DP02_0070P", 
                                                   DisabP = "DP02_0071P"),
                 year = 2020, geometry = FALSE) %>%
  select(GEOID, NAME, variable, estimate) %>% 
  spread(variable, estimate) %>% 
  mutate(eduNoHS = below9 + noHS) %>%
  select(GEOID, TotalPop, MaleP, FemP, SRatio, SRatio18, SRatio65,
         Under5P, Over16P, Under18P, Over18P, Over21P, Over25P, Over65P, MedAge, WhiteNHE,
         WhiteNHP, BlackNHE, BlackNHP, AIANNHE, AIANNHP,
         AsianNHE, AsianNHP, NAPINHE, NAPINHP, HispLatE, HispLatP, OthrNH, OthrNHP,
         TwoNH, TwoNHP, eduNoHS, eduHS, someCollege, Bachelors, GradScl, CivilnPop, VetP, DisabP)

# Inspect the first few rows, the structure, and summary statistics of the zip20 data
head(zip20)
glimpse(zip20)
summary(zip20)

# Create a histogram of the percentage of the population that are veterans (VetP)
hist(zip20$VetP)

# Write the processed ZIP Code Tabulation Areas data for the year 2020 to a CSV file
write.csv(zip20, "../data/social_zcta20.csv")

##################
# Note: Each section of the code above is structured in a similar way:
# - Extract ACS data for a geographic level (county, tract, or ZCTA) and specific variables (e.g., population, race, education, etc.)
# - Perform transformations such as spreading the data into columns, mutating new variables, and selecting relevant columns
# - Inspect the data (head(), glimpse(), summary()) for quality control
# - Visualize data with histograms for key variables (e.g., veteran percentage)
# - Save the processed data to CSV files for future analysis

