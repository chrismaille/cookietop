{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
import pytest

from enterprise.rules.exceptions import NoverdeEnterpriseValidationErrors
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


def test_rule_model_from_document(noverde_{{cookiecutter.domain_slug}}_document):
    return noverde_{{cookiecutter.domain_slug}}_document.validate() is None


def test_invalid_rule():
    """Test validate in instance with no rule defined."""
    new_instance = Noverde{{cookiecutter.domain_class}}Document()
    new_instance.rule = None
    with pytest.raises(NoverdeEnterpriseValidationErrors):
        new_instance.save()
{% endif %}