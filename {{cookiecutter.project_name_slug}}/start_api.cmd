@ECHO OFF
ECHO ** Remove Artifacts
rmdir /S /Q .aws-sam
del /Q  .\{{cookiecutter.project_name_slug}}\requirements.txt
del /Q  .\{{cookiecutter.project_name_slug}}\pyproject.toml
del /Q  .\{{cookiecutter.project_name_slug}}\template.yml
rmdir /S /Q .\dependencies

ECHO ** Copy files to Project
COPY pyproject.toml .\{{cookiecutter.project_name_slug}}\pyproject.toml
COPY template.yml .\{{cookiecutter.project_name_slug}}\template.yml

ECHO ** Create requirements.txt
CALL poetry export --without-hashes --dev -f requirements.txt -o .\{{cookiecutter.project_name_slug}}\requirements.txt

ECHO ** Build dependencies folder
pip install --upgrade -r .\{{cookiecutter.project_name_slug}}\requirements.txt -t .\dependencies\python

ECHO ** Start SAM api local
sam local start-api --host 0.0.0.0 --port 3001 --debug -n local.json --docker-network lambda-local