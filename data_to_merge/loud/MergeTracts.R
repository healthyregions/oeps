library(tidyverse)
setwd("~/Code/oeps2/data_to_merge/loud")

commuting <- read.csv("../commuting_tract23.csv")
insurance <- read.csv("../insurance_tract23.csv")
internet <- read.csv("../internet_tract23.csv")

# Commuting in Stage 3
head(commuting)
loud <- commuting %>%
  select(HEROP_ID, NoVehHHld, CommTransit,CommWalking)
head(loud)

# Internet in Stage 1
internet.loud <- internet %>%
  select(HEROP_ID,CompHhldsP,BbndInternetP)
head(internet.loud)
dim(internet.loud)
loud.df <- merge(loud, internet.loud, by="HEROP_ID")
head(loud.df)

# Insurance in Stage 1
head(insurance)
insurance.loud <- insurance %>%
  select(HEROP_ID,InsuredPopP,PrivateInsP,PublicInsP)
head(insurance.loud)
dim(insurance.loud)
loud.df <- merge(loud, insurance.loud, by="HEROP_ID")
head(loud.df)

loud.df$NoVehHHldPL <- percent_rank(loud.df$NoVehHHld)
loud.df$CommTransitPL <- percent_rank(loud.df$CommTransit)
loud.df$CommWalkingPL <- percent_rank(loud.df$CommWalking)
loud.df$InsuredPopPPL <- percent_rank(loud.df$InsuredPopP)
loud.df$PrivateInsPPL <- percent_rank(loud.df$PrivateInsP)
loud.df$PublicInsPPL <- percent_rank(loud.df$PublicInsP)

head(loud.df)

save(loud.df,  file = "loud_staging.RData")


###############