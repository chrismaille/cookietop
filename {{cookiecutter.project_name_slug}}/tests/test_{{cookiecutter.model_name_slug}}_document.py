import json

import arrow
import pytest

from loguru import logger
from enterprise.helpers.get_uuid import get_uuid

from application.handlers.create_{{cookiecutter.model_name_slug}} import create
from application.handlers.retrieve_{{cookiecutter.model_name_slug}} import retrieve
from application.handlers.update_{{cookiecutter.model_name_slug}} import update
from application.handlers.delete_{{cookiecutter.model_name_slug}} import delete
from application.schemas.{{cookiecutter.model_name_slug}}_document_schema import (
    {{cookiecutter.model_name_camel}}DocumentSchema,
)

from enterprise.models.{{cookiecutter.model_name_slug}}_document import {{cookiecutter.model_name_camel}}Document


@pytest.fixture
@pytest.mark.freeze_time("2020-04-12 12:00:01")
def dynamo_document() -> {{cookiecutter.model_name_camel}}Document:
    payload = {
        "created_at": arrow.utcnow().isoformat(),
    }
    instance = {{cookiecutter.model_name_camel}}DocumentSchema().load(payload)
    instance.save()
    return instance


def test_create_{{cookiecutter.model_name_slug}}_document():
    test_uuid = get_uuid(as_string=True)
    payload = {
        "uuid": test_uuid,
    }
    event = {"body": json.dumps(payload)}
    response = create(event, None)
    assert response == {
        "body": {% raw %}f'{{"uuid": "{test_uuid}"}}',{% endraw %}
        "statusCode": 201,
        "headers": {"Access-Control-Allow-Origin": "*"},
    }


@pytest.mark.freeze_time("2020-04-12 12:00:01")
def test_retrieve_{{cookiecutter.model_name_slug}}_document(dynamo_document):
    event = {"pathParameters": {"uuid": dynamo_document.uuid}}
    response = retrieve(event, None)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    logger.debug(body)
    assert body["data"] == {
        "created_at": "2020-04-12T12:00:01+00:00",
        "updated_at": "2020-04-12T12:00:01+00:00",
        "uuid": str(dynamo_document.uuid),
    }


def test_update_{{cookiecutter.model_name_slug}}_document(dynamo_document):
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


def test_delete_{{cookiecutter.model_name_slug}}_document(dynamo_document):
    event = {
        "body": None,
        "pathParameters": {"uuid": dynamo_document.uuid},
    }
    response = delete(event, None)
    assert response == {
        "body": None,
        "statusCode": 204,
        "headers": {"Access-Control-Allow-Origin": "*"},
    }
