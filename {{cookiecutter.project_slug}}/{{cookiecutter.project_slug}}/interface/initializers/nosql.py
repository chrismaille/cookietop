{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
import os
import sys

from typing import Optional
from loguru import logger
from pynamodb.connection import Connection  # type: ignore
from pynamodb.models import Model
from stela import settings

test_environment = "pytest" in sys.modules
if test_environment:
    logger.warning(f"Running in Test Environment")


def get_nosql_database_url() -> Optional[str]:
    """Get Non relational Database URL.
    
    Return http://localhost:8000 if Pytest
    Return settings["database.nosql.url"] in Local Development (can be localhost or current docker container)
    For everything else, return Connection looking for current AWS Region

    :return: string
    """
    if test_environment:
        return "http://localhost:8000"
    elif settings.stela_options.current_environment == "development":
        if not os.environ.get("LAMBDA_TASK_ROOT", False):
            return str(settings["database.nosql.url"])
    return None


class Base(Model):
    """Base relational class.
    
    Use this class to add funcionality
    to PynamoDB Base class.
    """

    def __eq__(self, other):
        return self.uuid == other.uuid  # type: ignore

    def table_exists(self) -> None:
        """Check if Table exists.

        Running only in Development.

        :return: None
        """
        environment = settings.stela_options.current_environment
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
            return super().save(**kwargs)

    class Meta:
        abstract = True
        host = get_nosql_database_url()
        read_capacity_units = settings["database.nosql.capacity.read"]
        write_capacity_units = settings["database.nosql.capacity.write"]


host = get_nosql_database_url()
connection = (
    Connection(host=get_nosql_database_url())
    if host
    else Connection(region=os.environ["AWS_REGION"])
)
logger.debug(f"Session Registry created for {connection}")
{% endif %}