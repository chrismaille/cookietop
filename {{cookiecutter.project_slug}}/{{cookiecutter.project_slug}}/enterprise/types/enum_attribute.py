from enum import Enum
from typing import Any, Type

from pynamodb.attributes import UnicodeAttribute


class EnumAttribute(UnicodeAttribute):
    """Create Enum Unicode Attribute."""

    def __init__(self, *args, **kwargs):
        """Initialize Attribute.

        Will pop Enum attribute.

        :param args: arguments
        :param kwargs: keyword arguments
        """
        self.enum: Type[Enum] = args[0]
        list_args = list(args)
        list_args.pop()

        default = kwargs.get("default")
        if default:
            self.validate_enum(default, self.enum)

        if not list_args:
            super().__init__(**kwargs)
        else:
            super().__init__(*set(list_args), **kwargs)

    @staticmethod
    def validate_enum(value: Any, enum: Type[Enum]) -> None:
        """Validate valid Enum.

        :param enum: Type[Enum]
        :param value: Any
        :return: None
        :raise: ValueError
        """
        if value.__class__ != enum:
            raise ValueError(
                f"Default Value {value.__class__} must be an instance of {enum}"
            )

    def serialize(self, value: Enum) -> UnicodeAttribute:
        """Serialize Enum value.

        :param value: Enum Type
        :return: string
        """
        self.validate_enum(value, self.enum)
        return UnicodeAttribute.serialize(self, value.value)  # type: ignore

    def deserialize(self, value: str) -> Enum:
        """Deserialize enum object.
        
        :param value: string
        :return: Enum
        """
        return self.enum[value]
