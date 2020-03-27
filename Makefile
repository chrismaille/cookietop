export PYTHONPATH := $(PWD)/{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}

setup:
	@git flow init -d

install:
	@poetry install
	rm -rf ./src

test:
	@poetry run pytest

format:
	@poetry run black .
