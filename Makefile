export PYTHONPATH			:= $(PWD)/my_test_microservice:$(PWD)/my_test_microservice/my_test_microservice:$(PWD)/unit_tests

first_install:
	@git flow init -d
	@poetry install
	@rm -rf ./src

install:
	@poetry install
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

test_project:
	@echo Creating new test project on folder 'my_test_microservice' ...
	@cp -rf ../my_test_microservice/.idea /tmp/.idea 2>/dev/null || :
	@rm -rf ../my_test_microservice
	@echo Running Cookiecutter ...
	@poetry run cookiecutter --no-input . -o ..
	@echo Removing test project virtualenv ...
	@cd ../my_test_microservice
	@poetry env remove 3.8 /tmp/.idea 2>/dev/null || :
	@cp -rf ../tmp/.idea /my_test_microservice/.idea /tmp/.idea 2>/dev/null || :
	@echo Install Dependencies ...
	@poetry install
	@echo Running Git ...
	@git init && git add . && git commit -m "first commit"

.PHONY: dynamodb
# Run local DynamoDB
dynamodb:
	@docker-compose up -d dynamodb
