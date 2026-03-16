# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- GitHub Action to create and upload Frictionless data packages when `backend/oeps/data/package_rules/**` changes ([#277](https://github.com/healthyregions/oeps/issues/277)).

- `--stable-name` option for `flask create-data-package` so package filenames are fixed (e.g. `oeps-DSuite2018.zip`) and download links do not need updates ([#277](https://github.com/healthyregions/oeps/issues/277)).

- Sortable "Key Variables and Definitions" table on metadata docs pages ([#303](https://github.com/healthyregions/oeps/issues/303)). Default sort by Variable ID; clickable column headers for Variable, Variable ID, Years Available, and Spatial Scale with ↑/↓ indicators.

- "Adding images" section in `metadata/README.md`: HTML vs Markdown comparison, Option 1 (GitHub paste/drop), Option 2 (`metadata/images/`), and examples so images render correctly on the OEPS docs page ([#317](https://github.com/healthyregions/oeps/issues/317)).

### Changed

- Data package links on the download page use stable S3 URLs (`oeps-DSuite2018.zip`, `oeps-DSuite2023_no_foreign_keys.zip`) on `herop-geodata` ([#277](https://github.com/healthyregions/oeps/issues/277)).

- File size labels for data packages updated to "(100mb+)" on the download page ([#277](https://github.com/healthyregions/oeps/issues/277)).

### Fixed

- (none this release)
