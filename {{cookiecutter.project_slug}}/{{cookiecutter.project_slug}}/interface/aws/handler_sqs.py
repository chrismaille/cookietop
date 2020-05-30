import json
from functools import wraps
from typing import Optional, Type, Any, Dict

from aws_lambda_context import LambdaContext
from loguru import logger
from marshmallow import Schema
from sentry_sdk import capture_exception  # type: ignore
from stela import settings

from interface.aws.request import Request
from interface.initializers.log import initialize_log
from interface.initializers.sentry import initialize_sentry

# When running on AWS
# this code will be invoked once
# per handler
initialize_sentry()
initialize_log()


def handler_sqs(schema: Optional[Type[Schema]] = None) -> Any:
    """Configure Handler SQS Decorator.

    :param schema: Marshmallow Schema for POST
    :return: Dict
    """

    def config(f: Any) -> Any:
        @wraps(f)
        def wrapper(
            event: Dict[str, Any], context: LambdaContext, *args: Any, **kwargs: Any
        ) -> Any:
            try:
                # Inspect and generate request object.
                if schema:
                    data = schema().load(event)
                else:
                    record_list = [
                        {"body": json.loads(record["body"])}
                        for record in event["Records"]
                    ]
                    data = {"Records": record_list}
                request = Request(
                    validated_data=data, aws_event=event, aws_context=context
                )

                # Call Handler
                args = (request,)
                return f(*args, **kwargs)

            except Exception as error:
                # Handle Internal Server Errors
                capture_exception(error)

                logger.error(f"Internal Error during request: {error}")
                if settings.stela_options.current_environment == "development":
                    raise

        return wrapper

    return config
