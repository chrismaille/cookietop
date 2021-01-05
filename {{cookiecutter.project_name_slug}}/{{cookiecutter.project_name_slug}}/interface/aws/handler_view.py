import json
from functools import wraps
from typing import Optional, Type, Any, Dict

from loguru import logger
from marshmallow import Schema, ValidationError
from sentry_sdk import capture_exception  # type: ignore

from aws_lambda_context import LambdaContext
from stela import settings

from enterprise.types.exceptions import EnterpriseValidationErrors
from interface.aws.sherlock import Sherlock
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse
from interface.initializers.sentry import initialize_sentry
from pynamodb.exceptions import DoesNotExist

# When running on AWS
# this code will be invoked once
# per handler
initialize_sentry()


def handler_view(
    schema: Optional[Type[Schema]] = None, format_response: bool = True
) -> Any:
    """Configure Handler View Decorator.

    Handler View middleware. Current workflow is:

        1. Inspect data received from AWS using Sherlock.
        2. Invoke the Handler function passing request object.
        3. Return Handler data, in compatible API Gateway response
        4. Handle Errors

    :param schema: Marshmallow Schema for POST
    :param format_response: Format response before send?
    :return: Dict
    """

    def config(f: Any) -> Any:
        @wraps(f)
        def wrapper(
            event: Dict[str, Any], context: LambdaContext, *args: Any, **kwargs: Any
        ) -> Any:
            headers = {"Access-Control-Allow-Origin": settings["cors.allow_origin"]}
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
                if format_response:
                    response = {
                        "statusCode": ret.get("status_code", StatusCode.OK).value,
                        "body": json.dumps(ret["message"], default=lambda x: str(x))
                        if ret["message"]
                        else None,
                        "headers": headers,
                    }
                else:
                    ret.update({"headers": headers})
                    response = ret

                return response
            except ValidationError as error:
                # Handle Bad Request Errors
                logger.error(f"Validation Error during request: {error.messages}")
                error_list = [
                    f"{field_key}: {description}"
                    for field_key in error.messages
                    for description in error.messages[field_key]  # type: ignore
                ]
                return {
                    "statusCode": StatusCode.BAD_REQUEST.value,
                    "body": json.dumps(
                        {"errors": error_list}, default=lambda x: str(x)
                    ),
                    "headers": headers,
                }
            except DoesNotExist as error:
                return {
                    "statusCode": StatusCode.NOT_FOUND.value,
                    "body": json.dumps({"errors": [f"{error}"]}),
                    "headers": headers,
                }
            except EnterpriseValidationErrors as error:
                # Handle Enterprise Rules Validation Errors.
                capture_exception(error)
                logger.error(f"Rules Validation Error during request: {error}")
                return {
                    "statusCode": StatusCode.BAD_REQUEST.value,
                    "body": json.dumps(
                        {"errors": [f"{error}"]}, default=lambda x: str(x)
                    ),
                    "headers": headers,
                }
            except Exception as error:
                # Handle Internal Server Errors
                capture_exception(error)
                logger.error(f"Internal Error during request: {error}")
                return {
                    "statusCode": StatusCode.INTERNAL_ERROR.value,
                    "body": json.dumps(
                        {"errors": [str(error)]}, default=lambda x: str(x)
                    ),
                    "headers": headers,
                }

        return wrapper

    return config
