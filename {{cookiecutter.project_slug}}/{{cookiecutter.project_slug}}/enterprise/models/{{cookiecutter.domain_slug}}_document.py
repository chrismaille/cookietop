{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
from stela import settings

from datetime import datetime

from pynamodb.attributes import UTCDateTimeAttribute, UnicodeAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection

from interface.initializers.nosql import Base, connection, get_table_name
from enterprise.helpers.get_uuid import get_uuid
from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.types.enum_attribute import EnumAttribute


class {{cookiecutter.domain_class}}CreatedIndex(GlobalSecondaryIndex):  # type: ignore
    class Meta:
        index_name = "search_by_date"
        read_capacity_units = settings["database.nosql.capacity.read"]
        write_capacity_units = settings["database.nosql.capacity.write"]
        projection = AllProjection()

    created = UTCDateTimeAttribute(default=datetime.utcnow, hash_key=True)


class {{cookiecutter.domain_class}}RuleIndex(GlobalSecondaryIndex):  # type: ignore
    class Meta:
        index_name = "search_by_rule"
        read_capacity_units = settings["database.nosql.capacity.read"]
        write_capacity_units = settings["database.nosql.capacity.write"]
        projection = AllProjection()

    rule = EnumAttribute(EnterpriseResources, hash_key=True)


class {{cookiecutter.domain_class}}Document(Base):
    """{{cookiecutter.domain_class}} DynamoDB Document.

    This is the table created in DynamoDB.
    Each RuleModel Subclass can add new fields.

    """

    uuid = UnicodeAttribute(hash_key=True, default=get_uuid)
    search_by_date = {{cookiecutter.domain_class}}CreatedIndex()
    search_by_rule = {{cookiecutter.domain_class}}RuleIndex()
    created = UTCDateTimeAttribute(default=datetime.utcnow)
    rule = EnumAttribute(EnterpriseResources)

    class Meta(Base.Meta):
        abstract = False
        connection = connection
        table_name = get_table_name()
{% endif %}