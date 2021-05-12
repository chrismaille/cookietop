import uuid

import arrow
import pytest
from pynamodb.exceptions import DoesNotExist

from models import {{cookiecutter.model_name_camel}}Document


@pytest.mark.parametrize(
    "model_uuid",
    ["e98857bc-15d9-4932-8b60-a788da8d53f4", "e98857bc-15d9-4932-8b60-a788da8d53f4"],
    ids=["First try", "Same Id again"],
)
def test_save_document(model_uuid):
    with pytest.raises(DoesNotExist):
        {{cookiecutter.model_name_camel}}Document.get(hash_key=model_uuid)

    data = {
        "uuid": uuid.UUID(model_uuid),
    }
    new_instance = {{cookiecutter.model_name_camel}}Document(**data)
    new_instance.save()

    test_instance = {{cookiecutter.model_name_camel}}Document.get(hash_key=model_uuid)
    assert test_instance.uuid == uuid.UUID(model_uuid)


def test_read_document({{cookiecutter.model_name_slug}}_document):
    """Test Read Document.

    This test show:
        1. Document generated using Factory Boy.
        2. A simple query using PynamoDB.

    """
    new_instance = {{cookiecutter.model_name_camel}}Document.get(hash_key={{cookiecutter.model_name_slug}}_document.uuid)
    assert new_instance.uuid == {{cookiecutter.model_name_slug}}_document.uuid
    assert new_instance == {{cookiecutter.model_name_slug}}_document


@pytest.mark.freeze_time("2020-03-30 13:00:00")
def test_fixed_time(new_{{cookiecutter.model_name_slug}}_document_data):
    """Test save document in fixed time.

    This test show:
        1. Save new record with freeze time.
    """
    new_service = {{cookiecutter.model_name_camel}}Document(**new_{{cookiecutter.model_name_slug}}_document_data)
    assert new_service.created_at == arrow.utcnow().datetime
    assert new_service.created_at == arrow.get("2020-03-30 13:00:00").datetime
