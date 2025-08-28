## Author: Ashlynn Wimer
## Date: 8/5/2025

## This R File 

## Split tract data is used as tract level data suffers loses to suppression.
## For more, see this link: https://forum.ipums.org/t/1980-census-age-data/5362/2

## A lot of data is being transformed, so expect it to take a few (>10) minutes
## to run to completion, with total duration depending on your system specs.

##### Data Sources: ######
## This file uses the IPUMS NHGIS tables NT1, NT7, NT8, and NT10A. These data
## tables are based on the 1980 Census Summary Tape File 1, which is our ultimate
## source.
## It also uses the Longitudinal Tract Database (LTDB) census crosswalk file 
## for 1980 to to 2010.

library(dplyr)
library(stringr)

setwd(getSrcDirectory(function(){})[1])

### Load Data ###
print("Loading data!")
st_demos_data <- read.csv("temp_data/1980/nhgis0016_ds104_1980_tract_080.csv")
st_ed_data <- read.csv("temp_data/1980/nhgis0021_ds107_1980_tract_080.csv")
st_sex_data <- read.csv("temp_data/1980/nhgis0034_ds104_1980_tract_080.csv")
st_sex_age_data <- read.csv("temp_data/1980/nhgis0035_ds104_1980_tract_080.csv")

st_sex_age_data <- st_sex_age_data |>
  mutate(
    MaleOvr18 = C68012 + C68013 + C68014 + C68015 + C68016 + C68017 +
      C68018 + C68019 + C68020 + C68021 + C68022 + C68023 + C68024 + C68025 + 
      C68026,
    MaleOvr65 = C68024 + C68025 + C68026,
    FemaleOvr18 = C68038 + C68039 + C68040 + C68041 + C68042 + C68043 + C68044 +
      C68045 + C68046 + C68047 + C68048 + C68049 + C68050 + C68051 + C68052,
    FemaleOvr65 = C68050 + C68051 + C68052
  ) |>
  select(
    GISJOIN, MaleOvr18, MaleOvr65, FemaleOvr18, FemaleOvr65
  )

st_demos_data <- st_sex_data |>
  select(GISJOIN, Male = C9C001, Female = C9C002) |>
  merge(st_demos_data, by = "GISJOIN") |>
  merge(st_sex_age_data, by = 'GISJOIN')

split_tract_data <- st_ed_data |>
  select(GISJOIN, DHM001, DHM002, DHM003, DHM004, DHM005) |>
  merge(st_demos_data, by = "GISJOIN")

# In hopes of speeding up the sheet
rm(st_demos_data)
rm(st_ed_data)
rm(st_sex_data)

# Rename to ease debugging + legibility
print("Transforming initial dataset!")
split_tract_data <- split_tract_data |>
  rename(
    ageUnd1     = C67001, age1_2         = C67002,
    age3_4      = C67003, age5           = C67004,
    age6        = C67005, age7_9         = C67006,
    age10_13    = C67007, age14          = C67008,
    age15       = C67009, age16          = C67010,
    age17       = C67011, age18          = C67012,
    age19       = C67013, age20          = C67014,
    age21       = C67015, age22_24       = C67016,
    age25_29    = C67017, age30_34       = C67018,
    age35_44    = C67019, age45_54       = C67020,
    age55_59    = C67021, age60_61       = C67022,
    age62_64    = C67023, age65_74       = C67024,
    age75_84    = C67025, ageOv85        = C67026,
    notHispPop  = C9E001, mexicanPop     = C9E002,
    prPop       = C9E003, cubanPop       = C9E004,
    otherHisp   = C9E005, whitePop       = C9D001,
    blackPop    = C9D002, contigAmIndPop = C9D003,
    inuitPop    = C9D004, unanganPop     = C9D005,
    japanesePop = C9D006, chinesePop     = C9D007,
    filipinoPop = C9D008, koreanPop      = C9D009,
    indianPop   = C9D010, vietnamesePop  = C9D011,
    hawaiinPop  = C9D012, guamanianPop   = C9D013,
    samoanPop   = C9D014, otherPop       = C9D015,
    totPop      = C7L001, elementary     = DHM001,
    hghschl1_3  = DHM002, hghschl4       = DHM003,
    college1_3  = DHM004, college4orMore = DHM005
  )

## Aggregate into relevant variables
split_tract_data <- split_tract_data |>
  mutate(
    Ovr18 = age18 + age19 + age20 + age21 + age22_24 + age25_29 +
      age30_34 + age35_44 + age45_54 + age55_59 + age60_61 +
      age62_64 + age65_74 + age75_84 + ageOv85,
    Ovr16 = age16 + age17 + age18 + age19 + age20 + age21 + age22_24 +
      age25_29 + age30_34 + age35_44 + age45_54 + age55_59 + age60_61 +
      age62_64 + age65_74 + age75_84 + ageOv85,
    Ovr21 = age21 + age22_24 + age25_29 + age30_34 + age35_44 + age45_54 +
      age55_59 + age60_61 + age62_64 + age65_74 + age75_84 + ageOv85,
    Ovr65 = age65_74 + age75_84 + ageOv85,
    Age15_44 = age15 + age16 + age17 + age18 + age19 + age20 +
      age21 + age22_24 + age25_29 + age30_34 + age35_44,
    hispPop  = mexicanPop + prPop + cubanPop + otherHisp,
    amIndPop = contigAmIndPop + inuitPop + unanganPop,
    asianPop = japanesePop + chinesePop + filipinoPop +
      koreanPop + indianPop + vietnamesePop,
    pacIsPop = hawaiinPop + guamanianPop + samoanPop,
    EduNoHs  = elementary + hghschl1_3,
    EduHsP = hghschl4,
    SomeCollege = college1_3,
    edSampl = elementary + hghschl1_3 + hghschl4 + college1_3 + college4orMore
  )

