## Welcome to {{ cookiecutter.project_name }}

[![Tests](https://github.com/megalus/{{ cookiecutter.project_name_slug
}}/workflows/tests/badge.svg)](https://github.com/megalus/{{
cookiecutter.project_name_slug }}/actions)
[![Python](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-green)](https://www.python.org)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
<a href="https://github.com/psf/black"><img alt="Code style: black"
src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Model](https://img.shields.io/badge/Model-{{ cookiecutter.model }}-purple)]()

{{ cookiecutter.project_description }}

### Requirements

* [Python{{ cookiecutter.python_version }}](https://www.python.org)
* [AWS CLI](https://aws.amazon.com/cli/)
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Docker](https://www.docker.com)
* [Poetry](https://python-poetry.org/)

### First install

```shell
# Configure your AWS account
$ aws configure

# Install project
$ make first_install

# Test project
$ make ci
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

#### The AWS Toolkit

The
[AWS Toolkit](https://aws.amazon.com/pt/getting-started/tools-sdks/#IDE_and_IDE_Toolkits)
integrates AWS SAM with your IDE. With this plugin you can invoke and
debug local or remote lambda functions. We strongly recommend his use.
Please check the following links:
* [AWS Toolkit for PyCharm](https://aws.amazon.com/pt/pycharm/)
* [AWS Toolkit for VSCode](https://aws.amazon.com/pt/visualstudiocode/)
