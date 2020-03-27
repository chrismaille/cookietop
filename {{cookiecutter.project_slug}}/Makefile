# Noverde (c) Makefile for {{ cookiecutter.project_name }}
# Version: 0.1b
# Language: Python
# Targets:
#	setup:    Install autoenv [optional]
#	install:	Install project
#	serve:	  Run local api via SAM client
#	test:     Run unit and coverage tests, stopping at first error
#	ci:       Run all unit, typing, style and coverage tests
#	format:		Format code as per Black settings

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

export PYTHONPATH := $(PWD)/{{cookiecutter.project_slug}}

.PHONY: install show_config autoenv package build_dependencies deploy serve test ci format

show_config:
	echo "PACKAGE_TMPL: $(PACKAGE_TMPL)"
	echo "S3_BUCKET: $(S3_BUCKET)"
	echo "STACK_NAME: $(STACK_NAME)"
	echo "AWS_PROFILE: $(AWS_PROFILE)"

autoenv:
	git clone git://github.com/inishchith/autoenv.git ~/.autoenv
	echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc
	$(if $(wildcard $(LOCAL_ENV_FILE)),$(shell cp $(LOCAL_ENV_FILE) $(ENV_FILE)),)
	echo 'Autoenv instaled and .env created. Please close this terminal before continue.'

package: show_config
	# for different profiles use AWS_PROFILE environment variable
	@poetry run sam package \
		--output-template-file $(PACKAGE_TMPL) \
		--s3-bucket '$$S3_BUCKET' \

build_dependencies:
	@mkdir -p ./dependencies/python
	@poetry export -f requirements.txt -o ./dependencies/python/requirements.txt
	@pip install -r ./dependencies/python/requirements.txt -t ./dependencies/python

deploy: build_dependencies package
	@poetry run sam deploy \
		--template-file $(PACKAGE_TMPL) \
		--stack-name '$$STACK_NAME' \

install:
	@poetry install
	{%- if cookiecutter.use_pre_commit == "y" -%}
  @poetry run pre-commit install
  {% endif %}
	rm -rf ./src

serve: build_dependencies
	@poetry run sam local start-api

test:
	@poetry run ptw -c -w -n

ci:
	@poetry run pytest --cov=./{{cookiecutter.project_slug}} --black --mypy --pydocstyle --ignore=migrations

format:
	@poetry run black .

clean:
	{%- if cookiecutter.use_pre_commit == "y" -%}
	@poetry run pre-commit uninstall
	{% endif %}
	@rm -rf $(ARTIFACTS)