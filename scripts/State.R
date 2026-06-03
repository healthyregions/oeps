library(tidyverse)
library(sf)
library(tmap)

Nalt_tracts25 <- read.csv("/Users/sanket/Documents/Herop/Nalt-2025.csv")

head(Nalt_tracts25)
summary(Nalt_tracts25)
glimpse(Nalt_tracts25)

# Flag tracts with Nalt Testing Facility within 30-minute drive
Nalt_tracts25$NaltInRangeDr30  <- ifelse(Nalt_tracts25$NaltTmDr < 30, 1, 0)
Nalt_tracts25$NaltInRangeDr302 <- ifelse(Nalt_tracts25$NaltTmDr2 < 30, 1, 0)

# Extract State FIPS from tract HEROP_ID
Nalt_tracts25$StateFIPS <- str_sub(Nalt_tracts25$HEROP_ID, 6, 7)

head(Nalt_tracts25)

# Aggregate tract-level data to state level
Nalt_states25 <- Nalt_tracts25 %>%
  group_by(StateFIPS) %>%
  summarize(
    TotTracts = n(),
    
    # Number of tracts within 30-minute drive
    NaltCtTmDr  = sum(NaltInRangeDr30,  na.rm = TRUE),
    NaltCtTmDr2 = sum(NaltInRangeDr302, na.rm = TRUE),
    
    # Percent of tracts within 30-minute drive
    NaltTmDrP  = (NaltCtTmDr  / TotTracts) * 100,
    NaltTmDrP2 = (NaltCtTmDr2 / TotTracts) * 100,
    
    # Average drive time
    NaltAvTmDr  = mean(NaltTmDr,  na.rm = TRUE),
    NaltAvTmDr2 = mean(NaltTmDr2, na.rm = TRUE)
  ) %>%
  ungroup() %>%
  select(
    StateFIPS, TotTracts,
    NaltCtTmDr, NaltCtTmDr2,
    NaltTmDrP, NaltTmDrP2,
    NaltAvTmDr, NaltAvTmDr2
  )

head(Nalt_states25)
summary(Nalt_states25)
dim(Nalt_states25)

# Create state-level HEROP_ID
Nalt_states25$HEROP_ID <- paste0("040US", Nalt_states25$StateFIPS)

glimpse(Nalt_states25)

# Read state GeoJSON from local computer
state.sf <- st_read("https://herop-geodata.s3.us-east-2.amazonaws.com/census/state-2020-500k.geojson")
#state.sf <- st_read("/Users/sanket/Documents/Herop/state-2020-500k.geojson")
glimpse(state.sf)
names(state.sf)

# Keep only needed columns
state.sf2 <- state.sf %>%
  select(HEROP_ID, NAME, STUSPS, GEOID)

dim(state.sf2)
head(state.sf2)

# Merge state geoNaltry with state Naltrics
state.Nalt <- merge(state.sf2, Nalt_states25, by = "HEROP_ID")

dim(state.Nalt)
head(state.Nalt)

# Maps
tm_shape(state.Nalt) + tm_polygons("NaltAvTmDr", style = "jenks")
tm_shape(state.Nalt) + tm_fill("NaltAvTmDr", style = "jenks")
tm_shape(state.Nalt) + tm_fill("NaltTmDrP2", style = "jenks")
tm_shape(state.Nalt) + tm_fill("NaltTmDrP", style = "jenks")
tm_shape(state.Nalt) + tm_fill("NaltCtTmDr2", style = "jenks")
tm_shape(state.Nalt) + tm_fill("NaltCtTmDr", style = "jenks")
tm_shape(state.Nalt) + tm_fill("TotTracts", style = "jenks")

# Drop geoNaltry for CSV export
state.Nalt.save <- st_drop_geometry(state.Nalt)

state.Nalt.save <- state.Nalt.save %>%
  select(
    HEROP_ID, GEOID,
    TotTracts,
    NaltCtTmDr, NaltCtTmDr2,
    NaltTmDrP, NaltTmDrP2,
    NaltAvTmDr, NaltAvTmDr2
  )

# Round numeric columns to 2 decimals
state.Nalt.save2 <- state.Nalt.save %>%
  mutate(across(where(is.numeric), ~ round(.x, 2)))

head(state.Nalt.save2)
dim(state.Nalt.save2)

# Export CSV

write.csv(
  state.Nalt.save2,
  "/Users/sanket/Documents/Herop/State/Nalt State-2025.csv",
  row.names = FALSE
)

