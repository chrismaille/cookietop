{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
from stela import settings

from datetime import datetime

from pynamodb.attributes import UTCDateTimeAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection

from interface.initializers.nosql import Base, connection


class {{cookiecutter.domain_class}}CreatedIndex(GlobalSecondaryIndex):  # type: ignore
    class Meta:
        index_name = "created-index"
        read_capacity_units = settings["database.nosql.capacity.read"]
        write_capacity_units = settings["database.nosql.capacity.write"]
        projection = AllProjection()

    created = UTCDateTimeAttribute(default=datetime.utcnow, hash_key=True)


class {{cookiecutter.domain_class}}Document(Base):
    class Meta(Base.Meta):
        abstract = False
        connection = connection
        table_name = "{{cookiecutter.domain_slug}}_document"
{% endif %}