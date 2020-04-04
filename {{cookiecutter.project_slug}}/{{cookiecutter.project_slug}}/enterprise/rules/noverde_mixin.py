from stela import settings

from enterprise.rules.base import EnterpriseRules
from enterprise.rules.exceptions import NoverdeRuleValidationErrors
from enterprise.types.enterprise_resources import EnterpriseResources


class NoverdeMixin(EnterpriseRules):
    """Noverde Rules Mixin.

    This class contain all
    Enterprise Rules for Noverde.

    This Mixin is meant to be used with
    {{cookiecutter.domain_class}}Model together.

    """

    def check_if_is_noverde(self):
        """Check if instance rule is noverde.

        :return: None
        :raise: NoverdeRuleValidationErrors
        """
        if self.rule != EnterpriseResources.noverde:
            raise NoverdeRuleValidationErrors(
                f"{{cookiecutter.domain_class}} {self.id} is not from Noverde."
            )

    def check_if_active(self):
        """Check if domain is active.

        :return: None
        :raise: NoverdeRuleValidationErrors
        """
        if not bool(settings["noverde.{{cookiecutter.domain_slug}}.settings.active"]):
            raise NoverdeRuleValidationErrors("Domain not available")

    def validate(self) -> bool:
        """Validate Noverde Rules.

        This is a simple example. This
        method must run all rules,
        based on Model attributes

        :return: Boolean
        """
        self.check_if_is_noverde()
        self.check_if_active()
        return True
