import pytest

from enterprise.rules.exceptions import NoverdeRuleValidationErrors
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model


def test_rule_model({{cookiecutter.domain_slug}}_model):
    return {{cookiecutter.domain_slug}}_model.validate() is None


def test_invalid_rule():
    """Test validate in instance with no rule defined."""
    new_instance = Noverde{{cookiecutter.domain_class}}Model()
    with pytest.raises(NoverdeRuleValidationErrors):
        new_instance.validate()
