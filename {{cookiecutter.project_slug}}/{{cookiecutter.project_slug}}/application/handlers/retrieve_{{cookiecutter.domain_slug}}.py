from loguru import logger

from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse


@handler_view()
def retrieve(request: Request) -> HandlerResponse:
    """Retrieve {{cookiecutter.domain_class}}.

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(f"Data received: {request.original_body}")

    response: HandlerResponse = {
        "status_code": StatusCode.OK,
        "message": {"result": "OK"},
    }
    return response
