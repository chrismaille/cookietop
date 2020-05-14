"""Pytest main conftest module."""
import json
import os
from pathlib import Path
from typing import Any, Dict

from stela import settings

{% if cookiecutter.database != "None" %}
# flake8: noqa
# fmt: off
import pytest
from loguru import logger
{% if cookiecutter.database == "RDS" or cookiecutter.database == "Both" %}
import alembic.config

from pytest_postgresql.janitor import DatabaseJanitor

from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model
from interface.initializers.sql import Session
from tests.factories.models import Noverde{{cookiecutter.domain_class}}ModelFactory
{% endif %}
from enterprise.types.enterprise_resources import EnterpriseResources
{% if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" %}
from enterprise.models.{{cookiecutter.domain_slug}}_document import {{cookiecutter.domain_class}}Document
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document
{% endif %}
{% if cookiecutter.database == "RDS" or cookiecutter.database == "Both" %}
@pytest.fixture(scope="session", autouse=True)
def start_session():
    """Start database in Session.

    This automatic fixture is used at session level:
        * Before any tests: will create and migrate test database.
        * After all tests: will drop test database.

    """
    user = "noverde"
    password = "noverde"
    host = "localhost"
    port = "5432"
    db_name = "test"
    version = 11

    janitor = DatabaseJanitor(user, host, port, db_name, version, password)
    logger.info("Creating test database...")
    janitor.drop()
    janitor.init()

    # Run Alembic Migrations in Test Database
    logger.info("Running database migration...")
    alembicArgs = [
        "--raiseerr",
        "upgrade",
        "head",
    ]
    alembic.config.main(argv=alembicArgs)

    # Start Tests
    yield

    # Drop Database
    janitor.drop()


@pytest.fixture(autouse=True)
def model_session():
    """Rollback transactions after test.

    This automatic fixture is used at function level:
        * After each test: rollback and close session database.

    """

    # Run Tests
    yield

    # After test
    Session.rollback()
    Session.remove()
{% endif %}
{% if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" %}
@pytest.fixture(autouse=True)
def document_session():
    """Remove table after test.

    This automatic fixture is used at function level:
        * After each test: delete and create dynamodb table.

    """
    if Noverde{{cookiecutter.domain_class}}Document.exists():
        Noverde{{cookiecutter.domain_class}}Document.delete_table()
    Noverde{{cookiecutter.domain_class}}Document.create_table(
        read_capacity_units=1, write_capacity_units=1, wait=True
    )

    # Run tests
    yield

    # Remove table
    {{cookiecutter.domain_class}}Document.delete_table()
{% endif %}
{% if cookiecutter.database == "RDS" or cookiecutter.database == "Both" %}
@pytest.fixture
def noverde_{{cookiecutter.domain_slug}}_model() -> Noverde{{cookiecutter.domain_class}}Model:
    """Return Noverde{{cookiecutter.domain_class}}Model Fixture.

    :return: Noverde{{cookiecutter.domain_class}}Model instance
    """
    return Noverde{{cookiecutter.domain_class}}ModelFactory.create(rule=EnterpriseResources.noverde)
{% endif %}
{% if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" %}
@pytest.fixture
def new_{{cookiecutter.domain_slug}}_document_data():
    return {
        "noverde_unique_field": "foo"
    }

@pytest.fixture
def noverde_{{cookiecutter.domain_slug}}_document(new_{{cookiecutter.domain_slug}}_document_data) -> Noverde{{cookiecutter.domain_class}}Document:
    """Return Noverde{{cookiecutter.domain_class}}Document Fixture.

    :return: Noverde{{cookiecutter.domain_class}}Document instance
    """
    new_instance = Noverde{{cookiecutter.domain_class}}Document(**new_{{cookiecutter.domain_slug}}_document_data)
    new_instance.save()
    return new_instance
{% endif %}
{% endif %}
def load_fixture(filename: str) -> Dict[Any, Any]:
    """Load fixtures from fixtures folder.

    :param filename: json filename
    :return: Dict
    """
    if settings.get("use_cookie_path", False):
        base_path = os.environ.get("PYTHONPATH").split(":")[0]
    else:
        base_path = str(Path().cwd())
    file_path = Path().joinpath(base_path, "tests", "fixtures", filename)
    with open(str(file_path)) as file:
        fixture = json.load(file)
    return fixture


# fmt: on
