{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
import os
import sys
import arrow

from typing import Optional
from loguru import logger
from pynamodb.connection import Connection  # type: ignore
from pynamodb.models import Model
from pynamodb.attributes import UTCDateTimeAttribute
from stela import settings

from enterprise.helpers.get_now import get_now

test_environment = "pytest" in sys.modules
if test_environment:
    logger.warning("Running in Test Environment")


def get_table_name() -> str:
    """Return table name.

    Return real name if running in real Lambda.

    :return: String
    """
    table_name = settings["database.nosql.table_name"]
    developing = get_nosql_database_url() is not None
    return "{{cookiecutter.project_slug}}_development" if developing else table_name


def get_nosql_database_url() -> Optional[str]:
    """Get Non relational Database URL.

                            | Windows   | Mac       | Linux
    SAM local via Docker    | dynamodb  | dynamodb  | dynamodb
    AWS Lambda              | Region    | Region    | Region
    Pytest                  | localhost | localhost | localhost

    Return None if running real Lambda in AWS.

    :return: string
    """
    # Pytest
    if test_environment:
        return "http://localhost:8000"

    # AWS Lambda
    if (
        os.environ.get("LAMBDA_TASK_ROOT", None) is not None  # Running inside Lambda
        and bool(os.getenv("AWS_SAM_LOCAL")) is False  # But not on SAM local
    ):
        return None

    # SAM Local
    # `dynamodb` is the service name inside
    # docker-compose.yml
    return "http://dynamodb:8000"


class Base(Model):
    """Base relational class.

    Use this class to add functionality
    to PynamoDB Base class.
    """

    created_at = UTCDateTimeAttribute(default=get_now)
    updated_at = UTCDateTimeAttribute(default=get_now)

    def __eq__(self, other):
        return self.uuid == other.uuid  # type: ignore

    def table_exists(self) -> None:
        """Check if Table exists.

        Running only in Development.
        :return: None
        """
        environment = os.getenv("ENVIRONMENT", "development")
        if environment == "development":
            if not self.exists():
                logger.warning(
                    f"Table {self.Meta.table_name} in {environment} "  # type: ignore
                    f"does not exist. Creating..."
                )
                self.create_table(wait=True)

    def save(self, **kwargs):
        """Validate before save DynamoDB."""
        self.table_exists()
        if self.validate():  # type: ignore
            self.updated_at = arrow.utcnow().datetime
            return super().save(**kwargs)


host = get_nosql_database_url()
connection = (
    Connection(host=get_nosql_database_url())
    if host
    else Connection(region=os.environ["AWS_REGION"])
)
logger.debug(f"Session Registry created for {connection}")
{% endif %}