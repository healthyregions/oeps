################################ State Level Cleaning ##########################

## Original CSV data has been cleaned in Excel before importing in R
## Removed un-related variables and added HEROP_ID

# Read pre-cleaned state data
state <- read.csv("Prison_Incarceration_Rates_state_level.csv")

# Subset the data for 2024
state_2024 <- subset(state, YEAR == 2024)
state_2024 <- subset(state_2024, select = -c(TtlPrAPpr, TtlPrAPp))
state_2024$GEOID <- sprintf("%02d", as.numeric(state_2024$GEOID))

# Subset the data for 2022
state_2022 <- subset(state, YEAR == 2022)
state_2022$GEOID <- sprintf("%02d", as.numeric(state_2022$GEOID))

# Save state data
write.csv(state_2024, "state_2024.csv", row.names = FALSE)
write.csv(state_2022, "state_2022.csv", row.names = FALSE)


############################### County Level Cleaning ##########################

## Original CSV data has been cleaned in Excel before importing in R
## Removed un-related variables and added HEROP_ID

# Read pre-cleaned data
county <- read.csv("Prison_Incarceration_Rates_county_level.csv")

# Subset the data for 2019
county_2019 <- subset(county, Year == 2019)

# Identify which columns are character/factor
char_cols <- sapply(county_2019, function(x) is.character(x) || is.factor(x))

# For character/factor columns:
# Mark a row TRUE if ANY of its character fields is an empty string after trimming
# If there are no character columns, just treat as all FALSE
# Remove empty rows here because multiple blank rows of invalid values exist after the first row of valid values within the same county
empty_any <- if (any(char_cols)) {
  apply(as.data.frame(lapply(county_2019[, char_cols, drop = FALSE], function(x)
    trimws(as.character(x)) == "")), 1, any)
} else {
  rep(FALSE, nrow(county_2019))
}

# No NA in ANY column, no blank strings in character columns
complete_nonempty <- complete.cases(county_2019) & !empty_any

# Split into blocks
complete_block   <- county_2019[complete_nonempty, , drop = FALSE]
incomplete_block <- county_2019[!complete_nonempty, , drop = FALSE]  # keep as-is

# De-duplicate only the complete rows (exact duplicate rows)
dedup_complete <- complete_block[!duplicated(complete_block), , drop = FALSE]

# Re-combine: deduped complete rows + original incomplete rows
county_2019_clean <- rbind(dedup_complete, incomplete_block)


# When duplicates exist for the same county (HEROP_ID), keep the row with real values
# If a county only has NA-only rows, keep one NA-only row (don’t drop the county)

library(dplyr)

meas <- c("TtlPrPpr","TtlPrAPpr","TtlPrPp","TtlPrAPp")

is_nonmissing <- function(x) {
  if (is.character(x)) {
    !is.na(x) & trimws(x) != ""
  } else {
    !is.na(x)
  }
}

# Build a non-missing indicator matrix for the measure columns
# (each column becomes TRUE/FALSE per row)
nonmiss_mat <- as.data.frame(lapply(county_2019[meas], is_nonmissing))

# Add a score: how many of the 4 measure columns are non-missing in each row
county_2019_scored <- county_2019 %>%
  mutate(nonmiss = rowSums(nonmiss_mat))

# Standardize year column name to YEAR (handles YEAR / Year / year)
county_2019_scored <- county_2019_scored %>%
  rename(YEAR = any_of(c("YEAR","Year","year")))

nrow(county_2019)
nrow(county_2019_clean)

county_2019_clean %>% filter(HEROP_ID == "050US51001") # Accomack, VA: keep 1 NA-only row
county_2019_clean %>% filter(HEROP_ID == "050US28003") # Alcorn, MS: keep the row with values

n_distinct(county_2019_clean$HEROP_ID) # how many unique counties kept
any(duplicated(county_2019_clean[c("HEROP_ID","YEAR")]))

# Ensure county GEOID is always 5-digit FIPS
county_2019_clean <- county_2019_clean %>%
  mutate(GEOID = sprintf("%05d", as.integer(GEOID)))

## Order by HEROP_ID and only keep the first row for repeated rows:
## Clean whitespace and types
## Compute nonmiss score from the 4 measure columns
## Sort so higher nonmiss comes first
## Keep the first row per HEROP_ID

