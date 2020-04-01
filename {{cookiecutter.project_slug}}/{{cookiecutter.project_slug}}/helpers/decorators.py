import json
from functools import wraps
from typing import Optional, Type, Any, Dict

from loguru import logger
from marshmallow import Schema, ValidationError
from sentry_sdk import capture_exception  # type: ignore

from helpers.types import HandlerResponse
from helpers.sherlock import Sherlock
from helpers.status_code import StatusCode
from initializers.sql import Session
from aws_lambda_context import LambdaContext


def handler_view(schema: Optional[Type[Schema]] = None) -> Any:
    """Configure Handler View Decorator.

    Handler View middleware. Current workflow is:

        1. Inspect data received from AWS using Sherlock.
        2. Invoke the Handler function passing request object.
        3. Return Handler data, in compatible API Gateway response
        4. Handle Errors

    :param schema: Marshmallow Schema
    :return: Dict
    """

    def config(f: Any) -> Any:
        @wraps(f)
        def wrapper(event: Dict[str, Any], context: LambdaContext, *args, **kwargs):  # type: ignore
            try:
                # Inspect and generate request object.
                sherlock = Sherlock(
                    event_data=event, context_data=context, schema=schema
                )
                request = sherlock.inspect()

                # Call Handler
                args = (request,)
                ret: HandlerResponse = f(*args, **kwargs)

                # Return API Gateway compatible data
                response = {
                    "statusCode": ret.get("status_code", StatusCode.OK).value,
                    "body": json.dumps(ret["message"]),
                }

                # Commit database
                Session.commit()
                return response
            except ValidationError as error:
                # Handle Bad Request Errors
                Session.rollback()
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
                Session.rollback()
                capture_exception(error)
                logger.error(f"Internal Error during request: {error}")
                return {
                    "statusCode": StatusCode.INTERNAL_ERROR.value,
                    "body": json.dumps({"errors": [str(error)]}),
                }
            finally:
                Session.close()

        return wrapper

    return config
