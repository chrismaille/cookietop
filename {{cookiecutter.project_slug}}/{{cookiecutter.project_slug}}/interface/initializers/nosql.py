import sys

from loguru import logger
from pynamodb.connection import Connection  # type: ignore
from pynamodb.models import Model
from stela import settings

test_environment = "pytest" in sys.modules
if test_environment:
    logger.warning(f"Running in Test Environment")


def get_nosql_database_url() -> str:
    """Get Non relational Database URL.
    
    If not running inside Pytest, will look for the
    "DATABASE_NOSQL_URL" environment
    or settings "database.nosql.url"

    :return: string
    """
    nosql_database_test_url = "http://localhost:8000"
    return (
        nosql_database_test_url
        if test_environment
        else str(settings["database.nosql.url"])
    )


class Base(Model):
    """Base relational class
    
    Use this class to add funcionality
    to PynamoDB Base class.
    """

    class Meta:
        abstract = True
        host = get_nosql_database_url()

    @classmethod
    def query(cls):
        """Return PynamoDB Query.

        :return: PynamoDB query instance
        """
        return dynamodb_session().query(cls)


connection = Connection(host=get_nosql_database_url())
dynamodb_session = connection.session
logger.debug(f"Session Registry created for {connection}")
