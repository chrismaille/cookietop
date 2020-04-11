from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection

from interface.initializers.nosql import Base, connection


class {{cookiecutter.domain_class}}CreatedIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = "created-index"
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    created = UTCDateTimeAttribute(default=datetime.utcnow, hash_key=True)


class {{cookiecutter.domain_class}}Document(Base):
    def __eq__(self, other):
        return self.uuid == other.uuid

    class Meta(Base.Meta):
        abstract = False
        connection = connection
        table_name = "{{cookiecutter.domain_slug}}_document"
