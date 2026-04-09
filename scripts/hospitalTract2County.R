library(tidyverse)

# Open tract-level Hospital travel time data (2025)
Hosp_tracts25 <- read.csv("C:/Users/adrit/Downloads/Hospital-Tract-2025.csv")
head(Hosp_tracts25)
summary(Hosp_tracts25)
# Flag tracts with Hospital within 30-minute drive
Hosp_tracts25$HospInRangeDr30 = ifelse(Hosp_tracts25$HospTmDr < 30, 1, 0)
Hosp_tracts25$HospInRangeDr302 = ifelse(Hosp_tracts25$HospTmDr2 < 30, 1, 0)

summary(Hosp_tracts25)
glimpse(Hosp_tracts25)

# Add correct county FIPS (strip tract from GEOID)
Hosp_tracts25$CountyFIPS <- str_sub(Hosp_tracts25$HEROP_ID, 6, -7)
head(Hosp_tracts25)

Hosp_counties25 <- Hosp_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(
    
    TotTracts = n(),
    
    # --- Coverage: # tracts within 30-min drive
    HospCtTmDr  = sum(HospInRangeDr30,  na.rm = TRUE),
    HospCtTmDr2 = sum(HospInRangeDr302, na.rm = TRUE),
    
    # --- Coverage: % tracts within 30-min drive
    HospTmDrP  = (HospCtTmDr  / TotTracts) * 100,
    HospTmDrP2 = (HospCtTmDr2 / TotTracts) * 100,
    
    # Average driving time
    HospAvTmDr = mean(HospTmDr, na.rm = TRUE),
    HospAvTmDr2 = mean(HospTmDr2, na.rm = TRUE)
  ) %>%
  select(
    CountyFIPS, TotTracts,
    HospCtTmDr, HospCtTmDr2,
    HospTmDrP, HospTmDrP2,
    HospAvTmDr, HospAvTmDr2
  )

head(Hosp_counties25)
summary(Hosp_counties25)
dim(Hosp_counties25)  # should be ~3590

Hosp_counties25$HEROP_ID <- paste0("050US", Hosp_counties25$CountyFIPS)
glimpse(Hosp_counties25)


library(sf)

county.sf <- st_read(
  "https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2020-500k.geojson"
)

county.sf2 <- select(county.sf, HEROP_ID, NAMELSAD, STUSPS, GEOID)
dim(county.sf2)  # ~3234

county.Hosp <- merge(county.sf2, Hosp_counties25, by = "HEROP_ID")
dim(county.Hosp)  # ~3234
head(county.Hosp)


library(tmap)

tm_shape(county.Hosp) + tm_polygons("HospAvTmDr", style = "jenks")
tm_shape(county.Hosp) + tm_fill("HospAvTmDr", style = "jenks")
tm_shape(county.Hosp) + tm_fill("HospTmDrP2", style = "jenks")
tm_shape(county.Hosp) + tm_fill("HospTmDrP", style = "jenks")
tm_shape(county.Hosp) + tm_fill("HospCtTmDr2", style = "jenks")
tm_shape(county.Hosp) + tm_fill("HospCtTmDr", style = "jenks")
tm_shape(county.Hosp) + tm_fill("TotTracts", style = "jenks")

county.Hosp.save <- st_drop_geometry(county.Hosp)

county.Hosp.save <- select(
  county.Hosp.save,
  HEROP_ID, GEOID,
  TotTracts,
  HospCtTmDr, HospCtTmDr2,
  HospTmDrP, HospTmDrP2,
  HospAvTmDr, HospAvTmDr2
)

# Round numeric values to 2 decimals
county.Hosp.save2 <- county.Hosp.save %>%
  mutate(across(where(is.numeric), round, 2))

head(county.Hosp.save2)
dim(county.Hosp.save2)  # ~3234

write.csv(
  county.Hosp.save2,
  "C:/Users/adrit/Downloads/Hospital-county-2025.csv",
  row.names = FALSE
)
