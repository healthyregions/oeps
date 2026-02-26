## Original CSV data has been cleaned in Excel before importing in R, removed un-related variables
## County Health Rankings files list the state summary first within each state block,followed by county-level rows
## We store data in specific order and use this structure to distinguish state and county data

# Install library
library(dplyr)

# Read pre-cleaned data (it has been stored in specific order)
dat <- read.csv("state_county_combined.csv", stringsAsFactors = FALSE, check.names = FALSE)

# Tag position within each state group (based on existing order)
dat_tagged <- dat %>%
  group_by(state) %>%
  mutate(.within_state_row = dplyr::row_number()) %>%
  ungroup()

#  Extract state-level (first row per state, repeated rows founded), excluding the national total
state_data <- dat_tagged %>%
  filter(state != "United States", .within_state_row == 1) %>%
  select(-.within_state_row)

# Extract county-level (remaining rows per state, repeated rows founded)), also excluding the national total
county_data <- dat_tagged %>%
  filter(state != "United States", .within_state_row > 1) %>%
  select(-.within_state_row)

# Save state and county data
write.csv(state_data,  "Smoking Population_state_level_2025.csv",  row.names = FALSE)
write.csv(county_data, "Smoking Population_county_level_2025.csv", row.names = FALSE)

## Check the output data and add HEROP_ID

## Read finalized data
state_data <- read.csv("Smoking Population_state_level_2025.csv", stringsAsFactors = FALSE, check.names = FALSE)
county_data <- read.csv("Smoking Population_county_level_2025.csv", stringsAsFactors = FALSE, check.names = FALSE)

# OEPS Geographic Boundaries: https://geodata.healthyregions.org/
library(sf)
state_boundary <- read_sf('/vsizip//vsicurl/https://herop-geodata.s3.us-east-2.amazonaws.com/oeps/state-2018-500k-shp.zip')
county_boundary <- read_sf('/vsizip//vsicurl/https://herop-geodata.s3.us-east-2.amazonaws.com/oeps/county-2018-500k-shp.zip')

# Add libraries
library(dplyr)
library(sf)
library(ggplot2)

# Ensure HEROP_ID is character on both sides
state_data  <- state_data  %>% mutate(HEROP_ID = as.character(HEROP_ID))
county_data <- county_data %>% mutate(HEROP_ID = as.character(HEROP_ID))

state_boundary  <- state_boundary  %>% mutate(HEROP_ID = as.character(HEROP_ID))
county_boundary <- county_boundary %>% mutate(HEROP_ID = as.character(HEROP_ID))

# Join smoking data to geometry
state_map_df <- state_boundary %>%
  left_join(state_data, by = "HEROP_ID")

county_map_df <- county_boundary %>%
  left_join(county_data, by = "HEROP_ID")

# Map state-level smoking (SmokeP)
ggplot(state_map_df) +
  geom_sf(aes(fill = SmokeP), color = "white", linewidth = 0.2) +
  coord_sf(
    xlim = c(-125, -66),
    ylim = c(24, 50),
    expand = FALSE
  ) +
  scale_fill_gradient(
    low = "lightblue",     # low smoking
    high = "darkblue",     # high smoking
    na.value = "white",    # no data only
    name = "Smoking (%)"
  ) +
  labs(title = "State-level Smoking Prevalence (2025)") +
  theme_minimal()

# Map county-level smoking (SmokeP)
ggplot(county_map_df) +
  geom_sf(aes(fill = SmokeP), color = NA) +
  coord_sf(
    xlim = c(-125, -66),
    ylim = c(24, 50),
    expand = FALSE
  ) +
  scale_fill_gradient(
    low = "lightblue",     # low smoking
    high = "darkblue",     # high smoking
    na.value = "white",    # no data only
    name = "Smoking (%)"
  ) +
  labs(title = "County-level Smoking Prevalence (2025)") +
  theme_minimal()

## Use natural break if needed
library(classInt)
library(RColorBrewer)
n_classes_state <- 5
n_classes_county <- 5

## State natural break map
jenks_state <- classInt::classIntervals(
  state_map_df$SmokeP,
  n = n_classes_state,
  style = "jenks",
  na.rm = TRUE
)

state_map_df <- state_map_df %>%
  mutate(
    SmokeP_jenks = cut(SmokeP, breaks = jenks_state$brks, include.lowest = TRUE),
    SmokeP_cat = ifelse(is.na(SmokeP), "No data", as.character(SmokeP_jenks))
  )

jenks_levels_state <- c(
  "No data",
  levels(state_map_df$SmokeP_jenks)
)

state_map_df$SmokeP_cat <- factor(
  state_map_df$SmokeP_cat,
  levels = jenks_levels_state
)

blue_colors <- brewer.pal(n_classes_state + 1, "Blues")[2:(n_classes_state + 1)]

fill_colors_state <- c(
  "No data" = "white",
  setNames(blue_colors, levels(state_map_df$SmokeP_jenks))
)

ggplot(state_map_df) +
  geom_sf(aes(fill = SmokeP_cat), color = "white", linewidth = 0.2) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_manual(
    values = fill_colors_state,
    limits = jenks_levels_state,
    name = "SmokeP"
  ) +
  labs(title = "State-level Smoking Prevalence (2025)") +
  theme_minimal()

## County Natural break map
jenks_county <- classInt::classIntervals(
  county_map_df$SmokeP,
  n = n_classes_county,
  style = "jenks",
  na.rm = TRUE
)

county_map_df <- county_map_df %>%
  mutate(
    SmokeP_jenks = cut(SmokeP, breaks = jenks_county$brks, include.lowest = TRUE),
    SmokeP_cat = ifelse(is.na(SmokeP), "No data", as.character(SmokeP_jenks))
  )

jenks_levels_county <- c(
  "No data",
  levels(county_map_df$SmokeP_jenks)
)

county_map_df$SmokeP_cat <- factor(
  county_map_df$SmokeP_cat,
  levels = jenks_levels_county
)

blue_colors <- brewer.pal(n_classes_county + 1, "Blues")[2:(n_classes_county + 1)]

fill_colors_county <- c(
  "No data" = "white",
  setNames(blue_colors, levels(county_map_df$SmokeP_jenks))
)

ggplot(county_map_df) +
  geom_sf(aes(fill = SmokeP_cat), color = NA) +
  coord_sf(xlim = c(-125, -66), ylim = c(24, 50), expand = FALSE) +
  scale_fill_manual(
    values = fill_colors_county,
    limits = jenks_levels_county,
    name = "SmokeP"
  ) +
  labs(title = "County-level Smoking Prevalence (2025)") +
  theme_minimal()