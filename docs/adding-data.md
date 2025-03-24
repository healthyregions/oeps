# How to add data to OEPS

At the core of the OEPS data structure is the idea of a **variable**. A variable, like _Total Population_, must be configured in the registry before any data can be added to OEPS for that variable. Datasets themselves (the actual values for _Total Population_, for example) are defined as **data sources** and stored as CSVs in any downloadable location. This guide will first walk through how to define a new variable in the system, and then how to add a new data source for that variable.

For a detailed description of how the entire data registry is put together, see [registry.md](./registry.md).

## Adding a new variable

All variables are defined in a single file, `backend/oeps/registry/variables.json` so adding a new variable to the system only requires a new entry in that file. A basic variable entry looks like this:

```
  "TotPop": {
    "title": "Total Population",
    "name": "TotPop",
    "type": "integer",
    "example": "1632480",
    "description": "Total population",
    "constraints": "1980-2000 historic data was acquired from NHGIS and then interpolated to modern county boundaries through a population weighted interpolation using the tidycensus `interpolate_pw` function. For 1980, the underlying population weighting was county subdivisions, while for 1990 and 200 the underlying population weighting was tracts.",
    "construct": "Population",
    "source": "ACS 2018, 5-Year; Census 2010; IPUMS NHGIS",
    "source_long": "American Community Survey 2014-2018 5 Year Estimate; 2010 Decennial Census; Integrated Public Use Microdata Series National Historic Geographic Information System",
    "comments": "",
    "metadata_doc_url": "https://github.com/GeoDaCenter/opioid-policy-scan/blob/main/data_final/metadata/Age_2018.md",
    "table_sources": []
  }
```



