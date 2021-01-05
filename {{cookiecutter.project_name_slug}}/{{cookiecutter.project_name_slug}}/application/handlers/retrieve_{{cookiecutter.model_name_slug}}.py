from loguru import logger

from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse
from typing import Any

from enterprise.models.{{cookiecutter.model_name_slug}}_document import (
    {{cookiecutter.model_name_camel}}Document,
)
from application.schemas.{{cookiecutter.model_name_slug}}_document_schema import (
    {{cookiecutter.model_name_camel}}DocumentSchema,
)


@handler_view()
def retrieve(request: Request, **kwargs: Any) -> HandlerResponse:
    """Retrieve {{cookiecutter.model_name_camel}}.

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(f"UUID received: {request.path['uuid']}")

    instance = {{cookiecutter.model_name_camel}}Document.get(hash_key=request.path["uuid"])
    data = {{cookiecutter.model_name_camel}}DocumentSchema().dump(instance)

    response: HandlerResponse = {
        "status_code": StatusCode.OK,
        "message": {"data": data},
    }
    return response
