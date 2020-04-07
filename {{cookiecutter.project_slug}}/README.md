## Welcome to {{ cookiecutter.project_name }}

[![Tests](https://github.com/noverde/{{ cookiecutter.project_slug
}}/workflows/tests/badge.svg)](https://github.com/noverde/{{
cookiecutter.project_slug }}/actions)
[![Python](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-green)](https://www.python.org)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
<a href="https://github.com/psf/black"><img alt="Code style: black"
src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![GitFlow](https://img.shields.io/badge/GitFlow-Friendly-brightgreen)](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Domain](https://img.shields.io/badge/Domain-{{ cookiecutter.domain_class }}-purple)](https://www.notion.so/noverde/Engineering-5388610204db436a81b992b1b146f83e)

{{ cookiecutter.project_description }}

For detailed instructions how to install and use this project, please
check our
[Engineering Section](https://www.notion.so/noverde/Engineering-5388610204db436a81b992b1b146f83e)
in [Notion](https://www.notion.so/noverde)


### Requirements

* [Make](https://www.gnu.org/software/make/)
* [Python3.7](https://www.python.org)
* [AWS CLI](https://aws.amazon.com/cli/)
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Docker](https://www.docker.com)
* [Poetry](https://python-poetry.org/)
* [GitFlow](https://github.com/petervanderdoes/gitflow-avh/wiki/Installation)

### First install

```shell
# Configure your Noverde AWS account
$ aws configure

# Install project
$ make first_install

# Prepare relational database (postgres)
# Make sure you have the "noverde:noverde"
# superuser created in postgres.
$ make create_db
$ make revision message="First commit"
$ make migrate

# Test project
$ make test # or make ci
```


### Command List

```shell
# Install application (first time)
$ make first_install

# (Re)install application
$ make install

# Quick-Test Application
$ make test

# Test in watch mode
$ make watch

# Lint and Test Application
$ make ci

# Format code
$ make format

# Run Local server
$ make serve

# Manual Deploy (check your permissions first)
$ make deploy
```

#### Relational Database Commands

```shell
# Create development database
# In Postgres create user: noverde, pass: noverde
$ make create_db

# Create new Revision
$ make revision message="foo"

# Migrate Database
$ make migrate
```

#### The AWS Toolkit

The
[AWS Toolkit](https://aws.amazon.com/pt/getting-started/tools-sdks/#IDE_and_IDE_Toolkits)
integrates AWS SAM with your IDE. With this plugin you can invoke and
debug local or remote lambda functions. We strongly recommend his use.
Please check the following links:
* [AWS Toolkit for PyCharm](https://aws.amazon.com/pt/pycharm/)
* [AWS Toolkit for VSCode](https://aws.amazon.com/pt/visualstudiocode/)

