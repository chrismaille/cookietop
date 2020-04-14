# Noverde (c) Makefile for {{ cookiecutter.project_name }}

# Internal variables
LOCAL_ENV_FILE	:= ./{{cookiecutter.project_slug}}/local.env
ENV_FILE		:= ./{{cookiecutter.project_slug}}/.env
PACKAGE_FILE	:= ./{{cookiecutter.project_slug}}/packaged.yaml
CURRENT_BRANCH	:= $(shell git rev-parse --abbrev-ref HEAD)
ARTIFACTS		:= \
	./{{cookiecutter.project_slug}}/.aws-sam \
	./{{cookiecutter.project_slug}}/.pytest_cache \
	./{{cookiecutter.project_slug}}/.coverage \
	./{{cookiecutter.project_slug}}/dependencies

# External variables and his default values
ENVIRONMENT		?= "develop"
S3_BUCKET		?= "{{cookiecutter.project_bucket}}-"$(ENVIRONMENT)
STACK_NAME		?= "{{cookiecutter.project_bucket}}-"$(ENVIRONMENT)"-stack"
AWS_PROFILE		?= "default"

# Exported variables for subshells
export PYTHONPATH := $(PWD)/{{cookiecutter.project_slug}}


.PHONY: show_config
# Show configuration used in SAM operations
show_config:
	@echo "ENVIRONMENT: $(ENVIRONMENT)"
	@echo "PACKAGE_TMPL: $(PACKAGE_FILE)"
	@echo "S3_BUCKET: $(S3_BUCKET)"
	@echo "STACK_NAME: $(STACK_NAME)"
	@echo "AWS_PROFILE: $(AWS_PROFILE)"

.PHONY: autoenv
# Install autoenv (optional)
autoenv:
	git clone git://github.com/inishchith/autoenv.git ~/.autoenv
	echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc
	$(if $(wildcard $(LOCAL_ENV_FILE)),$(shell cp $(LOCAL_ENV_FILE) $(ENV_FILE)),)
	echo 'Autoenv instaled and .env created. Please close this terminal before continue.'

.PHONY: build
# Run SAM build command
build: build_dependencies
	@rm -rf .aws-sam
	@sam build

.PHONY: build_dependencies
# Build dependencies for SAM operations
build_dependencies:
	@mkdir -p ./dependencies/python
	@poetry export --without-hashes -f requirements.txt -o ./dependencies/python/requirements.txt
	@cp *.toml ./{{cookiecutter.project_slug}}
	@poetry run pip install --upgrade -r ./dependencies/python/requirements.txt -t ./dependencies/python

.PHONY: package
# Run `sam package` command
# for different profiles use AWS_PROFILE environment variable
package: show_config build_dependencies
	@aws s3 mb s3://$(S3_BUCKET)
	@poetry run sam package \
		--output-template-file $(PACKAGE_FILE) \
		--s3-bucket $(S3_BUCKET)

.PHONY: deploy
# Run `sam deploy` command
deploy: build_dependencies package
	@poetry run sam deploy \
		--template-file $(PACKAGE_FILE) \
		--capabilities CAPABILITY_IAM \
		--stack-name $(STACK_NAME)

	@rm -f ./{{cookiecutter.project_slug}}/env-*.toml
	@rm -f ./{{cookiecutter.project_slug}}/packaged.yaml

.PHONY: first_install
# Runs setup operations for first install
first_install:
	@git flow init -d
	@poetry install
	@poetry run pre-commit install
	@docker network create lambda-local

.PHONY: install
# Install application
install:
	@poetry install
	@rm -rf ./src

.PHONY: serve
# Runs local API via SAM client
serve: build_dependencies
	@poetry run sam local start-api --debug -n local.json --docker-network lambda-local

.PHONY: watch
# Runs pytest in watch mode
watch:
	@poetry run ptw -c -w -n --ignore=dependencies

.PHONY: test
# Runs pytest stopping at first error
test:
	@poetry run pytest -x  --disable-warnings --ignore=dependencies

.PHONY: ci
# Runs pytest for full testing
ci:
	@poetry run pytest --disable-warnings --cov=./{{cookiecutter.project_slug}} --black --mypy --pydocstyle --ignore=migrations --ignore=dependencies

.PHONY: format
# Format code using black
format:
	@poetry run black .

.PHONY: clean
# Clear created artifacts
clean:
	@poetry run pre-commit uninstall
	@rm -rf $(ARTIFACTS)

.PHONY: create_db
# Create Development Database
createdb:
	@echo "Creating database {{cookiecutter.project_slug}}_develop..."
	@psql postgres -c "DROP DATABASE IF EXISTS {{cookiecutter.project_slug}}_develop;"
	@sleep 1
	@psql postgres -c "CREATE DATABASE {{cookiecutter.project_slug}}_develop;"

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

.PHONY: config_cookie
# After run `make reload`
# change to noverde_test_project folder
# and use this command to quick config the test project
config_cookie: first_install createdb
	@mkdir -p ./migrations/versions
	@poetry run alembic revision --autogenerate -m "First Commit"
	@poetry run alembic upgrade head
