"""Pytest main conftest module."""

import alembic.config
import pytest
from loguru import logger
from pytest_postgresql.janitor import DatabaseJanitor

from entities import Service
from initializers.sql import Session
from tests.factories.entities import ServiceFactory


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
def service_model() -> Service:
    """Return Service Model Fixture.

    :return: Service Model instance
    """
    return ServiceFactory.create(name="fixture_service")
