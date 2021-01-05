from typing import Dict, Any, Optional

from typing_extensions import TypedDict

from application.types.status_code import StatusCode


class HandlerResponse(TypedDict):
    """Handler Return Dictionary.

    This class represents the Dictionary contract.
    This is similar to Typescript interface for the dict object.
    """

    message: Optional[Dict[Any, Any]]
    status_code: Optional[StatusCode]
