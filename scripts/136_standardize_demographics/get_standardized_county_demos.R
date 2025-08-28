# Author: Ashlynn Wimer
# Date: August 8th 2025

# Libraries
library(dplyr)
library(stringr)
library(tidycensus)
library(sf)

fix_geom <- function(x) {
  x |>
    st_make_valid() |>
    st_buffer(0) |>
    st_simplify(dTolerance = 100) # 100 meters, should be neglible at this scale
}

# If running in RStudio, uncomment this
setwd(getSrcDirectory(function() {})[1])

# Import Data
print("Loading data!")
cty_demos_data <- read.csv("temp_data/1980/nhgis0037_ds104_1980_county.csv")
cty_ed_data <- read.csv("temp_data/1980/nhgis0037_ds107_1980_county.csv")

cntySbdv_pop_data <- read.csv("temp_data/1980/nhgis0039_ds104_1980_cty_sub.csv")
cnty1980 <- st_read("temp_data/shapes/US_county_1980_conflated.shp")
cnty2010 <- st_read("/vsizip//vsicurl/https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2010-500k-shp.zip") # nolint: line_length_linter.
cntySbdv1980 <- st_read("temp_data/shapes/US_mcd_1980.shp") # nolint: line_length_linter.

cntySbdv1980 <- fix_geom(cntySbdv1980)
cnty1980 <- fix_geom(cnty1980)
cnty2010 <- fix_geom(cnty2010)

cty_ed_data <- cty_ed_data |> select(-STATEA, -COUNTYA)

cnty_data <- merge(cty_demos_data, cty_ed_data, by = "GISJOIN") |>
  mutate(
    mOvr18 = C68012 + C68013 + C68014 + C68015 + C68016 + C68017 +
      C68018 + C68019 + C68020 + C68021 + C68022 + C68023 + C68024 + C68025 + 
      C68026,
    mOvr65 = C68024 + C68025 + C68026,
    fOvr18 = C68038 + C68039 + C68040 + C68041 + C68042 + C68043 + C68044 +
      C68045 + C68046 + C68047 + C68048 + C68049 + C68050 + C68051 + C68052,
    fOvr65 = C68050 + C68051 + C68052
  ) |>
  rename(
    Male        = C9C001, Female         = C9C002,
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
    otherHisp   = C9E005, WhitePop       = C9D001,
    BlackPop    = C9D002, contigAmIndPop = C9D003,
    inuitPop    = C9D004, unanganPop     = C9D005,
    japanesePop = C9D006, chinesePop     = C9D007,
    filipinoPop = C9D008, koreanPop      = C9D009,
    indianPop   = C9D010, vietnamesePop  = C9D011,
    hawaiinPop  = C9D012, guamanianPop   = C9D013,
    samoanPop   = C9D014, otherPop       = C9D015,
    TotPop      = C7L001, elementary     = DHM001,
    hghschl1_3  = DHM002, hghschl4       = DHM003,
    college1_3  = DHM004, college4orMore = DHM005
  ) |>
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
    HisPop  = mexicanPop + prPop + cubanPop + otherHisp,
    AmIndPop = contigAmIndPop + inuitPop + unanganPop,
    AsianPop = japanesePop + chinesePop + filipinoPop +
      koreanPop + indianPop + vietnamesePop,
    PacIsPop = hawaiinPop + guamanianPop + samoanPop,
    EduNoHs  = elementary + hghschl1_3,
    EduHs = hghschl4,
    SomeCollege = college1_3,
    edSampl = elementary + hghschl1_3 + hghschl4 + college1_3 + college4orMore
  ) |>
  select(GISJOIN, STATEA, COUNTYA,
    Ovr18, Ovr16, Ovr21, Ovr65, Age15_44, Male, Female,
    EduNoHs, EduHs, SomeCollege, HisPop, AmIndPop, AsianPop,
    PacIsPop, WhitePop, BlackPop, edSampl, mOvr18, mOvr65,
    fOvr18, fOvr65, TotPop
  )

cnty1980 <- cnty1980 |>
  merge(cnty_data, by = "GISJOIN") |>
  st_transform(st_crs(cnty2010))

print("Final preparation before interpolating..")
cnty2010$GEOID <- substr(cnty2010$HEROP_ID, 6, 11100)

cnty2010 <- cnty2010 |>
  select(HEROP_ID, GEOID)

