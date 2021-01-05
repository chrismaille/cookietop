from functools import wraps
from typing import Type, Any, Dict, Optional

from aws_lambda_context import LambdaContext
from loguru import logger
from marshmallow import Schema
from sentry_sdk import capture_exception  # type: ignore

from interface.aws.request import Request
from interface.initializers.sentry import initialize_sentry

# When running on AWS
# this code will be invoked once
# per handler
initialize_sentry()


def handler_step(schema: Optional[Type[Schema]] = None) -> Any:
    """Configure Handler Step Functions Decorator.

    Every step receives the same Event, if you
    do not return any dict on Handler.

    If you do, we will return to next step your dict.

    :param schema: Marshmallow Schema for Event
    :return: Original or Updated Event
    """

    def config(f: Any) -> Any:
        @wraps(f)
        def wrapper(
            event: Dict[Any, Any], context: LambdaContext, *args: Any, **kwargs: Any
        ) -> Any:
            try:
                logger.debug(f"event is: {event}")
                # Inspect and generate request object.
                data = schema().load(event) if schema else event

                request = Request(
                    validated_data=data, aws_event=event, aws_context=context
                )

                # Call Handler
                args = (request,)
                ret = f(*args, **kwargs)

                return ret if isinstance(ret, dict) else event

            except Exception as error:
                # Handle Internal Server Errors
                capture_exception(error)

                logger.error(f"Internal Error during request: {error}")
                raise

        return wrapper

    return config
