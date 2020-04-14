{%- if cookiecutter.database == "RDS" or cookiecutter.database == "Both" -%}
from enterprise.types.enterprise_resources import EnterpriseResources
from application.schemas.noverde_{{cookiecutter.domain_slug}}_model_schema import Noverde{{cookiecutter.domain_class}}ModelSchema
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model


def test_create_model_from_schema():
    # fmt: off
    test_model = Noverde{{cookiecutter.domain_class}}ModelSchema().load(
        {"rule": EnterpriseResources.noverde}
    )
    # fmt: on
    assert isinstance(test_model, Noverde{{cookiecutter.domain_class}}Model) is True
{% endif %}