# Create population weights
pop_weights <- cntySbdv1980 |>
  merge(cntySbdv_pop_data, by = 'GISJOIN') |>
  st_transform(st_crs(cnty2010)) |>
  rename(totPop = C7L001)

# Run the interpolation algorithm
print("Interpolating!")
cnty1980_on_2010 <- interpolate_pw(
  from = cnty1980,
  to = cnty2010,
  to_id = "GEOID",
  extensive = TRUE,
  weights = pop_weights,
  weight_column = "totPop",
  weight_placement = "surface",
  crs = "EPSG:9311"
)

# Filter out PR data
# Alaska NAs are left in for posterity.
cnty1980_on_2010 <- cnty1980_on_2010 |> 
  filter(substr(GEOID, start=1, stop=2) != "72") |>
  st_drop_geometry() |>
  mutate(
    Ovr16P = round(100 * Ovr16 / TotPop, 2),
    Ovr18P = round(100 * Ovr18 / TotPop, 2),
    Ovr21P = round(100 * Ovr21 / TotPop, 2),
    Ovr65P = round(100 * Ovr65 / TotPop, 2),
    Age15_44P = round(100 * Age15_44 / TotPop, 2),
    WhiteP = round(100 * WhitePop / TotPop, 2),
    BlackP = round(100 * BlackPop / TotPop, 2),
    MaleP = round(100 * Male / TotPop, 2),
    FemaleP = round(100 * Female / TotPop, 2),
    SRatio = round(100 * Male / Female, 2),
    SRatio18 =  round(100 * mOvr18 / fOvr18, 2),
    SRatio65 = round(100 * mOvr65 / fOvr65, 2),
    HisP = round(100 * HisPop / TotPop, 2),
    AmIndP = round(100 * AmIndPop / TotPop, 2),
    AsianP = round(100 * AsianPop / TotPop, 2),
    PacIsP = round(100 * PacIsPop / TotPop, 2),
    EduHsP = round(100 * EduHs / edSampl, 2),
    EduNoHsP = round(100 * EduNoHs / edSampl, 2),
    SomeCollege = round(100 * SomeCollege / edSampl, 2)
  ) |>
  mutate(
    HEROP_ID = str_c("050US", str_pad(GEOID, 5, "right", "0")),
    FIPS = str_pad(GEOID, 5, side = "right", "0"),
  ) |>
  select(
    HEROP_ID, FIPS, TotPop, Ovr16, Ovr16P, Ovr18, Ovr18P, Ovr21,
    Ovr21P, Ovr65, Ovr65P, Age15_44, Age15_44P, WhitePop, WhiteP, BlackPop,
    BlackP, MaleP, FemaleP, SRatio, SRatio18, SRatio65, HisPop, HisP, AmIndPop,
    AmIndP, AsianPop, AsianP, PacIsPop, PacIsP, EduHsP, EduNoHsP, SomeCollege
  )

# Save
write.csv(
  cnty1980_on_2010,
  "exported/county_1980.csv", row.names=FALSE
)

# Let's try not to hog RAM *too* much
rm(cnty1980_on_2010)
rm(cnty2010)
rm(cnty1980)
rm(cntySbdv1980)
rm(cty_demos_data)
rm(cty_ed_data)
rm(cntySbdv_pop_data)

# Import Data
print("Loading data!")
cnty_full_data <-   read.csv("temp_data/1990/nhgis0037_ds120_1990_county.csv")
cnty_sample_data <- read.csv("temp_data/1990/nhgis0037_ds123_1990_county.csv")
trct_demos <- read.csv("temp_data/1990/nhgis0020_ds120_1990_tract.csv")
cnty1990 <- st_read("temp_data/shapes/US_county_1990_conflated.shp")
cnty2010 <- st_read("/vsizip//vsicurl/https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2010-500k-shp.zip") # nolint: line_length_linter.
trct1990 <- st_read("temp_data/shapes/US_tract_1990_conflated.shp")

cnty1990 <- fix_geom(cnty1990)
cnty2010 <- fix_geom(cnty2010)

# Transform
c1990 <- cnty_sample_data |>
  select(
    GISJOIN, noHs = E33001, hsNoGrad = E33002,
    EduHs = E33003, collegeNoGrad = E33004, associates = E33005,
    Bachelors = E33006, GradScl = E33007
  ) |>
  merge(cnty_full_data, by = "GISJOIN")

