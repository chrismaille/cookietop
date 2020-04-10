from uuid import uuid4

import arrow
from loguru import logger

from application.schemas.noverde_{{cookiecutter.domain_slug}}_document_schema import Noverde{{cookiecutter.domain_class}}DocumentSchema
from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


def test_create_document_from_schema():
    # fmt: off
    data = {
        "uuid": uuid4().hex,
        "created": arrow.utcnow().datetime,
        "rule": EnterpriseResources.noverde,
    }

    test_document = Noverde{{cookiecutter.domain_class}}DocumentSchema().load(data)
    # fmt: on
    # assert isinstance(test_document, Noverde{{cookiecutter.domain_class}}Document) is True
