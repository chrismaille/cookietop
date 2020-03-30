from typing import Dict, Any

from stela import settings

from helpers.decorators import handler_view
from helpers.status_code import StatusCode


@handler_view()
def health_check() -> Dict[str, Any]:
    """Do the check health status of application.

    :return: Dict
    """
    return {
        "status": "OK",
        "environment": settings.stela_options.current_environment,
        "statusCode": StatusCode.OK,
    }
