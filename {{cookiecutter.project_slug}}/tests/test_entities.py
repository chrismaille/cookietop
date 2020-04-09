from uuid import uuid4

import arrow
import pytest
from freezegun import freeze_time
from loguru import logger

from enterprise.models.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document
from enterprise.types.enterprise_resources import EnterpriseResources
from tests.factories.entities import Noverde{{cookiecutter.domain_class}}ModelFactory
from tests.factories.entities import Noverde{{cookiecutter.domain_class}}DocumentFactory


def test_create_model():
    """Test create model.

    This test show:
        1. Creating a new Noverde{{cookiecutter.domain_class}}Model using Factory Boy
        2. Using the scoped database session from fixture(dbsession)

    It will run twice to ensure transaction are rollback after each test.
    """
    Noverde{{cookiecutter.domain_class}}ModelFactory.create(id=1)
    # fmt: off
    test_instance = (
        Noverde{{cookiecutter.domain_class}}Model.query()
        .filter(Noverde{{cookiecutter.domain_class}}Model.id == 1)
        .one()
    )
    # fmt: on
    assert test_instance is not None


def test_read_model({{cookiecutter.domain_slug}}_model):
    """Test Read Model.

    This test show:
        1. Model generated using Factory Boy, via fixture (service_model).
        2. A simple query using SQLAlchemy.

    """
    test_instance = (
        Noverde{{cookiecutter.domain_class}}Model.query()
        .filter(Noverde{{cookiecutter.domain_class}}Model.id == {{cookiecutter.domain_slug}}_model.id)
        .one()
    )
    assert test_instance == {{cookiecutter.domain_slug}}_model


@freeze_time("2020-03-30 13:00:00")
def test_fixed_time():
    """Test save model in fixed time.

    This test show:
        1. Save new record with freeze time.
    """
    new_service = Noverde{{cookiecutter.domain_class}}ModelFactory.create()
    assert new_service.created == arrow.utcnow().datetime
    # fmt: off
    test_service = (
        Noverde{{cookiecutter.domain_class}}Model.query()
        .filter(Noverde{{cookiecutter.domain_class}}Model.id == new_service.id)
        .one()
    )
    # fmt: on
    assert test_service.created == arrow.get("2020-03-30 13:00:00").datetime


def test_create_document():
    """Test create document.

    This test show:
        1. Creating a new Noverde{{cookiecutter.domain_class}}Document using Factory Boy
        2. Using the database session from fixture(dbsession)

    It will run twice to ensure transaction are rollback after each test.
    """
    model_uuid = uuid4().hex
    data = {
        "uuid": model_uuid,
        "created": arrow.utcnow().datetime,
        "rule": EnterpriseResources.noverde,
    }
    Noverde{{cookiecutter.domain_class}}DocumentFactory.create(**data)
    # fmt: off
    test_instance = (
        Noverde{{cookiecutter.domain_class}}DocumentFactory.uuid == model_uuid
    )
    # fmt: on
    assert test_instance is not None

def test_read_document({{cookiecutter.domain_slug}}_document):
    """Test Read Document.

    This test show:
        1. Document generated using Factory Boy.
        2. A simple query using PynamoDB.

    """
    new_instance = Noverde{{cookiecutter.domain_class}}Document.get(
        hash_key={{cookiecutter.domain_slug}}_document.uuid)
    logger.debug(new_instance)
    logger.debug({{cookiecutter.domain_slug}}_document)

    assert new_instance.uuid == {{cookiecutter.domain_slug}}_document.uuid
    assert new_instance.rule == {{cookiecutter.domain_slug}}_document.rule
    assert new_instance.created == {{cookiecutter.domain_slug}}_document.created
    logger.debug(type(new_instance))
    logger.debug(type({{cookiecutter.domain_slug}}_document))

    assert new_instance == {{cookiecutter.domain_slug}}_document
