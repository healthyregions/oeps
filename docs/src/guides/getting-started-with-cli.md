# Getting Started with the CLI

The OEPS Backend provides a suite of management commands, or a "command line interface" (CLI) that allows you to interact with data in the registry.

## Prerequisites

You must [install the OEPS Backend](./install-backend.md) before you can begin using the CLI.

To use CLI commands, make sure you have entered the backend directory and activated the Python virtual environment.

```bash
cd backend

## on mac/linux
source ./env/bin/activate

## on windows
.\env\Scripts\activate
```

## Running commands

All commands must be invoked with the prefix `flask`. To get a list of all available commands, run

```shell
flask --help
```

You should see a list of about 10 commands. To run one of these commands, use

```shell
flask [command]
```

!!! warning
    If you only see three commands (`routes`, `run`, and `shell`), then you either need to activate your virtual environment or make sure you have a `.env` file with `FLASK_APP=oeps` in it. (These three are default Flask commands.)

For example, to validate the registry, just run

```shell
flask validate-registry
```

Some commands require extra arguments or allow options to be supplied. The best way to learn about arguments and options is to run the command and add `--help` on to the end of it. For example:

```shell
flask create-data-package --help
```

You can also consult the "CLI Reference" section of this documentation for details about each command.