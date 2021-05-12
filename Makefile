export PYTHONPATH			:= $(PWD)/my_test_microservice:$(PWD)/my_test_microservice/my_test_microservice:$(PWD)/unit_tests

first_install:
	@git flow init -d
	@poetry install
	@rm -rf ./src

install:
	@poetry install
	@poetry run pre-commit install -f
	@rm -rf ./src

cookie:
	@echo Running Cookiecutter...
	@rm -rf ./my_test_microservice
	@poetry run cookiecutter --no-input .

test: cookie
	@poetry run pytest --disable-warnings --ignore=./{{cookiecutter.project_name_slug}}

ci: cookie
	@poetry run pytest --disable-warnings --flake8 --black --mypy --ignore=./{{cookiecutter.project_name_slug}} --ignore=hooks

watch: cookie
	@poetry run ptw -c -w -n --ignore=./{{cookiecutter.project_name_slug}}

format:
	@poetry run black .

project:
	@echo ">>> Creating new test project on folder: ${TARGET} ..."
	@echo ">>> Running Cookiecutter ..."
	@rm -rf ./tmp_project
	@poetry run cookiecutter . -f -o ./tmp_project
	@mkdir -p ${TARGET}
	@mv -f ./tmp_project/* ${TARGET}

.PHONY: dynamodb
# Run local DynamoDB
dynamodb:
	@docker-compose up -d dynamodb
