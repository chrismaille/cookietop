export PYTHONPATH := $(PWD):$(PWD)/{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}:$(PWD)/tests

setup:
	@git flow init -d

install:
	@poetry install
	rm -rf ./src

test:
	@rm -rf ./noverde_test_project
	@poetry run pytest --disable-warnings

ci:
	@echo Running Cookiecutter...
	@rm -rf ./noverde_test_project
	@poetry run cookiecutter --no-input .
	@poetry run pytest  --cov=./noverde_test_project --disable-warnings --black --mypy --ignore=./{{cookiecutter.project_slug}} --ignore=alembic --ignore=migrations
	@rm -rf ./noverde_test_project

watch:
	@rm -rf ./noverde_test_project
	@poetry run ptw -c -w -n

format:
	@poetry run black .

reload:
	@echo Creating new test project on folder 'noverde_test_project' ...
	@rm -rf ../noverde_test_project
	@cookiecutter --no-input . -o ..
	@echo Removing test project virtualenv ...
	@cd ../noverde_test_project && poetry env remove 3.7

.PHONY: create_db
# Create Database
create_db:
	@echo "Creating database cookiecutter_test..."
	@psql postgres -c "DROP DATABASE IF EXISTS cookiecutter_test;"
	@sleep 1
	@psql postgres -c "CREATE DATABASE cookiecutter_test;"

.PHONY: revision
# Create new Alembic Migration
# Usage: make revision message="foo"
revision:
	@poetry run alembic revision --autogenerate -m "$(message)"

.PHONY: migrate
# Run Alembic Migrations
migrate:
	@poetry run alembic upgrade head