## Select only relevant variables
split_tract_data <- split_tract_data |>
  select(GISJOIN, STATEA, COUNTYA, PLACEA, TRACTA,
    Ovr18, Ovr16, Ovr21, Ovr65, Age15_44, Male, Female,
    EduNoHs, EduHsP, SomeCollege, hispPop, amIndPop, asianPop,
    pacIsPop, totPop, whitePop, blackPop, edSampl, MaleOvr18, MaleOvr65, 
    FemaleOvr18, FemaleOvr65
  )


## Recombine partial census tracts into whole census tracts
# Pad keys
split_tract_data$STATEA <- str_pad(
  split_tract_data$STATEA, width = 2, side = "left", pad = "0"
)
split_tract_data$COUNTYA <- str_pad(
  split_tract_data$COUNTYA, width = 3, side = "left", pad = "0"
)

# GISJOIN is needed in order to get the actual TRACTA
# This is because Census Tract codes are of form XXXX.YY, where the .YY
# is optional. Unfortunately, the TRACTA variable simply drops the period and
# all leading 0s, making it impossible to differentiate tract 101 from 1.01
# as both would have TRACTA 101.

# GISJOIN preserves the uniqueness of Tract Codes, but also contains the PLACEA
# if it exists, so we have to do casework by whether or not there is a PLACEA.

has_placea <- !is.na(split_tract_data$PLACEA)
split_tract_data$GISJOIN <- ifelse(
  has_placea,
  str_pad(split_tract_data$GISJOIN, width = 21, side = "right", pad = "0"),
  str_pad(split_tract_data$GISJOIN, width = 17, side = "right", pad = "0")
)

split_tract_data$TRACTA <- ifelse(
  has_placea,
  substr(split_tract_data$GISJOIN, start = 16, stop = 21),
  substr(split_tract_data$GISJOIN, start = 12, stop = 17)
)

split_tract_data$trtid80 <- paste(
  split_tract_data$STATEA,
  split_tract_data$COUNTYA,
  split_tract_data$TRACTA,
  sep = ""
)

crosswalk <- read.csv("temp_data/crosswalk_1980_2010.csv")
crosswalk$trtid80 <- crosswalk$trtid80 |>
  str_pad(width = 11, side = "left", pad = "0")
crosswalk$trtid10 <- crosswalk$trtid10 |>
  str_pad(width = 11, side = "left", pad = "0")


t1980cw <- merge(
  split_tract_data, crosswalk, by = "trtid80"
)

t1980cw <- t1980cw |>
  select(
    -trtid80, -GISJOIN, -STATEA, -COUNTYA, -PLACEA,
    -TRACTA, -placefp10, -cbsa10, -metdiv10, -ccflag10
  ) |>
  mutate(
    Ovr18       = weight * Ovr18,
    Ovr16       = weight * Ovr16,
    Ovr21       = weight * Ovr21,
    Ovr65       = weight * Ovr65,
    Age15_44    = weight * Age15_44,
    Male        = weight * Male,
    Female      = weight * Female,
    EduNoHs     = weight * EduNoHs,
    EduHsP      = weight * EduHsP,
    SomeCollege = weight * SomeCollege,
    hispPop     = weight * hispPop,
    amIndPop    = weight * amIndPop,
    asianPop    = weight * asianPop,
    pacIsPop    = weight * pacIsPop,
    totPop      = weight * totPop,
    whitePop    = weight * whitePop,
    blackPop    = weight * blackPop,
    edSampl     = weight * edSampl,
    MaleOvr18   = weight * MaleOvr18,
    MaleOvr65   = weight * MaleOvr65,
    FemaleOvr18 = weight * FemaleOvr18,
    FemaleOvr65 = weight * FemaleOvr65,
  ) |>
  group_by(trtid10) |>
  summarise(
    Ovr18       = sum(Ovr18),
    Ovr18P      = round(sum(Ovr18) / sum(totPop), 2),
    Ovr16       = sum(Ovr16),
    Ovr16P      = round(100 * sum(Ovr16) / sum(totPop), 2),
    Ovr21       = sum(Ovr21),
    Ovr21P      = round(100 * sum(Ovr21) / sum(totPop), 2),
    Ovr65       = sum(Ovr65),
    Ovr65P      = round(100 * sum(Ovr65) / sum(totPop), 2),
    Age15_44    = sum(Age15_44),
    Age15_44P   = round(100 * sum(Age15_44) / sum(totPop), 2),
    MaleP       = round(100 * sum(Male) / sum(totPop), 2),
    FemaleP     = round(100 * sum(Female) / sum(totPop), 2),
    SRatio      = round(100 * sum(Male) / sum(Female), 2),
    SRatio18    = round(100 * sum(MaleOvr18) / sum(FemaleOvr18), 2),
    SRatio65    = round(100 * sum(MaleOvr65) / sum(FemaleOvr65), 2),
    EduNoHsP     = round(100 * sum(EduNoHs) / sum(edSampl), 2),
    EduHsP      = round(100 * sum(EduHsP) / sum(edSampl), 2),
    SomeCollege = round(100 * sum(SomeCollege) / sum(edSampl), 2),
    HispP     = round(100 * sum(hispPop) / sum(totPop), 2),
    HispPop   = sum(hispPop),
    AmIndP    = round(100 * sum(amIndPop) / sum(totPop), 2),
    AmIndPop  = sum(amIndPop),
    AsianP    = round(100 * sum(asianPop) / sum(totPop), 2),
    AsianPop  = sum(asianPop),
    PacIsP    = round(100 * sum(pacIsPop) / sum(totPop), 2),
    PacIsPop  = sum(pacIsPop),
    TotPop    = sum(totPop),
    WhiteP    = round(100 * sum(whitePop) / sum(totPop), 2),
    WhitePop  = sum(whitePop),
    BlackP    = round(100 * sum(blackPop) / sum(totPop), 2),
    BlackPop  = sum(blackPop),
    Female    = sum(Female),
    FemaleOvr18 = sum(FemaleOvr18),
    FemaleOvr65 = sum(FemaleOvr65)
  ) |>
  mutate(
    SRatio = ifelse(Female < 1, NA, SRatio),
    SRatio18 = ifelse(FemaleOvr18 < 1, NA, SRatio18),
    SRatio65 = ifelse(FemaleOvr65 < 1, NA, SRatio65)
  ) |> 
  select(-Female, -FemaleOvr18, -FemaleOvr65) |> 
  mutate(
    HEROP_ID = str_c('140US', str_pad(trtid10, 11, "left", "0")),
    SRatio   = ifelse(SRatio > 1000, NA, SRatio),
    SRatio18 = ifelse(SRatio > 1000, NA, SRatio18),
    SRatio65 = ifelse(SRatio > 1000, NA, SRatio65)
  )

