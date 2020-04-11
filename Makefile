export PYTHONPATH := $(PWD)/noverde_test_project:$(PWD)/noverde_test_project/noverde_test_project:$(PWD)/unit_tests

first_install:
	@git flow init -d
	@poetry install$(PWD)/noverde_
	@rm -rf ./src

install:
	@poetry install
	@rm -rf ./src

cookie:
	@echo Running Cookiecutter...
	@rm -rf ./noverde_test_project
	@poetry run cookiecutter --no-input .

test: cookie
	@poetry run pytest --disable-warnings --ignore=./{{cookiecutter.project_slug}}

ci: cookie
	@poetry run pytest  --disable-warnings --black --mypy --ignore=./{{cookiecutter.project_slug}} --ignore=alembic --ignore=migrations

watch: cookie
	@poetry run ptw -c -w -n --ignore=./{{cookiecutter.project_slug}}

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
createdb:
	@echo "Creating database cookiecutter_develop..."
	@psql postgres -c "DROP DATABASE IF EXISTS cookiecutter_develop;"
	@sleep 1
	@psql postgres -c "CREATE DATABASE cookiecutter_develop;"

.PHONY: revision
# Create new Alembic Migration
# Usage: make revision message="foo"
revision:
	@mkdir -p ./migrations/versions
	@poetry run alembic revision --autogenerate -m "$(message)"

.PHONY: migrate
# Run Alembic Migrations
migrate:
	@poetry run alembic upgrade head

.PHONY: dynamodb
# Run local DynamoDB
dynamodb:
	@docker-compose up -d dynamodb

.PHONY: test_full_ci
# Run make ci for all database options
test_full_ci:
	./full_ci_tests.sh