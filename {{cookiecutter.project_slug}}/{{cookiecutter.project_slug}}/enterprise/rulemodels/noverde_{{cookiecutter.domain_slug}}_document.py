{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute

from enterprise.models.{{cookiecutter.domain_slug}}_document import (
    {{cookiecutter.domain_class}}CreatedIndex,
    {{cookiecutter.domain_class}}Document,
    {{cookiecutter.domain_class}}RuleIndex,
)
from enterprise.rules.noverde_mixin import NoverdeMixin


class Noverde{{cookiecutter.domain_class}}Document(NoverdeMixin, {{cookiecutter.domain_class}}Document):
    """Noverde{{cookiecutter.domain_class}}Model.

    This class will join:
    * Noverde enterprise rules (NoverdeMixin)
    * Noverde {{cookiecutter.domain}} Document (from PynamoDB model)

    Usage:
        - For save or update a record, use instance.save() (will validate first)
        - For validation use instance.validate()

    """

    noverde_unique_field = UnicodeAttribute()

    def __str__(self):
        return (
            f"<Noverde{{cookiecutter.domain_class}}Document("
            f"uuid={self.uuid}, "
            f"rule={self.rule}, "
            f"created={self.created.isoformat() if self.created else '-'}, "
            f"id={id(self)})>"
        )

    class Meta({{cookiecutter.domain_class}}Document.Meta):
        pass
{% endif %}