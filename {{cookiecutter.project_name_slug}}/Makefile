# Makefile for {{ cookiecutter.project_name }}

# Internal variables
LOCAL_ENV_FILE	:= ./{{cookiecutter.project_name_slug}}/local.env
ENV_FILE		:= ./{{cookiecutter.project_name_slug}}/.env
PACKAGE_FILE	:= ./{{cookiecutter.project_name_slug}}/packaged.yaml
CURRENT_BRANCH	:= $(shell git rev-parse --abbrev-ref HEAD)
ARTIFACTS		:= \
	./{{cookiecutter.project_name_slug}}/.aws-sam \
	./{{cookiecutter.project_name_slug}}/.pytest_cache \
	./{{cookiecutter.project_name_slug}}/.coverage \
	./{{cookiecutter.project_name_slug}}/dependencies

# External variables and his default values
ENVIRONMENT		?= "development"
S3_BUCKET		?= "megalus-artifacts-"$(ENVIRONMENT)
STACK_NAME		?= "{{cookiecutter.project_name_slug}}-"$(ENVIRONMENT)"-stack"
AWS_REGION		?= "us-east-1"

# Exported variables for subshells
export PYTHONPATH := $(PWD)/{{cookiecutter.project_name_slug}}


.PHONY: requirements
# Copy needed files in {{cookiecutter.project_name_slug}} folder
# for AWS Toolkit Plugin and `sam invoke` command work
requirements:
	@rm -rf .aws-sam
	@cp -f *.toml ./{{cookiecutter.project_name_slug}}
	@cp -f ./template.yml ./{{cookiecutter.project_name_slug}}/template.yml
	@poetry export --without-hashes -f requirements.txt -o ./{{cookiecutter.project_name_slug}}/requirements.txt

.PHONY: show_config
# Show configuration used in SAM operations
show_config:
	@echo "ENVIRONMENT: $(ENVIRONMENT)"
	@echo "PACKAGE_TMPL: $(PACKAGE_FILE)"
	@echo "S3_BUCKET: $(S3_BUCKET)"
	@echo "STACK_NAME: $(STACK_NAME)"
	@echo "AWS_REGION: $(AWS_REGION)"

.PHONY: build
# Run SAM build command
build: build_dependencies
	@rm -rf .aws-sam
	# Need requirements in profile folder for AWS Toolkit plugin works
	@poetry export --without-hashes -f requirements.txt -o ./{{cookiecutter.project_name_slug}}/requirements.txt
	@sam build

.PHONY: build_dependencies
# Build dependencies for SAM operations
build_dependencies:
	@mkdir -p ./dependencies/python
	@poetry export --without-hashes -f requirements.txt -o ./dependencies/python/requirements.txt
	@cp *.toml ./{{cookiecutter.project_name_slug}}
	@poetry run pip install --upgrade -r ./dependencies/python/requirements.txt -t ./dependencies/python

.PHONY: package
# Run `sam package` command
package: show_config build_dependencies
	@rm -rf .aws-sam
	@aws s3api create-bucket --bucket $(S3_BUCKET) 1> /dev/null
	@poetry run sam package \
		--output-template-file $(PACKAGE_FILE) \
		--s3-bucket $(S3_BUCKET)

.PHONY: deploy
# Run `sam deploy` command
deploy: package
	@poetry run sam deploy \
		--template-file $(PACKAGE_FILE) \
		--capabilities CAPABILITY_IAM \
		--stack-name $(STACK_NAME) \
		--region $(AWS_REGION)

	@rm -f ./{{cookiecutter.project_name_slug}}/env-*.toml
	@rm -f ./{{cookiecutter.project_name_slug}}/pyproject.toml
	@rm -f ./{{cookiecutter.project_name_slug}}/packaged.yaml

.PHONY: first_install
# Runs setup operations for first install
first_install:
	@poetry install
	@poetry run pre-commit install
	@docker network create lambda-local &

.PHONY: install
# Install application
install:
	@poetry install

.PHONY: serve
# Runs local API via SAM client
serve: build_dependencies
	@rm -rf .aws-sam
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
	@poetry run pytest --disable-warnings --flake8 --cov=./{{cookiecutter.project_name_slug}} --black --mypy --pydocstyle --ignore=dependencies

.PHONY: format
# Format code using pre-commit and black
format:
	@poetry run pre-commit run --all-files
	@poetry run black .

.PHONY: clean
# Clear created artifacts
clean:
	@poetry run pre-commit uninstall
	@rm -rf $(ARTIFACTS)

.PHONY: dynamodb
# Run local DynamoDB
dynamodb:
	@docker-compose up -d dynamodb
