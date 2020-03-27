export PYTHONPATH := $(PWD)/{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}:$(PWD)

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

reload:
	@echo Creating new test project on folder '../noverde_test_project' ...
	@rm -rf ../noverde_test_project
	@cookiecutter --no-input . -o ..
	@echo Removing test project virtualenv ...
	@cd ../noverde_test_project && poetry env remove 3.7
