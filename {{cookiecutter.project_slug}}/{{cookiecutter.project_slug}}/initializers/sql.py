"""Initialize Database Session.

As per SQLAlchemy API.
Database URL must have this format: postgres://<user>:<password>@<host>:<port>/<name>

You can define the settings "database.sql.url" or
the DATABASE_SQL_URL environment variable.

"""
import sys

from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Query, scoped_session, sessionmaker
from stela import settings

test_environment = "pytest" in sys.modules
if test_environment:
    logger.warning(f"Running in Test Environment")


def get_database_url() -> str:
    """Get Database URL.

    If not running inside Pytest,
    will look for the "DATABASE_SQL_URL" environment
    or settings "database.sql.url"

    :return: string
    """
    database_test_url = "postgres://noverde:noverde@localhost/test"
    return database_test_url if test_environment else str(settings["database.sql.url"])


@as_declarative()
class Base:
    """Base ORM class.

    Use this class to add functionality
    to SQLAlchemy Base class.

    """

    @classmethod
    def query(cls) -> Query:
        """Return SQLAlchemy Query.

        :return: SQAlchemy query instance
        """
        return Session().query(cls)


engine = create_engine(get_database_url(), echo=settings["database.sql.echo"])
Session = scoped_session(sessionmaker(bind=engine, autoflush=True))
logger.debug(f"Session Registry created for {engine}")