c1990 <- c1990 |>
  rename(
    Male              = EUX001, Female              = EUX002,
    WhitePop          = EUZ001, BlackPop            = EUZ002,
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
  ) |>
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
  rename(
    notHisp   = EU1001, mexicanHisp = EU1002,
    prHisp    = EU1003, cubanHisp   = EU1004,
    otherHisp = EU1005
  ) |>
  rename(
    ageUnd1   = ET3001, age1_2   = ET3002,
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
    ageOver85 = ET3031
  ) |>
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
    HisPop  = mexicanHisp + cubanHisp + prHisp + otherHisp,
    AmIndPop = contigAmIndPop + inuitPop + unanganPop,
    AsianPop = chinesePop + filipinoPop + japanesePop + indianPop + koreanPop +
      vietnamesePop + cambodianPop + hmongPop + loatianPop + thaiPop +
      otherAsianPop,
    PacIsPop = hawaiinPop + samoanPop + tonganPop + otherPlynsnPop +
      guamianPop + otherMcrnsnPop + melanesianPop + unspecPcfcIslndrPop +
      otherMcrnsnRcePop,
    EduNoHs = noHs + hsNoGrad,
    SomeCollege = collegeNoGrad + associates,
    EdSampl = noHs + hsNoGrad + EduHs + collegeNoGrad + associates +
      Bachelors + GradScl,
  ) |>
  select(
    GISJOIN, EduHs, EduNoHs, SomeCollege, EdSampl, Bachelors, GradScl,
    STATEA, COUNTYA, ANPSADPI, TRACTA, TotPop = totPop, Ovr16, Ovr18, Ovr21,
    Ovr65, Age15_44, WhitePop, BlackPop, HisPop, AmIndPop, AsianPop, PacIsPop,
    mlOvr18, flOvr18, mlOvr65, flOvr65, Male, Female
  )

cnty1990 <- cnty1990 |>
  merge(c1990, by = "GISJOIN") |>
  st_transform(st_crs(cnty2010))

print("Final preparation before interpolating..")
cnty2010$GEOID <- substr(cnty2010$HEROP_ID, 6, 11100)

cnty2010 <- cnty2010 |>
  select(HEROP_ID, GEOID)

trct1990 <- merge(trct1990, trct_demos, by = "GISJOIN") |> 
  st_transform(st_crs(cnty2010)) |>
  select(GISJOIN, totPop = ET1001)

# Create population weights
pop_weights <- trct1990 |>
  merge(trct_demos, by = "GISJOIN") |>
  st_transform(st_crs(cnty2010))

# Run the interpolation algorithm
print("Interpolating!")
cnty1990_on_2010 <- interpolate_pw(
  from = cnty1990,
  to = cnty2010,
  to_id = "GEOID",
  extensive = TRUE,
  weights = pop_weights,
  weight_column = "totPop",
  weight_placement = "surface",
  crs = "EPSG:9311"
)

# Filter out PR data
# Alaska NAs are left in for posterity.
cnty1990_on_2010 <- cnty1990_on_2010 |>
  filter(substr(GEOID, start = 1, stop = 2) != "72") |>
  st_drop_geometry() |>
  mutate(
    Ovr16P = round(100 * Ovr16 / TotPop, 2),
    Ovr18P = round(100 * Ovr18 / TotPop, 2),
    Ovr21P = round(100 * Ovr21 / TotPop, 2),
    Ovr65P = round(100 * Ovr65 / TotPop, 2),
    Age15_44P = round(100 * Age15_44 / TotPop, 2),
    WhiteP = round(100 * WhitePop / TotPop, 2),
    BlackP = round(100 * BlackPop / TotPop, 2),
    MaleP = round(100 * Male / TotPop, 2),
    FemaleP = round(100 * Female / TotPop, 2),
    SRatio = round(100 * Male / Female, 2),
    SRatio18 =  round(100 * mlOvr18 / flOvr18, 2),
    SRatio65 = round(100 * mlOvr65 / flOvr65, 2),
    HisP = round(100 * HisPop / TotPop, 2),
    AmIndP = round(100 * AmIndPop / TotPop, 2),
    AsianP = round(100 * AsianPop / TotPop, 2),
    PacIsP = round(100 * PacIsPop / TotPop, 2),
    EduHsP = round(100 * EduHs / EdSampl, 2),
    EduNoHsP = round(100 * EduNoHs / EdSampl, 2),
    BachelorsP = round(100 * Bachelors / EdSampl, 2),
    GradSclP = round(100 * GradScl / EdSampl, 2),
    SomeCollege = round(100 * SomeCollege / EdSampl, 2)
  ) |>
  mutate(
    HEROP_ID = str_c("050US", GEOID),
    FIPS = str_pad(GEOID, 5, side = "right", "0"),
  ) |>
  select(
    HEROP_ID, FIPS, TotPop, Ovr16, Ovr16P, Ovr18, Ovr18P, Ovr21, Ovr21P, Ovr65,
    Ovr65P, Age15_44, Age15_44P, WhitePop, WhiteP, BlackPop, BlackP, MaleP,
    FemaleP, SRatio, SRatio18, SRatio65, HisPop, HisP, AmIndPop, AmIndP,
    AsianPop, AsianP, PacIsPop, PacIsP, EduHsP, EduNoHsP, BachelorsP, GradSclP,
    SomeCollege
  )

