# Noverde (c) Makefile for {{ cookiecutter.project_name }}

# Internal variables
LOCAL_ENV_FILE	:= ./{{cookiecutter.project_slug}}/local.env
ENV_FILE     		:= ./{{cookiecutter.project_slug}}/.env
PACKAGE_FILE 		:= ./{{cookiecutter.project_slug}}/packaged.yaml
CURRENT_BRANCH	:= $(shell git rev-parse --abbrev-ref HEAD)
ARTIFACTS    		:= \
	./{{cookiecutter.project_slug}}/.aws-sam \
	./{{cookiecutter.project_slug}}/.pytest_cache \
	./{{cookiecutter.project_slug}}/.coverage \
	./{{cookiecutter.project_slug}}/dependencies/python

# External variables and his default values
S3_BUCKET       ?= $(suffix "{{cookiecutter.project_slug}}" "_" $(USER))
STACK_NAME      ?= $(suffix "{{cookiecutter.project_slug}}" "_" $(USER) "_" $(CURRENT_BRANCH))

# Exported variables for subshells
export PYTHONPATH := $(PWD)/{{cookiecutter.project_slug}}


.PHONY: show_config
# Show configuration used in SAM operations
show_config:
	echo "PACKAGE_TMPL: $(PACKAGE_TMPL)"
	echo "S3_BUCKET: $(S3_BUCKET)"
	echo "STACK_NAME: $(STACK_NAME)"
	echo "AWS_PROFILE: $(AWS_PROFILE)"

.PHONY: autoenv
# Install autoenv (optional)
autoenv:
	git clone git://github.com/inishchith/autoenv.git ~/.autoenv
	echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc
	$(if $(wildcard $(LOCAL_ENV_FILE)),$(shell cp $(LOCAL_ENV_FILE) $(ENV_FILE)),)
	echo 'Autoenv instaled and .env created. Please close this terminal before continue.'

.PHONY: package
# Run `sam package` command
package: show_config
	# for different profiles use AWS_PROFILE environment variable
	@poetry run sam package \
		--output-template-file $(PACKAGE_TMPL) \
		--s3-bucket '$$S3_BUCKET' \

.PHONY: build_dependencies
# Build dependencies for SAM operations
build_dependencies:
	@mkdir -p ./dependencies/python
	@poetry export -f requirements.txt -o ./dependencies/python/requirements.txt
	@pip install -r ./dependencies/python/requirements.txt -t ./dependencies/python

.PHONY: deploy
# Run `sam deploy` command
deploy: build_dependencies package
	@poetry run sam deploy \
		--template-file $(PACKAGE_TMPL) \
		--stack-name '$$STACK_NAME' \

.PHONY: setup
# Runs setup operations for first install
setup:
	@git flow init -d
	@poetry install
	@poetry run pre-commit install

.PHONY: install
# Install application
install:
	@poetry install
	@rm -rf ./src

.PHONY: serve
# Runs local API via SAM client
serve: build_dependencies
	@poetry run sam local start-api

.PHONY: watch
# Runs pytest in watch mode
watch:
	@poetry run ptw -c -w -n

.PHONY: test
# Runs pytest stopping at first error
test:
	@poetry run pytest -x

.PHONY: ci
# Runs pytest for full testing
ci:
	@poetry run pytest --cov=./{{cookiecutter.project_slug}} --black --mypy --pydocstyle --ignore=migrations

.PHONY: format
# Format code using black
format:
	@poetry run black .

.PHONY: clean
# Clear created artifacts
clean:
	@poetry run pre-commit uninstall
	@rm -rf $(ARTIFACTS)