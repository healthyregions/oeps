# Load necessary libraries for data manipulation and analysis
library(sf)  # For working with spatial data
library(tidyverse)  # For data manipulation (dplyr, ggplot2, etc.)
library(tidycensus)  # For accessing US Census data

setwd(getSrcDirectory(function(){})[1])

# Check for Census API key
Sys.getenv("CENSUS_API_KEY")

### Variables for editing script output quickly
save_dir <- "exported"
year <- 2020
dc_variables_2010 <- c(
  # -------------------- Tot Pop -------------------- #
  "TotPop"     = "P003001",
  # --------------- Race and Ethnicity -------------- #
  "WhiteE"     = "P003002", "BlackE"     = "P003003",
  "AmIndE"     = "P003004", "AsianE"     = "P003005",
  "PacIsE"     = "P003006", "OtherE"     = "P003007",
  "TwoPlsE"    = "P003008", "HispE"      = "P011002",
  # ------------------ Age Data --------------------- #
  "Female"     = "P014023", "Male"       = "P014002",
  "ageMl16"    = "P014019", "ageMl17"    = "P014020",
  "ageFm16"    = "P014040", "ageFm17"    = "P014041",
  "ageMl0_4"   = "P012003", "ageMl5_9"   = "P012004",
  "ageMl10_14" = "P012005", "ageMl15_17" = "P012006",
  "ageMl18_19" = "P012007", "ageMl20"    = "P012008",
  "ageMl21"    = "P012009", "ageMl22_24" = "P012010",
  "ageMl25_29" = "P012011", "ageMl30_34" = "P012012",
  "ageMl35_39" = "P012013", "ageMl40_44" = "P012014",
  "ageMl45_49" = "P012015", "ageMl50_54" = "P012016",
  "ageMl55_59" = "P012017", "ageMl60_61" = "P012018",
  "ageMl62_64" = "P012019", "ageMl65_66" = "P012020",
  "ageMl67_69" = "P012021", "ageMl70_74" = "P012022",
  "ageMl75_79" = "P012023", "ageMl80_84" = "P012024",
  "ageMlOv85"  = "P012025", "ageFm0_4"   = "P012027",
  "ageFm5_9"   = "P012028", "ageFm10_14" = "P012029",
  "ageFm15_17" = "P012030", "ageFm18_19" = "P012031",
  "ageFm20"    = "P012032", "ageFm21"    = "P012033",
  "ageFm22_24" = "P012034", "ageFm25_29" = "P012035",
  "ageFm30_34" = "P012036", "ageFm35_39" = "P012037",
  "ageFm40_44" = "P012038", "ageFm45_49" = "P012039",
  "ageFm50_54" = "P012040", "ageFm55_59" = "P012041",
  "ageFm60_61" = "P012042", "ageFm62_64" = "P012043",
  "ageFm65_66" = "P012044", "ageFm67_69" = "P012045",
  "ageFm70_74" = "P012046", "ageFm75_79" = "P012047",
  "ageFm80_84" = "P012048", "ageFmOv85"  = "P012049"
)

