# Load required libraries

library(sf)
library(tmap)
library(units)
library(dplyr)


# 1. Read tract level geojson

Boundary <- st_read("https://herop-geodata.s3.us-east-2.amazonaws.com/census/tract-2020-500k.geojson")

# Transform tracts to Illinois State Plane (Meters)
Boundary <- st_transform(Boundary, 5070)


# 2. Read Hospital Clinics from CSV
#    (CSV must have latitude & longitude)

Hospital_csv <- read.csv("C:/Users/adrit/Downloads/Hospitals (1).csv")

# Expected columns:
# Hospital_csv$longitude
# Hospital_csv$latitude
head(Hospital_csv)
# Convert CSV to sf point object (WGS84)
HospitalSf <- st_as_sf(
  Hospital_csv,
  coords = c("X", "Y"),
  crs = 4326,
  remove = FALSE
)

# Transform clinics to match ZIP CRS
HospitalSf <- st_transform(HospitalSf, 5070)

# ===============================
# 3. Quick data checks
# ===============================
st_crs(Boundary)
st_crs(HospitalSf)

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
  tm_shape(HospitalSf) +
  tm_dots(
    col = "red",
    size = 0.02,
    alpha = 0.8,
    title = "Hospital clinics"
  ) +
  tm_layout(
    main.title = "Hospital Clinics vs Census Tracts (US)",
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
  HospitalSf
)

nearestClinic <-HospitalSf[nearestClinic_idx, ]


# 7. Calculate distance (Hospers → miles)

minDist_m <- st_distance(
  BoundaryCentroids,
  nearestClinic,
  by_element = TRUE
)

# Convert to miles
minDist_mi <- set_units(minDist_m, "mi")


# 8. Attach distances back to ZIP polygons

minDistSf <- Boundary  %>%
  mutate(HospMinDis = as.numeric(minDist_mi))


# 9. Map results
tmap_mode("plot")

tm_shape(minDistSf) +
  tm_polygons(
    "HospMinDis",
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
    main.title = "Minimum Distance from Tract Centroid to Hospital Clinic",
    main.title.position = "center",
    legend.outside = TRUE,
    frame = FALSE
  )
# 10. Export results


# Save attribute table as CSV (geometry dropped)
write.csv(
  st_drop_geometry(minDistSf),
  "C:/Users/adrit/Downloads/HospitalMinimumDistance-2025.csv",
  row.names = FALSE
)

# Save full spatial layer as GeoJSON (keeps geometry)
st_write(
  minDistSf,
  "C:/Users/adrit/Downloads/HospitalMinimumDistance-2025.geojson",
  driver = "GeoJSON",
  delete_dsn = TRUE
)