# Save
write.csv(
  cnty1990_on_2010,
  "exported//county_1990.csv", row.names=FALSE
)

rm(cnty_full_data)
rm(cnty_sample_data)
rm(trct_demos)
rm(cnty1990)
rm(cnty2010)
rm(trct1990)

# Import Data
print("Loading data!")
cnty_full_data <- read.csv("temp_data/2000/nhgis0037_ds146_2000_county.csv")
cnty_sample_data <- read.csv("temp_data/2000/nhgis0040_ds151_2000_county.csv")
block_group_data <- read.csv("temp_data/2000/nhgis0037_ds147_2000_blck_grp.csv")
trct_demos <- read.csv("temp_data/2000/nhgis0020_ds146_2000_tract.csv")
cnty2000 <- st_read("temp_data/shapes/US_county_2000_conflated.shp")
cnty2010 <- st_read("/vsizip//vsicurl/https://herop-geodata.s3.us-east-2.amazonaws.com/census/county-2010-500k-shp.zip") # nolint: line_length_linter.
trct2000 <- st_read("temp_data/shapes/US_tract_2000_conflated.shp")

cnty2000 <- fix_geom(cnty2000)
cnty2010 <- fix_geom(cnty2010)

cnty_sample_data <- cnty_sample_data |>
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
    EduNoHs = mNoSchool + m0_4 + m5_6 + m7_8 + m9 + m10 + m11 + m12 + 
      fNoSchool + f0_4 + f5_6 + f7_8 + f9 + f10 + f11 + f12,
    EduHs = fHS + mHS,
    Bachelors = fBach + mBach,
    SomeCollege = fSmClg + mSmClg + fAss + mAss,
    GradScl = fMas + fProf + fDoc + mMas + mProf + mDoc,
    edSmpl = mNoSchool + fNoSchool + m0_4 + f0_4 + m5_6 + f5_6 + m7_8 + f7_8 + 
      m9 + f9 + m10 + f10 + m11 + f11 + m12 + f12 + mHS + fHS +
      mLtlClg + fLtlClg + mSmClg + fSmClg + mAss + fAss + mBach + 
      fBach + mMas + fMas + mProf + fProf + mDoc + fDoc
  ) |>
  select(GISJOIN, EduNoHs, EduHs, Bachelors, SomeCollege, GradScl, edSmpl)

block_group_data <- block_group_data |>
  mutate(
    GISJOIN = str_c(substr(GISJOIN, 1, 8))
  ) |>
  select(GISJOIN, HisPop = FXZ001) |>
  group_by(GISJOIN) |>
  summarize(HisPop = sum(HisPop))

c2000 <- cnty_full_data |> 
  merge(block_group_data, by = "GISJOIN") |>
  merge(cnty_sample_data, by = "GISJOIN")

