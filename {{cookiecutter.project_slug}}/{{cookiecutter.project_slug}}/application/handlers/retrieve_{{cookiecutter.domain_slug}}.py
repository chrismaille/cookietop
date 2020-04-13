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
@handler_view()
def retrieve(request: Request) -> HandlerResponse:
    """Retrieve {{cookiecutter.domain_class}}.

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(f"UUID received: {request.path['uuid']}")
    {% if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" %}
    instance = RuleModelClass.get(hash_key=request.path['uuid'])
    {%- else -%}
    instance = RuleModelClass.query().filter(uuid=request.path['uuid']).one()
    {% endif%}
    data = Noverde{{cookiecutter.domain_class}}Schema().dump(instance)

    response: HandlerResponse = {
        "status_code": StatusCode.OK,
        "message": {"data": data},
    }
    return response
{% else %}
from loguru import logger

from interface.aws.handler_view import handler_view
from interface.aws.request import Request
from application.types.status_code import StatusCode
from application.types.handler_response import HandlerResponse

@handler_view()
def retrieve(request: Request) -> HandlerResponse:
    """Retrieve {{cookiecutter.domain_class}}.

    TODO: Without databases its up to you
        define how to handle retrieve domain instance

    :param: request: Sherlock instance
    :return: HandlerResponse Dict
    """
    logger.info(f"UUID received: {request.path['uuid']}")

    response: HandlerResponse = {
        "status_code": StatusCode.OK,
        "message": {"result": "OK"},
    }
    return response
{% endif %}