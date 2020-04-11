from uuid import uuid4

import arrow

from application.schemas.noverde_{{cookiecutter.domain_slug}}_document_schema import (
    Noverde{{cookiecutter.domain_class}}DocumentSchema,
)
from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


def test_create_document_from_schema():

    data = {
        "rule": EnterpriseResources.noverde.value,
        "noverde_unique_field": "foo",
    }

    test_document = Noverde{{cookiecutter.domain_class}}DocumentSchema().load(data)
    assert isinstance(test_document, Noverde{{cookiecutter.domain_class}}Document) is True
