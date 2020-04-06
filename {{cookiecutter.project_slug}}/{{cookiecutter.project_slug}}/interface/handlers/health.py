from stela import settings

from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from interface.types.status_code import StatusCode
from interface.types.handler_response import HandlerResponse


@handler_view()
def health_check(request: Request) -> HandlerResponse:
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
