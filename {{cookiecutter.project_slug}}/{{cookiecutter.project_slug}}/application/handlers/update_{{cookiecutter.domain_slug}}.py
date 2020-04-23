# fmt: off
# flake8: noqa
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
@handler_view()
def update(request: Request) -> HandlerResponse:
    """Update existing {{cookiecutter.domain_class}}.

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(
        f"Data received: {request.body} - "
        f"UUID received: {request.path['uuid']}"
    )
    {% if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" %}
    # Get Record
    current_instance = RuleModelClass.get(hash_key=request.path['uuid'])
    logger.debug(f"Current instance is: {current_instance}")

    # Get Current Data
    current_data = Noverde{{cookiecutter.domain_class}}Schema().dump(current_instance)
    logger.debug(f"Current data is: {current_data}")

    # Validate and Update Data:
    current_data.update(request.body)
    logger.debug(f"New data is: {current_data}")
    instance = Noverde{{cookiecutter.domain_class}}Schema().load(current_data)
    instance.save()
    {%- else -%}
    # Get instance and update data
    current_instance = RuleModelClass.query().filter(uuid=request.path['uuid']).one()
    instance = Noverde{{cookiecutter.domain_class}}Schema().load(request.body, instance=current_instance)
    {% endif%}
    instance.save()

    response: HandlerResponse = {
        "status_code": StatusCode.OK,
        "message": {"uuid": instance.uuid},
    }
    return response
{% else %}
from loguru import logger

from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse


@handler_view()
def update(request: Request) -> HandlerResponse:
    """Update existing {{cookiecutter.domain_class}}.

    TODO: Without databases its up to you
        define how to handle update domain instance

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(f"Data received: {request.original_body}")

    response: HandlerResponse = {
        "status_code": StatusCode.OK,
        "message": {"result": "OK"},
    }
    return response
{% endif %}