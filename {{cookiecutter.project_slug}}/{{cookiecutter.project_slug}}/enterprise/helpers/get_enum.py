from pynamodb.constants import STRING
from pynamodb.attributes import UnicodeAttribute

from enterprise.types.enterprise_resources import EnterpriseResources


class EnumUnicodeAttribute(UnicodeAttribute):
    """
    An enumerated unicode attribute
    """
    attr_type = STRING

    def serialize(self, value):
        """
        Raises ValueError if input value not in EnterpriseResources.
        Otherwise continues as parent class
        """
        if value not in EnterpriseResources:
            raise ValueError(f"{self.attr_name} must be one of "
                             f"{EnterpriseResources}, not '{value}'")
        else:
            return UnicodeAttribute.serialize(self, value.name)
