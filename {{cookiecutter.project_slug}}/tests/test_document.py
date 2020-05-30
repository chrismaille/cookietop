{%- if cookiecutter.database == "DynamoDB (recommended)" or cookiecutter.database == "Both" -%}
import uuid

import arrow
import pytest
from pynamodb.exceptions import DoesNotExist

from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document


@pytest.mark.parametrize(
    "model_uuid",
    ["e98857bc-15d9-4932-8b60-a788da8d53f4", "e98857bc-15d9-4932-8b60-a788da8d53f4"],
    ids=["First try", "Same Id again"],
)
def test_save_document(model_uuid):
    with pytest.raises(DoesNotExist):
        Noverde{{cookiecutter.domain_class}}Document.get(hash_key=model_uuid)

    data = {
        "uuid": uuid.UUID(model_uuid),
        "created_at": arrow.utcnow().datetime,
        "rule": EnterpriseResources.noverde,
    }
    new_instance = Noverde{{cookiecutter.domain_class}}Document(**data)
    new_instance.save()

    test_instance = Noverde{{cookiecutter.domain_class}}Document.get(hash_key=model_uuid)
    assert test_instance.uuid == uuid.UUID(model_uuid)


def test_read_document(noverde_{{cookiecutter.domain_slug}}_document):
    """Test Read Document.

    This test show:
        1. Document generated using Factory Boy.
        2. A simple query using PynamoDB.

    """
    new_instance = Noverde{{cookiecutter.domain_class}}Document.get(hash_key=noverde_{{cookiecutter.domain_slug}}_document.uuid)

    assert new_instance.uuid == noverde_{{cookiecutter.domain_slug}}_document.uuid
    assert new_instance.rule == noverde_{{cookiecutter.domain_slug}}_document.rule
    assert new_instance.created_at == noverde_{{cookiecutter.domain_slug}}_document.created_at

    assert new_instance == noverde_{{cookiecutter.domain_slug}}_document


@pytest.mark.freeze_time("2020-03-30 13:00:00")
def test_fixed_time(new_{{cookiecutter.domain_slug}}_document_data):
    """Test save document in fixed time.

    This test show:
        1. Save new record with freeze time.
    """
    new_service = Noverde{{cookiecutter.domain_class}}Document(**new_{{cookiecutter.domain_slug}}_document_data)
    assert new_service.created_at == arrow.utcnow().datetime
    assert new_service.created_at == arrow.get("2020-03-30 13:00:00").datetime
{% endif %}