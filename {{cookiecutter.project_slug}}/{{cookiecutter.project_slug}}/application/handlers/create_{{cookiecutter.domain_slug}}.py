# fmt: off
{% if cookiecutter.database != "None" %}
from loguru import logger

from enterprise.rules.exceptions import EnterpriseValidationErrors
from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse
from typing import Any
{% if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" %}
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import (
    Noverde{{cookiecutter.domain_class}}Document as RuleModelClass,
)
{% endif %}
{% if cookiecutter.database == "RDS" %}
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_model import (
    Noverde{{cookiecutter.domain_class}}Model as RuleModelClass
)

{% endif %}
@handler_view()
def create(request: Request, **kwargs: Any) -> HandlerResponse:
    """Create new {{cookiecutter.domain_class}}.

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(f"Data received: {request.original_body}")

    if not request.validated_data:
        raise EnterpriseValidationErrors("Data not found in request body.")

    new_instance: RuleModelClass = request.validated_data
    new_instance.save()

    response: HandlerResponse = {
        "status_code": StatusCode.CREATED,
        "message": {"uuid": new_instance.uuid},
    }
    return response
{% else %}
from loguru import logger
from typing import Any

from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse


@handler_view()
def create(request: Request, **kwargs: Any) -> HandlerResponse:
    """Create new {{cookiecutter.domain_class}}.

    TODO: Without databases its up to you
        define how to handle create domain instance

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(f"Data received: {request.original_body}")

    response: HandlerResponse = {
        "status_code": StatusCode.CREATED,
        "message": {"result": "OK"},
    }
    return response
{% endif %}