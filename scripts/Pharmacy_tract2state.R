# Author: Mahjabin Kabir Adrita
# Date: 2026-08-02
# Data Source: Substance Abuse and Mental Health Services Administration (SAMHSA)

library(tidyverse)
library(sf)
library(tmap)

Rx_tracts25 <- read.csv("C:/Users/adrit/Downloads/Pharmacy-Tract-2025 (1).csv")

head(Rx_tracts25)
summary(Rx_tracts25)
glimpse(Rx_tracts25)

# Flag tracts with Pharmacy within 30-minute drive
Rx_tracts25$RxInRangeDr30  <- ifelse(Rx_tracts25$RxTmDr < 30, 1, 0)
Rx_tracts25$RxInRangeDr302 <- ifelse(Rx_tracts25$RxTmDr2 < 30, 1, 0)

# Extract State FIPS from tract HEROP_ID
Rx_tracts25$StateFIPS <- str_sub(Rx_tracts25$HEROP_ID, 6, 7)

head(Rx_tracts25)

# Aggregate tract-level data to state level
Rx_states25 <- Rx_tracts25 %>%
  group_by(StateFIPS) %>%
  summarize(
    TotTracts = n(),
    
    # Number of tracts within 30-minute drive
    RxCtTmDr  = sum(RxInRangeDr30,  na.rm = TRUE),
    RxCtTmDr2 = sum(RxInRangeDr302, na.rm = TRUE),
    
    # Percent of tracts within 30-minute drive
    RxTmDrP  = (RxCtTmDr  / TotTracts) * 100,
    RxTmDrP2 = (RxCtTmDr2 / TotTracts) * 100,
    
    # Average drive time
    RxAvTmDr  = mean(RxTmDr,  na.rm = TRUE),
    RxAvTmDr2 = mean(RxTmDr2, na.rm = TRUE)
  ) %>%
  ungroup() %>%
  select(
    StateFIPS, TotTracts,
    RxCtTmDr, RxCtTmDr2,
    RxTmDrP, RxTmDrP2,
    RxAvTmDr, RxAvTmDr2
  )

head(Rx_states25)
summary(Rx_states25)
dim(Rx_states25)

# Create state-level HEROP_ID
Rx_states25$HEROP_ID <- paste0("040US", Rx_states25$StateFIPS)

glimpse(Rx_states25)

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
state.Rx <- merge(state.sf2, Rx_states25, by = "HEROP_ID")

dim(state.Rx)
head(state.Rx)

# Maps
tm_shape(state.Rx) + tm_polygons("RxAvTmDr", style = "jenks")
tm_shape(state.Rx) + tm_fill("RxAvTmDr", style = "jenks")
tm_shape(state.Rx) + tm_fill("RxTmDrP2", style = "jenks")
tm_shape(state.Rx) + tm_fill("RxTmDrP", style = "jenks")
tm_shape(state.Rx) + tm_fill("RxCtTmDr2", style = "jenks")
tm_shape(state.Rx) + tm_fill("RxCtTmDr", style = "jenks")
tm_shape(state.Rx) + tm_fill("TotTracts", style = "jenks")

# Drop geometry for CSV export
state.Rx.save <- st_drop_geometry(state.Rx)

state.Rx.save <- state.Rx.save %>%
  select(
    HEROP_ID, GEOID,
    TotTracts,
    RxCtTmDr, RxCtTmDr2,
    RxTmDrP, RxTmDrP2,
    RxAvTmDr, RxAvTmDr2
  )

# Round numeric columns to 2 decimals
state.Rx.save2 <- state.Rx.save %>%
  mutate(across(where(is.numeric), ~ round(.x, 2)))

head(state.Rx.save2)
dim(state.Rx.save2)

# Export CSV
write.csv(
  state.Rx.save2,
  "C:/Users/adrit/Downloads/PharmacyState-2025.csv",
  row.names = FALSE
)

