setwd("~/Code/oeps2/scripts")

library(tidyverse)

# Open tract-level pharmacy travel time data (2025)
Rx_tracts25 <- read.csv("C:/Users/adrit/Downloads/pharmacy-tract-2025 (2).csv")
head(Rx_tracts25)

# Flag tracts with pharmacy within 30-minute drive
Rx_tracts25$RxTmDr <- ifelse(Rx_tracts25$RxTmDr < 30, 1, 0)
Rx_tracts25$RxTmDr2 <- ifelse(Rx_tracts25$RxTmDr2 < 30, 1, 0)

summary(Rx_tracts25)
glimpse(Rx_tracts25)

# Add correct county FIPS (strip tract from GEOID)
Rx_tracts25$CountyFIPS <- str_sub(Rx_tracts25$HEROP_ID, 6, -7)
head(HRx_tracts25)

Rx_counties25 <- Rx_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(
    TotTracts = n(),
    
    # Tracts with pharmacy access
    RxTmDr = sum(RxTmDr, na.rm = TRUE),
    RxTmDr2 = sum(RxTmDr2, na.rm = TRUE),
    
    # Percent of tracts with access
    RxTmDrP = (RxTmDr / TotTracts) * 100,
    RxTmDrP2 = (RxTmDr2 / TotTracts) * 100,
    
    # Average driving time
    RxAvTmDr = mean(RxTmDr, na.rm = TRUE),
    RxAvTmDr2 = mean(RxTmDr2, na.rm = TRUE)
  ) %>%
  select(
    CountyFIPS, TotTracts,
    RxTmDr, RxTmDr2,
    RxTmDrP, RxTmDrP2,
    RxAvTmDr, RxAvTmDr2
  )

head(Rx_counties25)
dim(Rx_counties25)  # should be ~3590

Rx_counties25$HEROP_ID <- paste0("050US", Rx_counties25$CountyFIPS)
glimpse(Rx_counties25)

library(sf)

county.sf <- st_read(
  "https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2020-500k.geojson"
)

county.sf2 <- select(county.sf, HEROP_ID, NAMELSAD, STUSPS, GEOID)
dim(county.sf2)  # ~3234

county.Rx <- merge(county.sf2, Rx_counties25, by = "HEROP_ID")
dim(county.Rx)  # ~3234
head(county.Rx)

library(tmap)

tm_shape(county.Rx) + tm_fill("RxAvTmDr2", style = "jenks")
tm_shape(county.Rx) + tm_fill("RxAvTmDr", style = "jenks")
tm_shape(county.Rx) + tm_fill("RxTmDrP2", style = "jenks")
tm_shape(county.Rx) + tm_fill("RxTmDrP", style = "jenks")
tm_shape(county.Rx) + tm_fill("RxCtTmDr2", style = "jenks")
tm_shape(county.Rx) + tm_fill("RxCtTmDr", style = "jenks")
tm_shape(county.Rx) + tm_fill("TotTracts", style = "jenks")

county.Rx.save <- st_drop_geometry(county.Rx)

county.Rx.save <- select(
  county.Rx.save,
  HEROP_ID, GEOID,
  TotTracts,
  RxTmDr, RxTmDr2,
  RxTmDrP, RxTmDrP2,
  RxAvTmDr, RxAvTmDr2
)

# Round numeric values to 2 decimals
county.Rx.save2 <- county.Rx.save %>%
  mutate(across(where(is.numeric), round, 2))

head(county.Rx.save2)
dim(county.Rx.save2)  # ~3234

write.csv(
  county.Rx.save2,
  "C:/Users/adrit/Downloads/pharmacy-county-2025.csv",
  row.names = FALSE
)