print("Done combining all split tracts!")


### 1990 #########################################3

# Load Data 
print("Loading data!")
t1990_demos <- read.csv("temp_data/1990/nhgis0020_ds120_1990_tract.csv")
t1990_education <- read.csv("temp_data/1990/nhgis0013_ds123_1990_tract.csv")
t1990_sex   <- read.csv("temp_data/1990/nhgis0033_ds120_1990_tract.csv")
t1990_sex_race_age <- read.csv("temp_data/1990/nhgis0035_ds120_1990_tract.csv")

print("Transforming initial dataset!")
t1990_sex <- t1990_sex |>
  select(GISJOIN, Male = EUX001, Female = EUX002)

t1990_sex_race_age <- t1990_sex_race_age |>
  mutate(
    whtMlOvr18 = ET4013 + ET4014 + ET4015 + ET4016 + ET4017 + ET4018 + ET4019 +
      ET4020 + ET4021 + ET4022 + ET4023 + ET4024 + ET4025 + ET4026 + ET4027 +
      ET4028 + ET4029 + ET4030 + ET4031,
    whtMlOvr65 = ET4027 + ET4028 + ET4029 + ET4030 + ET4031,
    blkMlOvr18 = ET4075 + ET4076 + ET4077 + ET4078 + ET4079 + ET4080 + ET4081 +
      ET4082 + ET4083 + ET4084 + ET4085 + ET4086 + ET4087 + ET4088 + ET4089 +
      ET4090 + ET4091 + ET4092 + ET4093,
    blkMlOvr65 = ET4089 + ET4090 + ET4091 + ET4092 + ET4093,
    aiMlOvr18  = ET4137 + ET4138 + ET4139 + ET4140 + ET4141 + ET4142 + ET4143 +
      ET4144 + ET4145 + ET4146 + ET4147 + ET4148 + ET4149 + ET4150 + ET4151 +
      ET4152 + ET4153 + ET4154 + ET4155,
    aiMlOvr65  = ET4151 + ET4152 + ET4153 + ET4154 + ET4155,
    asMlOvr18  = ET4199 + ET4200 + ET4201 + ET4202 + ET4203 + ET4204 + ET4205 +
      ET4206 + ET4207 + ET4208 + ET4209 + ET4210 + ET4211 + ET4212 + ET4213 +
      ET4214 + ET4215 + ET4216 + ET4217,
    asMlOvr65  = ET4213 + ET4214 + ET4215 + ET4216 + ET4217,
    othMlOvr18 = ET4261 + ET4262 + ET4263 + ET4264 + ET4265 + ET4266 + ET4267 +
      ET4268 + ET4269 + ET4270 + ET4271 + ET4272 + ET4273 + ET4274 + ET4275 +
      ET4276 + ET4277 + ET4278 + ET4279,
    othMlOvr65 = ET4275 + ET4276 + ET4277 + ET4278 + ET4279,
    whtFlOvr18 = ET4044 + ET4045 + ET4046 + ET4047 + ET4048 + ET4049 + ET4050 +
      ET4051 + ET4052 + ET4053 + ET4054 + ET4055 + ET4056 + ET4057 + ET4058 +
      ET4059 + ET4060 + ET4061 + ET4062,
    whtFlOvr65 = ET4058 + ET4059 + ET4060 + ET4061 + ET4062,
    blkFlOvr18 = ET4106 + ET4107 + ET4108 + ET4109 + ET4110 + ET4111 + ET4112 +
      ET4113 + ET4114 + ET4115 + ET4116 + ET4117 + ET4118 + ET4119 + ET4120 +
      ET4121 + ET4122 + ET4123 + ET4124,
    blkFlOvr65 = ET4120 + ET4121 + ET4122 + ET4123 + ET4124,
    aiFlOvr18  = ET4168 + ET4169 + ET4170 + ET4171 + ET4172 + ET4173 + ET4174 +
      ET4175 + ET4176 + ET4177 + ET4178 + ET4179 + ET4180 + ET4181 + ET4182 +
      ET4183 + ET4184 + ET4185 + ET4186,
    aiFlOvr65  = ET4182 + ET4183 + ET4184 + ET4185 + ET4186,
    asFlOvr18  = ET4230 + ET4231 + ET4232 + ET4233 + ET4234 + ET4235 + ET4236 +
      ET4237 + ET4238 + ET4239 + ET4240 + ET4241 + ET4242 + ET4243 + ET4244 +
      ET4245 + ET4246 + ET4247 + ET4248,
    asFlOvr65  = ET4244 + ET4245 + ET4246 + ET4247 + ET4248,
    othFlOvr18 = ET4292 + ET4293 + ET4294 + ET4295 + ET4296 + ET4297 + ET4298 +
      ET4299 + ET4300 + ET4301 + ET4302 + ET4303 + ET4304 + ET4305 + ET4306 +
      ET4307 + ET4308 + ET4309 + ET4310,
    othFlOvr65 = ET4306 + ET4307 + ET4308 + ET4309 + ET4310
  ) |>
  mutate(
    mlOvr18 = whtMlOvr18 + blkMlOvr18 + aiMlOvr18 + asMlOvr18 + othMlOvr18,
    flOvr18 = whtFlOvr18 + blkFlOvr18 + aiFlOvr18 + asFlOvr18 + othFlOvr18,
    mlOvr65 = whtMlOvr65 + blkMlOvr65 + aiMlOvr65 + asMlOvr65 + othMlOvr65,
    flOvr65 = whtFlOvr65 + blkFlOvr65 + aiFlOvr65 + asFlOvr65 + othFlOvr65
  ) |>
  select(GISJOIN, mlOvr18, flOvr18, mlOvr65, flOvr65)

