setwd("~/Code/oeps2/scripts")

library(tidyverse)

# Open tract-level Hospital travel time data (2025)
Hosp_tracts25 <- read.csv("C:/Users/adrit/Downloads/Hospital-Tract-2025.csv")
head(Hosp_tracts25)

# Flag tracts with Hospital within 30-minute drive
Hosp_tracts25$HospTmDr <- ifelse(Hosp_tracts25$HospTmDr < 30, 1, 0)
Hosp_tracts25$HospTmDr2 <- ifelse(Hosp_tracts25$HospTmDr2 < 30, 1, 0)

summary(Hosp_tracts25)
glimpse(Hosp_tracts25)

# Add correct county FIPS (strip tract from GEOID)
Hosp_tracts25$CountyFIPS <- str_sub(Hosp_tracts25$HEROP_ID, 6, -7)
head(Hosp_tracts25)

Hosp_counties25 <- Hosp_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(
    TotTracts = n(),
    
    # Tracts with Hospital access
    HospTmDr = sum(HospTmDr, na.rm = TRUE),
    HospTmDr2 = sum(HospTmDr2, na.rm = TRUE),
    
    # Percent of tracts with access
    HospTmDrP = (HospTmDr / TotTracts) * 100,
    HospTmDrP2 = (HospTmDr2 / TotTracts) * 100,
    
    # Average driving time
    HospAvTmDr = mean(HospTmDr, na.rm = TRUE),
    HospAvTmDr2 = mean(HospTmDr2, na.rm = TRUE)
  ) %>%
  select(
    CountyFIPS, TotTracts,
    HospTmDr, HospTmDr2,
    HospTmDrP, HospTmDrP2,
    HospAvTmDr, HospAvTmDr2
  )

head(Hosp_counties25)
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

tm_shape(county.Hosp) + tm_fill("HospAvTmDr2", style = "jenks")
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

library(tmap)


my_breaks <- c(0, 1, 21, 101, 250, 500, Inf)

# Update each map layer
tm_shape(county.Hosp) + tm_fill("HospAvTmDr2", style = "fixed", breaks = my_breaks)
tm_shape(county.Hosp) + tm_fill("HospAvTmDr",  style = "fixed", breaks = my_breaks)
tm_shape(county.Hosp) + tm_fill("HospTmDrP2",  style = "fixed", breaks = my_breaks)
tm_shape(county.Hosp) + tm_fill("HospTmDrP",   style = "fixed", breaks = my_breaks)
tm_shape(county.Hosp) + tm_fill("HospCtTmDr2", style = "fixed", breaks = my_breaks)
tm_shape(county.Hosp) + tm_fill("HospCtTmDr",  style = "fixed", breaks = my_breaks)
tm_shape(county.Hosp) + tm_fill("TotTracts", style = "fixed", breaks = my_breaks)


# Define breaks to create 6 classes
# 1: [min, 0], 2: (0, 20], 3: (20, 100], etc.
my_breaks <- c(-Inf, 0, 20, 100, 250, 500, Inf)
my_labels <- c("0", "0.1 - 20", "21 - 100", "101 - 250", "251 - 500", "500+")

# Example for one variable; repeat for others
tm_shape(county.Hosp) + 
  tm_fill("HospAvTmDr2", 
          style = "fixed", 
          breaks = my_breaks,
          labels = my_labels,
          interval.closure = "right", # Ensures 0 is isolated in the first class
          palette = "Reds") +
  tm_layout(legend.outside = TRUE)

