## Welcome to Noverde Cookiecutter

[![Tests](https://github.com/noverde/noverde_cookiecutter/workflows/tests/badge.svg)](https://github.com/noverde/noverde_cookiecutter/actions)
[![Python](https://img.shields.io/badge/python-3.7-green)](https://www.python.org)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
<a href="https://github.com/psf/black"><img alt="Code style: black"
src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![GitFlow](https://img.shields.io/badge/GitFlow-Friendly-brightgreen)](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

### What is:

Its the boilerplate we need to create a new Noverde micro-service. This
project is based on the
[Cookiecutter Project](https://github.com/cookiecutter/cookiecutter).
Our goal with this project are:

* Quick create new project with CI/CD, base configuration, commands and
  tests configured.
* Give a simple example how to handle and test a View Handler.
* Give a simple example how to handle and test project's **API
  Gateway**.
* Give a simple example how to handle and test project's **AWS
  DynamoDB** documents, if available.
* Give a simple example how to handle and test project's **AWS Aurora**
  tables, if available.
* Give a simple example how to handle and test project's **AWS Step
  Functions** machines, if available.

### What is not:

* *This is NOT a mandatory way to work*. We deeply value new ideas,
  libraries, patterns, services, etc.. - if you want to suggest new
  features, libs, commands, etc, please look our
  [issues](https://github.com/noverde/noverde_cookiecutter/issues).

### Requirements

* [Make](https://www.gnu.org/software/make/)
* [Python3.7](https://www.python.org)
* [AWS CLI](https://aws.amazon.com/cli/)
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Docker](https://www.docker.com)
* [Poetry](https://python-poetry.org/)
* [GitFlow](https://github.com/petervanderdoes/gitflow-avh/wiki/Installation)

### How to use
```shell
# Install Cookiecutter if you dont have.
$ pip install -U --user cookiecutter

# Create your new Microservice
$ cookiecutter gh:noverde/noverde_cookiecutter

# Install and Test new Microservice
$ cd path/to/new_project
$ make first_install
$ make test
```

### Developing Cookiecutter

Use the following commands to install and develop our cookiecutter:

```shell
# First install
$ make first_install

# Reinstall Project
$ make install

# Run tests once (stop a first error)
$ make test

# Run tests in watch mode
$ make watch

# Format code
$ make format

# Run all CI tests
$ make ci

# Run all CI tests for
# all database options
$ make test_full_ci

# Create test Project
# called Noverde Test Project
# in ../noverde_test_project folder
$ make reload
```

Every time you run tests, this project will create a "Noverde Test
Project" in `noverde_test_project` subfolder using local cookiecutter
code. Also you can use command `make reload` to install this test
project in parent folder.

#### Testing Relational Database
```shell
# Create new database
$ make create_db

# Add new migration
$ make revision message="foo"

# Migrate Database
$ make migrate
```
