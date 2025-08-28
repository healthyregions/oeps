# Load necessary libraries for data manipulation and analysis
library(sf)  # For working with spatial data
library(tidyverse)  # For data manipulation (dplyr, ggplot2, etc.)
library(tidycensus)  # For accessing US Census data

setwd(getSrcDirectory(function(){})[1])

# Check for Census API key
Sys.getenv("CENSUS_API_KEY")

##### Helper Variables and Functions ---------------

### Variables for editing script output quickly
save_dir <- "exported"
year <- 2023

state_fips <- tigris::fips_codes |>
  filter(! state_code %in% c("60", "72", "66", "69", "78", "74")) |>
  select(state_code) |>
  unique()

state_fips <- state_fips$state_code

## set the ACS variables
variables_to_fetch <- c(
  #### Race, Ethnicity, and Age Variables
  TotPop    = "B02001_001",    Ovr18     = "S0101_C01_026",
  WhiteE    = "B02001_002",    BlackE    = "B02001_003",
  AmIndE    = "B02001_004",    AsianE    = "B02001_005",
  PacIsE    = "B02001_006",    HisE      = "B03003_003",
  OtherE    = "B02001_007",    TwoPlsE   = "B02001_008",
  age0_4    = "S0101_C01_002", age5_14   = "S0101_C01_020",
  age15_19  = "S0101_C01_005", age20_24  = "S0101_C01_006",
  age15_44  = "S0101_C01_024", age45_49  = "S0101_C01_011",
  age50_54  = "S0101_C01_012", age55_59  = "S0101_C01_013",
  age60_64  = "S0101_C01_014", Ovr65     = "S0101_C01_030", 
  ### Additional age variables borrowed from Sex by Age by Employment Status
  fAge16_19 = "B23001_089",    mAge16_19 = "B23001_003",
  ### For SRatio
  male      = "B01001_002",    female    = "B01001_026",
  m18_19    = "B01001_007",    m20       = "B01001_008",
  m21       = "B01001_009",    m22_24    = "B01001_010",
  m25_29    = "B01001_011",    m30_34    = "B01001_012",
  m35_39    = "B01001_013",    m40_44    = "B01001_014",
  m45_49    = "B01001_015",    m50_54    = "B01001_016",
  m55_59    = "B01001_017",    m60_61    = "B01001_018",
  m62_64    = "B01001_019",    m65_66    = "B01001_020",
  m67_69    = "B01001_021",    m70_74    = "B01001_022",
  m75_79    = "B01001_023",    m80_84    = "B01001_024",
  mOvr85    = "B01001_025",
  f18_19    = "B01001_031",    f20       = "B01001_032",
  f21       = "B01001_033",    f22_24    = "B01001_034",
  f25_29    = "B01001_035",    f30_34    = "B01001_036",
  f35_39    = "B01001_037",    f40_44    = "B01001_038",
  f45_49    = "B01001_039",    f50_54    = "B01001_040",
  f55_59    = "B01001_041",    f60_61    = "B01001_042",
  f62_64    = "B01001_043",    f65_66    = "B01001_044",
  f67_69    = "B01001_045",    f70_74    = "B01001_046",
  f75_79    = "B01001_047",    f80_84    = "B01001_048",
  fOvr85    = "B01001_049",
  ### Educational variables
  TotPopEd = "B15001_001",   m1824    = "B15001_003",
  f1824    = "B15001_044",   m2534_sc = "B15001_015",
  m3544_sc = "B15001_023",   m4564_sc = "B15001_031",
  m65p_sc  = "B15001_039",   f2534_sc = "B15001_056",
  f3544_sc = "B15001_064",   f4564_sc = "B15001_072",
  f65p_sc  = "B15001_080",
  # s9 = less than 9th grade, nhs = 9th to 12th no diploma
  m2534_s9 = "B15001_012", m2534_nhs = "B15001_013",
  m3544_s9 = "B15001_020", m3544_nhs = "B15001_021",
  m4564_s9 = "B15001_028", m4564_nhs = "B15001_029",
  m65p_s9  = "B15001_036", m65p_nhs  = "B15001_037",
  f2534_s9 = "B15001_053", f2534_nhs = "B15001_054",
  f3544_s9 = "B15001_061", f3544_nhs = "B15001_062",
  f4564_s9 = "B15001_069", f4564_nhs = "B15001_070",
  f65p_s9  = "B15001_077", f65p_nhs  = "B15001_078",
  # b = bachelors, g = grad or prof, hs = hs
  m2534_hs = "B15001_014", m3544_hs = "B15001_022",
  m4564_hs = "B15001_030", m65p_hs  = "B15001_038",
  f2534_hs = "B15001_055", f3544_hs = "B15001_063",
  f4564_hs = "B15001_071", f65p_hs  = "B15001_079",
  m2534_b  = "B15001_017", m3544_b  = "B15001_025",
  m4564_b  = "B15001_033", m65p_b   = "B15001_041",
  f2534_b  = "B15001_058", f3544_b  = "B15001_066",
  f4564_b  = "B15001_074", f65p_b   = "B15001_082",
  m2534_g  = "B15001_018", m3544_g  = "B15001_026",
  m4564_g  = "B15001_034", m65p_g   = "B15001_042",
  f2534_g  = "B15001_059", f3544_g  = "B15001_067",
  f4564_g  = "B15001_075", f65p_g   = "B15001_083"
) 

