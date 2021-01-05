## Welcome to Cookietop

[![Tests](https://github.com/megalus/cookietop/workflows/tests/badge.svg)](https://github.com/megalus/cookietop/actions)
[![Python](https://img.shields.io/badge/python-3.8-green)](https://www.python.org)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
<a href="https://github.com/psf/black"><img alt="Code style: black"
src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Cookietop is a
[cookiecutter template](https://github.com/cookiecutter/cookiecutter)
for AWS based microservices. This template will create a fully
microservice service with the following features:

* Model handling using full API Gateway CRUD views
* Model validation using
  [Marshmallow](https://github.com/chrismaille/marshmallow-pynamodb)
* Model persistence using
  [PynamoDB](https://github.com/pynamodb/PynamoDB)
* Project settings using [Stela](https://github.com/chrismaille/stela)
* A simple, optional, Step Function machine
* Complete **Cloudformation** configuration
* Complete **Github Actions** configuration
* Production ready with **Poetry**, **Black**, **MyPy**, **Flake**,
  **Docker** and **Pre-Commit** pre-configured.

### How to use

```shell
# Install Cookiecutter if you dont have.
$ pip install -U --user cookiecutter
# or sudo apt install cookiecutter

# Create your new Microservice
$ python3 -m cookiecutter git@github.com:chrismaille/cookietop.git

# Install and Test new Microservice
$ make first_install
$ make test
```

### Cookietop Options

| Option               | Description                                                                | Default value              |
|:---------------------|:---------------------------------------------------------------------------|:---------------------------|
| Project Name         | The Project Name, which will be used on README                             | My Test Microservice       |
| Project Name Camel   | CamelCase for Project Name, which will used on Class names                 | MyTestMicroservice         |
| Project Name Slug    | sneak_case for Project Name, which will used on module names               | my_test_microservice       |
| Project Bucket       | Default AWS Bucket name for Project Assets                                 | My-Test-Microservice       |
| Project Description  | The Project Name, which will be used on README                             | "This project contains..." |
| Python Version       | Project Python Version (must be a valid AWS lambda python version runtime) | 3.8                        |
| Black Target Version | Python version for Black formatting/testing (must be the same)             | py38                       |
| Model                | The Model Name for this microservice, which will used in README            | My Model                   |
| Model Name Camel     | CamelCase for Model Name, which will used in Class names                   | MyModel                    |
| Model Name Slug      | sneak_case for Model Name, which will used in modules and definitions      | my_model                   |
| Add Step Functions   | Add Step Functions example code                                            | yes                        |

### Developing the Microservice Project inside this Cookietop

If you need to develop the microservice project inside this
cookiecutter, the easiest way is creating a new Test Project and develop
in there. For this, you can use this command:

```shell
$ make test_project
```

This command will create a directory called "my_test_microservice" in
parent folder, with a project generated using this template, and with
default options found in file "cookiecutter.json".

### Makefile commands

```shell
# Run tests once (stop a first error)
$ make test

# Run tests in watch mode
$ make watch

# Format code
$ make format

# Run all CI tests
$ make ci

```

