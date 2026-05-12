# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- GitHub Action **Validate registry** that runs `flask validate-registry` on pull requests when `backend/oeps/registry/**`, `backend/oeps/data/**`, or the workflow file changes, plus manual **`workflow_dispatch`** ([#262](https://github.com/healthyregions/oeps/issues/262)).

- GitHub Action to create and upload Frictionless data packages when `backend/oeps/data/package_rules/**` changes ([#277](https://github.com/healthyregions/oeps/issues/277)).

- `--stable-name` option for `flask create-data-package` so package filenames are fixed (e.g. `oeps-DSuite2018.zip`) and download links do not need updates ([#277](https://github.com/healthyregions/oeps/issues/277)).

- Sortable "Key Variables and Definitions" table on metadata docs pages ([#303](https://github.com/healthyregions/oeps/issues/303)). Default sort by Variable ID; clickable column headers for Variable, Variable ID, Years Available, and Spatial Scale with ↑/↓ indicators.

- "Adding images" section in `metadata/README.md`: HTML vs Markdown, storing figures under `metadata/images/`, relative `images/...` links, and avoiding GitHub-only attachment URLs so images render reliably on the OEPS docs page ([#317](https://github.com/healthyregions/oeps/issues/317)).

- GitHub Action **Clean explorer S3 bucket** (`workflow_dispatch`) to remove stale map CSVs under `explorer/csv` using `explorer/config/sources.json`, with optional dry-run input ([#280](https://github.com/healthyregions/oeps/issues/280)).

- `flask clean-explorer-bucket`: `--non-interactive` (fail if `sources.json` is missing, for CI) and `--dry-run` (list keys to delete without deleting) ([#280](https://github.com/healthyregions/oeps/issues/280)).

- `*-geography-keys.csv` resources in Frictionless data packages so CSV Table Schema foreign keys reference tabular data that Frictionless can validate, alongside existing geography CSVs and shapefiles ([#311](https://github.com/healthyregions/oeps/issues/311)).

### Changed

- Create Data Packages GitHub Action: run Frictionless validation on each package (removed `--skip-validation`); DSuite2023 builds with foreign keys like other suites (removed `--skip-foreign-keys`) ([#311](https://github.com/healthyregions/oeps/issues/311)).

- Data package links on the download page use stable S3 URLs (`oeps-DSuite2018.zip`, `oeps-DSuite2023.zip`) on `herop-geodata` ([#277](https://github.com/healthyregions/oeps/issues/277), [#311](https://github.com/healthyregions/oeps/issues/311)).

- File size labels for data packages updated to "(100mb+)" on the download page ([#277](https://github.com/healthyregions/oeps/issues/277)).

- Smoking (`SmokeP`) and incarceration (prison/jail) variables and canonical table data refreshed for county-2019 and state/county 2022–2025 using `remove-variable` and `merge-csv` with updated source CSVs ([#261](https://github.com/healthyregions/oeps/issues/261)).

- Metadata docs for access measures (FQHCs, HCV/HIV testing, hospitals, mental health, MOUDs, pharmacies), jail/prison maps, and related README guidance: figures stored in `metadata/images/` with stable underscore filenames; markdown uses relative `images/...` links instead of `user-attachments` or branch `blob` URLs ([#317](https://github.com/healthyregions/oeps/issues/317)).

### Fixed

- Frictionless data package validation no longer fails when CSV foreign keys pointed at shapefile resources (`FileResource` / `row_stream`) ([#311](https://github.com/healthyregions/oeps/issues/311)).
