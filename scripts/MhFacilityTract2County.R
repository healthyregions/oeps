library(tidyverse)

# Open tract-level Mental Health Facility travel time data (2025)
Mh_tracts25 <- read.csv("C:/Users/adrit/Downloads/MhFacility-Tract25.csv")
head(Mh_tracts25)
summary(Mh_tracts25)
# Flag tracts with Mental Health Facility within 30-minute drive
Mh_tracts25$MhInRangeDr30 = ifelse(Mh_tracts25$MhTmDr < 30, 1, 0)
Mh_tracts25$MhInRangeDr302 = ifelse(Mh_tracts25$MhTmDr2 < 30, 1, 0)

summary(Mh_tracts25)
glimpse(Mh_tracts25)

# Add correct county FIPS (strip tract from GEOID)
Mh_tracts25$CountyFIPS <- str_sub(Mh_tracts25$HEROP_ID, 6, -7)
head(Mh_tracts25)

Mh_counties25 <- Mh_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(
    
    TotTracts = n(),
    
    # --- Coverage: # tracts within 30-min drive
    MhCtTmDr  = sum(MhInRangeDr30,  na.rm = TRUE),
    MhCtTmDr2 = sum(MhInRangeDr302, na.rm = TRUE),
    
    # --- Coverage: % tracts within 30-min drive
    MhTmDrP  = (MhCtTmDr  / TotTracts) * 100,
    MhTmDrP2 = (MhCtTmDr2 / TotTracts) * 100,
    
    # Average driving time
    MhAvTmDr = mean(MhTmDr, na.rm = TRUE),
    MhAvTmDr2 = mean(MhTmDr2, na.rm = TRUE)
  ) %>%
  select(
    CountyFIPS, TotTracts,
    MhCtTmDr, MhCtTmDr2,
    MhTmDrP, MhTmDrP2,
    MhAvTmDr, MhAvTmDr2
  )

head(Mh_counties25)
summary(Mh_counties25)
dim(Mh_counties25)  # should be ~3590

Mh_counties25$HEROP_ID <- paste0("050US", Mh_counties25$CountyFIPS)
glimpse(Mh_counties25)


library(sf)

county.sf <- st_read(
  "https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2020-500k.geojson"
)

county.sf2 <- select(county.sf, HEROP_ID, NAMELSAD, STUSPS, GEOID)
dim(county.sf2)  # ~3234

county.Mh <- merge(county.sf2, Mh_counties25, by = "HEROP_ID")
dim(county.Mh)  # ~3234
head(county.Mh)


library(tmap)

tm_shape(county.Mh) + tm_fill("MhAvTmDr", style = "jenks")
tm_shape(county.Mh) + tm_fill("MhTmDrP2", style = "jenks")
tm_shape(county.Mh) + tm_fill("MhTmDrP", style = "jenks")
tm_shape(county.Mh) + tm_fill("MhCtTmDr2", style = "jenks")
tm_shape(county.Mh) + tm_fill("MhCtTmDr", style = "jenks")
tm_shape(county.Mh) + tm_fill("TotTracts", style = "jenks")

county.Mh.save <- st_drop_geometry(county.Mh)

county.Mh.save <- select(
  county.Mh.save,
  HEROP_ID, GEOID,
  TotTracts,
  MhCtTmDr, MhCtTmDr2,
  MhTmDrP, MhTmDrP2,
  MhAvTmDr, MhAvTmDr2
)

# Round numeric values to 2 decimals
county.Mh.save2 <- county.Mh.save %>%
  mutate(across(where(is.numeric), round, 2))

head(county.Mh.save2)
dim(county.Mh.save2)  # ~3234

write.csv(
  county.Mh.save2,
  "C:/Users/adrit/Downloads/MhFacility-county25.csv",
  row.names = FALSE
)


