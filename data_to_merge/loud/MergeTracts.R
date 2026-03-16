library(tidyverse)
setwd("~/Code/oeps2/data_to_merge/loud")

commuting <- read.csv("../commuting_tract23.csv")
insurance <- read.csv("../insurance_tract23.csv")

###############
## STAGE 1 
###############

### Internet Access ###
internet <- read.csv("../internet_tract23.csv")

internet.loud <- internet %>%
  select(HEROP_ID,GEOID,CompHhldsP,BbndInternetP)

head(internet.loud)
dim(internet.loud) #84400

loud.stage1 <- internet.loud
head(loud.stage1)

loud.stage1$HEROP_County <- str_sub(loud.stage1$HEROP_ID, 6,10)
head(loud.stage1)

loud.stage1 <- select(loud.stage1,HEROP_ID,HEROP_County,CompHhldsP,BbndInternetP)
head(loud.stage1)
  
loud.stage1$IntInd <- (scale(loud.stage1$CompHhldsP)+ scale(loud.stage1$BbndInternetP))/2
head(loud.stage1)

### Census Response Rate ###
CensusRate.county <- read.csv("~/Downloads/Social Capital-selected/RspRt_county_2023.csv")
head(CensusRate.county)

CensusRate.county$HEROP_County <- str_sub(CensusRate.county$HEROP_ID, 6,10)
head(CensusRate.county)

CensusRate.county <- select(CensusRate.county,HEROP_County,RspRt)
head(CensusRate.county)

loud.stage1x <- left_join(loud.stage1,CensusRate.county, by="HEROP_County")
head(loud.stage1x)

### Social Capital ###

social.capital <- read.csv("~/Downloads/Social Capital-selected/Social_Capital_Measures_2023.csv")
head(social.capital)

social.capital.loud <- social.capital %>%
  select(HEROP_ID,LibPerCap,RlgPerCap, LngTermP,SocCapInd) 

head(social.capital.loud)

social.capital.loud$SocCapIndPL <- percent_rank(social.capital.loud$SocCapInd)
head(social.capital.loud)

loud.stage1y <- merge(loud.stage1x, social.capital.loud, by="HEROP_ID")
head(loud.stage1y)

hist(loud.stage1y$SocCapIndPL)
dim(loud.stage1y) # 83364


#### Limited English Proficiency
oeps <- read.csv("~/Code/tract.csv")
head(oeps)

english <- select(oeps,HEROP_ID,EngProf)
head(english)
summary(english)

english$EngProf <- english$EngProf * 100
head(english)

loud.stage1.df <- merge(loud.stage1y, english, by="HEROP_ID")
head(loud.stage1.df)

### Stage 1 Prep
loud.stage1.df$IntIndPPL <- percent_rank(loud.stage1.df$IntInd)
loud.stage1.df$CenRspRtPL <- percent_rank(loud.stage1.df$RspRt)
loud.stage1.df$SocCapIndPL <- percent_rank(loud.stage1.df$SocCapInd)
loud.stage1.df$EngProfPL <- percent_rank(loud.stage1.df$EngProf.x)
head(loud.stage1.df)

# Equally Weighted
loud.stage1.df$Stage1 <- (loud.stage1.df$IntIndPPL + loud.stage1.df$CenRspRtPL+
                     loud.stage1.df$SocCapIndPL + loud.stage1.df$EngProfPL )/4
hist(loud.stage1.df$Stage1)
head(loud.stage1.df)

# Weighted by Advisory

loud.stage1.df$Stage1W <- ((.613*loud.stage1.df$IntIndPPL) + 
                            (.380*loud.stage1.df$CenRspRtPL) +
                            (.761*loud.stage1.df$SocCapIndPL) + 
                            (.716*loud.stage1.df$EngProfPL) )/4
hist(loud.stage1.df$Stage1W)
head(loud.stage1.df)

save(loud.stage1.df,  file = "loud_stage1.RData")

write.csv(loud.stage1.df, "loud_stage1.csv", row.names = FALSE)

library(sf)
tract.sf <- st_read("https://herop-geodata.s3.us-east-2.amazonaws.com/census/tract-2010-500k.geojson")
loud.stage1.sf <- left_join(tract.sf,loud.stage1.df, by="HEROP_ID")
st_write(loud.stage1.sf, "~/Code/loud.stage1.geojson")

###################


# Commuting in Stage 3
head(commuting)

loud <- commuting %>%
  select(HEROP_ID, GEOID, NoVehHHld, CommTransit,CommWalking)
head(loud)



# Insurance in Stage 4
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


loud.df <- merge(loud.df, fqhc.loud, by="GEOID")
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

moud.loud <- moud %>%
  select(GEOID,MetTmDr,MetTmDrPL,BupTmDr,BupTmDrPL,NaltTmDr,NaltTmDrPL)
head(moud.loud)

loud.df <- merge(loud.df, moud.loud, by="GEOID")
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


