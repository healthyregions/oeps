# Provisioning OEPS Explorer

The data that drives the OEPS Explorer is generated through commands run in the backend app.

## Interactive Map

To regenerate the data that is displayed on the OEPS interactive web map, use the following:

```shell
flask build-explorer-map
```

!!! tip ""
    [view in cli reference &rarr;](../reference/cli/build-explorer-map.md)

CSV content will be restructured and written to a directory that the frontend OEPS Explorer can read. The `variables.json` file within the OEPS Explorer will be updated as well, pointing to the newly uploaded files.

Run with `--upload` to put the output in S3. You must do this to publish changes to the production site.

![breakdown of config content](../img/explorer-build-process.png)

## Docs/Download Pages

The [oeps.healthyregions.org/docs](https://oeps.healthyregions.org/docs) and [oeps.healthyregions.org/download](https://oeps.healthyregions.org/download) pages are driven by a generated set of JSON files that link themes, constructs, and variable-specific information. Generate this content with:

```shell
flask build-explorer-docs
```

!!! tip ""
    [view in cli reference &rarr;](../reference/cli/build-explorer-docs.md)
