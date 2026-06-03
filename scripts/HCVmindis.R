# Author: Mahjabin Kabir Adrita
# Date: 2026-08-02
# Data Source: Substance Abuse and Mental Health Services Administration (SAMHSA)

# Load required libraries

library(sf)
library(tmap)
library(units)
library(dplyr)


# 1. Read tract level geojson

Boundary <- st_read("https://herop-geodata.s3.us-east-2.amazonaws.com/census/tract-2020-500k.geojson")

# Transform tracts to Illinois State Plane (Meters)
Boundary <- st_transform(Boundary, 5070)


# 2. Read Hcv Clinics from CSV
#    (CSV must have latitude & longitude)

Hcv_csv <- read.csv("C:/Users/adrit/Downloads/HCV.csv")

# Expected columns:
# Hcv_csv$longitude
# Hcv_csv$latitude
head(Hcv_csv)
# Convert CSV to sf point object (WGS84)
HcvSf <- st_as_sf(
  Hcv_csv,
  coords = c("longitude", "latitude"),
  crs = 4326,
  remove = FALSE
)

# Transform clinics to match ZIP CRS
HcvSf <- st_transform(HcvSf, 5070)

# ===============================
# 3. Quick data checks
# ===============================
st_crs(Boundary)
st_crs(HcvSf)

# ===============================
# 4. Visualize ZIPs and Clinics
# ===============================
library(tmap)

tmap_mode("plot")

tm_shape(Boundary) +
  tm_polygons(
    col = "lightblue",
    border.col = "blue",
    lwd = 0.05,
    alpha = 0.35,
    title = "Census tracts"
  ) +
  tm_shape(HcvSf) +
  tm_dots(
    col = "red",
    size = 0.02,
    alpha = 0.8,
    title = "Hcv clinics"
  ) +
  tm_layout(
    main.title = "Hcv Clinics vs Census Tracts (US)",
    main.title.position = "center",
    legend.outside = TRUE,
    frame = FALSE
  )

# ===============================
# 5. Create ZIP centroids

BoundaryCentroids <- st_centroid(Boundary)

# Optional geometry check
plot(st_geometry(Boundary), col = "grey90", border = "grey80", lwd = 0.1)
plot(st_geometry(BoundaryCentroids), add = TRUE, pch = 16, cex = 0.15, col = grDevices::adjustcolor("red", alpha.f = 0.4))


# 6. Find nearest clinic to each ZIP centroid

nearestClinic_idx <- st_nearest_feature(
  BoundaryCentroids,
  HcvSf
)

nearestClinic <-HcvSf[nearestClinic_idx, ]


# 7. Calculate distance (Meters → miles)

minDist_m <- st_distance(
  BoundaryCentroids,
  nearestClinic,
  by_element = TRUE
)

# Convert to miles
minDist_mi <- set_units(minDist_m, "mi")


# 8. Attach distances back to ZIP polygons

minDistSf <- Boundary  %>%
  mutate(HcvMinDis = as.numeric(minDist_mi))


# 9. Map results
tmap_mode("plot")

tm_shape(minDistSf) +
  tm_polygons(
    "HcvMinDis",
    style = "quantile",
    n = 7,
    palette = "viridis",
    lwd = 0,             
    border.alpha = 0,
    alpha = 0.95,
    colorNA = "grey90",
    title = "Minimum Distance (miles)"
  ) +
  tm_layout(
    main.title = "Minimum Distance from Tract Centroid to Hcv Clinic",
    main.title.position = "center",
    legend.outside = TRUE,
    frame = FALSE
  )
# 10. Export results


# Save attribute table as CSV (geometry dropped)
write.csv(
  st_drop_geometry(minDistSf),
  "C:/Users/adrit/Downloads/HCVMinimumDistance-2025.csv",
  row.names = FALSE
)

# Save full spatial layer as GeoJSON (keeps geometry)
st_write(
  minDistSf,
  "C:/Users/adrit/Downloads/HcvMinimumDistance-2025.geojson",
  driver = "GeoJSON",
  delete_dsn = TRUE
)
