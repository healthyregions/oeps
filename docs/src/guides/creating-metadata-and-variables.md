# Creating Metadata and Variables

## Creating a new metadata entry

To add a new metadata entry, you should begin the process in GitHub by creating a new branch and added a new markdown file to in this directory: https://github.com/healthyregions/oeps/tree/main/metadata. Create your file based on [metadata-template](https://github.com/healthyregions/oeps/tree/main/metadata/metadata-template.md), and also review these [Metadata Writing Guidelines](https://github.com/healthyregions/oeps/tree/main/metadata/README.md).

In `registry/metadata` there are individual JSON files for that represent each metadata markdown file. Instead of editing these files directly, we can edit them through PagesCMS (see ).

!!! note
    In the future, we could further integrate the Markdown files with PagesCMS, such that instead of PagesCMS writing/editing JSON files that are loosely linked to the actual Markdown files, we could reconfigure the app such that PagesCMS writes the Markdown files themselves, and these are read by the registry (using front matter) instead of the surrogate JSON files.

With your markdown file complete, you need to create an entry for it in PagesCMS. See [getting started with PagesCMS](adding-data-overview.md#getting-started-with-pagescms), and be sure to use the branch you have already created (no need to make a new one).

Once the new metadata entry has been created, you can also attach new variables to it if needed.

## Editing an existing Metadata Document

- Switch to your working branch
- Find the appropriate metadata document and make updates. At the very least, you'll need to update the new year or years that you are adding.


## Creating a new variable entry

In `registry/variables` there are individual files for each variable with data in OEPS. Instead of editing these files directly, we can edit them through PagesCMS.

See [getting started with PagesCMS](adding-data-overview.md#getting-started-with-pagescms) to continue.

Some data entry notes:

- `name` must follow these rules:
    - Follow abbreviation patterns we already use
    - Follow [PascalCase](https://pascal-case.com/)
        - For example, use `TotPop`, not `tot_pop` or `totPop` or `tot-pop`
- `type` must be one of:
    - `number` for any decimal number values
    - `integer` for any integer values
    - `string` for text values, for example a coded entry
    - `boolean` for true/false or yes/no values
    - `date` for date values
    - see [Frictionless field data types](https://specs.frictionlessdata.io/table-schema/#types-and-formats) for more info
- `table_sources` leave this blank, it should not be edited in PagesCMS.

!!! tip
    See [variables](../registry/data-model.md#variables) for a full explanation of variables.