# Rename variables to enable easier debugging later on.
t1990_demos <- t1990_demos |> # race variables 
  rename(WhitePop          = EUZ001, BlackPop            = EUZ002,
         contigAmIndPop    = EUZ003, inuitPop            = EUZ004,
         unanganPop        = EUZ005, chinesePop          = EUZ006,
         filipinoPop       = EUZ007, japanesePop         = EUZ008,
         indianPop         = EUZ009, koreanPop           = EUZ010,
         vietnamesePop     = EUZ011, cambodianPop        = EUZ012,
         hmongPop          = EUZ013, loatianPop          = EUZ014,
         thaiPop           = EUZ015, otherAsianPop       = EUZ016,
         hawaiinPop        = EUZ017, samoanPop           = EUZ018,
         tonganPop         = EUZ019, otherPlynsnPop      = EUZ020,
         guamianPop        = EUZ021, otherMcrnsnPop      = EUZ022,
         melanesianPop     = EUZ023, unspecPcfcIslndrPop = EUZ024,
         otherMcrnsnRcePop = EUZ025, totPop              = ET1001
         ) |> # ethnicity variables
  rename(notHisp   = EU1001, mexicanHisp = EU1002,
         prHisp    = EU1003, cubanHisp   = EU1004,
         otherHisp = EU1005
         ) |> # age
  rename(ageUnd1   = ET3001, age1_2   = ET3002,
         age3_4    = ET3003, age5     = ET3004,
         age6      = ET3005, age7_9   = ET3006,
         age10_11  = ET3007, age12_13 = ET3008,
         age14     = ET3009, age15    = ET3010,
         age16     = ET3011, age17    = ET3012,
         age18     = ET3013, age19    = ET3014,
         age20     = ET3015, age21    = ET3016,
         age22_24  = ET3017, age25_29 = ET3018,
         age30_34  = ET3019, age35_39 = ET3020,
         age40_44  = ET3021, age45_49 = ET3022,
         age50_54  = ET3023, age55_59 = ET3024,
         age60_61  = ET3025, age62_64 = ET3026,
         age65_69  = ET3027, age70_74 = ET3028,
         age75_79  = ET3029, age80_84 = ET3030,
         ageOver85 = ET3031) |>
  mutate(
    Ovr16 = age16 + age17 + age18 + age19 + age20 + age21 + age22_24 +
      age25_29 + age30_34 + age35_39 + age40_44 + age45_49 + age50_54 +
      age55_59 + age60_61 + age62_64 + age65_69 + age70_74 + age75_79 +
      age80_84 + ageOver85,
    Ovr18 = age18 + age19 + age20 + age21 + age22_24 + age25_29 + age30_34 +
      age35_39 + age40_44 + age45_49 + age50_54 + age55_59 + age60_61 +
      age62_64 + age65_69 + age70_74 + age75_79 + age80_84 + ageOver85,
    Ovr21 = age21 + age22_24 + age25_29 + age30_34 + age35_39 + age40_44 +
      age45_49 + age50_54 + age55_59 + age60_61 + age62_64 + age65_69 +
      age70_74 + age75_79 + age80_84 + ageOver85,
    Ovr65 = age65_69 + age70_74 + age75_79 + age80_84 + ageOver85,
    Age15_44 = age15 + age16 + age17 + age18 + age19 + age20 + age21 +
      age22_24 + age25_29 + age30_34 + age35_39 + age40_44,
    WhitePop = WhitePop,
    BlackPop = BlackPop,
    HispPop  = mexicanHisp + cubanHisp + prHisp + otherHisp,
    AmIndPop = contigAmIndPop + inuitPop + unanganPop,
    AsianPop = chinesePop + filipinoPop + japanesePop + indianPop + koreanPop +
      vietnamesePop + cambodianPop + hmongPop + loatianPop + thaiPop +
      otherAsianPop,
    PacIsPop = hawaiinPop + samoanPop + tonganPop + otherPlynsnPop +
      guamianPop + otherMcrnsnPop + melanesianPop + unspecPcfcIslndrPop +
      otherMcrnsnRcePop,
  ) |>
  select(
    GISJOIN, TotPop = totPop, Ovr16, Ovr18, Ovr21, Ovr65, Age15_44, WhitePop,
    BlackPop, HispPop, AmIndPop, AsianPop, PacIsPop
  )

