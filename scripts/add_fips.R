### Author: Ashlynn Wimer
### Date: 6/16/2025
### About: As per issue #121 on the Github, we need to add FIPS columns to all the data CSVs! 
###        The easiest way to do this for current CSVs is a one-off script, such as this one.

library(dplyr)
library(stringr)
library(purrr)

add_fips <- function(file_name) {
  data <- read.csv(file_name)

  is_zcta <- str_detect(file_name, "zcta")
  if (is_zcta) {
    data <- data |>
      mutate(ZCTA5 = as.character(substr(HEROP_ID, 6, nchar(HEROP_ID)))) |>
      select(HEROP_ID, ZCTA5, everything())
  } else {
    data <- data |>
      mutate(FIPS = as.character(substr(HEROP_ID, 6, nchar(HEROP_ID)))) |>
      select(HEROP_ID, FIPS, everything())
  }
  invisible(write.csv(data, file_name, row.names = FALSE))
}

tables <- list.files("../backend/oeps/data/tables/", full.names = TRUE)
map(tables, add_fips)