c2000 <- c2000 |>
  rename(
    WhitePop = FMR001, BlackPop = FMR002,
    AmIndPop = FMR003, AsianPop = FMR004,
    PacIsPop = FMR005,
    m16        = FNG017,  m17        = FNG018,
    f16        = FNG037,  f17        = FNG038,
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
    Ovr21 = mAge21 + mAge22_24 +
      mAge25_29 + mAge30_34 + mAge35_39 + mAge40_44 + mAge45_49 + mAge50_54 +
      mAge55_59 + mAge60_61 + mAge62_64 + mAge65_66 + mAge67_69 + mAge70_74 +
      mAge75_79 + mAge80_84 + mAgeOver85 + fAge21 + fAge22_24 +
      fAge25_29 + fAge30_34 + fAge35_39 + fAge40_44 + fAge45_49 + fAge50_54 +
      fAge55_59 + fAge60_61 + fAge62_64 + fAge65_66 + fAge67_69 + fAge70_74 +
      fAge75_79 + fAge80_84 + fAgeOver85,
    Ovr65 = fOvr65 + mOvr65,
    Age15_44 = mAge15_17 + mAge18_19 + mAge20 + mAge21 + mAge22_24 +
      mAge25_29 + mAge30_34 + mAge35_39 + mAge40_44 + fAge15_17 + fAge18_19 +
      fAge20 + fAge21 + fAge22_24 + fAge25_29 + fAge30_34 + fAge35_39 +
      fAge40_44
  ) |>
  mutate(TotPop = Male + Female) |>
  select(
    GISJOIN, fOvr18, mOvr18, fOvr65, mOvr65, Ovr16, Ovr18, Ovr21, Ovr65,
    Age15_44, HisPop, WhitePop, BlackPop, AmIndPop, AsianPop, PacIsPop, TotPop,
    Male, Female, EduNoHs, EduHs, Bachelors, SomeCollege, GradScl, edSmpl
  )

c2000 <- cnty2000 |>
  merge(c2000, by = "GISJOIN") |>
  st_transform(st_crs(cnty2010))

# Make population weights.
pop_weights <- trct2000 |>
  merge(trct_demos, by = "GISJOIN") |>
  select(GISJOIN, FL5001) |>
  rename(totPop = FL5001) |>
  st_transform(st_crs(cnty2010))

# Interpolate
cnty2000_on_2010 <- interpolate_pw(
  from = c2000,
  to = cnty2010,
  to_id = "HEROP_ID",
  extensive = TRUE,
  weights = pop_weights,
  weight_column = "totPop",
  weight_placement = "surface",
  crs = "EPSG:9311"
)

# Clean result
cnty2000_on_2010 <- cnty2000_on_2010 |>
  filter(substr(HEROP_ID, start = 6, stop = 8) != "72") |>
  st_drop_geometry() |>
  mutate(
    Ovr16P      = round(100 * Ovr16 / TotPop, 2),
    Ovr18P      = round(100 * Ovr18 / TotPop, 2),
    Ovr21P      = round(100 * Ovr21 / TotPop, 2),
    Ovr65P      = round(100 * Ovr65 / TotPop, 2),
    Age15_44P   = round(100 * Age15_44 / TotPop, 2),
    WhiteP      = round(100 * WhitePop / TotPop, 2),
    BlackP      = round(100 * BlackPop / TotPop, 2),
    MaleP       = round(100 * Male / TotPop, 2),
    FemaleP     = round(100 * Female / TotPop, 2),
    SRatio      = round(100 * Male / Female, 2),
    SRatio18    = round(100 * mOvr18 / fOvr18, 2),
    SRatio65    = round(100 * mOvr65 / fOvr65, 2),
    HisP        = round(100 * HisPop / TotPop, 2),
    AmIndP      = round(100 * AmIndPop / TotPop, 2),
    AsianP      = round(100 * AsianPop / TotPop, 2),
    PacIsP      = round(100 * PacIsPop / TotPop, 2),
    EduHsP      = round(100 * EduHs / edSmpl, 2),
    EduNoHsP    = round(100 * EduNoHs / edSmpl, 2),
    BachelorsP  = round(100 * Bachelors / edSmpl, 2),
    GradSclP    = round(100 * GradScl / edSmpl, 2),
    SomeCollege = round(100 * SomeCollege / edSmpl, 2)
  ) |>
  mutate(
    FIPS = str_pad(substr(HEROP_ID, 6, 100), 5, side = "right", "0"),
  ) |>
  select(
    HEROP_ID, FIPS, TotPop, Ovr16, Ovr16P, Ovr18, Ovr18P, Ovr21, Ovr21P, Ovr65, 
    Ovr65P, Age15_44, Age15_44P, WhitePop, WhiteP, BlackPop, BlackP, MaleP, 
    FemaleP, SRatio, SRatio18, SRatio65, HisPop, HisP, AmIndPop, AmIndP,
    AsianPop, AsianP, PacIsPop, PacIsP, EduHsP, EduNoHsP, BachelorsP,
    GradSclP, SomeCollege
  )

# Save
write.csv(
  cnty2000_on_2010,
  "exported/county_2000.csv", row.names = FALSE
)

rm(cnty_full_data)
rm(cnty_sample_data)
rm(trct_demos)
rm(c2000)
rm(cnty2010)
rm(trct2000)
rm(block_group_data)
