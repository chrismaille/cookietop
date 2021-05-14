from loguru import logger

from interface.aws.handler_view import view
from interface.aws.request import Request
from helpers.status_code import StatusCode
from helpers.handler_response import HandlerResponse
from typing import Any

from models import {{cookiecutter.model_name_camel}}Document

from schemas import {{cookiecutter.model_name_camel}}DocumentSchema


@view()
def update(request: Request, **kwargs: Any) -> HandlerResponse:
    """Update existing {{cookiecutter.model_name_camel}}.

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(
        f"Data received: {request.body} - UUID received: {request.path['uuid']}"
    )
    # Get Record
    current_instance = {{cookiecutter.model_name_camel}}Document.get(hash_key=request.path["uuid"])
    logger.debug(f"Current instance is: {current_instance}")
    current_data = {{cookiecutter.model_name_camel}}DocumentSchema().dump(current_instance)
    logger.debug(f"Current data is: {current_data}")

    # Update Data:
    current_data.update(request.body)
    instance = {{cookiecutter.model_name_camel}}DocumentSchema().load(current_data)
    instance.save()
    logger.debug(f"New data is: {instance}")

    response: HandlerResponse = {
        "status_code": StatusCode.OK,
        "message": {"uuid": instance.uuid},
    }
    return response
