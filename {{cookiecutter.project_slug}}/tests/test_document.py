from uuid import uuid4

import arrow
import pytest
from freezegun import freeze_time
from pynamodb.exceptions import DoesNotExist

from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model
from tests.factories.entities import Noverde{{cookiecutter.domain_class}}DocumentFactory


@pytest.mark.parametrize(
    "model_uuid",
    ["eff8fbede0f04f3985d21f09ea9f1280", "eff8fbede0f04f3985d21f09ea9f1280"],
    ids=["First try", "Same Id again"],
)
def test_save_document(model_uuid):
    with pytest.raises(DoesNotExist):
        Noverde{{cookiecutter.domain_class}}Document.get(hash_key=model_uuid)

    data = {
        "uuid": model_uuid,
        "created": arrow.utcnow().datetime,
        "rule": EnterpriseResources.noverde,
    }
    new_instance = Noverde{{cookiecutter.domain_class}}Document(**data)
    new_instance.save()

    test_instance = Noverde{{cookiecutter.domain_class}}Document.get(hash_key=model_uuid)
    assert test_instance.uuid == model_uuid


def test_create_document():
    """Test create document.

    This test show:
        1. Creating a new NoverdeMydomainDocument using Factory Boy
        2. Using the database session from fixture(dbsession)

    It will run twice to ensure transaction are rollback after each test.
    """
    model_uuid = uuid4().hex
    data = {
        "uuid": model_uuid,
        "created": arrow.utcnow().datetime,
        "rule": EnterpriseResources.noverde,
    }
    NoverdeMydomainDocumentFactory.create(**data)
    # fmt: off
    test_instance = (
            NoverdeMydomainDocumentFactory.uuid == model_uuid
    )
    # fmt: on
    assert test_instance is not None


def test_read_document(noverde_mydomain_document):
    """Test Read Document.

    This test show:
        1. Document generated using Factory Boy.
        2. A simple query using PynamoDB.

    """
    new_instance = NoverdeMydomainDocument.get(hash_key=noverde_mydomain_document.uuid)

    assert new_instance.uuid == noverde_mydomain_document.uuid
    assert new_instance.rule == noverde_mydomain_document.rule
    assert new_instance.created == noverde_mydomain_document.created


@freeze_time("2020-03-30 13:00:00")
def test_fixed_time():
    """Test save document in fixed time.

    This test show:
        1. Save new record with freeze time.
    """
    new_service = NoverdeMydomainDocumentFactory.create()
    assert new_service.created == arrow.utcnow().datetime
    assert new_service.created == arrow.get("2020-03-30 13:00:00").datetime
