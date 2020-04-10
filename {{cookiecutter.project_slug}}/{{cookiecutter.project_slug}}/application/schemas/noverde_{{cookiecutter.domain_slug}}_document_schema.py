from marshmallow_enum import EnumField

from application.schemas.base import BaseDocumentSchema
from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


class Noverde{{cookiecutter.domain_class}}DocumentSchema(BaseDocumentSchema):
    rule = EnumField(EnterpriseResources, by_value=True, required=True)

    class Meta:
        fields = ("uuid", "created", "rule")
