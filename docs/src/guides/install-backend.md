# Installing the OEPS Backend

The OEPS Backend is a suite of command line tools, built with the Flask framework. However:

- Using the backend does not require a connection to a proper database like SQLite or Postgres
- The backend does not run as a service, and there are no actual API routes using the typical Flask patterns]

Instead, the backend is better thought of as a suite of command line operations that modify static content. After an operation has been performed, there will typically be changes to registry or data files, and it is necessary to commit those changes and then create a pull request.

In the future, perhaps it will make sense to convert some of the operations to API routes, but for now **Flask is merely a wrapper for command line arguments**.

## Using Docker

The easiest way to run backend commands is to use Docker. Simply enter the backend directory and run:

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

## Local install

To make a local install without Docker, just install the Python requirements into a Python virtual environment.

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
