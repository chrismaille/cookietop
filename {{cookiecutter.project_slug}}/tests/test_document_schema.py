{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
from application.schemas.noverde_{{cookiecutter.domain_slug}}_document_schema import (
    Noverde{{cookiecutter.domain_class}}DocumentSchema,
)
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


def test_create_document_from_schema(new_{{cookiecutter.domain_slug}}_document_data):

    test_document = Noverde{{cookiecutter.domain_class}}DocumentSchema().load(new_{{cookiecutter.domain_slug}}_document_data)
    assert isinstance(test_document, Noverde{{cookiecutter.domain_class}}Document) is True
{% endif %}