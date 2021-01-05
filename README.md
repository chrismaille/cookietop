## Welcome to Cookietop

[![Tests](https://github.com/megalus/cookietop/workflows/tests/badge.svg)](https://github.com/megalus/cookietop/actions)
[![Python](https://img.shields.io/badge/python-3.7-green)](https://www.python.org)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
<a href="https://github.com/psf/black"><img alt="Code style: black"
src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

### How to use
```shell
# Install Cookiecutter if you dont have.
$ pip install -U --user cookiecutter
# or sudo apt install cookiecutter

# Create your new Microservice
$ python3 -m cookiecutter git@github.com:megalus/cookietop.git

# Install and Test new Microservice
$ make first_install
$ make test
```

### Developing Cookiecutter

The easy way is creating a new Test Project from this project and
develop in there. For this, you can use this command:

```shell
# Create a new test Project
# called "Cookietop Test Project"
# in ../cookietop_test_project folder
$ make reload
```

Then, use the following commands to install and develop on test
project:

```shell
# Install and migrate database
$ make config_cookie

# Run pre-commit for errors
$ git add .
$ git commit -m "First commit" 

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
$ make ci
```

