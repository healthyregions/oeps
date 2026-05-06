library(tidyverse)

# Open tract-level HIV Testing Facility travel time data (2025)
Hiv_tracts25 <- read.csv("C:/Users/adrit/Downloads/HIV-Tract-2025.csv")
head(Hiv_tracts25)
summary(Hiv_tracts25)
# Flag tracts with HIV Testing Facility within 30-minute drive
Hiv_tracts25$HivInRangeDr30 = ifelse(Hiv_tracts25$HivTmDr < 30, 1, 0)
Hiv_tracts25$HivInRangeDr302 = ifelse(Hiv_tracts25$HivTmDr2 < 30, 1, 0)

summary(Hiv_tracts25)
glimpse(Hiv_tracts25)

# Add correct county FIPS (strip tract from GEOID)
Hiv_tracts25$CountyFIPS <- str_sub(Hiv_tracts25$HEROP_ID, 6, -7)
head(Hiv_tracts25)

Hiv_counties25 <- Hiv_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(
    
    TotTracts = n(),
    
    # --- Coverage: # tracts within 30-min drive
    HivCtTmDr  = sum(HivInRangeDr30,  na.rm = TRUE),
    HivCtTmDr2 = sum(HivInRangeDr302, na.rm = TRUE),
    
    # --- Coverage: % tracts within 30-min drive
    HivTmDrP  = (HivCtTmDr  / TotTracts) * 100,
    HivTmDrP2 = (HivCtTmDr2 / TotTracts) * 100,
    
    # Average driving time
    HivAvTmDr = mean(HivTmDr, na.rm = TRUE),
    HivAvTmDr2 = mean(HivTmDr2, na.rm = TRUE)
  ) %>%
  select(
    CountyFIPS, TotTracts,
    HivCtTmDr, HivCtTmDr2,
    HivTmDrP, HivTmDrP2,
    HivAvTmDr, HivAvTmDr2
  )

head(Hiv_counties25)
summary(Hiv_counties25)
dim(Hiv_counties25)  # should be ~3590

Hiv_counties25$HEROP_ID <- paste0("050US", Hiv_counties25$CountyFIPS)
glimpse(Hiv_counties25)


library(sf)

county.sf <- st_read(
  "https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2020-500k.geojson"
)

county.sf2 <- select(county.sf, HEROP_ID, NAMELSAD, STUSPS, GEOID)
dim(county.sf2)  # ~3234

county.Hiv <- merge(county.sf2, Hiv_counties25, by = "HEROP_ID")
dim(county.Hiv)  # ~3234
head(county.Hiv)


library(tmap)

tm_shape(county.Hiv) + tm_polygons("HivAvTmDr", style = "jenks")
tm_shape(county.Hiv) + tm_fill("HivAvTmDr", style = "jenks")
tm_shape(county.Hiv) + tm_fill("HivTmDrP2", style = "jenks")
tm_shape(county.Hiv) + tm_fill("HivTmDrP", style = "jenks")
tm_shape(county.Hiv) + tm_fill("HivCtTmDr2", style = "jenks")
tm_shape(county.Hiv) + tm_fill("HivCtTmDr", style = "jenks")
tm_shape(county.Hiv) + tm_fill("TotTracts", style = "jenks")

county.Hiv.save <- st_drop_geometry(county.Hiv)

county.Hiv.save <- select(
  county.Hiv.save,
  HEROP_ID, GEOID,
  TotTracts,
  HivCtTmDr, HivCtTmDr2,
  HivTmDrP, HivTmDrP2,
  HivAvTmDr, HivAvTmDr2
)

# Round numeric values to 2 decimals
county.Hiv.save2 <- county.Hiv.save %>%
  mutate(across(where(is.numeric), round, 2))

head(county.Hiv.save2)
dim(county.Hiv.save2)  # ~3234

write.csv(
  county.Hiv.save2,
  "C:/Users/adrit/Downloads/HIV Testing Facility-county-2025.csv",
  row.names = FALSE
)