# Education variables
t1990_education <- t1990_education |>
  rename(
    noHS        = E33001, hsNoGrad      = E33002,
    EduHS       = E33003, collegeNoGrad = E33004,
    associates  = E33005, Bachelors     = E33006,
    GradScl     = E33007
  ) |>
  mutate(
    EduNoHS = noHS + hsNoGrad,
    SomeCollege = collegeNoGrad + associates,
    EdSampl = noHS + hsNoGrad + EduHS + collegeNoGrad + associates +
      Bachelors + GradScl,
  ) |>
  select(GISJOIN, EduHS, EduNoHS, SomeCollege, EdSampl, Bachelors, GradScl,
         STATEA, COUNTYA, ANPSADPI, TRACTA)


# Merge into a large dataframe
t1990 <- t1990_demos |>
  merge(t1990_education, by = "GISJOIN") |>
  merge(t1990_sex, by = "GISJOIN") |>
  merge(t1990_sex_race_age, by = "GISJOIN")

# Mutate in a new key column to neable crosswalking.
# Special care is taken to avoid an issue arrising from TRACTA ignoring
# the decimal in tractids.
t1990 <- t1990 |>
  mutate(
    trtid90 = paste(
      str_pad(STATEA, side='left', width=2, pad='0'), 
      str_pad(COUNTYA, side='left', width=3, pad='0'),
      ifelse(
        str_detect(ANPSADPI, "\\."), # if it has a decmial
        str_pad(TRACTA, width=6, side='left', pad='0'), # it pads easily
        str_pad( #otherwise, we have to pad with effort
          str_pad(TRACTA, width=4, side='left', pad='0'), 
          width=6, side='right', pad='0')
        ), 
      sep = "")) |>
  select(-GISJOIN, -STATEA, -COUNTYA, -ANPSADPI, -TRACTA)

crosswalk <- read.csv('temp_data/crosswalk_1990_2010.csv')
crosswalk$trtid90 <- crosswalk$trtid90 |>
  str_pad(width = 11, side = "left", pad = "0")
crosswalk$trtid10 <- crosswalk$trtid10 |>
  str_pad(width = 11, side = "left", pad = "0")

t1990cw <- t1990 |> 
  merge(crosswalk, by = 'trtid90') |>
  select(-trtid90, -placefp10, -cbsa10, -metdiv10, -ccflag10) |>
  mutate(
    TotPop = weight * TotPop,
    Ovr16 = weight * Ovr16,
    Ovr18 = weight * Ovr18,
    Ovr21 = weight * Ovr21,
    Ovr65 = weight * Ovr65,
    Age15_44 = weight * Age15_44,
    WhitePop = weight * WhitePop,
    BlackPop = weight * BlackPop,
    Male = weight * Male,
    Female = weight * Female,
    mlOvr18 = weight * mlOvr18,
    mlOvr65 = weight * mlOvr65,
    flOvr18 = weight * flOvr18,
    flOvr65 = weight * flOvr65,
    HispPop = weight * HispPop,
    AmIndPop = weight * AmIndPop,
    AsianPop = weight * AsianPop,
    PacIsPop = weight * PacIsPop,
    EduHS = weight * EduHS,
    EduNoHs = weight * EduNoHS,
    SomeCollege = weight * SomeCollege,
    EdSampl = weight * EdSampl, 
    Bachelors = weight * Bachelors,
    GradScl = weight * GradScl
  )

