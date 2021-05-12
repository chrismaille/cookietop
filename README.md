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
* VSCode Remote Development support
* PyCharm Run/Debug support


```shell
# Clone this project
$ git clone https://github.com/access55/django_cookie.git

# Install project
$ make install

# Run `make project` informing your target folder
$ TARGET=/path/to/my_projects make project

# Run `make config_project`
$ cd /path/to/my_projects/new_project
$ make first_config
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


