from schemas import {{cookiecutter.model_name_camel}}DocumentSchema
from models import {{cookiecutter.model_name_camel}}Document


def test_create_document_from_schema(new_{{cookiecutter.model_name_slug}}_document_data):

    test_document = {{cookiecutter.model_name_camel}}DocumentSchema().load(new_{{cookiecutter.model_name_slug}}_document_data)
    assert isinstance(test_document, {{cookiecutter.model_name_camel}}Document) is True
