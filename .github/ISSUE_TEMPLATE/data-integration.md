---
name: Data Integration
about: Create a ticket to track the integration of a new dataset into OEPS
title: "[Data]"
labels: data
---


**Data integration summary**

_Remove this text and add the following to this section:_
- _The source URLs/database of the data that will be processed_
- _The years and geography level of the data you will be creating_

**Task completion checklist**

- [x] Create ticket for progress tracking (this ticket!)
- [ ] Create a new branch that starts with the number of this ticket, and includes the name of the data to be added
  - Example: `244_fqhc_data_update`
- [ ] Perform all processing on your source data and completed "Processing notes" section below
- [ ] Place any R or Python scripts you create during the process in the /scripts folder **(use your new branch)**
- [ ] Update the metadata document for your new data **(use your new branch)**
- [ ] Update the variables and metadata registry entries in the [CMS](https://app.pagescms.org/healthyregions/oeps) **(use your new branch)**
- [ ] Create a [new pull request](https://github.com/healthyregions/oeps/pulls) from your new branch into the `main` branch, and tag `@makosak` as a reviewer

**Processing notes**

As you complete the work, update this section with details and screenshots of your work. You can click **Edit** above to make changes to this ticket, and use `ctrl + v` to post screenshots directly into the ticket, or dragging & dropping them into this interface.

Specifically make sure to include:

- [ ] item 1
- [ ] item 2
