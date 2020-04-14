import json

import arrow
import cookiecutter
import pytest

from freezegun import freeze_time
from loguru import logger

from application.handlers.create_{{cookiecutter.domain_slug}} import create
from application.handlers.retrieve_{{cookiecutter.domain_slug}} import retrieve
from application.handlers.update_{{cookiecutter.domain_slug}} import update
from application.schemas.noverde_{{cookiecutter.domain_slug}}_document_schema import (
    Noverde{{cookiecutter.domain_class}}DocumentSchema,
)

from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


@pytest.fixture
@freeze_time("2020-04-12 12:00:01")
def dynamo_document() -> Noverde{{cookiecutter.domain_class}}Document:
    payload = {
        "noverde_unique_field": "foo",
        "rule": "noverde",
        "created": arrow.utcnow().isoformat(),
    }
    instance = Noverde{{cookiecutter.domain_class}}DocumentSchema().load(payload)
    instance.save()
    return instance


def test_create_{{cookiecutter.domain_slug}}_document():
    event = {
        "body": json.dumps(
            {
                "uuid": "cd4ab3c099464e52bfa1bc84c1ec3db4",
                "noverde_unique_field": "foo",
                "rule": "noverde",
            }
        )
    }
    response = create(event, None)
    assert response == {
        "body": '{"uuid": "cd4ab3c099464e52bfa1bc84c1ec3db4"}',
        "statusCode": 201,
    }


def test_retrieve_{{cookiecutter.domain_slug}}_document(dynamo_document):
    event = {"pathParameters": {"uuid": dynamo_document.uuid}}
    response = retrieve(event, None)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    logger.debug(body)
    assert body["data"] == {
        "created": "2020-04-12T12:00:01+00:00",
        "noverde_unique_field": "foo",
        "rule": "noverde",
        "uuid": dynamo_document.uuid,
    }


def test_update_{{cookiecutter.domain_slug}}_document(dynamo_document):
    event = {
        "body": json.dumps({"noverde_unique_field": "new data"}),
        "pathParameters": {"uuid": dynamo_document.uuid},
    }
    response = update(event, None)
    assert response == {
        "body": {% raw %}f'{{"uuid": "{dynamo_document.uuid}"}}',{% endraw %}
        "statusCode": 200,
    }
