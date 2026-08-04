library(tidyverse)

# Open tract-level OTP travel time data (2025)
Otp_tracts25 <- read.csv("C:/Users/adrit/Downloads/OTP-2025.csv")
head(Otp_tracts25)
summary(Otp_tracts25)
# Flag tracts with OTP within 30-minute drive
Otp_tracts25$OtpInRangeDr30 = ifelse(Otp_tracts25$OtpTmDr < 30, 1, 0)
Otp_tracts25$OtpInRangeDr302 = ifelse(Otp_tracts25$OtpTmDr2 < 30, 1, 0)

summary(Otp_tracts25)
glimpse(Otp_tracts25)

# Add correct county FIPS (strip tract from GEOID)
Otp_tracts25$CountyFIPS <- str_sub(Otp_tracts25$HEROP_ID, 6, -7)
head(Otp_tracts25)

Otp_counties25 <- Otp_tracts25 %>%
  group_by(CountyFIPS) %>%
  summarize(
    
    TotTracts = n(),
    
    # --- Coverage: # tracts within 30-min drive
    OtpCtTmDr  = sum(OtpInRangeDr30,  na.rm = TRUE),
    OtpCtTmDr2 = sum(OtpInRangeDr302, na.rm = TRUE),
    
    # --- Coverage: % tracts within 30-min drive
    OtpTmDrP  = (OtpCtTmDr  / TotTracts) * 100,
    OtpTmDrP2 = (OtpCtTmDr2 / TotTracts) * 100,
    
    # Average driving time
    OtpAvTmDr = mean(OtpTmDr, na.rm = TRUE),
    OtpAvTmDr2 = mean(OtpTmDr2, na.rm = TRUE)
  ) %>%
  select(
    CountyFIPS,
    OtpCtTmDr, OtpCtTmDr2,
    OtpTmDrP, OtpTmDrP2,
    OtpAvTmDr, OtpAvTmDr2
  )

head(Otp_counties25)
summary(Otp_counties25)
dim(Otp_counties25)  # should be ~3590

Otp_counties25$HEROP_ID <- paste0("050US", Otp_counties25$CountyFIPS)
glimpse(Otp_counties25)


library(sf)

county.sf <- st_read(
  "https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2020-500k.geojson"
)

county.sf2 <- select(county.sf, HEROP_ID, NAMELSAD, STUSPS, GEOID)
dim(county.sf2)  # ~3234

county.Otp <- merge(county.sf2, Otp_counties25, by = "HEROP_ID")
dim(county.Otp)  # ~3234
head(county.Otp)


library(tmap)

tm_shape(county.Otp) + tm_fill("OtpAvTmDr", style = "jenks")
tm_shape(county.Otp) + tm_fill("OtpTmDrP2", style = "jenks")
tm_shape(county.Otp) + tm_fill("OtpTmDrP", style = "jenks")
tm_shape(county.Otp) + tm_fill("OtpCtTmDr2", style = "jenks")
tm_shape(county.Otp) + tm_fill("OtpCtTmDr", style = "jenks")
tm_shape(county.Otp) + tm_fill("TotTracts", style = "jenks")

county.Otp.save <- st_drop_geometry(county.Otp)

county.Otp.save <- select(
  county.Otp.save,
  HEROP_ID, GEOID,
  OtpCtTmDr, OtpCtTmDr2,
  OtpTmDrP, OtpTmDrP2,
  OtpAvTmDr, OtpAvTmDr2
)

# Round numeric values to 2 decimals
county.Otp.save2 <- county.Otp.save %>%
  mutate(across(where(is.numeric), round, 2))

head(county.Otp.save2)
dim(county.Otp.save2)  # ~3234

write.csv(
  county.Otp.save2,
  "C:/Users/adrit/Downloads/Otp_County25.csv",
  row.names = FALSE
)


