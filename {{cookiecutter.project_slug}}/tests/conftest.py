"""Pytest main conftest module."""
import alembic.config
import pytest
from _pytest.monkeypatch import MonkeyPatch
from pytest_postgresql.janitor import DatabaseJanitor
from stela import stela_reload

from entities import Service
from initializers.sql import db_session
from tests.factories.entities import ServiceFactory


@pytest.fixture(scope="session", autouse=True)
def start_database():
    """Start database in Session.

    This automatic fixture is used at session level:
        * Before any tests: will create/migrate test database.
        * After all tests: will drop test database.

    """
    user = "noverde"
    password = "noverde"
    host = "localhost"
    port = "5432"
    db_name = "test"
    version = 11

    # Reload SQLAlchemy test database session
    mpatch = MonkeyPatch()
    mpatch.setenv(
        "DATABASE_SQL_URL", f"postgres://{user}:{password}@{host}:{port}/{db_name}"
    )
    stela_reload()

    # Create Test Database
    janitor = DatabaseJanitor(user, host, port, db_name, version, password)
    janitor.drop()
    janitor.init()

    # Run Alembic Migrations in Test Database
    alembicArgs = [
        '--raiseerr',
        'upgrade',
        'head',
    ]
    alembic.config.main(argv=alembicArgs)

    # Start Tests
    yield

    # Drop Database
    janitor.drop()


@pytest.fixture(autouse=True)
def dbsession() -> db_session:
    """Rollback transactions after test.

    This automatic fixture is used at function level:
        * After each test: rollback and close session database.

    This session can be accessed through fixture.

    :return: SQLAlchemy database scoped session
    """
    # Run Test passing database session
    yield db_session

    # After test
    db_session.rollback()
    db_session.close()


@pytest.fixture()
def service_model() -> Service:
    """Return Service Model Fixture.

    :return: Service Model instance
    """
    return ServiceFactory.create(name="test_service")
