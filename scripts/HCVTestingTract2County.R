library(tidyverse)

# Open tract-level HCV Testing Facility travel time data (2025)
hcv_tracts25 <- read.csv("C:/Users/adrit/Downloads/HCV-Tract-2025.csv")
head(hcv_tracts25)
summary(hcv_tracts25)
# Flag tracts with HCV Testing Facility within 30-minute drive
hcv_tracts25$hcvInRangeDr30 = ifelse(hcv_tracts25$HcvTmDr < 30, 1, 0)
hcv_tracts25$hcvInRangeDr302 = ifelse(hcv_tracts25$HcvTmDr2 < 30, 1, 0)

summary(hcv_tracts25)
glimpse(hcv_tracts25)

# Add correct county FIPS (strip tract from GEOID)
hcv_tracts25$CountyFIPS <- str_sub(hcv_tracts25$HEROP_ID, 6, -7)
head(hcv_tracts25)

hcv_counties25 <- hcv_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(
    
    TotTracts = n(),
    
    # --- Coverage: # tracts within 30-min drive
    HcvCtTmDr  = sum(hcvInRangeDr30,  na.rm = TRUE),
    HcvCtTmDr2 = sum(hcvInRangeDr302, na.rm = TRUE),
    
    # --- Coverage: % tracts within 30-min drive
    HcvTmDrP  = (HcvCtTmDr  / TotTracts) * 100,
    HcvTmDrP2 = (HcvCtTmDr2 / TotTracts) * 100,
    
    # Average driving time
    HcvAvTmDr = mean(HcvTmDr, na.rm = TRUE),
    HcvAvTmDr2 = mean(HcvTmDr2, na.rm = TRUE)
  ) %>%
  select(
    CountyFIPS, TotTracts,
    HcvCtTmDr, HcvCtTmDr2,
    HcvTmDrP, HcvTmDrP2,
    HcvAvTmDr, HcvAvTmDr2
  )

head(hcv_counties25)
summary(hcv_counties25)
dim(hcv_counties25)  # should be ~3590

hcv_counties25$HEROP_ID <- paste0("050US", hcv_counties25$CountyFIPS)
glimpse(hcv_counties25)


library(sf)

county.sf <- st_read(
  "https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2020-500k.geojson"
)

county.sf2 <- select(county.sf, HEROP_ID, NAMELSAD, STUSPS, GEOID)
dim(county.sf2)  # ~3234

county.hcv <- merge(county.sf2, hcv_counties25, by = "HEROP_ID")
dim(county.hcv)  # ~3234
head(county.hcv)


library(tmap)

tm_shape(county.hcv) + tm_fill("HcvAvTmDr", style = "jenks")
tm_shape(county.hcv) + tm_fill("HcvTmDrP2", style = "jenks")
tm_shape(county.hcv) + tm_fill("HcvTmDrP", style = "jenks")
tm_shape(county.hcv) + tm_fill("HcvCtTmDr2", style = "jenks")
tm_shape(county.hcv) + tm_fill("HcvCtTmDr", style = "jenks")
tm_shape(county.hcv) + tm_fill("TotTracts", style = "jenks")

county.hcv.save <- st_drop_geometry(county.hcv)

county.hcv.save <- select(
  county.hcv.save,
  HEROP_ID, GEOID,
  TotTracts,
  HcvCtTmDr, HcvCtTmDr2,
  HcvTmDrP, HcvTmDrP2,
  HcvAvTmDr, HcvAvTmDr2
)

# Round numeric values to 2 decimals
county.hcv.save2 <- county.hcv.save %>%
  mutate(across(where(is.numeric), round, 2))

head(county.hcv.save2)
dim(county.hcv.save2)  # ~3234

write.csv(
  county.hcv.save2,
  "C:/Users/adrit/Downloads/HCV Testing Facility-county-2025.csv",
  row.names = FALSE
)


