from loguru import logger

from interface.aws.handler_view import view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse
from typing import Any

from enterprise.models.{{cookiecutter.model_name_slug}}_document import (
    {{cookiecutter.model_name_camel}}Document,
)


@view()
def delete(request: Request, **kwargs: Any) -> HandlerResponse:
    """Delete {{cookiecutter.model_name_camel}}.

    :param: request: Request instance
    :return: HandlerResponse Dict
    """
    logger.info(f"UUID received: {request.path['uuid']}")

    instance = {{cookiecutter.model_name_camel}}Document.get(hash_key=request.path["uuid"])
    instance.delete()

    response: HandlerResponse = {
        "status_code": StatusCode.DELETED,
        "message": None,
    }
    return response
