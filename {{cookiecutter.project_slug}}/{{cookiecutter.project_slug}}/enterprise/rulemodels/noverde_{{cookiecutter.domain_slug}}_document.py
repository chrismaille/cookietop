{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from stela import settings

from enterprise.helpers.get_now import get_now
from pynamodb.attributes import UTCDateTimeAttribute
from pynamodb_attributes import UUIDAttribute, UnicodeEnumAttribute

from interface.initializers.nosql import (
    Base,
    get_table_name,
    get_nosql_database_url,
    connection,
)

from enterprise.rules.noverde_mixin import NoverdeMixin
from enterprise.helpers.get_uuid import get_uuid
from enterprise.types.enterprise_resources import EnterpriseResources


class {{cookiecutter.domain_class}}CreatedIndex(GlobalSecondaryIndex):  # type: ignore
    class Meta:
        index_name = "search_by_creation_date"
        read_capacity_units = settings["database.nosql.capacity.read"]
        write_capacity_units = settings["database.nosql.capacity.write"]
        projection = AllProjection()

    created_at = UTCDateTimeAttribute(default=get_now, hash_key=True)


class Noverde{{cookiecutter.domain_class}}Document(NoverdeMixin, Base):
    """Noverde{{cookiecutter.domain_class}}Model.

    This class will join:
    * Noverde enterprise rules (NoverdeMixin)
    * Noverde {{cookiecutter.domain}} Document (from PynamoDB model)

    Usage:
        - For save or update a record, use instance.save() (will validate first)
        - For validation use instance.validate()

    """

    uuid = UUIDAttribute(hash_key=True, default=get_uuid)
    search_by_date = {{cookiecutter.domain_class}}CreatedIndex()
    rule = UnicodeEnumAttribute(
        EnterpriseResources, default=EnterpriseResources.noverde
    )

    def __str__(self):
        return (
            f"<Noverde{{cookiecutter.domain_class}}Document("
            f"uuid={self.uuid}, "
            f"rule={self.rule}, "
            f"created_at={self.created_at.isoformat() if self.created_at else '-'}, "
            f"id={id(self)})>"
        )

    class Meta:
        connection = connection
        table_name = get_table_name()
        host = get_nosql_database_url()
        read_capacity_units = settings["database.nosql.capacity.read"]
        write_capacity_units = settings["database.nosql.capacity.write"]
{% endif %}