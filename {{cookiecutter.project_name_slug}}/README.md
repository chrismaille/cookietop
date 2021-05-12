## Welcome to {{ cookiecutter.project_name }}

[![Tests](https://github.com/megalus/{{ cookiecutter.project_name_slug
}}/workflows/pull_request/badge.svg)](https://github.com/megalus/{{
cookiecutter.project_name_slug }}/actions)
[![Python](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-green)](https://www.python.org)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Model](https://img.shields.io/badge/Model-{{ cookiecutter.model }}-purple)]()

{{ cookiecutter.project_description }}

### Requirements

* [Python3.8](https://www.python.org)
* [AWS CLI](https://aws.amazon.com/cli/)
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Docker](https://www.docker.com)
* [Poetry](https://python-poetry.org/)

### Install

```shell
# [Optional] Configure your AWS account
$ aws configure

# Install project and create .env file
$ make install
$ cp env.local .env
```

### Developing in Docker
```shell
# Build Application
$ docker-compose build

# Start Application
$ docker-compose up
```

### Developing in PyCharm

1. Install [AWS Toolkit for PyCharm](https://aws.amazon.com/pt/pycharm/)

2. Open PyCharm terminal and create AWS Toolkit artifacts:
```shell
# Prepare Artifacts
$ make build
```
3. On Run/Debug Configuration select `[Local] Run Health-Check` to test application

4. On Run/Debug Configuration select `Run SAM Api` to start local Api

### Developing in VSCode

1. Install the following extensions:
* [AWS Toolkit for PyCharm](https://aws.amazon.com/pt/pycharm/)
* Remote Development
* Python
* Docker

2. On command-palette select "**Remote-Containers: Rebuild and Reopen in
   Container**"
   
2. Open VSCode terminal and create AWS Toolkit artifacts:
```shell
# Prepare Artifacts
$ make build
```