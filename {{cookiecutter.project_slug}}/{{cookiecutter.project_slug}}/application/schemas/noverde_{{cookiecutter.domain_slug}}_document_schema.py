{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
from marshmallow_pynamodb import ModelSchema as DocumentSchema

from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


class Noverde{{cookiecutter.domain_class}}DocumentSchema(DocumentSchema):
    class Meta:
        model = Noverde{{cookiecutter.domain_class}}Document
        inherit_field_models = True
{% endif %}