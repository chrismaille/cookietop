from loguru import logger

from helpers.exceptions import EnterpriseValidationErrors
from interface.aws.handler_view import view
from interface.aws.request import Request
from helpers.status_code import StatusCode
from helpers.handler_response import HandlerResponse
from typing import Any

from models import {{cookiecutter.model_name_camel}}Document

from schemas import {{cookiecutter.model_name_camel}}DocumentSchema


@view(schema={{cookiecutter.model_name_camel}}DocumentSchema)
def create(request: Request, **kwargs: Any) -> HandlerResponse:
    """Create new {{cookiecutter.model_name_camel}}.

    :param: request: Request instance
    :return: HandlerResponse Dict
    """
    logger.info(f"Data received: {request.original_body}")

    if not request.body:
        raise EnterpriseValidationErrors("Data not found in request body.")

    new_instance: {{cookiecutter.model_name_camel}}Document = request.schema().load(request.body)
    new_instance.save()

    response: HandlerResponse = {
        "status_code": StatusCode.CREATED,
        "message": {"uuid": new_instance.uuid},
    }
    return response
