import arrow
import pytest
from freezegun import freeze_time

from entities import Service
from tests.factories.entities import ServiceFactory


@pytest.mark.parametrize("description", ["first description", "second description"])
def test_create_model(description):
    """Test create model.

    This test show:
        1. Creating a new "Service" using Factory Boy
        2. Using the scoped database session from fixture(dbsession)

    It will run twice to ensure transaction are rollback after each test.
    """
    ServiceFactory.create(name="test_service", description=description)
    test_service = Service.query().filter(Service.name == "test_service").one()
    assert test_service is not None


def test_read_model(service_model):
    """Test Read Model.

    This test show:
        1. Model generated using Factory Boy, via fixture (service_model).
        2. A simple query using SQLAlchemy.

    """
    test_service = Service.query().filter(Service.name == "fixture_service").one()
    assert test_service == service_model


@freeze_time("2020-03-30 13:00:00")
def test_fixed_time():
    """Test save model in fixed time.

    This test show:
        1. Save new record with freeze time.
    """
    new_service = ServiceFactory.create()
    assert new_service.created == arrow.utcnow().datetime
    test_service = Service.query().filter(Service.id == new_service.id).one()
    assert test_service.created == arrow.get("2020-03-30 13:00:00").datetime
