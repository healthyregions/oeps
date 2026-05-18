library(tidyverse)

# Open tract-level Methadone travel time data (2025)
Met_tracts25 <- read.csv("C:/Users/adrit/Downloads/Met-2025.csv")
head(Met_tracts25)
summary(Met_tracts25)
# Flag tracts with Methadone within 30-minute drive
Met_tracts25$MetInRangeDr30 = ifelse(Met_tracts25$MetTmDr < 30, 1, 0)
Met_tracts25$MetInRangeDr302 = ifelse(Met_tracts25$MetTmDr2 < 30, 1, 0)

summary(Met_tracts25)
glimpse(Met_tracts25)

# Add correct county FIPS (strip tract from GEOID)
Met_tracts25$CountyFIPS <- str_sub(Met_tracts25$HEROP_ID, 6, -7)
head(Met_tracts25)

Met_counties25 <- Met_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(
    
    TotTracts = n(),
    
    # --- Coverage: # tracts within 30-min drive
    MetCtTmDr  = sum(MetInRangeDr30,  na.rm = TRUE),
    MetCtTmDr2 = sum(MetInRangeDr302, na.rm = TRUE),
    
    # --- Coverage: % tracts within 30-min drive
    MetTmDrP  = (MetCtTmDr  / TotTracts) * 100,
    MetTmDrP2 = (MetCtTmDr2 / TotTracts) * 100,
    
    # Average driving time
    MetAvTmDr = mean(MetTmDr, na.rm = TRUE),
    MetAvTmDr2 = mean(MetTmDr2, na.rm = TRUE)
  ) %>%
  select(
    CountyFIPS,
    MetCtTmDr, MetCtTmDr2,
    MetTmDrP, MetTmDrP2,
    MetAvTmDr, MetAvTmDr2
  )

head(Met_counties25)
summary(Met_counties25)
dim(Met_counties25)  # should be ~3590

Met_counties25$HEROP_ID <- paste0("050US", Met_counties25$CountyFIPS)
glimpse(Met_counties25)


library(sf)

county.sf <- st_read(
  "https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2020-500k.geojson"
)

county.sf2 <- select(county.sf, HEROP_ID, NAMELSAD, STUSPS, GEOID)
dim(county.sf2)  # ~3234

county.Met <- merge(county.sf2, Met_counties25, by = "HEROP_ID")
dim(county.Met)  # ~3234
head(county.Met)


library(tmap)

tm_shape(county.Met) + tm_fill("MetAvTmDr", style = "jenks")
tm_shape(county.Met) + tm_fill("MetTmDrP2", style = "jenks")
tm_shape(county.Met) + tm_fill("MetTmDrP", style = "jenks")
tm_shape(county.Met) + tm_fill("MetCtTmDr2", style = "jenks")
tm_shape(county.Met) + tm_fill("MetCtTmDr", style = "jenks")
tm_shape(county.Met) + tm_fill("TotTracts", style = "jenks")

county.Met.save <- st_drop_geometry(county.Met)

county.Met.save <- select(
  county.Met.save,
  HEROP_ID, GEOID,
  MetCtTmDr, MetCtTmDr2,
  MetTmDrP, MetTmDrP2,
  MetAvTmDr, MetAvTmDr2
)

# Round numeric values to 2 decimals
county.Met.save2 <- county.Met.save %>%
  mutate(across(where(is.numeric), round, 2))

head(county.Met.save2)
dim(county.Met.save2)  # ~3234

write.csv(
  county.Met.save2,
  "C:/Users/adrit/Downloads/Met_County25.csv",
  row.names = FALSE
)


