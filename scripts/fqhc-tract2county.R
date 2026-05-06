setwd("~/Code/oeps2/scripts")

library(tidyverse)

#open tract measures of fqhc 2025 resources
fqhc_tracts25 <- read.csv("../data/travel-times/fqhc-tract-2025.csv")
head(fqhc_tracts25)

#flag tracts with <30 minutes
fqhc_tracts25$fqhc_driving30 = ifelse(fqhc_tracts25$fqhc_drvingtime < 30, 1, 0)
fqhc_tracts25$fqhc_driving302 = ifelse(fqhc_tracts25$fqhc_drvingtime2 < 30, 1, 0)
head(fqhc_tracts25)

summary(fqhc_tracts25)
glimpse(fqhc_tracts25)

#add correct county id (with leading 0, removing tract IDs)
fqhc_tracts25$CountyFIPS <- str_sub(fqhc_tracts25$HEROP_ID, 6,-7)
head(fqhc_tracts25)

#summarize by county
fqhc_counties25 <- fqhc_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(TotTracts = n(),
            FqhcCtTmDr = sum(fqhc_driving30, na.rm = TRUE),
            FqhcCtTmDr2 = sum(fqhc_driving302, na.rm = TRUE),
            FqhcTmDrP = (FqhcCtTmDr/TotTracts) * 100,
            FqhcTmDrP2 = (FqhcCtTmDr2/TotTracts) * 100,
            FqhcAvTmDr = mean(fqhc_drvingtime, na.rm = TRUE),
            FqhcAvTmDr2 = mean(fqhc_drvingtime2, na.rm = TRUE),
            ) %>%
  select(CountyFIPS, TotTracts, 
         FqhcCtTmDr, FqhcCtTmDr2,
         FqhcTmDrP, FqhcTmDrP2, 
         FqhcAvTmDr,FqhcAvTmDr2)

head(fqhc_counties25)  
dim(fqhc_counties25) #3590. #3234

fqhc_counties25$HEROP_ID <- paste0("050US",fqhc_counties25$CountyFIPS)
glimpse(fqhc_counties25)

library(sf)
county.sf <- st_read("https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2020-500k.geojson")
head(county.sf)

county.sf2 <- select(county.sf,HEROP_ID,NAMELSAD, STUSPS,GEOID )
head(county.sf2)
dim(county.sf2) #3234

glimpse(fqhc_counties25)

county.fqhc <- merge(county.sf2,fqhc_counties25, by="HEROP_ID")
dim(county.fqhc) #3234
head(county.fqhc)

library(tmap)
tmap_mode("view") #this works best for county+
tm_shape(county.fqhc) + tm_fill("FqhcAvTmDr2", style = "jenks") # plot for metadata

tm_shape(county.fqhc) + tm_fill("FqhcAvTmDr", style = "jenks") # plot for metadata
tm_shape(county.fqhc) + tm_fill("FqhcTmDrP2", style = "jenks") # plot for metadata
tm_shape(county.fqhc) + tm_fill("FqhcTmDrP", style = "jenks") # plot for metadata
tm_shape(county.fqhc) + tm_fill("FqhcCtTmDr2", style = "jenks") # plot for metadata
tm_shape(county.fqhc) + tm_fill("FqhcCtTmDr", style = "jenks") # plot for metadata
tm_shape(county.fqhc) + tm_fill("TotTracts", style = "jenks") # plot for metadata

county.fqhc.save <- st_drop_geometry(county.fqhc)
head(county.fqhc.save)

county.fqhc.save <- select(county.fqhc.save,
                           HEROP_ID, GEOID, 
                           TotTracts, FqhcCtTmDr, FqhcCtTmDr2, 
                           FqhcTmDrP, FqhcTmDrP2, 
                           FqhcAvTmDr, FqhcAvTmDr2)
head(county.fqhc.save)

# Format specific columns (e.g., 'var1' and 'var2') to 2 decimal places
county.fqhc.save2 <- county.fqhc.save %>%
  mutate(across(where(is.numeric), round, 2))

head(county.fqhc.save2)
dim(county.fqhc.save2) #3234

write.csv(county.fqhc.save2, "../data/travel-times/fqhc-county-2025.csv",row.names = FALSE)
