from typing import Dict, Any

import stringcase
from marshmallow import post_dump, pre_load
from marshmallow_pynamodb import ModelSchema

from models import {{cookiecutter.model_name_camel}}Document


class {{cookiecutter.model_name_camel}}DocumentSchema(ModelSchema):
    @pre_load
    def sneak_case_keys(self, in_data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        return {stringcase.snakecase(key): in_data[key] for key in in_data}

    @post_dump
    def camel_case_keys(self, data: Dict[Any, Any], **kwargs: Any) -> Dict[str, Any]:
        return {stringcase.camelcase(key): data.get(key, None) for key in data}

    class Meta:
        model = {{cookiecutter.model_name_camel}}Document
