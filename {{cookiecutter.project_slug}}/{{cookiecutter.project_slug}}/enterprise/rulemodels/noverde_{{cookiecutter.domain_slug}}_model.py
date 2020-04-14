{%- if cookiecutter.database == "RDS" or cookiecutter.database == "Both" -%}
from sqlalchemy import Column, String

from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.models.{{cookiecutter.domain_slug}}_model import {{cookiecutter.domain_class}}Model
from enterprise.rules.noverde_mixin import NoverdeMixin


class Noverde{{cookiecutter.domain_class}}Model(NoverdeMixin, {{cookiecutter.domain_class}}Model):
    """Noverde{{cookiecutter.domain_class}}Model.

    This class will join:
    * Noverde enterprise rules (NoverdeMixin)
    * Noverde {{cookiecutter.domain}} Model (from SQLAlchemy model)

    You can add Noverde unique fields here,
    as per SQLAlchemy Single Table Inheritance rules:
    https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/inheritance.html#single-table-inheritance

    Usage:
        - For save or update a record, use instance.save() (will validate first)
        - For validation use instance.validate()

    """

    __mapper_args__ = {"polymorphic_identity": EnterpriseResources.noverde}
    noverde_unique_field = Column(String)
{% endif %}