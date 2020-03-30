import json
from functools import wraps
from typing import Optional, Type

from loguru import logger
from marshmallow import Schema, ValidationError
from sentry_sdk import capture_exception

from helpers.sherlock import Sherlock
from helpers.status_code import StatusCode


def handler_view(model_schema: Optional[Type[Schema]] = None) -> None:
    """Configure Handler View Decorator.

    Handler View middleware. Current workflow is:

        1. Get json data from event["body"] if exists
        2. Deserialize data using Sherlock.
        3. Invoke the Handler function passing validated_data, if exists.
        4. Return Handler data, in compatible API Gateway response
        5. Handle Errors

    :param model_schema: Marshmallow Schema
    :return: Dict
    """

    def config(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                # Get Body data
                event_data = args[0]
                sherlock = Sherlock(
                    event_data=event_data, schema=model_schema
                ).inspect()
                kwargs["validated_data"] = sherlock.validated_data

                # Call Handler
                ret = f(*args, **kwargs)

                # Return API Gateway compatible data
                return {
                    "statusCode": ret.get("statusCode", StatusCode.OK).value,
                    "body": json.dumps(ret["body"]),
                }
            except ValidationError as error:
                # Handle Bad Request Errors
                logger.error(f"Validation Error during request: {error.messages}")
                error_list = [
                    f"{field_key}: {description}"
                    for field_key in error.messages
                    for description in error.messages[field_key]
                ]
                return {
                    "statusCode": StatusCode.BAD_REQUEST.value,
                    "body": json.dumps({"errors": error_list}),
                }
            except Exception as error:
                # Handle Internal Server Errors
                capture_exception(error)
                logger.error(f"Internal Error during request: {error}")
                return {
                    "statusCode": StatusCode.INTERNAL_ERROR.value,
                    "body": json.dumps({"error": [str(error)]}),
                }

        return wrapper

    return config
