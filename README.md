## Welcome to Cookietop

[![Tests](https://github.com/noverde/cookietop/workflows/tests/badge.svg)](https://github.com/noverde/cookietop/actions)
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
  [issues](https://github.com/noverde/cookietop/issues).

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
# or sudo apt install cookiecutter

# Create your new Microservice
$ python3 -m cookiecutter git@github.com:noverde/cookietop.git

# Install and Test new Microservice
$ make first_install
$ make test
```

### Developing Cookiecutter

The easy way is creating a new Test Project from this project and
develop in there. For this, you can use this command:

```shell
# Create a new test Project
# called "Noverde Test Project"
# in ../noverde_test_project folder
# using "Both Databases" option
$ make reload
```

Then, use the following commands to install and develop on test
project:

```shell
# Install and migrate database
$ make config_cookie

# Run tests once (stop a first error)
$ make test

# Run tests in watch mode
$ make watch

# Format code
$ make format

# Run all CI tests
$ make ci

```

After developing on test project, update the code correspondingly in
this project, and then, use the following command to test everything:

```shell
# Run all CI tests for
# all database options
$ make test_full_ci
```

