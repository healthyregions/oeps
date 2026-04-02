library(tidyverse)
library(sf)
library(tmap)

Fqhc_tracts25 <- read.csv("C:/Users/adrit/Documents/tract_fqhc_access_2025.csv")

head(Fqhc_tracts25)
summary(Fqhc_tracts25)
glimpse(Fqhc_tracts25)

# Flag tracts with Fqhc within 30-minute drive
Fqhc_tracts25$FqhcInRangeDr30  <- ifelse(Fqhc_tracts25$FqhcTmDr < 30, 1, 0)
Fqhc_tracts25$FqhcInRangeDr302 <- ifelse(Fqhc_tracts25$FqhcTmDr2 < 30, 1, 0)

# Extract State FIPS from tract HEROP_ID
Fqhc_tracts25$StateFIPS <- str_sub(Fqhc_tracts25$HEROP_ID, 6, 7)

head(Fqhc_tracts25)

# Aggregate tract-level data to state level
Fqhc_states25 <- Fqhc_tracts25 %>%
  group_by(StateFIPS) %>%
  summarize(
    TotTracts = n(),
    
    # Number of tracts within 30-minute drive
    FqhcCtTmDr  = sum(FqhcInRangeDr30,  na.rm = TRUE),
    FqhcCtTmDr2 = sum(FqhcInRangeDr302, na.rm = TRUE),
    
    # Percent of tracts within 30-minute drive
    FqhcTmDrP  = (FqhcCtTmDr  / TotTracts) * 100,
    FqhcTmDrP2 = (FqhcCtTmDr2 / TotTracts) * 100,
    
    # Average drive time
    FqhcAvTmDr  = mean(FqhcTmDr,  na.rm = TRUE),
    FqhcAvTmDr2 = mean(FqhcTmDr2, na.rm = TRUE)
  ) %>%
  ungroup() %>%
  select(
    StateFIPS, TotTracts,
    FqhcCtTmDr, FqhcCtTmDr2,
    FqhcTmDrP, FqhcTmDrP2,
    FqhcAvTmDr, FqhcAvTmDr2
  )

head(Fqhc_states25)
summary(Fqhc_states25)
dim(Fqhc_states25)

# Create state-level HEROP_ID
Fqhc_states25$HEROP_ID <- paste0("040US", Fqhc_states25$StateFIPS)

glimpse(Fqhc_states25)

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
state.Fqhc <- merge(state.sf2, Fqhc_states25, by = "HEROP_ID")

dim(state.Fqhc)
head(state.Fqhc)

# Maps
tm_shape(state.Fqhc) + tm_polygons("FqhcAvTmDr", style = "jenks")
tm_shape(state.Fqhc) + tm_fill("FqhcAvTmDr", style = "jenks")
tm_shape(state.Fqhc) + tm_fill("FqhcTmDrP2", style = "jenks")
tm_shape(state.Fqhc) + tm_fill("FqhcTmDrP", style = "jenks")
tm_shape(state.Fqhc) + tm_fill("FqhcCtTmDr2", style = "jenks")
tm_shape(state.Fqhc) + tm_fill("FqhcCtTmDr", style = "jenks")
tm_shape(state.Fqhc) + tm_fill("TotTracts", style = "jenks")

# Drop geometry for CSV export
state.Fqhc.save <- st_drop_geometry(state.Fqhc)

state.Fqhc.save <- state.Fqhc.save %>%
  select(
    HEROP_ID, GEOID,
    TotTracts,
    FqhcCtTmDr, FqhcCtTmDr2,
    FqhcTmDrP, FqhcTmDrP2,
    FqhcAvTmDr, FqhcAvTmDr2
  )

# Round numeric columns to 2 decimals
state.Fqhc.save2 <- state.Fqhc.save %>%
  mutate(across(where(is.numeric), ~ round(.x, 2)))

head(state.Fqhc.save2)
dim(state.Fqhc.save2)

# Export CSV
write.csv(
  state.Fqhc.save2,
  "C:/Users/adrit/Downloads/FqhcState-2025.csv",
  row.names = FALSE
)
