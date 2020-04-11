from stela import settings

from enterprise.rules.base import EnterpriseRules
from enterprise.rules.exceptions import NoverdeEnterpriseValidationErrors
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
            raise NoverdeEnterpriseValidationErrors(
                f"{{cookiecutter.domain_class}} {self} is not from Noverde."
            )

    def check_if_active(self):
        """Check if domain is active.

        :return: None
        :raise: NoverdeRuleValidationErrors
        """
        if not bool(settings["noverde.{{cookiecutter.domain_slug}}.settings.active"]):
            raise NoverdeEnterpriseValidationErrors("Domain not available")

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
