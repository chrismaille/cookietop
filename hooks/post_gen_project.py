# flake8: noqa
"""Remove not used files.

From database choices: "DynamoDB (recommended)", "RDS", "Both", "None"

"""
import logging
import os
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

manifest = {
    "dynamo": [
        "tests/factories/documents.py",
        "tests/test_document.py",
        "tests/test_document_schema.py",
        "tests/test_rule_document.py",
        "tests/test_{{cookiecutter.domain_slug}}_document.py",
        "{{cookiecutter.project_slug}}/application/schemas/noverde_{{cookiecutter.domain_slug}}_document_schema.py",
        "{{cookiecutter.project_slug}}/enterprise/models/{{cookiecutter.domain_slug}}_document.py",
        "{{cookiecutter.project_slug}}/enterprise/rulemodels/noverde_{{cookiecutter.domain_slug}}_document.py",
        "{{cookiecutter.project_slug}}/interface/initializers/nosql.py",
    ],
    "rds": [
        "tests/factories/models.py",
        "tests/test_model.py",
        "tests/test_model_schema.py",
        "tests/test_rule_model.py",
        "{{cookiecutter.project_slug}}/application/schemas/noverde_{{cookiecutter.domain_slug}}_model_schema.py",
        "{{cookiecutter.project_slug}}/enterprise/models/{{cookiecutter.domain_slug}}_model.py",
        "{{cookiecutter.project_slug}}/enterprise/rulemodels/noverde_{{cookiecutter.domain_slug}}_model.py",
        "{{cookiecutter.project_slug}}/interface/initializers/sql.py",
        "migrations",
        "alembic.ini",
    ],
}

database_choice = "{{ cookiecutter.database }}"
logger.debug(f"database choose: {database_choice}")

exclude_files = []

if database_choice == "None":
    exclude_files = manifest["dynamo"] + manifest["rds"]
elif database_choice == "DynamoDB (recommended)":
    exclude_files = manifest["rds"]
elif database_choice == "RDS":
    exclude_files = manifest["dynamo"]

for string_path in exclude_files:
    path = Path().cwd().joinpath(string_path)
    # logger.debug(f"Removing {path}...")
    if path.is_dir():
        shutil.rmtree(path)
    else:
        os.remove(str(path))