#### County Logic -------

county_i <- map_dfr(
  .x = state_fips,
  ~ get_acs(
    geography = "county",
    variables = variables_to_fetch,
    year = year,
    geometry = FALSE,
    state = .x
  )
)

county_i <- county_i |>
  select(GEOID, variable, estimate) |>
  spread(variable, estimate)

county_i |> names()

county <- county_i |>
  mutate(
    mOvr18 = m18_19 + m20 + m21 + m22_24 + m25_29 + m30_34 +
      m35_39 + m40_44 + m45_49 + m55_59 + m60_61 + m62_64 +
      m65_66 + m67_69 + m70_74 + m75_79 + m80_84 + mOvr85,
    fOvr18 = f18_19 + f20 + f21 + f22_24 + f25_29 + f30_34 +
      f35_39 + f40_44 +f45_49 + f55_59 + f60_61 + f62_64 +
      f65_66 + f67_69 + f70_74 + f75_79 + f80_84 + fOvr85,
    mOvr65 = m65_66 + m67_69 + m70_74 + m75_79 + m80_84 + mOvr85,
    fOvr65 = f65_66 + f67_69 + f70_74 + f75_79 + f80_84 + fOvr85,
    Pop25  = TotPopEd - m1824 - f1824,
    SomeCollege = m2534_sc + m3544_sc + m4564_sc + m65p_sc + f2534_sc +
      f3544_sc + f4564_s9 + f65p_sc,
    EduNoHs =  m2534_s9 + m2534_nhs + m3544_s9 + m3544_nhs + m4564_s9 +
      m4564_nhs + m65p_s9 + m65p_nhs + f2534_s9 + f2534_nhs + f3544_s9 +
      f3544_nhs + f4564_s9 + f4564_nhs + f65p_s9 + f65p_nhs,
    EduHs = m2534_hs + m3544_hs + m4564_hs + m65p_hs + f2534_hs + f3544_hs +
      f4564_hs + f65p_hs,
    Bachelors = m2534_b + m3544_b + m4564_b + m65p_b + f2534_b + f3544_b +
      f4564_b + f65p_b,
    GradScl   = m2534_g + m3544_g + m4564_g + m65p_g + f2534_g + f3544_g +
      f4564_g + f65p_g
    ) |>
    mutate(
      SRatio   = round(100 * male   / female, 2),
      SRatio18 = round(100 * mOvr18 / fOvr18, 2),
      SRatio65 = round(100 * mOvr65 / fOvr65, 2),
      SomeCollege = round(100 * SomeCollege / Pop25, 2),
      EduNoHsP    = round(100 * EduNoHs     / Pop25, 2),
      EduHsP      = round(100 * EduHs       / Pop25, 2),
      BachelorsP  = round(100 * Bachelors   / Pop25, 2),
      GradSclP     = round(100 * GradScl    / Pop25, 2)
    ) |>
    mutate(
      Ovr16 = fAge16_19 + mAge16_19 + (age15_44 - age15_19) + age45_49 +
        age50_54 + age55_59 + age60_64 + Ovr65,
      Ovr21 = mOvr18 + fOvr18 - (m18_19 + f18_19 + m20 + f20),
    ) |>
    mutate(
      Ovr16P = round(100 * Ovr16  / TotPop, 2),
      Ovr18P = round(100 * Ovr18  / TotPop, 2),
      Ovr21P = round(100 * Ovr21  / TotPop, 2),
      Ovr65P = round(100 * Ovr65  / TotPop, 2),
      MaleP  = round(100 * male   / TotPop, 2),
      FemP   = round(100 * female / TotPop, 2)
    ) |>
    select(
      GEOID, TotPop, MaleP, FemP, Ovr16, Ovr16P, Ovr18, Ovr18P, Ovr21, Ovr21P,
      Ovr65, Ovr65P, SRatio, SRatio18, SRatio65, WhiteE, AsianE, PacIsE,
      HisE, AmIndE, TwoPlsE, OtherE, SomeCollege, EduNoHsP, EduHsP,
      BachelorsP, GradSclP
    )

