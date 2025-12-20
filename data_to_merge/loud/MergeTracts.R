library(tidyverse)
setwd("~/Code/oeps2/data_to_merge/loud")

commuting <- read.csv("../commuting_tract23.csv")
insurance <- read.csv("../insurance_tract23.csv")
internet <- read.csv("../internet_tract23.csv")

# Commuting in Stage 3
head(commuting)

loud <- commuting %>%
  select(HEROP_ID, GEOID, NoVehHHld, CommTransit,CommWalking)
head(loud)

# Internet in Stage 1
internet.loud <- internet %>%
  select(HEROP_ID,GEOID,CompHhldsP,BbndInternetP)
head(internet.loud)
dim(internet.loud)
loud.df <- merge(loud, internet.loud, by="HEROP_ID")
head(loud.df)


# Insurance in Stage 1
head(insurance)
insurance.loud <- insurance %>%
  select(HEROP_ID,GEOID,InsuredPopP,PrivateInsP,PublicInsP)
head(insurance.loud)
dim(insurance.loud)
loud.df <- merge(loud.df, insurance.loud, by="HEROP_ID")
head(loud.df)


loud.df$NoVehHHldPL <- percent_rank(loud.df$NoVehHHld)
loud.df$CommTransitPL <- percent_rank(loud.df$CommTransit)
loud.df$CommWalkingPL <- percent_rank(loud.df$CommWalking)
loud.df$BbndInternetPPL <- percent_rank(loud.df$BbndInternetP)
loud.df$InsuredPopPPL <- percent_rank(loud.df$InsuredPopP)
loud.df$PrivateInsPPL <- percent_rank(loud.df$PrivateInsP)
loud.df$PublicInsPPL <- percent_rank(loud.df$PublicInsP)

head(loud.df)

#save(loud.df,  file = "loud_staging.RData")


###############

#CensusRate.county <- read.csv("~/Downloads/Social Capital-selected/RspRt_county_2023.csv")
#head(CensusRate.county)

social.capital <- read.csv("~/Downloads/Social Capital-selected/Social_Capital_Measures_2023.csv")
head(social.capital)

social.capital.loud <- social.capital %>%
  select(HEROP_ID,LibPerCap,RlgPerCap, LngTermP,SocCapInd) 

head(social.capital.loud)

social.capital.loud$SocCapIndPL <- percent_rank(social.capital.loud$SocCapInd)
head(social.capital.loud)

loud.df <- merge(loud.df, social.capital.loud, by="HEROP_ID")
head(loud.df)

hist(loud.df$SocCapIndPL)
dim(loud.df) # 83364


### Stage 1 Prep
loud.df$Stage1 <- (loud.df$SocCapIndPL + loud.df$BbndInternetPPL)/2
hist(loud.df$Stage1)
head(loud.df)

save(loud.df,  file = "loud_staging.RData")

####

# Access metrics from summer 2025
# Reading from https://uofi.app.box.com/folder/331413455769

fqhc <- read.csv("~/Downloads/FQHC.csv")
head(fqhc)
summary(fqhc)

# Indicate areas over 90 minutes as 999 = no access
fqhc$FqhcTmDr[is.na(fqhc$FqhcTmDr)] <- 999
head(fqhc)

fqhc$FqhcTmDrPL <- percent_rank(fqhc$FqhcTmDr)
hist(fqhc$FqhcTmDrPL)

fqhc.loud <- select(fqhc, GEOID,FqhcTmDr, FqhcTmDrPL)
head(fqhc.loud)

fqhc.loud$HEROP_ID <- paste0("140US",fqhc.loud$GEOID)

loud.df <- merge(loud.df, fqhc.loud, by="HEROP_ID")
head(loud.df)

save(loud.df,  file = "loud_staging.RData")


####

# Access metrics from summer 2025
# Reading from https://uofi.app.box.com/folder/331413455769

moud <- read.csv("~/Downloads/MOUDS.csv")
head(moud)
summary(moud)
dim(moud)

# Indicate areas over 90 minutes as 999 = no access
moud$MetTmDr[is.na(moud$MetTmDr)] <- 999
moud$MetTmDrPL <- percent_rank(moud$MetTmDr)
head(moud)
hist(moud$MetTmDrPL)

# Indicate areas over 90 minutes as 999 = no access
moud$BupTmDr[is.na(moud$BupTmDr)] <- 999
moud$BupTmDrPL <- percent_rank(moud$BupTmDr)
head(moud)
hist(moud$BupTmDrPL)

# Indicate areas over 90 minutes as 999 = no access
moud$NaltTmDr[is.na(moud$NaltTmDr)] <- 999
moud$NaltTmDrPL <- percent_rank(moud$NaltTmDr)
head(moud)
hist(moud$NaltTmDrPL)

moud$HEROP_ID <- paste0("140US",moud$GEOID)

moud.loud <- moud %>%
  select(HEROP_ID,MetTmDr,MetTmDrPL,BupTmDr,BupTmDrPL,NaltTmDr,NaltTmDrPL)
head(moud.loud)

loud.df <- merge(loud.df, moud.loud, by="HEROP_ID")
head(loud.df)

save(loud.df,  file = "loud_staging.RData")



### Stage 2 Prep
loud.df$Stage2 <- (loud.df$MetTmDrPL + loud.df$BupTmDrPL +
                     loud.df$NaltTmDrPL + loud.df$FqhcTmDrPL +
                     loud.df$NoVehHHldPL + loud.df$CommWalkingPL +
                     loud.df$CommTransitPL)/8
hist(loud.df$Stage2)
head(loud.df)

save(loud.df,  file = "loud_staging.RData")

write.csv(loud.df, "loud.csv", row.names = FALSE)


