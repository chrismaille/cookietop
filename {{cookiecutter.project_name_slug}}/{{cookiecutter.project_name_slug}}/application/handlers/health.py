from typing import Any

from stela import settings

from interface.aws.handler_view import view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse


@view()
def health_check(request: Request, **kwargs: Any) -> HandlerResponse:
    """Return application's health status.

    This is a very simple example for a GET request.
    All request validation occurs in `handler_view` logic
    before call this decorated function.

    The Request object will have all data received from
    AWS event and context arguments.

    Response must be a Dictionary compatible
    with HandlerResponse TypedDict.

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    response = {
        "message": {
            "status": "OK",
            "environment": settings.stela_options.current_environment,
        },
        "status_code": StatusCode.OK,
    }

    return response
