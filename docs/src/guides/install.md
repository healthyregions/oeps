# Installing the Components

The OEPS Explorer, OEPS Backend (which contains the registry), and this set of documentation each live in different directories of the same repository: [github.com/healthyregions/oeps](https://github.com/healthyregions/oeps). Each component operates independently, so there is no need to install them all at once.


To begin, clone the repo locally,

```shell
git clone https://github.com/healthyregions/oeps
```

then you can install any of the following components:

- [OEPS Explorer](#oeps-explorer)
- [OEPS Backend](#oeps-backend)
- [OEPS Documentation](#oeps-documentation)

## OEPS Explorer

To get started locally with the explorer:

```

cd oeps/explorer
yarn install
cp .env.example .env
```

Some environment variable values will already be set in `.env`, but you'll need to add a Mapbox token. Then run

```
yarn dev
```

and open `http://localhost:3000`

### More about Mapbox dependencies

Two Mapbox Tilesets must be configured externally and linked within this app, one for Zip Code Tabulation Areas (ZCTAs) and one for Census Tracts. These geometries are joined with CSV tables to drive map visualizations.

Additionally, a basemap style must be provided, as well as a Mapbox access token. All of these elements are (currently) provided through environment variables, so make sure your `.env` file has the following:

```
NEXT_PUBLIC_MAPBOX_TOKEN=<your token>
NEXT_PUBLIC_MAPBOX_STYLE="mapbox://styles/<account id>/<style id>"
```

## OEPS Backend

The OEPS Backend is a suite of command line tools, built within the Flask framework. _Using the backend does not require a long running process or external database._ It simply automates certain operations that are performed on files within the repository. After an operation has been performed, it is typically necessary to commit the changes and then create a pull request. In the future, perhaps it will make sense to convert some of the operations to API routes, but for now Flask is merely a wrapper.

### Install Python dependencies

#### Using Docker

The easiest way to run backend commands is to use Docker--no need to create a Python virtual environment. Simply enter the backend directory and run:

```
docker compose run -it oeps [CLI COMMAND]
```

For example, to print help for all of the commands, run

```
docker compose run -it oeps flask --help
```

and you should get a printout of about 10 commands.

If you are making changes to the backend code, then include the `--build` flag to rebuild the container during the command:

```
docker compose run -it oeps [CLI COMMAND]
```

Because the build process takes a little while, you may want to create a local install for more rapid development.

#### Local install

1. Enter the backend directory

        cd oeps/backend

2. Create and activate a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) with [venv](https://docs.python.org/3/library/venv.html), [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), or your other tool of choice.

    For example, using the `venv` module that is included in Python 3, the commands will be:

        python3 -m venv env
        source ./env/bin/activate

    This will create a new directory `env/`, and when properly activated your command prompt will have a `(env)` prefix.

3. Install this package and its dependencies

        pip install -e .

4. Create a `.env` file from the provided template (no need to update any values right now)

        cp .env.example .env

Success! To test your install, run:

```shell
flask --help
```

You should see a printout that lists about 10 commands. You can now head to [Getting Started with the CLI](./getting-started-with-cli.md) to learn more about using these commands.

!!! warning
    If you only see three commands (`routes`, `run`, and `shell`), then you either need to activate your virtual environment or make sure you have a `.env` file with `FLASK_APP=oeps` in it. (These three are default Flask commands.)


### Dev dependencies

If you are contributing code or otherwise developing on this code base, use the following commands to install dev dependencies

```shell
pip install -e .[dev]
pip install md-click@git+https://github.com/kid-116/md-click@support-arguments
```

!!! warning
    The `md-click` library is used to generate documentation of the CLI commands, and the particular branch is needed to handle Arguments on the commands that are being documented. Hopefully, this PR will be merged at some point and this install process could be updated: https://github.com/RiveryIO/md-click/pull/12.<br/><br/>There is a dependency resolution bug (or something) when putting that github reference directly in the `pyproject.toml` file, so it needs to be run separately after everything else is installed.

### Docs dependencies

The [documentation site](#oeps-documentation) (which you are reading right now!) is built with dependencies that are best installed directly into the backend virtual environment, so may as well install them now:

```shell
pip install -e .[docs]
```

## OEPS Documentation

It is easiest to install the documentation dependencies directly into the backend's Python virtual environment, as [described above](#docs-dependencies). Once that is completed, enter the docs directory and run mkdocs commands from there.

To view the docs locally:

```shell
cd oeps/docs
mkdocs serve
```

Visit http://localhost:8000 for a live preview of the docs content, and make changes to Markdown files in `/docs/src`.

!!! tip
    All files inside of `/docs/src/reference` are autogenerated by CLI commands, so those files should never be edited directly.

To build and publish the docs:

```shell
mkdocs build
```

Updated content is now in `/docs/output`. Commit these changes and push to Github to rebuild the public site.
