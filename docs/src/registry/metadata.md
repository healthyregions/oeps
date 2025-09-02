# Metadata

!!! tip
    For a list of all metadata documents currently in the registry (and links to the markdown files), see [metadata.csv](https://github.com/healthyregions/oeps/blob/main/docs/src/reference/registry/metadata.csv) on Github.

The registry contains JSON references to metadata documents, which are ultimately stored as Markdown files on Github. Each reference defines a theme, construct, and proxy to be attached to the document, as well as the URL to the file.

Within OEPS, themes, constructs, and proxies create a hierarchical conceptual framework through which each variable can be interpreted. Metadata documents are created one-per-proxy, a proxy being a grouping of variables that (typically) have been created or extracted from the same source.

An example metadata entry looks like this:

```json
{
  "id": "Access_MOUDs",
  "theme": "Environment",
  "construct": "Spatial Access to MOUDs",
  "proxy": "Spatial access metrics... (this is a description of the variables themselves)",
  "url": "https://github.com/healthyregions/oeps/blob/main/metadata/Access_MOUDs.md",
  "source": "SAMSHA 2019, 2021; Vivitrol 2020; OSRM 2020;",
  "source_long": "U.S. Substance Abuse and Mental Health Services Administration, Treatment Locator Tool, 2019; Vivitrol, 2020; Open Source Routing Machine, 2020"
}
```

Each [variable entry](variables.md) must reference a metadata entry, making a linkage to the document that describes its provenance. Typically, multiple variables are described in the same metadata document, so their `metadata` value will all be the same.
