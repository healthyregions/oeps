# Author: Mahjabin Kabir Adrita
# Date: 2026-08-02
# Data Source: Substance Abuse and Mental Health Services Administration (SAMHSA)

library(tidyverse)
library(sf)
library(tmap)

Hiv_tracts25 <- read.csv("C:/Users/adrit/Downloads/Hiv-Tract-2025.csv")

head(Hiv_tracts25)
summary(Hiv_tracts25)
glimpse(Hiv_tracts25)

# Flag tracts with HIV Testing Facility within 30-minute drive
Hiv_tracts25$HivInRangeDr30  <- ifelse(Hiv_tracts25$HivTmDr < 30, 1, 0)
Hiv_tracts25$HivInRangeDr302 <- ifelse(Hiv_tracts25$HivTmDr2 < 30, 1, 0)

# Extract State FIPS from tract HEROP_ID
Hiv_tracts25$StateFIPS <- str_sub(Hiv_tracts25$HEROP_ID, 6, 7)

head(Hiv_tracts25)

# Aggregate tract-level data to state level
Hiv_states25 <- Hiv_tracts25 %>%
  group_by(StateFIPS) %>%
  summarize(
    TotTracts = n(),
    
    # Number of tracts within 30-minute drive
    HivCtTmDr  = sum(HivInRangeDr30,  na.rm = TRUE),
    HivCtTmDr2 = sum(HivInRangeDr302, na.rm = TRUE),
    
    # Percent of tracts within 30-minute drive
    HivTmDrP  = (HivCtTmDr  / TotTracts) * 100,
    HivTmDrP2 = (HivCtTmDr2 / TotTracts) * 100,
    
    # Average drive time
    HivAvTmDr  = mean(HivTmDr,  na.rm = TRUE),
    HivAvTmDr2 = mean(HivTmDr2, na.rm = TRUE)
  ) %>%
  ungroup() %>%
  select(
    StateFIPS, TotTracts,
    HivCtTmDr, HivCtTmDr2,
    HivTmDrP, HivTmDrP2,
    HivAvTmDr, HivAvTmDr2
  )

head(Hiv_states25)
summary(Hiv_states25)
dim(Hiv_states25)

# Create state-level HEROP_ID
Hiv_states25$HEROP_ID <- paste0("040US", Hiv_states25$StateFIPS)

glimpse(Hiv_states25)

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
state.Hiv <- merge(state.sf2, Hiv_states25, by = "HEROP_ID")

dim(state.Hiv)
head(state.Hiv)

# Maps
tm_shape(state.Hiv) + tm_polygons("HivAvTmDr", style = "jenks")
tm_shape(state.Hiv) + tm_fill("HivAvTmDr", style = "jenks")
tm_shape(state.Hiv) + tm_fill("HivTmDrP2", style = "jenks")
tm_shape(state.Hiv) + tm_fill("HivTmDrP", style = "jenks")
tm_shape(state.Hiv) + tm_fill("HivCtTmDr2", style = "jenks")
tm_shape(state.Hiv) + tm_fill("HivCtTmDr", style = "jenks")
tm_shape(state.Hiv) + tm_fill("TotTracts", style = "jenks")

# Drop geometry for CSV export
state.Hiv.save <- st_drop_geometry(state.Hiv)

state.Hiv.save <- state.Hiv.save %>%
  select(
    HEROP_ID, GEOID,
    TotTracts,
    HivCtTmDr, HivCtTmDr2,
    HivTmDrP, HivTmDrP2,
    HivAvTmDr, HivAvTmDr2
  )

# Round numeric columns to 2 decimals
state.Hiv.save2 <- state.Hiv.save %>%
  mutate(across(where(is.numeric), ~ round(.x, 2)))

head(state.Hiv.save2)
dim(state.Hiv.save2)

# Export CSV
write.csv(
  state.Hiv.save2,
  "C:/Users/adrit/Downloads/HivState-2025.csv",
  row.names = FALSE
)