#### State Logic -------

state <- get_acs(
  geography = "state",
  variables = variables_to_fetch,
  year = year,
  geometry = FALSE,
)
  
state <- state |>
  select(GEOID, variable, estimate) |>
  spread(variable, estimate) |>
  mutate(
      mOvr18 = m18_19 + m20 + m21 + m22_24 + m25_29 + m30_34 +
        m35_39 + m40_44 + m45_49 + m55_59 + m60_61 + m62_64 +
        m65_66 + m67_69 + m70_74 + m75_79 + m80_84 + mOvr85,
      fOvr18 = f18_19 + f20 + f21 + f22_24 + f25_29 + f30_34 +
        f35_39 + f40_44 +f45_49 + f55_59 + f60_61 + f62_64 +
        f65_66 + f67_69 + f70_74 + f75_79 + f80_84 + fOvr85,
      mOvr65 = m65_66 + m67_69 + m70_74 + m75_79 + m80_84 + mOvr85,
      fOvr65 = f65_66 + f67_69 + f70_74 + f75_79 + f80_84 + fOvr85,
      Pop25  = TotPopEd - m1824 - f1824,
      SomeCollege = m2534_sc + m3544_sc + m4564_sc + m65p_sc + f2534_sc +
        f3544_sc + f4564_s9 + f65p_sc,
      EduNoHs =  m2534_s9 + m2534_nhs + m3544_s9 + m3544_nhs + m4564_s9 +
        m4564_nhs + m65p_s9 + m65p_nhs + f2534_s9 + f2534_nhs + f3544_s9 +
        f3544_nhs + f4564_s9 + f4564_nhs + f65p_s9 + f65p_nhs,
      EduHs = m2534_hs + m3544_hs + m4564_hs + m65p_hs + f2534_hs + f3544_hs +
        f4564_hs + f65p_hs,
      Bachelors = m2534_b + m3544_b + m4564_b + m65p_b + f2534_b + f3544_b +
        f4564_b + f65p_b,
      GradScl   = m2534_g + m3544_g + m4564_g + m65p_g + f2534_g + f3544_g +
        f4564_g + f65p_g
    ) |>
    mutate(
      SRatio   = round(100 * male   / female, 2),
      SRatio18 = round(100 * mOvr18 / fOvr18, 2),
      SRatio65 = round(100 * mOvr65 / fOvr65, 2),
      SomeCollege = round(100 * SomeCollege / Pop25, 2),
      EduNoHsP    = round(100 * EduNoHs     / Pop25, 2),
      EduHsP      = round(100 * EduHs       / Pop25, 2),
      BachelorsP  = round(100 * Bachelors   / Pop25, 2),
      GradSclP     = round(100 * GradScl    / Pop25, 2)
    ) |>
    mutate(
      Ovr16 = fAge16_19 + mAge16_19 + (age15_44 - age15_19) + age45_49 +
        age50_54 + age55_59 + age60_64 + Ovr65,
      Ovr21 = mOvr18 + fOvr18 - (m18_19 + f18_19 + m20 + f20),
    ) |>
    mutate(
      Ovr16P = round(100 * Ovr16  / TotPop, 2),
      Ovr18P = round(100 * Ovr18  / TotPop, 2),
      Ovr21P = round(100 * Ovr21  / TotPop, 2),
      Ovr65P = round(100 * Ovr65  / TotPop, 2),
      MaleP  = round(100 * male   / TotPop, 2),
      FemP   = round(100 * female / TotPop, 2)
    ) |>
    select(
      GEOID, TotPop, MaleP, FemP, Ovr16, Ovr16P, Ovr18, Ovr18P, Ovr21, Ovr21P,
      Ovr65, Ovr65P, SRatio, SRatio18, SRatio65, WhiteE, AsianE, PacIsE,
      HisE, AmIndE, TwoPlsE, OtherE, SomeCollege, EduNoHsP, EduHsP,
      BachelorsP, GradSclP
    )

