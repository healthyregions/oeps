# Overview

Getting new data into the OEPS data ecosystem requires a few steps.

- Download data from original source, and process as needed
- Prepare a CSV with the new data
- Update metadata document
    - For new variables, you will need to create a [new metadata document](creating-metadata-and-variables.md), via PagesCMS
- Add new variables to the registry via PagesCMS

## Getting Started with PagesCMS

PagesCMS is a web interface you can use to add new metadata or variable entries to the registry. **There is technically no need to use PagesCMS, you could edit the JSON files themselves directly, but it does make the process a bit easier.**

1. Go to [app.pagescms.org/healthyregions/oeps/main](https://app.pagescms.org/healthyregions/oeps/main)
2. Sign in with GitHub if needed
3. Once logged in, you'll see `oeps` and `main` in the left-hand menu
    - Click this button and go to > "Manage branches"
4. Create a new branch with a descriptive name, `add_my_new_variable`
    - You'll now see `oeps` and `add_my_new_variable` in the left-hand menu
5. Perform the edits you need to do
    - All work will be committed directly to your new branch.
6. When you are ready, [create a new pull request into main from your branch](https://github.com/healthyregions/oeps/pulls).