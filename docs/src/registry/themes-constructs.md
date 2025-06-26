# Themes & Constructs

!!! tip
    For a list of all themese & constructs currently in the registry, see [themes.csv](https://github.com/healthyregions/oeps/blob/main/docs/reference/themes.csv) on Github.

Themes are a very lightweight grouping of "constructs" that represent a variable (or a group of variables) at a conceptual level. Alongside each construct is a "proxy"; this is just a short description of all variables that fit within this construct. The structure of the `themes.json` file is very simple:

```json
{
  "<theme name>": {
    "<construct 1>": "<proxy for concept 1>",
    "<construct 2>": "<proxy for concept 2>",
  }
}
```

and with some real example values:

```json
{
  "Social": {
    "Age": "Age group estimates and percentages of population",
    "Race & Ethnicity": "Percentages of population defined by categories of race and ethnicity",
  }
}
```

Each variable is matched to one construct via its `construct` propert (see below).

Themes, construct, and proxies are only used in certain export formats, and are not a structurally central aspect of the registry.