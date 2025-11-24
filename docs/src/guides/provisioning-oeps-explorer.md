# Provisioning OEPS Explorer

The data that drives the OEPS Explorer is generated through commands run in the backend app.

```shell
flask build-explorer
```

This will build static assets to power the interactive map, and the docs and data download pages. This content is pulled from the backend registry and the 


!!! tip ""
    [view in cli reference &rarr;](../reference/cli/command-line-reference.md#build-explorer)

## Interactive Map

To regenerate the data that is displayed on the OEPS interactive web map, use the following:

```shell
flask build-explorer --map-only
```

CSV content will be restructured and written to a directory that the frontend OEPS Explorer can read. The `variables.json` file within the OEPS Explorer will be updated as well, pointing to the newly uploaded files.

Run with `--upload-map-data` to put the output in S3. **You must do this to publish changes to the production site.**

![breakdown of config content](../img/explorer-build-process.png)

## Docs/Download Pages

The [oeps.healthyregions.org/docs](https://oeps.healthyregions.org/docs) and [oeps.healthyregions.org/download](https://oeps.healthyregions.org/download) pages are driven by a generated set of JSON files that link themes, constructs, and variable-specific information. Generate this content with:

```shell
flask build-explorer --docs-only
```
