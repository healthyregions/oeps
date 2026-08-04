# Metadata Guidelines

This guideline explains how to create, edit, and maintain metadata files in the OEPS repository. A metadata file should help users understand what a dataset represents, where the data came from, how the variables were created, which years and geographic scales are included, and what limitations should be considered before using the data.

The metadata should be detailed enough that someone who did not create the dataset can still understand the source, processing steps, geographic files, typology files, variable definitions, assumptions, and known issues. Metadata files also document authorship and editing history, so every person who creates or substantially edits a metadata file must be added to the author list.

!!! note
    This page focuses on **metadata documentation** after a dataset has been accepted for inclusion. To prepare and format CSV datasets, see [Preparing CSV Data](preparing-csv-data.md). To add registry entries via PagesCMS, see [Creating Metadata and Variables](creating-metadata-and-variables.md).

!!! tip "Source draft"
    Adapted from the OEPS Metadata Guideline Document drafted by Mahjabin Kabir Adrita (Google Doc draft for [#408](https://github.com/healthyregions/oeps/issues/408); original request [#224](https://github.com/healthyregions/oeps/issues/224)).

## Quality expectations

Before opening a pull request, confirm:

- Metadata is complete and free of typos
- Metadata matches the data variables and years in the final dataset being uploaded
- Comments and notes are sufficient for a reader who did not create the data
- Sources, processing steps, geography vintages, and known limitations are documented

## GitHub workflow

1. Complete all metadata work on a **new branch**. Do not edit `main` directly. Use a clear branch name related to the task, for example `metadata-hcv-testing-update`, `metadata-economic-variables-2025`, or `metadata-ruca-measures`.
2. Work in the [`metadata/`](https://github.com/healthyregions/oeps/tree/main/metadata) folder. Create a new markdown file or update an existing one. New files should follow the structure in this guideline; edits should preserve the overall format while updating sections that need clarification, correction, or expansion.
3. Update authorship whenever you create or edit a file:
    - Add your name to the **Authors** list (most recent author first)
    - Update **Date Last Modified**
    - Set **Last Modified By** to your name only
    - Updating only the last-modified fields is not enough -- contributors who create, revise, or substantially edit the file must appear in the author list
4. Save files as Markdown (`.md`). Use short, descriptive names with underscores instead of spaces. Prefer `Topic_Resource.md` patterns such as `Access_HCVTesting.md`, `Access_Buprenorphine.md`, or `Economic_Variables.md`. Avoid special characters, long phrases, and unclear abbreviations. Keep an existing file name unless it is inaccurate.
5. After the markdown file is ready, create or update the matching registry metadata entry in [PagesCMS](adding-data-overview.md#getting-started-with-pagescms). See also [Creating Metadata and Variables](creating-metadata-and-variables.md).

## Required metadata sections

Include the following sections when applicable:

1. Header information
2. Data Source(s) Description
3. Description of Data Source Tables
4. Description of Data Processing
5. Geographic Boundaries, Typology Files, or Shapefiles
6. Years and Timeline
7. Data Limitations
8. Comments/Notes
9. Images or Figures
10. References or Links

### Required header information

Every metadata file should begin with a standard header:

```markdown
**Meta Data Name**: Name of the metadata topic or data resource  
**Date Added**: Month Day, Year  
**Authors**: Full names of all contributors (most recent author first)  
**Date Last Modified**: Month Day, Year of the most recent update  
**Last Modified By**: Full name of the most recent editor  
```

- **Meta Data Name** should clearly describe the topic or resource (for example, "Access to HCV Testing" or "Rural-Urban Commuting Area Measures").
- **Date Added** is when the metadata file was first created.
- **Date Last Modified** is the most recent edit date.
- **Authors** lists everyone who created, revised, or substantially edited the file.
- **Last Modified By** is only the most recent editor.

### Data Source(s) Description

Explain where the original data came from. Include:

- The main resource dataset and the organization or agency that produced it
- The website or repository where it was obtained
- The year or date of download if known
- Geographic coverage and scale

For provider access measures, identify the provider database, source organization, locator tool or download page, and the types of facilities or services included.

If the metadata uses travel time or network-based accessibility measures, also document:

- Street network source (for example, OpenStreetMap)
- How travel times were generated
- Travel modes (driving, biking, walking)
- Thresholds (for example, 30 or 60 minutes)
- Geographic scale (tract, ZCTA, county, state)
- Person, team, software, or method that generated the matrices, if known

Also describe geographic boundary files: source, boundary year, and geographic levels (for example, Census Bureau TIGER/Line). If archived copies exist in the HEROP GeoData Web Archive or another repository, include that information.

### Typology files, shapefiles, and geographic resources

Document any typology file, shapefile, or geographic classification clearly. Examples include RUCA typologies, urban-suburban-rural classifications, county/tract/ZCTA/state boundaries, census region files, HUD tract-to-ZIP crosswalks, and other spatial crosswalks.

For each file, include:

- File name, source, year, and geographic scale
- Link to the source or repository location
- Variables used from the file
- Join field used to connect it to the main dataset (`FIPS`, `GEOID`, ZIP, county, or state code)
- Known boundary issues (missing geographies, inconsistent FIPS, county definition changes, vintage mismatches)

Recommended paragraph form:

> The typology file used for this measure was [name of file]. It was sourced from [source] and represents [year]. The file was used to classify [geographic unit] into [classification categories]. The typology was joined to the main dataset using [join field]. Variables used from this file included [variable names and descriptions]. Known issues included [boundary mismatch, missing geographies, vintage differences, or FIPS/GEOID inconsistencies].

### Description of Data Source Tables

Describe the original tables, fields, or columns used to create OEPS variables. This is especially important for ACS tables, Census tables, provider lists, facility files, survey datasets, or administrative datasets.

For each table:

- Identify it by name or ID and briefly explain what it measures
- Describe variables used and define key fields
- Link to official documentation when available
- State whether values are estimates, percentages, counts, margins of error, or another measurement type

Example: if ACS table `B19301` was used for per capita income, identify the table and explain the selected variable. If ACS table `S1701` was used for poverty status, state whether the variable is a count, percent estimate, or another measure.

### Description of Data Processing

Explain how raw data were cleaned, transformed, joined, aggregated, or calculated. The section should be detailed enough that a reader understands the major steps without needing the full script.

Cover, as applicable:

- Cleaning, filtering, geocoding, coordinate systems
- Centroids, distances, travel times, thresholds
- Counts, percents, aggregation, crosswalks, weighting
- Missing-value treatment
- What changed from a previous version, and why
- Links to scripts, notebooks, or code folders

When processing differs by scale or method, use subheadings such as "Tract and ZIP Code," "County and State," "Minimum Distance," "Travel Time and Count Within Threshold," "Crosswalk Process," "Aggregation Method," or "Variable Creation."

### Years and Timeline

Clearly state which years are covered. Document:

- Data years included
- Source years and boundary years
- Travel matrix years and script update years
- Older versions that were replaced
- Planned future updates

Explain the timeline in paragraph form when sources, boundaries, and processing years differ. If a notebook or comparison is not yet available, state the expected release timeline so users know whether the metadata is final, provisional, or expected to change.

### Data Limitations

Limitations are constraints, uncertainties, or weaknesses that affect interpretation -- not general notes. Include a limitation when an issue may affect accuracy, completeness, comparability, geographic or temporal coverage, measurement validity, boundary consistency, access calculations, missing data, scale mismatch, or methodological assumptions.

Examples:

- Missing data for some U.S. territories
- ZIP data available only for more recent years
- Euclidean distance as an approximation rather than real travel time
- Travel times capped at a threshold
- Tract centroids not representing where people live
- Large Alaska or frontier tracts making centroid-based calculations less reliable
- County boundaries or FIPS codes changing over time
- Connecticut county-equivalent changes affecting county summaries
- Provider databases with outdated or inactive listings
- Measures not comparable across years because boundaries, methods, or definitions changed

Each limitation should explain **why it matters**. For example, do not only say travel times use tract centroids -- explain that centroid-to-centroid calculations may not represent all residents, especially in large or rural tracts. If values beyond a threshold appear blank, explain that blanks may mean very poor access rather than truly missing data.

### Comments/Notes

Use this section for helpful information that is **not** a limitation: units, coding decisions, interpretation details, practical reminders, links to related files, or minor methodological details.

| Limitations | Comments/Notes |
|---|---|
| Problems, uncertainties, or constraints that affect interpretation | Useful details, coding rules, or clarifications |
| "Travel times are calculated from tract centroid to tract centroid, which may not represent actual travel time for all residents" | "All travel time values are reported in minutes" |

### Images or figures

Add images when they help explain a method, workflow, map, comparison, or result. Surrounding text should explain what the image shows and why it is included.

Store files under [`metadata/images/`](https://github.com/healthyregions/oeps/tree/main/metadata/images) with short, descriptive names, for example:

- `Travel_Time_to_HCV_testing_facility_by_Census_Tract.png`
- `RUCA_typology_county_summary_map.png`
- `ACS_poverty_variable_workflow.png`

Use Markdown image syntax (not HTML `<img>` tags):

```markdown
![Short description of what the figure shows](images/file_name.png)
```

For explorer rendering rules and path details, see the [metadata README image guidance](https://github.com/healthyregions/oeps/blob/main/metadata/README.md#adding-images).

### Links and references

Use descriptive Markdown links for data sources, official documentation, scripts, notebooks, archived shapefiles, method papers, software docs, or crosswalk documentation:

```markdown
[American Community Survey](https://data.census.gov)
```

Prefer descriptive link text over long raw URLs. Link ACS subject definitions, census documentation, and relevant OEPS GitHub folders or files when the metadata relies on them.

## Markdown formatting tips

Metadata files are Markdown (`.md`) so they display clearly in GitHub preview and on the OEPS docs pages.

- **Bold** important labels, variable names, table names, or field names with `**text**`. Do not bold entire paragraphs.
- Use `###` for major metadata sections and `####` for subsections. Keep heading levels consistent.
- Use `- ` for bullet lists of variables, limitations, comments, or source fields. Prefer paragraphs for long explanations.
- Header fields often need two trailing spaces before Enter so each field appears on its own line.
- Use backticks for file names, branch names, variable names, and short technical terms (for example `` `Access_HCVTesting.md` ``, `` `GEOID` ``).
- Always check GitHub preview for headings, spacing, links, images, and readability before submitting.

## Final review checklist

- [ ] Someone who did not create the dataset can understand how variables were produced and how they should be interpreted
- [ ] Missing or planned-future information is stated transparently in the appropriate section
- [ ] Header authorship fields are updated (authors list, last modified date, last modified by)
- [ ] Variables and years in the metadata match the uploaded dataset
- [ ] Limitations explain *why* each issue matters
- [ ] Images use Markdown syntax and relative `images/...` paths
- [ ] Links work and use descriptive text
- [ ] GitHub preview shows correct headings, spacing, links, images, and overall readability

## Recommended metadata file template

Use this template when creating a new metadata file (also see [`metadata/metadata-template.md`](https://github.com/healthyregions/oeps/blob/main/metadata/metadata-template.md)):

```markdown
**Meta Data Name**: [Name of Metadata File]  
**Date Added**: [Month Day, Year]  
**Authors**: [Name of original author; add names of all contributors who create or edit this file]  
**Date Last Modified**: [Month Day, Year]  
**Last Modified By**: [Name of most recent editor]  


### Data Source(s) Description:
#### Resources
Describe the main data resource, source organization, year, link, and geographic coverage.
#### Street Network Topology and Travel Time Matrices
Include this subsection if travel time, road network, walking, biking, or driving measures are used.
#### Geographic Boundaries
Describe shapefiles, boundary years, geographic units, and archived copies.
#### Typology or Classification Files
Describe typology files, classification schemes, and how they were joined to the main dataset.

### Description of Data Source Tables:
Describe source tables, variables, field names, and official definitions.

### Description of Data Processing:
#### Cleaning and Preparation
Describe data cleaning, formatting, filtering, and preparation steps.
#### Geographic Processing
Describe joins, projections, centroids, shapefile processing, crosswalks, or boundary harmonization.
#### Variable Creation
Describe how each OEPS variable was created.
#### Aggregation
Describe tract-to-county, tract-to-state, tract-to-ZIP, or other aggregation methods.
#### Scripts and Notebooks
Link to relevant code, notebooks, or folders.

### Years and Timeline:
List included data years, source years, boundary years, processing years, and planned future updates.

### Data Limitations:
- Add limitations that affect interpretation, accuracy, completeness, comparability, or geographic coverage.

### Comments/Notes:
- Add units, coding conventions, null value definitions, practical reminders, or interpretation notes.
```

## Related guides

- [Overview: adding data to OEPS](adding-data-overview.md)
- [Preparing CSV Data](preparing-csv-data.md)
- [Creating Metadata and Variables](creating-metadata-and-variables.md)
- [Metadata writing tips and image rules (repo README)](https://github.com/healthyregions/oeps/blob/main/metadata/README.md)
