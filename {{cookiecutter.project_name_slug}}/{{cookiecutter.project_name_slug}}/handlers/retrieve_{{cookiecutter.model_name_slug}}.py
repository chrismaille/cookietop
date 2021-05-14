from loguru import logger

from interface.aws.handler_view import view
from interface.aws.request import Request
from helpers.status_code import StatusCode
from helpers.handler_response import HandlerResponse
from typing import Any

from models import {{cookiecutter.model_name_camel}}Document

from schemas import {{cookiecutter.model_name_camel}}DocumentSchema


@view()
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