#### Tract Logic -------

tract <- map_dfr(
  .x = state_fips,
  ~ get_acs(
    geography = "tract",
    year = year,
    variables = variables_to_fetch,
    state = .x
  )
)

tract <- tract |>
  select(-NAME, -moe) |>
  spread(variable, estimate) |>
    dplyr::mutate(
      mOvr18 = m18_19 + m20 + m21 + m22_24 + m25_29 + m30_34 +
        m35_39 + m40_44 + m45_49 + m55_59 + m60_61 + m62_64 +
        m65_66 + m67_69 + m70_74 + m75_79 + m80_84 + mOvr85,
      fOvr18 = f18_19 + f20 + f21 + f22_24 + f25_29 + f30_34 +
        f35_39 + f40_44 +f45_49 + f55_59 + f60_61 + f62_64 +
        f65_66 + f67_69 + f70_74 + f75_79 + f80_84 + fOvr85,
      mOvr65 = m65_66 + m67_69 + m70_74 + m75_79 + m80_84 + mOvr85,
      fOvr65 = f65_66 + f67_69 + f70_74 + f75_79 + f80_84 + fOvr85,
      Pop25  = TotPopEd - m1824 - f1824,
      SomeCollege = m2534_sc + m3544_sc + m4564_sc + m65p_sc + f2534_sc +
        f3544_sc + f4564_s9 + f65p_sc,
      EduNoHs =  m2534_s9 + m2534_nhs + m3544_s9 + m3544_nhs + m4564_s9 +
        m4564_nhs + m65p_s9 + m65p_nhs + f2534_s9 + f2534_nhs + f3544_s9 +
        f3544_nhs + f4564_s9 + f4564_nhs + f65p_s9 + f65p_nhs,
      EduHs = m2534_hs + m3544_hs + m4564_hs + m65p_hs + f2534_hs + f3544_hs +
        f4564_hs + f65p_hs,
      Bachelors = m2534_b + m3544_b + m4564_b + m65p_b + f2534_b + f3544_b +
        f4564_b + f65p_b,
      GradScl   = m2534_g + m3544_g + m4564_g + m65p_g + f2534_g + f3544_g +
        f4564_g + f65p_g
    ) |>
    mutate(
      SRatio   = round(100 * male   / female, 2),
      SRatio18 = round(100 * mOvr18 / fOvr18, 2),
      SRatio65 = round(100 * mOvr65 / fOvr65, 2),
      SomeCollege = round(100 * SomeCollege / Pop25, 2),
      EduNoHsP    = round(100 * EduNoHs     / Pop25, 2),
      EduHsP      = round(100 * EduHs       / Pop25, 2),
      BachelorsP  = round(100 * Bachelors   / Pop25, 2),
      GradSclP     = round(100 * GradScl    / Pop25, 2)
    ) |>
    mutate(
      Ovr16 = fAge16_19 + mAge16_19 + (age15_44 - age15_19) + age45_49 +
        age50_54 + age55_59 + age60_64 + Ovr65,
      Ovr21 = mOvr18 + fOvr18 - (m18_19 + f18_19 + m20 + f20),
    ) |>
    mutate(
      Ovr16P = round(100 * Ovr16  / TotPop, 2),
      Ovr18P = round(100 * Ovr18  / TotPop, 2),
      Ovr21P = round(100 * Ovr21  / TotPop, 2),
      Ovr65P = round(100 * Ovr65  / TotPop, 2),
      MaleP  = round(100 * male   / TotPop, 2),
      FemP   = round(100 * female / TotPop, 2)
    ) |>
    select(
      GEOID, TotPop, MaleP, FemP, Ovr16, Ovr16P, Ovr18, Ovr18P, Ovr21, Ovr21P,
      Ovr65, Ovr65P, SRatio, SRatio18, SRatio65, WhiteE, AsianE, PacIsE,
      HisE, AmIndE, TwoPlsE, OtherE, SomeCollege, EduNoHsP, EduHsP,
      BachelorsP, GradSclP
    )

#### ZCTA Logic -------