acs_variables <- c(
  # ---- Sex by Age by Educational Attainment ---- #
  TotPop   = "B15001_001", m1824    = "B15001_003",
  f1824    = "B15001_044", m2534_sc = "B15001_015",
  m3544_sc = "B15001_023", m4564_sc = "B15001_031",
  m65p_sc  = "B15001_039", f2534_sc = "B15001_056",
  f3544_sc = "B15001_064", f4564_sc = "B15001_072",
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
state_fips <- tigris::fips_codes |>
  filter(! state_code %in% c("60", "72", "66", "69", "78", "74")) |>
  select(state_code) |>
  unique()

state_fips <- state_fips$state_code

##### Tract Data -----

tract_acs <- map_dfr(
  .x = state_fips,
  ~ get_acs(
    geography = "tract",
    variables = acs_variables,
    year = year,
    geometry = FALSE,
    state = .x
  )
)

tract_acs <- tract_acs |>
  select(GEOID, variable, estimate) |>
  spread(variable, estimate) |>
  mutate(
    Pop25 = TotPop - m1824 - f1824
  ) |>
  mutate(
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
    SomeCollege = round(100 * SomeCollege / Pop25, 2),
    EduNoHsP    = round(100 * EduNoHs     / Pop25, 2),
    EduHsP      = round(100 * EduHs       / Pop25, 2),
    BachelorsP  = round(100 * Bachelors   / Pop25, 2),
    GradSclP     = round(100 * GradScl    / Pop25, 2)
  ) |>
  select(GEOID, SomeCollege, EduNoHsP, EduHsP, BachelorsP, GradSclP)

tract_dec <- map_dfr(
  .x = state_fips,
  ~ get_decennial(
    geography = "tract",
    year = year,
    variables = dc_variables_2010,
    state = .x
  )
)

tract_dec <- tract_dec |>
  select(-NAME) |>
  spread(variable, value) |>
  mutate(
    Ovr16 = ageMl16 + ageFm16 + ageMl17 + ageFm17 + ageMl18_19 +
      ageFm18_19 + ageMl20 + ageFm20 + ageMl21 + ageFm21 + ageMl22_24 +
      ageFm22_24 + ageMl25_29 + ageFm25_29 + ageMl30_34 + ageFm30_34 +
      ageMl35_39 + ageFm35_39 + ageMl40_44 + ageFm40_44 + ageMl45_49 +
      ageFm45_49 + ageMl50_54 + ageFm50_54 + ageMl55_59 + ageFm55_59 +
      ageMl60_61 + ageFm60_61 + ageMl62_64 + ageFm62_64 +  ageMl65_66 +
      ageFm65_66 + ageMl67_69 + ageFm67_69 + ageMl70_74 + ageFm70_74 +
      ageMl75_79 + ageFm75_79 + ageMl80_84 + ageFm80_84 + ageMlOv85 + ageFmOv85,
    Ovr18 = ageMl18_19 + ageFm18_19 + ageMl20 + ageFm20 + ageMl21 +
      ageFm21 + ageMl22_24 + ageFm22_24 + ageMl25_29 + ageFm25_29 + ageMl30_34 +
      ageFm30_34 + ageMl35_39 + ageFm35_39 + ageMl40_44 + ageFm40_44 +
      ageMl45_49 + ageFm45_49 + ageMl50_54 + ageFm50_54 + ageMl55_59 +
      ageFm55_59 + ageMl60_61 + ageFm60_61 + ageMl62_64 + ageFm62_64 +
      ageMl65_66 + ageFm65_66 + ageMl67_69 + ageFm67_69 + ageMl70_74 +
      ageFm70_74 + ageMl75_79 + ageFm75_79 + ageMl80_84 + ageFm80_84 +
      ageMlOv85 + ageFmOv85,
    fOvr18 = ageFm18_19 + ageFm20 + ageFm21 + ageFm22_24 + ageFm25_29 +
      ageFm30_34 + ageFm35_39 + ageFm40_44 + ageFm45_49 + ageFm50_54 +
      ageFm55_59 + ageFm60_61 + ageFm62_64 + ageFm65_66 + ageFm67_69 +
      ageFm70_74 + ageFm75_79 + ageFm80_84 + ageFmOv85,
    mOvr18 = ageMl18_19 + ageMl20 + ageMl21 + ageMl22_24 + ageMl25_29 +
      ageMl30_34 + ageMl35_39 + ageMl40_44 + ageMl45_49 + ageMl50_54 +
      ageMl55_59 + ageMl60_61 + ageMl62_64 + ageMl65_66 + ageMl67_69 +
      ageMl70_74 + ageMl75_79 + ageMl80_84 + ageMlOv85,
    Ovr21 = ageMl21 + ageFm21 + ageMl22_24 + ageFm22_24 + ageMl25_29 +
      ageFm25_29 + ageMl30_34 + ageFm30_34 + ageMl35_39 + ageFm35_39 +
      ageMl40_44 + ageFm40_44 + ageMl45_49 + ageFm45_49 + ageMl50_54 +
      ageFm50_54 + ageMl55_59 + ageFm55_59 + ageMl60_61 + ageFm60_61 +
      ageMl62_64 + ageFm62_64 + ageMl65_66 + ageFm65_66 + ageMl67_69 +
      ageFm67_69 + ageMl70_74 + ageFm70_74 + ageMl75_79 + ageFm75_79 +
      ageMl80_84 + ageFm80_84 + ageMlOv85 + ageFmOv85,
    Ovr65 = ageMl65_66 + ageFm65_66 + ageMl67_69 + ageFm67_69 + ageMl70_74 +
      ageFm70_74 + ageMl75_79 + ageFm75_79 + ageMl80_84 + ageFm80_84 +
      ageMlOv85 + ageFmOv85,
    mOvr65 = ageMl65_66 + ageMl67_69 + ageMl70_74 + ageMl75_79 + ageMl80_84 +
      ageMlOv85,
    fOvr65 = ageFm65_66 + ageFm67_69 + ageFm70_74 + ageFm75_79 + ageFm80_84 +
      ageFmOv85
  ) |>
  mutate(
    Ovr16P = round(100 * Ovr16 / TotPop, 2),
    Ovr18P = round(100 * Ovr18 / TotPop, 2),
    Ovr21P = round(100 * Ovr21 / TotPop, 2),
    Ovr65P = round(100 * Ovr65 / TotPop, 2),
    FemaleP = round(100 * Female / TotPop, 2),
    MaleP   = round(100 * Male / TotPop, 2),
    SRatio = round(100 * Male / Female, 2),
    SRatio18 = round(100 * mOvr18 / fOvr18, 2),
    SRatio65 = round(100 * mOvr65 / fOvr65, 2),
    WhiteP  = round(100 * WhiteE / TotPop, 2),
    BlackP  = round(100 * BlackE / TotPop, 2),
    AmIndP  = round(100 * AmIndE / TotPop, 2),
    AsianP  = round(100 * AsianE / TotPop, 2),
    PacIsP  = round(100 * PacIsE / TotPop, 2),
    OtherP  = round(100 * OtherE / TotPop, 2),
    TwoPlsP = round(100 * TwoPlsE / TotPop, 2),
    HispP   = round(100 * HispE / TotPop, 2)
  ) |>
  select(
    GEOID, Ovr16P, Ovr18P, Ovr21P, Ovr65P, SRatio, SRatio18, SRatio65,
    FemaleP, MaleP, WhiteP, WhiteE, BlackP, BlackE, AmIndP, AmIndE, AsianP,
    AsianE, PacIsP, PacIsE, OtherP, OtherE, TwoPlsP, TwoPlsE, HispP, HispE
  )

### County Data ----

county_acs <- map_dfr(
  .x = state_fips,
  ~ get_acs(
    geography = "county",
    variables = acs_variables,
    year = year,
    geometry = FALSE,
    state = .x
  )
)

county_acs <- county_acs |>
  select(GEOID, variable, estimate) |>
  spread(variable, estimate) |>
  mutate(
    Pop25 = TotPop - m1824 - f1824
  ) |>
  mutate(
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
    SomeCollege = round(100 * SomeCollege / Pop25, 2),
    EduNoHsP    = round(100 * EduNoHs     / Pop25, 2),
    EduHsP      = round(100 * EduHs       / Pop25, 2),
    BachelorsP  = round(100 * Bachelors   / Pop25, 2),
    GradSclP     = round(100 * GradScl    / Pop25, 2)
  ) |>
  select(GEOID, SomeCollege, EduNoHsP, EduHsP, BachelorsP, GradSclP)

county_dec <- map_dfr(
  .x = state_fips,
  ~ get_decennial(
    geography = "county",
    year = year,
    variables = dc_variables_2010,
    state = .x
  )
)

county_dec <- county_dec |>
  select(-NAME) |>
  spread(variable, value) |>
  mutate(
    Ovr16 = ageMl16 + ageFm16 + ageMl17 + ageFm17 + ageMl18_19 +
      ageFm18_19 + ageMl20 + ageFm20 + ageMl21 + ageFm21 + ageMl22_24 +
      ageFm22_24 + ageMl25_29 + ageFm25_29 + ageMl30_34 + ageFm30_34 +
      ageMl35_39 + ageFm35_39 + ageMl40_44 + ageFm40_44 + ageMl45_49 +
      ageFm45_49 + ageMl50_54 + ageFm50_54 + ageMl55_59 + ageFm55_59 +
      ageMl60_61 + ageFm60_61 + ageMl62_64 + ageFm62_64 +  ageMl65_66 +
      ageFm65_66 + ageMl67_69 + ageFm67_69 + ageMl70_74 + ageFm70_74 +
      ageMl75_79 + ageFm75_79 + ageMl80_84 + ageFm80_84 + ageMlOv85 + ageFmOv85,
    Ovr18 = ageMl18_19 + ageFm18_19 + ageMl20 + ageFm20 + ageMl21 +
      ageFm21 + ageMl22_24 + ageFm22_24 + ageMl25_29 + ageFm25_29 + ageMl30_34 +
      ageFm30_34 + ageMl35_39 + ageFm35_39 + ageMl40_44 + ageFm40_44 +
      ageMl45_49 + ageFm45_49 + ageMl50_54 + ageFm50_54 + ageMl55_59 +
      ageFm55_59 + ageMl60_61 + ageFm60_61 + ageMl62_64 + ageFm62_64 +
      ageMl65_66 + ageFm65_66 + ageMl67_69 + ageFm67_69 + ageMl70_74 +
      ageFm70_74 + ageMl75_79 + ageFm75_79 + ageMl80_84 + ageFm80_84 +
      ageMlOv85 + ageFmOv85,
    fOvr18 = ageFm18_19 + ageFm20 + ageFm21 + ageFm22_24 + ageFm25_29 +
      ageFm30_34 + ageFm35_39 + ageFm40_44 + ageFm45_49 + ageFm50_54 +
      ageFm55_59 + ageFm60_61 + ageFm62_64 + ageFm65_66 + ageFm67_69 +
      ageFm70_74 + ageFm75_79 + ageFm80_84 + ageFmOv85,
    mOvr18 = ageMl18_19 + ageMl20 + ageMl21 + ageMl22_24 + ageMl25_29 +
      ageMl30_34 + ageMl35_39 + ageMl40_44 + ageMl45_49 + ageMl50_54 +
      ageMl55_59 + ageMl60_61 + ageMl62_64 + ageMl65_66 + ageMl67_69 +
      ageMl70_74 + ageMl75_79 + ageMl80_84 + ageMlOv85,
    Ovr21 = ageMl21 + ageFm21 + ageMl22_24 + ageFm22_24 + ageMl25_29 +
      ageFm25_29 + ageMl30_34 + ageFm30_34 + ageMl35_39 + ageFm35_39 +
      ageMl40_44 + ageFm40_44 + ageMl45_49 + ageFm45_49 + ageMl50_54 +
      ageFm50_54 + ageMl55_59 + ageFm55_59 + ageMl60_61 + ageFm60_61 +
      ageMl62_64 + ageFm62_64 + ageMl65_66 + ageFm65_66 + ageMl67_69 +
      ageFm67_69 + ageMl70_74 + ageFm70_74 + ageMl75_79 + ageFm75_79 +
      ageMl80_84 + ageFm80_84 + ageMlOv85 + ageFmOv85,
    Ovr65 = ageMl65_66 + ageFm65_66 + ageMl67_69 + ageFm67_69 + ageMl70_74 +
      ageFm70_74 + ageMl75_79 + ageFm75_79 + ageMl80_84 + ageFm80_84 +
      ageMlOv85 + ageFmOv85,
    mOvr65 = ageMl65_66 + ageMl67_69 + ageMl70_74 + ageMl75_79 + ageMl80_84 +
      ageMlOv85,
    fOvr65 = ageFm65_66 + ageFm67_69 + ageFm70_74 + ageFm75_79 + ageFm80_84 +
      ageFmOv85
  ) |>
  mutate(
    Ovr16P = round(100 * Ovr16 / TotPop, 2),
    Ovr18P = round(100 * Ovr18 / TotPop, 2),
    Ovr21P = round(100 * Ovr21 / TotPop, 2),
    Ovr65P = round(100 * Ovr65 / TotPop, 2),
    FemaleP = round(100 * Female / TotPop, 2),
    MaleP   = round(100 * Male / TotPop, 2),
    SRatio = round(100 * Male / Female, 2),
    SRatio18 = round(100 * mOvr18 / fOvr18, 2),
    SRatio65 = round(100 * mOvr65 / fOvr65, 2),
    WhiteP  = round(100 * WhiteE / TotPop, 2),
    BlackP  = round(100 * BlackE / TotPop, 2),
    AmIndP  = round(100 * AmIndE / TotPop, 2),
    AsianP  = round(100 * AsianE / TotPop, 2),
    PacIsP  = round(100 * PacIsE / TotPop, 2),
    OtherP  = round(100 * OtherE / TotPop, 2),
    TwoPlsP = round(100 * TwoPlsE / TotPop, 2),
    HispP   = round(100 * HispE / TotPop, 2)
  ) |>
  select(
    GEOID, Ovr16P, Ovr18P, Ovr21P, Ovr65P, SRatio, SRatio18, SRatio65,
    FemaleP, MaleP, WhiteP, WhiteE, BlackP, BlackE, AmIndP, AmIndE, AsianP,
    AsianE, PacIsP, PacIsE, OtherP, OtherE, TwoPlsP, TwoPlsE, HispP, HispE
  )

### State Data ----

state_acs <- get_acs(
  geography = "state",
  variables = acs_variables,
  year = year,
  geometry = FALSE,
) |>
  select(GEOID, variable, estimate) |>
  spread(variable, estimate) |>
  mutate(
    Pop25 = TotPop - m1824 - f1824
  ) |>
  mutate(
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
    SomeCollege = round(100 * SomeCollege / Pop25, 2),
    EduNoHsP    = round(100 * EduNoHs     / Pop25, 2),
    EduHsP      = round(100 * EduHs       / Pop25, 2),
    BachelorsP  = round(100 * Bachelors   / Pop25, 2),
    GradSclP     = round(100 * GradScl    / Pop25, 2)
  ) |>
  select(GEOID, SomeCollege, EduNoHsP, EduHsP, BachelorsP, GradSclP)

state_dec <- get_decennial(
  geography = "state",
  year = year,
  variables = c('P003004'),
) |>
  select(-NAME) |>
  spread(variable, value) |>
  mutate(
    Ovr16 = ageMl16 + ageFm16 + ageMl17 + ageFm17 + ageMl18_19 +
      ageFm18_19 + ageMl20 + ageFm20 + ageMl21 + ageFm21 + ageMl22_24 +
      ageFm22_24 + ageMl25_29 + ageFm25_29 + ageMl30_34 + ageFm30_34 +
      ageMl35_39 + ageFm35_39 + ageMl40_44 + ageFm40_44 + ageMl45_49 +
      ageFm45_49 + ageMl50_54 + ageFm50_54 + ageMl55_59 + ageFm55_59 +
      ageMl60_61 + ageFm60_61 + ageMl62_64 + ageFm62_64 +  ageMl65_66 +
      ageFm65_66 + ageMl67_69 + ageFm67_69 + ageMl70_74 + ageFm70_74 +
      ageMl75_79 + ageFm75_79 + ageMl80_84 + ageFm80_84 + ageMlOv85 + ageFmOv85,
    Ovr18 = ageMl18_19 + ageFm18_19 + ageMl20 + ageFm20 + ageMl21 +
      ageFm21 + ageMl22_24 + ageFm22_24 + ageMl25_29 + ageFm25_29 + ageMl30_34 +
      ageFm30_34 + ageMl35_39 + ageFm35_39 + ageMl40_44 + ageFm40_44 +
      ageMl45_49 + ageFm45_49 + ageMl50_54 + ageFm50_54 + ageMl55_59 +
      ageFm55_59 + ageMl60_61 + ageFm60_61 + ageMl62_64 + ageFm62_64 +
      ageMl65_66 + ageFm65_66 + ageMl67_69 + ageFm67_69 + ageMl70_74 +
      ageFm70_74 + ageMl75_79 + ageFm75_79 + ageMl80_84 + ageFm80_84 +
      ageMlOv85 + ageFmOv85,
    fOvr18 = ageFm18_19 + ageFm20 + ageFm21 + ageFm22_24 + ageFm25_29 +
      ageFm30_34 + ageFm35_39 + ageFm40_44 + ageFm45_49 + ageFm50_54 +
      ageFm55_59 + ageFm60_61 + ageFm62_64 + ageFm65_66 + ageFm67_69 +
      ageFm70_74 + ageFm75_79 + ageFm80_84 + ageFmOv85,
    mOvr18 = ageMl18_19 + ageMl20 + ageMl21 + ageMl22_24 + ageMl25_29 +
      ageMl30_34 + ageMl35_39 + ageMl40_44 + ageMl45_49 + ageMl50_54 +
      ageMl55_59 + ageMl60_61 + ageMl62_64 + ageMl65_66 + ageMl67_69 +
      ageMl70_74 + ageMl75_79 + ageMl80_84 + ageMlOv85,
    Ovr21 = ageMl21 + ageFm21 + ageMl22_24 + ageFm22_24 + ageMl25_29 +
      ageFm25_29 + ageMl30_34 + ageFm30_34 + ageMl35_39 + ageFm35_39 +
      ageMl40_44 + ageFm40_44 + ageMl45_49 + ageFm45_49 + ageMl50_54 +
      ageFm50_54 + ageMl55_59 + ageFm55_59 + ageMl60_61 + ageFm60_61 +
      ageMl62_64 + ageFm62_64 + ageMl65_66 + ageFm65_66 + ageMl67_69 +
      ageFm67_69 + ageMl70_74 + ageFm70_74 + ageMl75_79 + ageFm75_79 +
      ageMl80_84 + ageFm80_84 + ageMlOv85 + ageFmOv85,
    Ovr65 = ageMl65_66 + ageFm65_66 + ageMl67_69 + ageFm67_69 + ageMl70_74 +
      ageFm70_74 + ageMl75_79 + ageFm75_79 + ageMl80_84 + ageFm80_84 +
      ageMlOv85 + ageFmOv85,
    mOvr65 = ageMl65_66 + ageMl67_69 + ageMl70_74 + ageMl75_79 + ageMl80_84 +
      ageMlOv85,
    fOvr65 = ageFm65_66 + ageFm67_69 + ageFm70_74 + ageFm75_79 + ageFm80_84 +
      ageFmOv85
  ) |>
  mutate(
    Ovr16P = round(100 * Ovr16 / TotPop, 2),
    Ovr18P = round(100 * Ovr18 / TotPop, 2),
    Ovr21P = round(100 * Ovr21 / TotPop, 2),
    Ovr65P = round(100 * Ovr65 / TotPop, 2),
    FemaleP = round(100 * Female / TotPop, 2),
    MaleP   = round(100 * Male / TotPop, 2),
    SRatio = round(100 * Male / Female, 2),
    SRatio18 = round(100 * mOvr18 / fOvr18, 2),
    SRatio65 = round(100 * mOvr65 / fOvr65, 2),
    WhiteP  = round(100 * WhiteE / TotPop, 2),
    BlackP  = round(100 * BlackE / TotPop, 2),
    AmIndP  = round(100 * AmIndE / TotPop, 2),
    AsianP  = round(100 * AsianE / TotPop, 2),
    PacIsP  = round(100 * PacIsE / TotPop, 2),
    OtherP  = round(100 * OtherE / TotPop, 2),
    TwoPlsP = round(100 * TwoPlsE / TotPop, 2),
    HispP   = round(100 * HispE / TotPop, 2)
  ) |>
  select(
    GEOID, Ovr16P, Ovr18P, Ovr21P, Ovr65P, SRatio, SRatio18, SRatio65,
    FemaleP, MaleP, WhiteP, WhiteE, BlackP, BlackE, AmIndP, AmIndE, AsianP,
    AsianE, PacIsP, PacIsE, OtherP, OtherE, TwoPlsP, TwoPlsE, HispP, HispE
  )

### Save

tracts <- merge(tract_acs, tract_dec, by = "GEOID", row.names=FALSE)
state <- merge(state_acs, state_dec, by = "GEOID", row.names=FALSE)
county <- merge(county_acs, county_dec, by = "GEOID", row.names=FALSE)

write.csv(tracts, str_c(save_dir, "/tracts", year, ".csv"))
write.csv(state, str_c(save_dir, "/state", year, ".csv"))
write.csv(county, str_c(save_dir, "/county", year, ".csv"))