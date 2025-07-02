# Creating Data Packages

Data packages can be generated from data in OEPS based on the [Frictionless Data spec](https://https://specs.frictionlessdata.io) (these specs are actually already implemented within the registry, as described [here](../registry/index.md)).

To generate a data package, run the following:

```
flask create-data-package
```

!!! tip ""
    [view in cli reference &rarr;](../reference/cli/create-data-package.md)

Run on its own, this command will end in a `row_stream` error. This is because a validation check is attempted that doesn't support foreign keys to shapefiles, which is how we have the package configured. You can avoid this by using either the `--skip-foreign-keys` or `--skip-validation` flags as described in the CLI reference for this command.

