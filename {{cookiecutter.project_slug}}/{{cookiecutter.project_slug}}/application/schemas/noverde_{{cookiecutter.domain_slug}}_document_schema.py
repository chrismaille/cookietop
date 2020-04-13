{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
from marshmallow import fields, post_load
from marshmallow_enum import EnumField
from marshmallow_pynamodb import ModelSchema as DocumentSchema

from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


class Noverde{{cookiecutter.domain_class}}DocumentSchema(DocumentSchema):
    rule = EnumField(EnterpriseResources, by_value=True, required=True)
    uuid = fields.UUID()
    created = fields.DateTime()

    @post_load
    def hydrate_pynamo_model(self, data, **kwargs):
        """Hydrate PynamoDB Model."""
        if data.get("uuid"):
            data["uuid"] = data["uuid"].hex
        return super().hydrate_pynamo_model(data, **kwargs)

    class Meta:
        model = Noverde{{cookiecutter.domain_class}}Document
{% endif %}