# fmt: off
# flake8: noqa
{% if cookiecutter.database != "None" %}
{% if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" %}
from typing import Dict, Type

from marshmallow import Schema

from enterprise.types.enterprise_resources import EnterpriseResources
from application.schemas.noverde_{{cookiecutter.domain_slug}}_document_schema import (
    Noverde{{cookiecutter.domain_class}}DocumentSchema,
)

rule_index: Dict[EnterpriseResources, Type[Schema]] = {
    EnterpriseResources.noverde: Noverde{{cookiecutter.domain_class}}DocumentSchema
}
{% endif %}
{% if cookiecutter.database == "RDS" %}
from typing import Dict, Type

from marshmallow import Schema

from enterprise.types.enterprise_resources import EnterpriseResources

from application.schemas.noverde_{{cookiecutter.domain_slug}}_model_schema import (
    Noverde{{cookiecutter.domain_class}}ModelSchema,
)

rule_index: Dict[EnterpriseResources, Type[Schema]] = {
    EnterpriseResources.noverde: Noverde{{cookiecutter.domain_class}}ModelSchema
}
{%- endif -%}
{%- else -%}
from typing import Dict, Any

rule_index: Dict[Any, Any] = {}
{% endif %}
# fmt: on
