from pynamodb_attributes import UUIDAttribute
from helpers.get_uuid import get_uuid
from interface.initializers.nosql import Base
from indexes import {{cookiecutter.model_name_camel}}CreatedIndex


class {{cookiecutter.model_name_camel}}Document(Base, discriminator="{{cookiecutter.model_name_camel}}"):
    """{{cookiecutter.model_name_camel}} Model."""

    uuid = UUIDAttribute(hash_key=True, default=get_uuid)
    created_date_index = {{cookiecutter.model_name_camel}}CreatedIndex()

    class Meta(Base.Meta):
        pass