t1990cw <- t1990cw |>
  group_by(trtid10) |>
  summarize(
    TotPop = sum(TotPop),
    Ovr16 = sum(Ovr16),
    Ovr16P = round(100 * sum(Ovr16) / sum(TotPop), 2),
    Ovr18 = sum(Ovr18),
    Ovr18P = round(100 * sum(Ovr18) / sum(TotPop), 2),
    Ovr21 = sum(Ovr21),
    Ovr21P = round(100 * sum(Ovr21) / sum(TotPop), 2),
    Ovr65 = sum(Ovr65),
    Ovr65P = round(100 * sum(Ovr65) / sum(TotPop), 2),
    Age15_44 = sum(Age15_44),
    Age15_44P = round(100 * sum(Age15_44) / sum(TotPop), 2),
    WhitePop = sum(WhitePop),
    WhiteP = round(100 * sum(WhitePop) / sum(TotPop), 2),
    BlackPop = sum(BlackPop),
    BlackP = round(100 * sum(BlackPop) / sum(TotPop), 2),
    MaleP = round(100 * sum(Male) / sum(TotPop), 2),
    FemaleP = round(100 * sum(Female) / sum(TotPop), 2),
    SRatio = round(100 * sum(Male) / sum(Female), 2),
    SRatio18 =  round(100 * sum(mlOvr18) / sum(flOvr18), 2),
    SRatio65 = round(100 * sum(mlOvr65) / sum(flOvr65), 2),
    HisPop = sum(HispPop),
    HisP = round(100 * sum(HisPop) / sum(TotPop), 2),
    AmIndPop = sum(AmIndPop),
    AmIndP = round(100 * sum(AmIndPop) / sum(TotPop), 2),
    AsianPop = sum(AsianPop),
    AsianP = round(100 * sum(AsianPop) / sum(TotPop), 2),
    PacIsPop = sum(PacIsPop),
    PacIsP = round(100 * sum(PacIsPop) / sum(TotPop), 2),
    EduHsP = round(100 * sum(EduHS) / sum(EdSampl), 2),
    EduNoHsP = round(100 * sum(EduNoHS) / sum(EdSampl), 2),
    BachelorsP = round(100 * sum(Bachelors) / sum(EdSampl), 2),
    GradSclP = round(100 * sum(GradScl) / sum(EdSampl), 2),
    SomeCollege = round(100 * sum(SomeCollege) / sum(EdSampl), 2),
    Female = sum(Female),
    flOvr18 = sum(flOvr18),
    flOvr65 = sum(flOvr65)
  ) |>
  mutate(
    SRatio = ifelse(Female < 1, NA, SRatio),
    SRatio18 = ifelse(flOvr18 < 1, NA, SRatio18),
    SRatio65 = ifelse(flOvr65 < 1, NA, SRatio65)
  ) |> 
  select(-Female, -flOvr18, -flOvr65) |>
  mutate(
    HEROP_ID = str_c('140US', str_pad(trtid10, 11, "left", "0")),
    SRatio   = ifelse(SRatio > 1000, NA, SRatio),
    SRatio18 = ifelse(SRatio > 1000, NA, SRatio18),
    SRatio65 = ifelse(SRatio > 1000, NA, SRatio65)
  )

### 2000

# Load Data 
print("Loading data!")
t2000_pop <- read.csv("temp_data/2000/nhgis0020_ds146_2000_tract.csv")
t2000_demos <- read.csv("temp_data/2000/nhgis0013_ds146_2000_tract.csv")
t2000_education <- read.csv("temp_data/2000/nhgis0013_ds151_2000_tract.csv")
t2000_youngins <- read.csv("temp_data/2000/nhgis0036_ds146_2000_tract.csv")
print("Transforming initial dataset!")

# we only need a few columns from this data frame
t2000_youngins <- t2000_youngins |> 
  select(GISJOIN, m16 = FNG017, m17 = FNG018, f16 = FNG037, f17 = FNG038)

# Rename and pare down population dataframe.
t2000_pop <- t2000_pop |>
  rename(totPop = FL5001) |>
  select(GISJOIN, totPop)

