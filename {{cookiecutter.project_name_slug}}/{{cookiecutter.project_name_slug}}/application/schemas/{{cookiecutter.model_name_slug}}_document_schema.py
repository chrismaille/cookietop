from marshmallow_pynamodb import ModelSchema

from enterprise.models.{{cookiecutter.model_name_slug}}_document import {{cookiecutter.model_name_camel}}Document


class {{cookiecutter.model_name_camel}}DocumentSchema(ModelSchema):
    class Meta:
        model = {{cookiecutter.model_name_camel}}Document
        inherit_field_models = True
