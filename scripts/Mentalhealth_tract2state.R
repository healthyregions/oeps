# Author: Mahjabin Kabir Adrita
# Date: 2026-08-02
# Data Source: Substance Abuse and Mental Health Services Administration (SAMHSA)

library(tidyverse)
library(sf)
library(tmap)

Mh_tracts25 <- read.csv("C:/Users/adrit/Downloads/Mh_tract25.csv")

head(Mh_tracts25)
summary(Mh_tracts25)
glimpse(Mh_tracts25)

# Flag tracts with Mental Health Treatment Facility within 30-minute drive
Mh_tracts25$MhInRangeDr30  <- ifelse(Mh_tracts25$MhTmDr < 30, 1, 0)
Mh_tracts25$MhInRangeDr302 <- ifelse(Mh_tracts25$MhTmDr2 < 30, 1, 0)

# Extract State FIPS from tract HEROP_ID
Mh_tracts25$StateFIPS <- str_sub(Mh_tracts25$HEROP_ID, 6, 7)

head(Mh_tracts25)

# Aggregate tract-level data to state level
Mh_states25 <- Mh_tracts25 %>%
  group_by(StateFIPS) %>%
  summarize(
    TotTracts = n(),
    
    # Number of tracts within 30-minute drive
    MhCtTmDr  = sum(MhInRangeDr30,  na.rm = TRUE),
    MhCtTmDr2 = sum(MhInRangeDr302, na.rm = TRUE),
    
    # Percent of tracts within 30-minute drive
    MhTmDrP  = (MhCtTmDr  / TotTracts) * 100,
    MhTmDrP2 = (MhCtTmDr2 / TotTracts) * 100,
    
    # Average drive time
    MhAvTmDr  = mean(MhTmDr,  na.rm = TRUE),
    MhAvTmDr2 = mean(MhTmDr2, na.rm = TRUE)
  ) %>%
  ungroup() %>%
  select(
    StateFIPS, TotTracts,
    MhCtTmDr, MhCtTmDr2,
    MhTmDrP, MhTmDrP2,
    MhAvTmDr, MhAvTmDr2
  )

head(Mh_states25)
summary(Mh_states25)
dim(Mh_states25)

# Create state-level HEROP_ID
Mh_states25$HEROP_ID <- paste0("040US", Mh_states25$StateFIPS)

glimpse(Mh_states25)

# Read state GeoJSON 
state.sf <- st_read("https://herop-geodata.s3.us-east-2.amazonaws.com/census/state-2020-500k.geojson")

glimpse(state.sf)
names(state.sf)

# Keep only needed columns
state.sf2 <- state.sf %>%
  select(HEROP_ID, NAME, STUSPS, GEOID)

dim(state.sf2)
head(state.sf2)

# Merge state geometry with state metrics
state.Mh <- merge(state.sf2, Mh_states25, by = "HEROP_ID")

dim(state.Mh)
head(state.Mh)

# Maps
tm_shape(state.Mh) + tm_polygons("MhAvTmDr", style = "jenks")
tm_shape(state.Mh) + tm_fill("MhAvTmDr", style = "jenks")
tm_shape(state.Mh) + tm_fill("MhTmDrP2", style = "jenks")
tm_shape(state.Mh) + tm_fill("MhTmDrP", style = "jenks")
tm_shape(state.Mh) + tm_fill("MhCtTmDr2", style = "jenks")
tm_shape(state.Mh) + tm_fill("MhCtTmDr", style = "jenks")
tm_shape(state.Mh) + tm_fill("TotTracts", style = "jenks")

# Drop geometry for CSV export
state.Mh.save <- st_drop_geometry(state.Mh)

state.Mh.save <- state.Mh.save %>%
  select(
    HEROP_ID, GEOID,
    TotTracts,
    MhCtTmDr, MhCtTmDr2,
    MhTmDrP, MhTmDrP2,
    MhAvTmDr, MhAvTmDr2
  )

# Round numeric columns to 2 decimals
state.Mh.save2 <- state.Mh.save %>%
  mutate(across(where(is.numeric), ~ round(.x, 2)))

head(state.Mh.save2)
dim(state.Mh.save2)

# Export CSV
write.csv(
  state.Mh.save2,
  "C:/Users/adrit/Downloads/MhTestingState-2025.csv",
  row.names = FALSE
)
