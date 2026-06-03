library(tidyverse)

# Open tract-level Sut Testing Facility travel time data (2025)
Sut_tracts25 <- read.csv("/Users/sanket/Documents/Herop/SUT-2025.csv")
head(Sut_tracts25)
summary(Sut_tracts25)
# Flag tracts with Sut Testing Facility within 30-minute drive
Sut_tracts25$SutInRangeDr30 = ifelse(Sut_tracts25$SutTmDr < 30, 1, 0)
Sut_tracts25$SutInRangeDr302 = ifelse(Sut_tracts25$SutTmDr2 < 30, 1, 0)

summary(Sut_tracts25)
glimpse(Sut_tracts25)

# Add correct county FIPS (strip tract from GEOID)
Sut_tracts25$CountyFIPS <- str_sub(Sut_tracts25$HEROP_ID, 6, -7)
head(Sut_tracts25)

Sut_counties25 <- Sut_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(
    
    TotTracts = n(),
    
    # --- Coverage: # tracts within 30-min drive
    SutCtTmDr  = sum(SutInRangeDr30,  na.rm = TRUE),
    SutCtTmDr2 = sum(SutInRangeDr302, na.rm = TRUE),
    
    # --- Coverage: % tracts within 30-min drive
    SutTmDrP  = (SutCtTmDr  / TotTracts) * 100,
    SutTmDrP2 = (SutCtTmDr2 / TotTracts) * 100,
    
    # Average driving time
    SutAvTmDr = mean(SutTmDr, na.rm = TRUE),
    SutAvTmDr2 = mean(SutTmDr2, na.rm = TRUE)
  ) %>%
  select(
    CountyFIPS, TotTracts,
    SutCtTmDr, SutCtTmDr2,
    SutTmDrP, SutTmDrP2,
    SutAvTmDr, SutAvTmDr2
  )

head(Sut_counties25)
summary(Sut_counties25)
dim(Sut_counties25)  # should be ~3590

Sut_counties25$HEROP_ID <- paste0("050US", Sut_counties25$CountyFIPS)
glimpse(Sut_counties25)


library(sf)

county.sf <- st_read(
  "https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2020-500k.geojson"
)

county.sf2 <- select(county.sf, HEROP_ID, NAMELSAD, STUSPS, GEOID)
dim(county.sf2)  # ~3234

county.Sut <- merge(county.sf2, Sut_counties25, by = "HEROP_ID")
dim(county.Sut)  # ~3234
head(county.Sut)


library(tmap)

tm_shape(county.Sut) + tm_polygons("SutAvTmDr", style = "jenks")
tm_shape(county.Sut) + tm_fill("SutAvTmDr", style = "jenks")
tm_shape(county.Sut) + tm_fill("SutTmDrP2", style = "jenks")
tm_shape(county.Sut) + tm_fill("SutTmDrP", style = "jenks")
tm_shape(county.Sut) + tm_fill("SutCtTmDr2", style = "jenks")
tm_shape(county.Sut) + tm_fill("SutCtTmDr", style = "jenks")
tm_shape(county.Sut) + tm_fill("TotTracts", style = "jenks")

county.Sut.save <- st_drop_geometry(county.Sut)

county.Sut.save <- select(
  county.Sut.save,
  HEROP_ID, GEOID,
  TotTracts,
  SutCtTmDr, SutCtTmDr2,
  SutTmDrP, SutTmDrP2,
  SutAvTmDr, SutAvTmDr2
)

# Round numeric values to 2 decimals
county.Sut.save2 <- county.Sut.save %>%
  mutate(across(where(is.numeric), round, 2))

head(county.Sut.save2)
dim(county.Sut.save2)  # ~3234

write.csv(
  county.Sut.save2,
  "/Users/sanket/Documents/Herop/SUT County-2025.csv",
  row.names = FALSE
)

