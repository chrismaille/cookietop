from typing import Any

from loguru import logger

from application.types.handler_response import HandlerResponse
from application.types.status_code import StatusCode
from interface.aws.handler_view import view
from interface.aws.request import Request
from interface.aws.step_functions import StepMachineService


@view()
def start_machine(request: Request, **kwargs: Any) -> HandlerResponse:
    """Start Step Machine using request payload.

    This is a very simple example.
    Payload received in request POST
    will be used as input for a new
    Step Machine execution.

    :param request: Sherlock Instance
    :param kwargs: Keyword Arguments
    :return: HandlerResponse Dict
    """
    logger.info(f"Receive event: {request.body} for Step Machine")
    machine = StepMachineService()
    machine_response = machine.start_execution(payload=request.body)
    response: HandlerResponse = {
        "status_code": StatusCode.OK,
        "message": {"response": machine_response},
    }
    return response
