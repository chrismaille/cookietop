import json

import arrow
import pytest

from loguru import logger
from enterprise.helpers.get_uuid import get_uuid

from application.handlers.create_{{cookiecutter.domain_slug}} import create
from application.handlers.retrieve_{{cookiecutter.domain_slug}} import retrieve
from application.handlers.update_{{cookiecutter.domain_slug}} import update
from application.schemas.noverde_{{cookiecutter.domain_slug}}_document_schema import (
    Noverde{{cookiecutter.domain_class}}DocumentSchema,
)

from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


@pytest.fixture
@pytest.mark.freeze_time("2020-04-12 12:00:01")
def dynamo_document() -> Noverde{{cookiecutter.domain_class}}Document:
    payload = {
        "rule": "noverde",
        "created_at": arrow.utcnow().isoformat(),
    }
    instance = Noverde{{cookiecutter.domain_class}}DocumentSchema().load(payload)
    instance.save()
    return instance


def test_create_{{cookiecutter.domain_slug}}_document():
    test_uuid = get_uuid(as_string=True)
    payload = {
        "uuid": test_uuid,
        "rule": "noverde",
    }
    event = {"body": json.dumps(payload)}
    response = create(event, None)
    assert response == {
        "body": {% raw %}f'{{"uuid": "{test_uuid}"}}',{% endraw %}
        "statusCode": 201,
        "headers": {"Access-Control-Allow-Origin": "*"},
    }


@pytest.mark.freeze_time("2020-04-12 12:00:01")
def test_retrieve_{{cookiecutter.domain_slug}}_document(dynamo_document):
    event = {"pathParameters": {"uuid": dynamo_document.uuid}}
    response = retrieve(event, None)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    logger.debug(body)
    assert body["data"] == {
        "created_at": "2020-04-12T12:00:01+00:00",
        "updated_at": "2020-04-12T12:00:01+00:00",
        "rule": "noverde",
        "uuid": str(dynamo_document.uuid),
    }


def test_update_{{cookiecutter.domain_slug}}_document(dynamo_document):
    event = {
        "body": json.dumps({"updated_at": "2020-04-12T12:00:01+00:00"}),
        "pathParameters": {"uuid": dynamo_document.uuid},
    }
    response = update(event, None)
    assert response == {
        "body": {% raw %}f'{{"uuid": "{dynamo_document.uuid}"}}',{% endraw %}
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
    }
