{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
import os
import sys

from typing import Optional
from loguru import logger
from pynamodb.connection import Connection  # type: ignore
from pynamodb.models import Model
from stela import settings

from interface.aws.sam_data import get_sam_data

test_environment = "pytest" in sys.modules
if test_environment:
    logger.warning(f"Running in Test Environment")


def get_table_name() -> str:
    """Return table name.

    Return real name if running in real Lambda.

    :return: String
    """
    developing = get_nosql_database_url() is not None
    if developing:
        return "{{ cookiecutter.project_slug }}_development"
    SAM_DATA = get_sam_data()
    dynamo_data = SAM_DATA["Resources"]["{{ cookiecutter.domain_class }}Document"]
    table_name = dynamo_data["Properties"]["TableName"]
    return table_name


def get_nosql_database_url() -> Optional[str]:
    """Get Non relational Database URL.

    Return None if running real Lambda in AWS.

    :return: string
    """
    if (
        os.environ.get("LAMBDA_TASK_ROOT", None) is not None  # Running inside Lambda
        and bool(os.getenv("AWS_SAM_LOCAL")) is False  # But not on SAM local
    ):
        return None
    return "http://localhost:8000"


class Base(Model):
    """Base relational class.

    Use this class to add functionality
    to PynamoDB Base class.
    """

    def __eq__(self, other):
        return self.uuid == other.uuid  # type: ignore

    def save(self, **kwargs):
        """Validate before save DynamoDB."""
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