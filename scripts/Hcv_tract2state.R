# Author: Mahjabin Kabir Adrita
# Date: 2026-08-02
# Data Source: Substance Abuse and Mental Health Services Administration (SAMHSA)

library(tidyverse)
library(sf)
library(tmap)

Hcv_tracts25 <- read.csv("C:/Users/adrit/Downloads/Hcv-Tract-2025.csv")

head(Hcv_tracts25)
summary(Hcv_tracts25)
glimpse(Hcv_tracts25)

# Flag tracts with Hcv Testing Facility within 30-minute drive
Hcv_tracts25$HcvInRangeDr30  <- ifelse(Hcv_tracts25$HcvTmDr < 30, 1, 0)
Hcv_tracts25$HcvInRangeDr302 <- ifelse(Hcv_tracts25$HcvTmDr2 < 30, 1, 0)

# Extract State FIPS from tract HEROP_ID
Hcv_tracts25$StateFIPS <- str_sub(Hcv_tracts25$HEROP_ID, 6, 7)

head(Hcv_tracts25)

# Aggregate tract-level data to state level
Hcv_states25 <- Hcv_tracts25 %>%
  group_by(StateFIPS) %>%
  summarize(
    TotTracts = n(),
    
    # Number of tracts within 30-minute drive
    HcvCtTmDr  = sum(HcvInRangeDr30,  na.rm = TRUE),
    HcvCtTmDr2 = sum(HcvInRangeDr302, na.rm = TRUE),
    
    # Percent of tracts within 30-minute drive
    HcvTmDrP  = (HcvCtTmDr  / TotTracts) * 100,
    HcvTmDrP2 = (HcvCtTmDr2 / TotTracts) * 100,
    
    # Average drive time
    HcvAvTmDr  = mean(HcvTmDr,  na.rm = TRUE),
    HcvAvTmDr2 = mean(HcvTmDr2, na.rm = TRUE)
  ) %>%
  ungroup() %>%
  select(
    StateFIPS, TotTracts,
    HcvCtTmDr, HcvCtTmDr2,
    HcvTmDrP, HcvTmDrP2,
    HcvAvTmDr, HcvAvTmDr2
  )

head(Hcv_states25)
summary(Hcv_states25)
dim(Hcv_states25)

# Create state-level HEROP_ID
Hcv_states25$HEROP_ID <- paste0("040US", Hcv_states25$StateFIPS)

glimpse(Hcv_states25)

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
state.Hcv <- merge(state.sf2, Hcv_states25, by = "HEROP_ID")

dim(state.Hcv)
head(state.Hcv)

# Maps
tm_shape(state.Hcv) + tm_polygons("HcvAvTmDr", style = "jenks")
tm_shape(state.Hcv) + tm_fill("HcvAvTmDr", style = "jenks")
tm_shape(state.Hcv) + tm_fill("HcvTmDrP2", style = "jenks")
tm_shape(state.Hcv) + tm_fill("HcvTmDrP", style = "jenks")
tm_shape(state.Hcv) + tm_fill("HcvCtTmDr2", style = "jenks")
tm_shape(state.Hcv) + tm_fill("HcvCtTmDr", style = "jenks")
tm_shape(state.Hcv) + tm_fill("TotTracts", style = "jenks")

# Drop geometry for CSV export
state.Hcv.save <- st_drop_geometry(state.Hcv)

state.Hcv.save <- state.Hcv.save %>%
  select(
    HEROP_ID, GEOID,
    TotTracts,
    HcvCtTmDr, HcvCtTmDr2,
    HcvTmDrP, HcvTmDrP2,
    HcvAvTmDr, HcvAvTmDr2
  )

# Round numeric columns to 2 decimals
state.Hcv.save2 <- state.Hcv.save %>%
  mutate(across(where(is.numeric), ~ round(.x, 2)))

head(state.Hcv.save2)
dim(state.Hcv.save2)

# Export CSV
write.csv(
  state.Hcv.save2,
  "C:/Users/adrit/Downloads/HcvState-2025.csv",
  row.names = FALSE
)

