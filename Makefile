export PYTHONPATH := $(PWD)/{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}

setup:
	@git flow init -d

install:
	@poetry install
	rm -rf ./src

test:
	@poetry run pytest

ci:
	@echo Running Cookiecutter...
	@rm -rf ./noverde_cookiecutter
	@poetry run cookiecutter --no-input .
	@poetry run pytest --ignore=./{{cookiecutter.project_slug}}
	@rm -rf ./noverde_cookiecutter

watch:
	@poetry run ptw -c -w -n

format:
	@poetry run black .
