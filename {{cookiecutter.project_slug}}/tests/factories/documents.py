{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
"""Documents Factory.

For more info: https://github.com/FactoryBoy/factory_boy
"""
from factory import Faker, Factory, LazyFunction

from enterprise.helpers.get_now import get_now
from enterprise.helpers.get_uuid import get_uuid
from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


class Noverde{{cookiecutter.domain_class}}DocumentFactory(Factory):
    """{{cookiecutter.domain_class}}Document Factory.

    This is a simple example for
    Entity's DynamoDB Factory suitable for tests.
    """

    class Meta:
        """Factory DynamoDB Meta Class."""

        model = Noverde{{cookiecutter.domain_class}}Document

    uuid = LazyFunction(get_uuid)
    created = LazyFunction(get_now)
    rule = EnterpriseResources.noverde
    noverde_unique_field = Faker("name")
{% endif %}