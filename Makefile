export PYTHONPATH := $(PWD):$(PWD)/noverde_test_project/noverde_test_project:$(PWD)/tests

first_install:
	@git flow init -d
	@poetry install
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
create_db:
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

.PHONY: start_docker_db_nosql
# Run DynamoDB with Docker
start_docker_db_nosql:
	@docker-compose up -d db_nosql