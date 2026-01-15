---
name: Data Integration
about: Create a ticket to track the integration of a new dataset into OEPS
title: "[Data]"
labels: data
---

**Summary**

- What data will be added?
  - Answer:
- What years and geographic units will be added?
  - Answer:
- Is this a new variable, or one that already exists in the registry? If existing, what is the variable's id?
  - Check [here](https://github.com/healthyregions/oeps/blob/main/docs/src/reference/registry/variables.csv) to see all existing variables.
  - Answer:

**Task completion checklist**

<!-- Do not alter this section during ticket creation: you can check the boxes off in the future. -->

- [x] Create ticket for progress tracking, add the dataset name to the ticket title (this ticket!)
- [ ] Create a new branch that starts with the number of this ticket, and includes the name of the data to be added
  - Example: `244_fqhc_data_update`
- [ ] Perform all processing on your source data and added content to all fo the sections below (Da
- [ ] Place any R or Python scripts you create during the process in the /scripts folder **(use your new branch)**
- [ ] Update the metadata document for your new data **(use your new branch)**
  - Or, if this new data needs its own metadata document, created one using the [metadata template](https://github.com/healthyregions/oeps/blob/main/metadata/metadata-template.md) **(use your new branch)**
- [ ] Update the variables and metadata registry entries in the [CMS](https://app.pagescms.org/healthyregions/oeps) **(use your new branch)**
- [ ] Create a [new pull request](https://github.com/healthyregions/oeps/pulls) from your new branch into the `main` branch, and tag `@makosak` as a reviewer

<!-- FOR THE FOLLOWING SECTIONS:
  No need to alter these sections during ticket creation, use the Edit button above to change them later when you are ready.
  To add images you can drag & drop or use `ctrl + v` to post screenshots directly into the ticket.
  -->

**Data Sources**

_Remove this text and add the following to this section throughout the course of your work:_
- _The source URLs/database of the data that will be processed_
- _The years and geography level of the data you will be creating_

**Processing Notes**

_Remove this text and add 1-3 images of to this section around these topics:_
- _Key variables added_
- _Recommended measures to use_
- _Potential issues_

**Data Limitations**

_Remove this text and add the following to this section throughout the course of your work:_
-  _Specific comments on missing data in the source content_
-  _Any other notes on data issues_
- _Potential issues_