zcta <- map_dfr(
  .x = state_fips,
  ~ get_acs(
    geography = "zcta",
    year = year,
    variables = variables_to_fetch,
    state = .x
  )
)

zcta <- zcta |>
  select(-NAME, -moe) |>
  spread(variable, estimate) |>
    dplyr::mutate(
      mOvr18 = m18_19 + m20 + m21 + m22_24 + m25_29 + m30_34 +
        m35_39 + m40_44 + m45_49 + m55_59 + m60_61 + m62_64 +
        m65_66 + m67_69 + m70_74 + m75_79 + m80_84 + mOvr85,
      fOvr18 = f18_19 + f20 + f21 + f22_24 + f25_29 + f30_34 +
        f35_39 + f40_44 +f45_49 + f55_59 + f60_61 + f62_64 +
        f65_66 + f67_69 + f70_74 + f75_79 + f80_84 + fOvr85,
      mOvr65 = m65_66 + m67_69 + m70_74 + m75_79 + m80_84 + mOvr85,
      fOvr65 = f65_66 + f67_69 + f70_74 + f75_79 + f80_84 + fOvr85,
      Pop25  = TotPopEd - m1824 - f1824,
      SomeCollege = m2534_sc + m3544_sc + m4564_sc + m65p_sc + f2534_sc +
        f3544_sc + f4564_s9 + f65p_sc,
      EduNoHs =  m2534_s9 + m2534_nhs + m3544_s9 + m3544_nhs + m4564_s9 +
        m4564_nhs + m65p_s9 + m65p_nhs + f2534_s9 + f2534_nhs + f3544_s9 +
        f3544_nhs + f4564_s9 + f4564_nhs + f65p_s9 + f65p_nhs,
      EduHs = m2534_hs + m3544_hs + m4564_hs + m65p_hs + f2534_hs + f3544_hs +
        f4564_hs + f65p_hs,
      Bachelors = m2534_b + m3544_b + m4564_b + m65p_b + f2534_b + f3544_b +
        f4564_b + f65p_b,
      GradScl   = m2534_g + m3544_g + m4564_g + m65p_g + f2534_g + f3544_g +
        f4564_g + f65p_g
    ) |>
    mutate(
      SRatio   = round(100 * male   / female, 2),
      SRatio18 = round(100 * mOvr18 / fOvr18, 2),
      SRatio65 = round(100 * mOvr65 / fOvr65, 2),
      SomeCollege = round(100 * SomeCollege / Pop25, 2),
      EduNoHsP    = round(100 * EduNoHs     / Pop25, 2),
      EduHsP      = round(100 * EduHs       / Pop25, 2),
      BachelorsP  = round(100 * Bachelors   / Pop25, 2),
      GradSclP     = round(100 * GradScl    / Pop25, 2)
    ) |>
    mutate(
      Ovr16 = fAge16_19 + mAge16_19 + (age15_44 - age15_19) + age45_49 +
        age50_54 + age55_59 + age60_64 + Ovr65,
      Ovr21 = mOvr18 + fOvr18 - (m18_19 + f18_19 + m20 + f20),
    ) |>
    mutate(
      Ovr16P = round(100 * Ovr16  / TotPop, 2),
      Ovr18P = round(100 * Ovr18  / TotPop, 2),
      Ovr21P = round(100 * Ovr21  / TotPop, 2),
      Ovr65P = round(100 * Ovr65  / TotPop, 2),
      MaleP  = round(100 * male   / TotPop, 2),
      FemP   = round(100 * female / TotPop, 2)
    ) |>
    select(
      GEOID, TotPop, MaleP, FemP, Ovr16, Ovr16P, Ovr18, Ovr18P, Ovr21, Ovr21P,
      Ovr65, Ovr65P, SRatio, SRatio18, SRatio65, WhiteE, AsianE, PacIsE,
      HisE, AmIndE, TwoPlsE, OtherE, SomeCollege, EduNoHsP, EduHsP,
      BachelorsP, GradSclP
    )

# write.csv(tract, file=str_c(save_dir, "/tract-", year, ".csv"), row.names=FALSE)
# write.csv(state, file=str_c(save_dir, "/state-", year, ".csv"), row.names=FALSE)
# write.csv(county, file=str_c(save_dir, "/county-", year, ".csv"), row.names=FALSE)
# write.csv(zcta, file=str_c(save_dir, "/zcta-", year, ".csv"), row.names=FALSE)
