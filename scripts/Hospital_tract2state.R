# Author: Mahjabin Kabir Adrita
# Date: 2026-08-02
# Data Source: Substance Abuse and Mental Health Services Administration (SAMHSA)

library(tidyverse)
library(sf)
library(tmap)

Hosp_tracts25 <- read.csv("C:/Users/adrit/Downloads/HospFacility-Tract25.csv")

head(Hosp_tracts25)
summary(Hosp_tracts25)
glimpse(Hosp_tracts25)

# Flag tracts with Hospital within 30-minute drive
Hosp_tracts25$HospInRangeDr30  <- ifelse(Hosp_tracts25$HospTmDr < 30, 1, 0)
Hosp_tracts25$HospInRangeDr302 <- ifelse(Hosp_tracts25$HospTmDr2 < 30, 1, 0)

# Extract State FIPS from tract HEROP_ID
Hosp_tracts25$StateFIPS <- str_sub(Hosp_tracts25$HEROP_ID, 6, 7)

head(Hosp_tracts25)

# Aggregate tract-level data to state level
Hosp_states25 <- Hosp_tracts25 %>%
  group_by(StateFIPS) %>%
  summarize(
    TotTracts = n(),
    
    # Number of tracts within 30-minute drive
    HospCtTmDr  = sum(HospInRangeDr30,  na.rm = TRUE),
    HospCtTmDr2 = sum(HospInRangeDr302, na.rm = TRUE),
    
    # Percent of tracts within 30-minute drive
    HospTmDrP  = (HospCtTmDr  / TotTracts) * 100,
    HospTmDrP2 = (HospCtTmDr2 / TotTracts) * 100,
    
    # Average drive time
    HospAvTmDr  = mean(HospTmDr,  na.rm = TRUE),
    HospAvTmDr2 = mean(HospTmDr2, na.rm = TRUE)
  ) %>%
  ungroup() %>%
  select(
    StateFIPS, TotTracts,
    HospCtTmDr, HospCtTmDr2,
    HospTmDrP, HospTmDrP2,
    HospAvTmDr, HospAvTmDr2
  )

head(Hosp_states25)
summary(Hosp_states25)
dim(Hosp_states25)

# Create state-level HEROP_ID
Hosp_states25$HEROP_ID <- paste0("040US", Hosp_states25$StateFIPS)

glimpse(Hosp_states25)

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
state.Hosp <- merge(state.sf2, Hosp_states25, by = "HEROP_ID")

dim(state.Hosp)
head(state.Hosp)

# Maps
tm_shape(state.Hosp) + tm_polygons("HospAvTmDr", style = "jenks")
tm_shape(state.Hosp) + tm_fill("HospAvTmDr", style = "jenks")
tm_shape(state.Hosp) + tm_fill("HospTmDrP2", style = "jenks")
tm_shape(state.Hosp) + tm_fill("HospTmDrP", style = "jenks")
tm_shape(state.Hosp) + tm_fill("HospCtTmDr2", style = "jenks")
tm_shape(state.Hosp) + tm_fill("HospCtTmDr", style = "jenks")
tm_shape(state.Hosp) + tm_fill("TotTracts", style = "jenks")

# Drop geometry for CSV export
state.Hosp.save <- st_drop_geometry(state.Hosp)

state.Hosp.save <- state.Hosp.save %>%
  select(
    HEROP_ID, GEOID,
    TotTracts,
    HospCtTmDr, HospCtTmDr2,
    HospTmDrP, HospTmDrP2,
    HospAvTmDr, HospAvTmDr2
  )

# Round numeric columns to 2 decimals
state.Hosp.save2 <- state.Hosp.save %>%
  mutate(across(where(is.numeric), ~ round(.x, 2)))

head(state.Hosp.save2)
dim(state.Hosp.save2)

# Export CSV
write.csv(
  state.Hosp.save2,
  "C:/Users/adrit/Downloads/HospFacilityState-2025.csv",
  row.names = FALSE
)

