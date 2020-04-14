# fmt: off
{% if cookiecutter.database != "None" %}
from loguru import logger

from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse
{% if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" %}
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import (
    Noverde{{cookiecutter.domain_class}}Document as RuleModelClass,
)
from application.schemas.noverde_{{cookiecutter.domain_slug}}_document_schema import (
    Noverde{{cookiecutter.domain_class}}DocumentSchema as Noverde{{cookiecutter.domain_class}}Schema,
)
{% endif %}
{% if cookiecutter.database == "RDS" %}
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_model import (
    Noverde{{cookiecutter.domain_class}}Model as RuleModelClass
)
from application.schemas.noverde_{{cookiecutter.domain_slug}}_model_schema import (
    Noverde{{cookiecutter.domain_class}}ModelSchema as Noverde{{cookiecutter.domain_class}}Schema,
)

{% endif %}
@handler_view(schema=Noverde{{cookiecutter.domain_class}}Schema)
def create(request: Request) -> HandlerResponse:
    """Create new {{cookiecutter.domain_class}}.

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(f"Data received: {request.original_body}")

    new_instance: RuleModelClass = request.validated_data
    new_instance.save()

    response: HandlerResponse = {
        "status_code": StatusCode.CREATED,
        "message": {"uuid": new_instance.uuid},
    }
    return response
{% else %}
from loguru import logger

from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse


@handler_view()
def create(request: Request) -> HandlerResponse:
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