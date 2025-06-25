# Contributing to this Repo

> This page describes how to make code contributions to this repo. If you are looking to add new data to the registry, see [Adding Data to OEPS](./docs/adding-data-to-oeps.md).

For contributions we use a standard branching pattern--make a new branch from `main`, add commits to it, and then create a pull request to get those changes merged back into `main`.

In the command line, this would look like the following steps. (VSCode and other editors have git integrations as well, but the steps are generally the same):

1. Make sure you are on the main branch locally

        git branch

2. Create a new branch from `main`

        git checkout -b your_new_branch_name

    You will now be on a new branch, as `git branch` will show you.

3. Change code, add commits

        git add path/to/your/new_file
        git commit -m "short description of the change you made"

    If you are addressing an open ticket with your commit, say ticket number 10, you should add `#10` to your commit message, like

        git commit -m "update file list for initialization #10"

4. Push your branch to the GitHub repo

        git push --set-upstream origin your_new_branch_name

5. Create a [Pull Request](https://github.com/healthyregions/oeps/pulls) in GitHub, including a description of the changes your branch contains.