# Rename demographic data.
t2000_demos <- t2000_demos |>
  merge(t2000_youngins, by = "GISJOIN") |>
  rename(
    WhitePop = FMR001, BlackPop = FMR002,
    AmIndPop = FMR003, AsianPop = FMR004,
    PacIsPop = FMR005) |>
  rename(
    HispPop = FMC001
  ) |>
  rename(
    mAgeUnder5 = FMZ001,  mAge5_9    = FMZ002,
    mAge10_14  = FMZ003,  mAge15_17  = FMZ004,
    mAge18_19  = FMZ005,  mAge20     = FMZ006,
    mAge21     = FMZ007,  mAge22_24  = FMZ008,
    mAge25_29  = FMZ009,  mAge30_34  = FMZ010,
    mAge35_39  = FMZ011,  mAge40_44  = FMZ012,
    mAge45_49  = FMZ013,  mAge50_54  = FMZ014,
    mAge55_59  = FMZ015,  mAge60_61  = FMZ016,
    mAge62_64  = FMZ017,  mAge65_66  = FMZ018,
    mAge67_69  = FMZ019,  mAge70_74  = FMZ020,
    mAge75_79  = FMZ021,  mAge80_84  = FMZ022,
    mAgeOver85 = FMZ023,  fAgeUnder5 = FMZ024,
    fAge5_9    = FMZ025,  fAge10_14  = FMZ026,
    fAge15_17  = FMZ027,  fAge18_19  = FMZ028,
    fAge20     = FMZ029,  fAge21     = FMZ030,
    fAge22_24  = FMZ031,  fAge25_29  = FMZ032,
    fAge30_34  = FMZ033,  fAge35_39  = FMZ034,
    fAge40_44  = FMZ035,  fAge45_49  = FMZ036,
    fAge50_54  = FMZ037,  fAge55_59  = FMZ038,
    fAge60_61  = FMZ039,  fAge62_64  = FMZ040,
    fAge65_66  = FMZ041,  fAge67_69  = FMZ042,
    fAge70_74  = FMZ043,  fAge75_79  = FMZ044,
    fAge80_84  = FMZ045,  fAgeOver85 = FMZ046
  ) |>
  mutate(
    fOvr16 = f16 + f17 + fAge18_19 + fAge20 + fAge21 + fAge22_24 +
      fAge25_29 + fAge30_34 + fAge35_39 + fAge40_44 + fAge45_49 + fAge50_54 +
      fAge55_59 + fAge60_61 + fAge62_64 + fAge65_66 + fAge67_69 + fAge70_74 +
      fAge75_79 + fAge80_84 + fAgeOver85,
    mOvr16 = m16 + m17 + mAge18_19 + mAge20 + mAge21 + mAge22_24 +
      mAge25_29 + mAge30_34 + mAge35_39 + mAge40_44 + mAge45_49 + mAge50_54 +
      mAge55_59 + mAge60_61 + mAge62_64 + mAge65_66 + mAge67_69 + mAge70_74 +
      mAge75_79 + mAge80_84 + mAgeOver85,
    fOvr18 = fAge18_19 + fAge20 + fAge21 + fAge22_24 +
      fAge25_29 + fAge30_34 + fAge35_39 + fAge40_44 + fAge45_49 + fAge50_54 +
      fAge55_59 + fAge60_61 + fAge62_64 + fAge65_66 + fAge67_69 + fAge70_74 +
      fAge75_79 + fAge80_84 + fAgeOver85,
    mOvr18 = mAge18_19 + mAge20 + mAge21 + mAge22_24 +
      mAge25_29 + mAge30_34 + mAge35_39 + mAge40_44 + mAge45_49 + mAge50_54 +
      mAge55_59 + mAge60_61 + mAge62_64 + mAge65_66 + mAge67_69 + mAge70_74 +
      mAge75_79 + mAge80_84 + mAgeOver85,
    fOvr65 = fAge65_66 + fAge67_69 + fAge70_74 + fAge75_79 + fAge80_84 +
      fAgeOver85,
    mOvr65 = mAge65_66 + mAge67_69 + mAge70_74 + mAge75_79 + mAge80_84 +
      mAgeOver85
  ) |>
  mutate(
    Male = mAgeUnder5 + mAge5_9 + mAge10_14 + mAge15_17 + mOvr18,
    Female = fAgeUnder5 + fAge5_9 + fAge10_14 + fAge15_17 + fOvr18,
    Ovr16 = fOvr16 + mOvr16,
    Ovr18 = fOvr18 + mOvr18,
    Ovr21 = fOvr18 + mOvr18 - (fAge18_19 + fAge20 + mAge18_19 + mAge20),
    Ovr65 = fOvr65 + mOvr65,
    Age15_44 = mAge15_17 + mAge18_19 + mAge20 + mAge21 + mAge22_24 +
      mAge25_29 + mAge30_34 + mAge35_39 + mAge40_44 + fAge15_17 + fAge18_19 +
      fAge20 + fAge21 + fAge22_24 + fAge25_29 + fAge30_34 + fAge35_39 +
      fAge40_44,
  ) |>
  mutate(
    TotPop = Male + Female,
  ) |>
  select(
    GISJOIN, STATEA, COUNTYA, NAME, TRACTA,
    fOvr18, mOvr18, fOvr65, mOvr65, Ovr16, Ovr18, Ovr21, Ovr65, Age15_44,
    HispPop, WhitePop, BlackPop, AmIndPop, AsianPop, PacIsPop, TotPop,
    Male, Female
  )

# Rename, mutate, and pare down education data.
t2000_education <- t2000_education |>
  rename(
    mNoSchool = GKT001, m0_4    = GKT002,
    m5_6      = GKT003, m7_8    = GKT004,
    m9        = GKT005, m10     = GKT006,
    m11       = GKT007, m12     = GKT008,
    mHS       = GKT009, mLtlClg = GKT010,
    mSmClg    = GKT011, mAss    = GKT012,
    mBach     = GKT013, mMas    = GKT014,
    mProf     = GKT015, mDoc    = GKT016,
    fNoSchool = GKT017, f0_4    = GKT018,
    f5_6      = GKT019, f7_8    = GKT020,
    f9        = GKT021, f10     = GKT022,
    f11       = GKT023, f12     = GKT024,
    fHS       = GKT025, fLtlClg = GKT026,
    fSmClg    = GKT027, fAss    = GKT028,
    fBach     = GKT029, fMas    = GKT030,
    fProf     = GKT031, fDoc    = GKT032
  ) |>
  mutate(
    EduNoHS = mNoSchool + m0_4 + m5_6 + m7_8 + m9 + m10 + m11 + m12 + 
      fNoSchool + f0_4 + f5_6 + f7_8 + f9 + f10 + f11 + f12,
    EduHS = fHS + mHS,
    Bachelors = fBach + mBach,
    SomeCollege = fSmClg + mSmClg + fAss + mAss,
    GradScl = fMas + fProf + fDoc + mMas + mProf + mDoc,
    edSmpl = mNoSchool + fNoSchool + m0_4 + f0_4 + m5_6 + f5_6 + m7_8 + f7_8 + 
      m9 + f9 + m10 + f10 + m11 + f11 + m12 + f12 + mHS + fHS +
      mLtlClg + fLtlClg + mSmClg + fSmClg + mAss + fAss + mBach + 
      fBach + mMas + fMas + mProf + fProf + mDoc + fDoc
  ) |>
  select(GISJOIN, EduNoHS, EduHS, Bachelors, SomeCollege, GradScl, edSmpl)

# Merge into a large dataframe, and mutate in a FIPS to work with LTDB files.
t2000 <- t2000_pop |>
  merge(t2000_demos, by = "GISJOIN") |>
  merge(t2000_education, by = "GISJOIN") |>
  mutate(
    trtid00 = paste(
      str_pad(STATEA, side = "left", width = 2, pad = "0"),
      str_pad(COUNTYA, side = "left", width = 3, pad = "0"),
      str_pad(TRACTA, side = "left", width = 6, pad = "0"),
      sep = ""
    )
  ) |>
  select(-STATEA, -COUNTYA, -TRACTA, -GISJOIN)

