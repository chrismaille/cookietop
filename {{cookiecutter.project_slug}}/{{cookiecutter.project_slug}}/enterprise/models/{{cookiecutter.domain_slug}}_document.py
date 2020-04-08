from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, \
    UTCDateTimeAttribute, NumberAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection

from enterprise.helpers.get_enum import EnumUnicodeAttribute
from interface.initializers.nosql import Base


class {{cookiecutter.domain_class}}CreatedIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = "created-index"
        read_capacity_units = 2
        write_capacity_units = 1
        projection = AllProjection()
    created = UTCDateTimeAttribute(default=datetime.utcnow, hash_key=True)


class {{cookiecutter.domain_class}}Document(Base):
    class Meta:
        table_name = "{{cookiecutter.domain_slug}}_document"

    uuid = UnicodeAttribute(hash_key=True)
    created_index = {{cookiecutter.domain_class}}CreatedIndex()
    created = UTCDateTimeAttribute(default=datetime.utcnow)
    rule = EnumUnicodeAttribute()

    def __str__(self):
        return (
            f"<{{cookiecutter.domain_class}}Document("
            f"uuid={self.uuid}, "
            f"rule={self.rule}, "
            f"created={self.created.isoformat()})>"
        )
