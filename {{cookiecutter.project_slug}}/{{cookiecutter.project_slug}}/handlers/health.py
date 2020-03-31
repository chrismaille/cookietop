from stela import settings

from helpers.decorators import handler_view
from helpers.status_code import StatusCode
from helpers.types import HandlerResponse


@handler_view()
def health_check() -> HandlerResponse:
    """Return application's health status.

    This is a very simple example for a GET request.
    All request validation occurs in `handler_view` logic
    before call this decorated function.

    Response must be a Dictionary compatible
    with HandlerResponse TypedDict.

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
