from application.schemas.base import BaseSchema
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model
from marshmallow_enum import EnumField

from enterprise.types.enterprise_resources import EnterpriseResources


class Noverde{{cookiecutter.domain_class}}ModelSchema(BaseSchema):

    rule = EnumField(EnterpriseResources, by_value=True, required=True)

    class Meta(BaseSchema.Meta):
        model = Noverde{{cookiecutter.domain_class}}Model
