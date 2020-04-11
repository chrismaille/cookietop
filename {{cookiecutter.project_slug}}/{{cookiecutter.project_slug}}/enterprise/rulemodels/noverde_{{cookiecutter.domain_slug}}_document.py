{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
from datetime import datetime

from pynamodb.attributes import UTCDateTimeAttribute, UnicodeAttribute

from enterprise.helpers.get_uuid import get_uuid
from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.types.enum_attribute import EnumAttribute
from enterprise.models.{{cookiecutter.domain_slug}}_document import {{cookiecutter.domain_class}}CreatedIndex, {{cookiecutter.domain_class}}Document
from enterprise.rules.noverde_mixin import NoverdeMixin


class Noverde{{cookiecutter.domain_class}}Document(NoverdeMixin, {{cookiecutter.domain_class}}Document):
    """Noverde{{cookiecutter.domain_class}}Model.

    This class will join:
    * Noverde enterprise rules (NoverdeMixin)
    * Noverde {{cookiecutter.domain}} Document (from PynamoDB model)

    Currently PynamoDB does not support Table inheritance.
    See info: https://github.com/pynamodb/PynamoDB/pull/440

    Until then, we need to add all fields here.

    Usage:
        - For save or update a record, use instance.save() (will validate first)
        - For validation use instance.validate()

    """

    uuid = UnicodeAttribute(hash_key=True, default=get_uuid)
    created_index = {{cookiecutter.domain_class}}CreatedIndex()
    created = UTCDateTimeAttribute(default=datetime.utcnow)
    rule = EnumAttribute(EnterpriseResources)
    noverde_unique_field = UnicodeAttribute()

    def __str__(self):
        return (
            f"<Noverde{{cookiecutter.domain_class}}Document("
            f"uuid={self.uuid}, "
            f"rule={self.rule}, "
            f"created={self.created.isoformat()}, "
            f"id={id(self)})>"
        )

    class Meta({{cookiecutter.domain_class}}Document.Meta):
        pass
{% endif %}