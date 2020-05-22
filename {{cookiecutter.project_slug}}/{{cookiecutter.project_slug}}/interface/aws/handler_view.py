# fmt: off
# flake8: noqa
import json
from functools import wraps
from typing import Optional, Type, Any, Dict

from loguru import logger
from marshmallow import Schema, ValidationError
from sentry_sdk import capture_exception  # type: ignore

from aws_lambda_context import LambdaContext
from stela import settings

from enterprise.rules.exceptions import EnterpriseValidationErrors
from interface.aws.sherlock import Sherlock
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse
from interface.initializers.log import initialize_log
from interface.initializers.sentry import initialize_sentry
{% if cookiecutter.database == "RDS" or cookiecutter.database == "Both" %}
from interface.initializers.sql import Session
from sqlalchemy.orm.exc import NoResultFound
{% endif %}
{% if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" %}
from pynamodb.exceptions import DoesNotExist
{% endif %}
# When running on AWS
# this code will be invoked once
# per handler
initialize_sentry()
initialize_log()


def handler_view(
    schema: Optional[Type[Schema]] = None,
    format_response: bool = True
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
        def wrapper(event: Dict[str, Any], context: LambdaContext, *args, **kwargs):  # type: ignore
            headers = {
                "Access-Control-Allow-Origin": settings["cors.allow_origin"]
            }
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
                        "body": json.dumps(ret["message"], default=lambda x: str(x)),
                        "headers": headers,
                    }
                else:
                    response = ret

                return response
            except ValidationError as error:
                # Handle Bad Request Errors
                logger.error(f"Validation Error during request: {error.messages}")
                {% if cookiecutter.database == "RDS" or cookiecutter.database == "Both" %}
                Session.rollback()
                {% endif %}
                error_list = [
                    f"{field_key}: {description}"
                    for field_key in error.messages
                    for description in error.messages[field_key]
                ]
                return {
                    "statusCode": StatusCode.BAD_REQUEST.value,
                    "body": json.dumps({"errors": error_list}, default=lambda x: str(x)),
                    "headers": headers,
                }
            {% if cookiecutter.database == "DynamoDB (recommended)" %}
            except DoesNotExist as error:
                return {
                    "statusCode": StatusCode.NOT_FOUND.value,
                    "body": json.dumps({"errors": [f"{error}"]}),
                    "headers": headers,
                }
            {% endif %}
            {% if cookiecutter.database == "RDS" %}
            except NoResultFound as error:
                return {
                    "statusCode": StatusCode.NOT_FOUND.value,
                    "body": json.dumps({"errors": [f"{error}"]}, default=lambda x: str(x)),
                    "headers": headers,
                }
            {% endif %}
            except EnterpriseValidationErrors as error:
                # Handle Enterprise Rules Validation Errors.
                capture_exception(error)
                {% if cookiecutter.database == "RDS" or cookiecutter.database == "Both" %}
                Session.rollback()
                {% endif %}
                logger.error(f"Rules Validation Error during request: {error}")
                return {
                    "statusCode": StatusCode.BAD_REQUEST.value,
                    "body": json.dumps({"errors": [f"{error}"]}, default=lambda x: str(x)),
                    "headers": headers,
                }
            except Exception as error:
                # Handle Internal Server Errors
                capture_exception(error)
                {% if cookiecutter.database == "RDS" or cookiecutter.database == "Both" %}
                Session.rollback()
                {% endif %}
                logger.error(f"Internal Error during request: {error}")
                return {
                    "statusCode": StatusCode.INTERNAL_ERROR.value,
                    "body": json.dumps({"errors": [str(error)]}, default=lambda x: str(x)),
                    "headers": headers,
                }
{% if cookiecutter.database == "RDS" or cookiecutter.database == "Both" %}
            finally:
                Session.close()
{% endif %}
        return wrapper

    return config
# fmt: on