# Prepare crosswalk table keys for compatability with our FIPS.
crosswalk <- read.csv("temp_data/crosswalk_2000_2010.csv")
crosswalk$trtid00 <- crosswalk$trtid00 |>
  str_pad(width = 11, side = "left", pad = "0")
crosswalk$trtid10 <- crosswalk$trtid10 |>
  str_pad(width = 11, side = "left", pad = "0")

t2000cw <- t2000 |>
  merge(crosswalk, by = "trtid00") |>
  mutate(
    TotPop      = weight * TotPop,
    fOvr18      = weight * fOvr18,
    mOvr18      = weight * mOvr18,
    fOvr65      = weight * fOvr65,
    mOvr65      = weight * mOvr65,
    Ovr16       = weight * Ovr16,
    Ovr18       = weight * Ovr18,
    Ovr21       = weight * Ovr21,
    Ovr65       = weight * Ovr65,
    Age15_44    = weight * Age15_44,
    HispPop     = weight * HispPop,
    WhitePop    = weight * WhitePop,
    BlackPop    = weight * BlackPop,
    AmIndPop    = weight * AmIndPop,
    AsianPop    = weight * AsianPop,
    PacIsPop    = weight * PacIsPop,
    Male        = weight * Male,
    Female      = weight * Female,
    EduNoHS     = weight * EduNoHS,
    EduHS       = weight * EduHS,
    Bachelors   = weight * Bachelors,
    SomeCollege = weight * SomeCollege,
    GradScl     = weight * GradScl,
    edSmpl      = weight * edSmpl,
  ) |>
  group_by(trtid10) |>
  summarize(
    TotPop = sum(TotPop),
    Ovr16 = sum(Ovr16),
    Ovr16P = round(100 * sum(Ovr16) / sum(TotPop), 2),
    Ovr18 = sum(Ovr18),
    Ovr18P = round(100 * sum(Ovr18) / sum(TotPop), 2),
    Ovr21 = sum(Ovr21),
    Ovr21P = round(100 * sum(Ovr21) / sum(TotPop), 2),
    Ovr65 = sum(Ovr65),
    Ovr65P = round(100 * sum(Ovr65) / sum(TotPop), 2),
    Age15_44 = sum(Age15_44),
    Age15_44P = round(100 * sum(Age15_44) / sum(TotPop), 2),
    WhitePop = sum(WhitePop),
    WhiteP = round(100 * sum(WhitePop) / sum(TotPop), 2),
    BlackPop = sum(BlackPop),
    BlackP = round(100 * sum(BlackPop) / sum(TotPop), 2),
    MaleP = round(100 * sum(Male) / sum(TotPop), 2),
    FemaleP = round(100 * sum(Female) / sum(TotPop), 2),
    SRatio = round(100 * sum(Male) / sum(Female), 2),
    SRatio18 =  round(100 * sum(mOvr18) / sum(fOvr18), 2),
    SRatio65 = round(100 * sum(mOvr65) / sum(fOvr65), 2),
    HisPop = sum(HispPop),
    HisP = round(100 * sum(HisPop) / sum(TotPop), 2),
    AmIndPop = sum(AmIndPop),
    AmIndP = round(100 * sum(AmIndPop) / sum(TotPop), 2),
    AsianPop = sum(AsianPop),
    AsianP = round(100 * sum(AsianPop) / sum(TotPop), 2),
    PacIsPop = sum(PacIsPop),
    PacIsP = round(100 * sum(PacIsPop) / sum(TotPop), 2),
    EduHsP = round(100 * sum(EduHS) / sum(edSmpl), 2),
    EduNoHsP = round(100 * sum(EduNoHS) / sum(edSmpl), 2),
    BachelorsP = round(100 * sum(Bachelors) / sum(edSmpl), 2),
    GradSclP = round(100 * sum(GradScl) / sum(edSmpl), 2),
    SomeCollege = round(100 * sum(SomeCollege) / sum(edSmpl), 2),
    Female = sum(Female),
    fOvr18 = sum(fOvr18),
    fOvr65 = sum(fOvr65)
  ) |>
  mutate(
    SRatio   = ifelse(Female < 1, NA, SRatio),
    SRatio18 = ifelse(fOvr18 < 1, NA, SRatio18),
    SRatio65 = ifelse(fOvr65 < 1, NA, SRatio65)
  ) |>
  mutate(
    HEROP_ID = str_c("140US", str_pad(trtid10, 11, "left", "0")),
    SRatio   = ifelse(SRatio > 1000, NA, SRatio),
    SRatio18 = ifelse(SRatio > 1000, NA, SRatio18),
    SRatio65 = ifelse(SRatio > 1000, NA, SRatio65)
  ) |>
  select(-Female, -fOvr18, -fOvr65, -trtid10) |>
  select(HEROP_ID, everything())

t1980cw[mapply(is.infinite, t1980cw)] <- NA
t1990cw[mapply(is.infinite, t1990cw)] <- NA
t2000cw[mapply(is.infinite, t2000cw)] <- NA

write.csv(t1980cw, "exported/tract-1980-add.csv", row.names=FALSE)
write.csv(t1990cw, "exported/tract-1990-add.csv", row.names=FALSE)
write.csv(t2000cw, "exported/tract-2000-add.csv", row.names=FALSE)