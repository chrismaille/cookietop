"""Pytest main conftest module."""
import alembic.config
import boto3
import pytest
from loguru import logger
from moto import mock_dynamodb2
from pytest_postgresql.janitor import DatabaseJanitor

from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document
from interface.initializers.sql import Session
from tests.factories.entities import Noverde{{cookiecutter.domain_class}}ModelFactory
from tests.factories.entities import Noverde{{cookiecutter.domain_class}}DocumentFactory


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

    # TODO: Create DynamoDB Local connection

    # Start Tests
    yield

    # Drop Database
    janitor.drop()


@pytest.fixture(autouse=True)
def dbsession():
    """Rollback transactions after test.

    This automatic fixture is used at function level:
        * After each test: rollback and close session database.

    This session can be accessed through fixture.

    """
    # Run Tests
    yield

    # After test
    Session.rollback()
    Session.remove()


@pytest.fixture()
def {{cookiecutter.domain_slug}}_model() -> Noverde{{cookiecutter.domain_class}}Model:
    """Return Noverde{{cookiecutter.domain_class}}Model Fixture.

    :return: Noverde{{cookiecutter.domain_class}}Model instance
    """
    return Noverde{{cookiecutter.domain_class}}ModelFactory.create(rule=EnterpriseResources.noverde)


@pytest.fixture()
def {{cookiecutter.domain_slug}}_document() -> Noverde{{cookiecutter.domain_class}}Document:
    """Return Noverde{{cookiecutter.domain_class}}Document Fixture.

    :return: Noverde{{cookiecutter.domain_class}}Document instance
    """
    return Noverde{{cookiecutter.domain_class}}DocumentFactory.create(rule=EnterpriseResources.noverde)