meas <- c("TtlPrPpr","TtlPrAPpr","TtlPrPp","TtlPrAPp")

is_nonmissing <- function(x) if (is.character(x)) !is.na(x) & trimws(x) != "" else !is.na(x)

county_2019 <- county_2019 %>%
  rename(YEAR = any_of(c("YEAR","Year","year"))) %>% # standardize the year name
  mutate(
    HEROP_ID   = trimws(as.character(HEROP_ID)),
    GEOID      = trimws(as.character(GEOID)),
    state_fips = trimws(as.character(state_fips)),
    county_name= trimws(as.character(county_name)),
    YEAR       = as.integer(YEAR)
  ) %>%
  # score each row by how many of the 4 measures are non-missing
  mutate(nonmiss = rowSums(as.data.frame(lapply(across(all_of(meas)), is_nonmissing)))) %>%
  arrange(HEROP_ID, desc(nonmiss)) %>%  # order by HEROP_ID, prefer rows with data
  distinct(HEROP_ID, .keep_all = TRUE) %>% # keep the first row per HEROP_ID
  select(-nonmiss) # drop helper column

any(duplicated(county_2019$HEROP_ID))
nrow(county_2019 # now one row per county

## Methods 2 Test
## - Sort by HEROP_ID
## - Keep the first row per HEROP_ID

county_2019 <- county_2019 %>%
  rename(YEAR = any_of(c("YEAR","Year","year"))) %>% # standardize column name
  mutate(
    HEROP_ID   = trimws(as.character(HEROP_ID)), # clean up spaces
    GEOID      = trimws(as.character(GEOID)),
    state_fips = trimws(as.character(state_fips)),
    county_name= trimws(as.character(county_name)),
    YEAR       = as.integer(YEAR)
  ) %>%
  arrange(HEROP_ID) %>% # order by HEROP_ID
  distinct(HEROP_ID, .keep_all = TRUE) # keep the first row per HEROP_ID

any(duplicated(county_2019$HEROP_ID)) # should return FALSE
nrow(county_2019) # now ~ one row per county

# Save
write.csv(county_2019, "county_2019_test2.csv", row.names = FALSE)

## Additional data cleaning processed in Excel


################################ Jail Data Cleaning ##########################

# read data
jail_state <- read.csv("Jail_Incarceration_Rates_state_level.csv")

# subset the data for 2023
jail_state_2023 <- subset(jail_state, YEAR == 2023)
jail_state_2023 <- subset(jail_state_2023, select = -c(TtlJlAdmr, TtlJlAdm))
jail_state_2023$GEOID <- sprintf("%02d", as.numeric(jail_state_2023$GEOID))

# subset the data for 2022
jail_state_2022 <- subset(jail_state, YEAR == 2022)
jail_state_2022$GEOID <- sprintf("%02d", as.numeric(jail_state_2022$GEOID))

# save files
write.csv(jail_state_2023, "jail_state_2023.csv", row.names = FALSE)
write.csv(jail_state_2022, "jail_state_2022.csv", row.names = FALSE)

## Additional data cleaning processed in Excel


################################ Prison Map Visualization ##########################

## Read finalized data
state_data_2024 <- read.csv("Prison Incarceration Rates_state_level_2024.csv", stringsAsFactors = FALSE, check.names = FALSE)
state_data_2022 <- read.csv("Prison Incarceration Rates_state_level_2022.csv", stringsAsFactors = FALSE, check.names = FALSE)
county_data_2019 <- read.csv("Prison Incarceration Rates_county_level_2019.csv", stringsAsFactors = FALSE, check.names = FALSE)

## Read finalized data
state_data <- read.csv("Smoking Population_state_level_2025.csv", stringsAsFactors = FALSE, check.names = FALSE)
county_data <- read.csv("Smoking Population_county_level_2025.csv", stringsAsFactors = FALSE, check.names = FALSE)

# OEPS Geographic Boundaries: https://geodata.healthyregions.org/
library(sf)
state_boundary <- read_sf('/vsizip//vsicurl/https://herop-geodata.s3.us-east-2.amazonaws.com/oeps/state-2018-500k-shp.zip')
county_boundary <- read_sf('/vsizip//vsicurl/https://herop-geodata.s3.us-east-2.amazonaws.com/oeps/county-2018-500k-shp.zip')

# Add libraries
library(dplyr)
library(ggplot2)

# Ensure HEROP_ID is character on both sides
state_data_2024  <- state_data_2024  %>% mutate(HEROP_ID = as.character(HEROP_ID))
state_data_2022  <- state_data_2022  %>% mutate(HEROP_ID = as.character(HEROP_ID))
county_data_2019 <- county_data_2019 %>% mutate(HEROP_ID = as.character(HEROP_ID))

state_boundary  <- state_boundary  %>% mutate(HEROP_ID = as.character(HEROP_ID))
county_boundary <- county_boundary %>% mutate(HEROP_ID = as.character(HEROP_ID))

# Join prison data to geometry
state_map_2024 <- state_boundary %>%
  left_join(state_data_2024, by = "HEROP_ID")

state_map_2022 <- state_boundary %>%
  left_join(state_data_2022, by = "HEROP_ID")

county_map_2019 <- county_boundary %>%
  left_join(county_data_2019, by = "HEROP_ID")

# State-level Prison Population Rate (2024)
ggplot(state_map_2024) +
  geom_sf(aes(fill = TtlPrPpr), color = "white", linewidth = 0.2) +
  coord_sf(
    xlim = c(-125, -66),
    ylim = c(24, 50),
    expand = FALSE
  ) +
  scale_fill_gradient(
    low = "lightblue",
    high = "darkblue",
    na.value = "white",
    name = "TtlPrPpr"
  ) +
  labs(title = "State-level Prison Population Rate (2024)") +
  theme_minimal()

# State-level Prison Population Rate (2022)
ggplot(state_map_2022) +
  geom_sf(aes(fill = TtlPrPpr), color = "white", linewidth = 0.2) +
  coord_sf(
    xlim = c(-125, -66),
    ylim = c(24, 50),
    expand = FALSE
  ) +
  scale_fill_gradient(
    low = "lightblue",
    high = "darkblue",
    na.value = "white",
    name = "TtlPrPpr"
  ) +
  labs(title = "State-level Prison Population Rate (2022)") +
  theme_minimal()

# County-level Prison Population Rate (2019)
ggplot(county_map_2019) +
  geom_sf(aes(fill = TtlPrPpr), color = NA) +
  coord_sf(
    xlim = c(-125, -66),
    ylim = c(24, 50),
    expand = FALSE
  ) +
  scale_fill_gradient(
    low = "lightblue",
    high = "darkblue",
    na.value = "white",
    name = "TtlPrPpr"
  ) +
  labs(title = "County-level Prison Population Rate (2019)") +
  theme_minimal()

## Natural Break
library(dplyr)
library(sf)
library(ggplot2)
library(classInt)
library(RColorBrewer)

n_classes_state  <- 5
n_classes_county <- 5

fmt_num <- function(x) format(x, scientific = FALSE, big.mark = ",", trim = TRUE)

make_jenks_cat <- function(x, n_classes) {
  jenks <- classInt::classIntervals(x, n = n_classes, style = "jenks", na.rm = TRUE)
  brks  <- jenks$brks

  labs <- c(
    paste0("[", fmt_num(brks[1]), ", ", fmt_num(brks[2]), "]"),
    paste0("(", fmt_num(brks[2:n_classes]), ", ", fmt_num(brks[3:(n_classes + 1)]), "]")
  ) 

  # Assign class index (NA stays NA)
  idx <- findInterval(x, brks, rightmost.closed = TRUE, all.inside = TRUE)
  cat <- ifelse(is.na(x), "No data", labs[idx])
  
  list(
    cat_factor = factor(cat, levels = c("No data", labs)),
    levels_all = c("No data", labs)
  )
} 

# State 2024 Natrual Breaks
jenks_obj_2024 <- make_jenks_cat(state_map_2024$TtlPrPpr, n_classes_state)
state_map_2024$TtlPrPpr_cat <- jenks_obj_2024$cat_factor

blue_state <- brewer.pal(n_classes_state + 1, "Blues")[2:(n_classes_state + 1)]
fill_state <- c("No data" = "white", setNames(blue_state, jenks_obj_2024$levels_all[-1]))

ggplot(state_map_2024) +
  geom_sf(aes(fill = TtlPrPpr_cat), color = "white", linewidth = 0.2) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_manual(values = fill_state, limits = jenks_obj_2024$levels_all, name = "TtlPrPpr") +
  labs(title = "State-level Prison Population Rate (2024)") +
  theme_minimal()

# State 2022: Natural Breaks
jenks_obj_2022 <- make_jenks_cat(state_map_2022$TtlPrPpr, n_classes_state)
state_map_2022$TtlPrPpr_cat <- jenks_obj_2022$cat_factor

blue_state <- brewer.pal(n_classes_state + 1, "Blues")[2:(n_classes_state + 1)]
fill_state <- c("No data" = "white", setNames(blue_state, jenks_obj_2022$levels_all[-1]))

ggplot(state_map_2022) +
  geom_sf(aes(fill = TtlPrPpr_cat), color = "white", linewidth = 0.2) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_manual(values = fill_state, limits = jenks_obj_2022$levels_all, name = "TtlPrPpr") +
  labs(title = "State-level Prison Population Rate (2022)") +
  theme_minimal()

# County 2019: Natural Breaks
jenks_obj_c2019 <- make_jenks_cat(county_map_2019$TtlPrPpr, n_classes_county)
county_map_2019$TtlPrPpr_cat <- jenks_obj_c2019$cat_factor

blue_county <- brewer.pal(n_classes_county + 1, "Blues")[2:(n_classes_county + 1)]
fill_county <- c("No data" = "white", setNames(blue_county, jenks_obj_c2019$levels_all[-1]))

ggplot(county_map_2019) +
  geom_sf(aes(fill = TtlPrPpr_cat), color = "white", linewidth = 0.2) +  # same as states
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_manual(values = fill_county, limits = jenks_obj_c2019$levels_all, name = "TtlPrPpr") +
  labs(title = "County-level Prison Population Rate (2019)") +
  theme_minimal()

ggplot(county_map_2019) +
  geom_sf(
    aes(fill = TtlPrPpr_cat),
    color = "grey80",
    linewidth = 0.05
  ) +
  coord_sf(
    xlim = c(-125, -66),
    ylim = c(24, 50),
    expand = FALSE
  ) +
  scale_fill_manual(
    values = fill_county,
    limits = jenks_obj_c2019$levels_all,
    name = "TtlPrPpr"
  ) +
  labs(title = "County-level Prison Population Rate (2019)") +
  theme_minimal()


################################ Jail Map Visualization ##########################

## Read finalized data (Jail)
j_state_2023 <- read.csv("Jail Incarceration Rates_state_level_2023.csv", stringsAsFactors = FALSE, check.names = FALSE)
j_state_2022 <- read.csv("Jail Incarceration Rates_state_level_2022.csv", stringsAsFactors = FALSE, check.names = FALSE)
j_county_2024 <- read.csv("Jail Incarceration Rates_county_level_2024.csv", stringsAsFactors = FALSE, check.names = FALSE)
j_county_2023 <- read.csv("Jail Incarceration Rates_county_level_2023.csv", stringsAsFactors = FALSE, check.names = FALSE)

# Ensure HEROP_ID is character on both sides
j_state_2023  <- j_state_2023  %>% mutate(HEROP_ID = as.character(HEROP_ID))
j_state_2022  <- j_state_2022  %>% mutate(HEROP_ID = as.character(HEROP_ID))
j_county_2024 <- j_county_2024 %>% mutate(HEROP_ID = as.character(HEROP_ID))
j_county_2023 <- j_county_2023 %>% mutate(HEROP_ID = as.character(HEROP_ID)

# Join jail data to geometry
j_state_map_2023 <- state_boundary %>% left_join(j_state_2023,  by = "HEROP_ID")
j_state_map_2022 <- state_boundary %>% left_join(j_state_2022,  by = "HEROP_ID")
j_county_map_2024 <- county_boundary %>% left_join(j_county_2024, by = "HEROP_ID")
j_county_map_2023 <- county_boundary %>% left_join(j_county_2023, by = "HEROP_ID")

# State-level Pretrial Jail Population Rate (2023)
ggplot(j_state_map_2023) +
  geom_sf(aes(fill = TtlJlPrtr), color = "white", linewidth = 0.2) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_gradient(low = "lightblue", high = "darkblue", na.value = "white", name = "TtlJlPrtr") +
  labs(title = "State-level Pretrial Jail Population Rate (2023)") +
  theme_minimal()

# State-level Pretrial Jail Population Rate (2022)
ggplot(j_state_map_2022) +
  geom_sf(aes(fill = TtlJlPpr), color = "white", linewidth = 0.2) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_gradient(low = "lightblue", high = "darkblue",
                      na.value = "white", name = "TtlJlPpr") +
  labs(title = "State-level Total Jail Population Rate (2022)") +
  theme_minimal()

# County-level Pretrial Jail Population Rate (2024 Quarter 1)
ggplot(j_county_map_2024) +
  geom_sf(aes(fill = TtlJlPpr), color = NA) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_gradient(low = "lightblue", high = "darkblue",
                      na.value = "white", name = "TtlJlPpr") +
  labs(title = "County-level Total Jail Population Rate (2024 Quarter 1)") +
  theme_minimal()

# County-level Pretrial Jail Population Rate (2023 Quarter 1)
ggplot(j_county_map_2023) +
  geom_sf(aes(fill = TtlJlPpr_Q1), color = NA) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_gradient(low = "lightblue", high = "darkblue",
                      na.value = "white", name = "TtlJlPpr_Q1") +
  labs(title = "County-level Total Jail Population Rate (2023 Quarter 1)") +
  theme_minimal()

## Natural Breaks

# State 2023
jenks_j_s2023 <- make_jenks_cat(j_state_map_2023$TtlJlPpr, n_classes_state)
j_state_map_2023$TtlJlPpr_cat <- jenks_j_s2023$cat_factor
fill_j_state_2023 <- c("No data" = "white",
                       setNames(blue_state, jenks_j_s2023$levels_all[-1]))

ggplot(j_state_map_2023) +
  geom_sf(aes(fill = TtlJlPpr_cat), color = "white", linewidth = 0.2) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_manual(values = fill_j_state_2023,
                    limits = jenks_j_s2023$levels_all,
                    name = "TtlJlPpr") +
  labs(title = "State-level Total Jail Population Rate (2023)") +
  theme_minimal()

# State 2022
jenks_j_s2022 <- make_jenks_cat(j_state_map_2022$TtlJlPpr, n_classes_state)
j_state_map_2022$TtlJlPpr_cat <- jenks_j_s2022$cat_factor
fill_j_state_2022 <- c("No data" = "white",
                       setNames(blue_state, jenks_j_s2022$levels_all[-1]))

ggplot(j_state_map_2022) +
  geom_sf(aes(fill = TtlJlPpr_cat), color = "white", linewidth = 0.2) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_manual(values = fill_j_state_2022,
                    limits = jenks_j_s2022$levels_all,
                    name = "TtlJlPpr") +
  labs(title = "State-level Total Jail Population Rate (2022)") +
  theme_minimal()

# County 2024 Quarter 1
jenks_j_c2024 <- make_jenks_cat(j_county_map_2024$TtlJlPpr, n_classes_county)
j_county_map_2024$TtlJlPpr_cat <- jenks_j_c2024$cat_factor
fill_j_county_2024 <- c("No data" = "white",
                        setNames(blue_county, jenks_j_c2024$levels_all[-1]))

ggplot(j_county_map_2024) +
  geom_sf(aes(fill = TtlJlPpr_cat), color = "white", linewidth = 0.05) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_manual(values = fill_j_county_2024,
                    limits = jenks_j_c2024$levels_all,
                    name = "TtlJlPpr") +
  labs(title = "County-level Total Jail Population Rate (2024 Quarter 1)") +
  theme_minimal()

# County 2023
jenks_j_c2023 <- make_jenks_cat(j_county_map_2023$TtlJlPpr_Q1, n_classes_county)
j_county_map_2023$TtlJlPpr_cat <- jenks_j_c2023$cat_factor
fill_j_county_2023 <- c("No data" = "white",
                        setNames(blue_county, jenks_j_c2023$levels_all[-1]))

ggplot(j_county_map_2023) +
  geom_sf(aes(fill = TtlJlPpr_cat), color = "grey80", linewidth = 0.05) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_manual(values = fill_j_county_2023,
                    limits = jenks_j_c2023$levels_all,
                    name = "TtlJlPpr_Q1") +
  labs(title = "County-level Total Jail Population Rate (2023 Quarter 1)") +
  theme_minimal()