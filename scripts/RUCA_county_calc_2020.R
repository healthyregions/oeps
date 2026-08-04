# ============================================================
# Calculate County-Level % Rural, Suburban, and Urban Tracts
# from tract-level RUCA data
# ============================================================

library(readxl)
library(dplyr)
library(stringr)
library(writexl)

# ------------------------------------------------------------
# 1. Read Excel file
# ------------------------------------------------------------

ruca_raw <- read_excel(
  "your_ruca_file.xls",
  col_types = "text"
)

# ------------------------------------------------------------
# 2. Clean and prepare data
# ------------------------------------------------------------

ruca_clean <- ruca_raw %>%
  mutate(
    # Keep tract FIPS as 11-digit text
    FIPS = str_pad(FIPS, width = 11, side = "left", pad = "0"),
    
    # Extract county FIPS from tract FIPS
    CountyFIPS = str_sub(FIPS, 1, 5),
    
    # Create county-level HEROP ID
    HeropID = paste0("050US", CountyFIPS),
    
    # Clean rurality labels
    Rurality = str_to_title(str_trim(Rurality))
  )

# ------------------------------------------------------------
# 3. Calculate county-level RUCA percentages
# ------------------------------------------------------------

ruca_county_measures <- ruca_clean %>%
  group_by(HeropID, CountyFIPS) %>%
  summarise(
    TotalTracts = n(),
    
    RuralTracts = sum(Rurality == "Rural", na.rm = TRUE),
    SuburbanTracts = sum(Rurality == "Suburban", na.rm = TRUE),
    UrbanTracts = sum(Rurality == "Urban", na.rm = TRUE),
    
    RcaRuralP = (RuralTracts / TotalTracts) * 100,
    RcaSuburbP = (SuburbanTracts / TotalTracts) * 100,
    RcaUrbanP = (UrbanTracts / TotalTracts) * 100,
    
    .groups = "drop"
  )

# ------------------------------------------------------------
# 4. Save county-level output
# ------------------------------------------------------------

write_xlsx(
  ruca_county_measures,
  "county_level_ruca_measures.xlsx"
)