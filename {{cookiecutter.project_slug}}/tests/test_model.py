{%- if cookiecutter.database == "RDS" or cookiecutter.database == "Both" -%}
import arrow
import pytest
from freezegun import freeze_time

from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model
from tests.factories.models import Noverde{{cookiecutter.domain_class}}ModelFactory


def test_save_model():
    data = {"noverde_unique_field": "foo"}
    new_instance = Noverde{{cookiecutter.domain_class}}Model(**data)
    assert new_instance.id is None
    new_instance.save()
    assert new_instance.id is not None

    test_instance = Noverde{{cookiecutter.domain_class}}Model.query().filter_by(id=new_instance.id).one()
    assert test_instance.noverde_unique_field == "foo"


@pytest.mark.parametrize(
    "unique_field", ["foo", "bar"], ids=["First insert", "Second insert"]
)
def test_create_model_from_factory(unique_field):
    """Test create model.

    This test show:
        1. Creating a new Noverde{{cookiecutter.domain_class}}Model using Factory Boy
        2. Using the scoped database session from fixture(dbsession)

    It will run twice to ensure transaction are rollback after each test.
    """
    Noverde{{cookiecutter.domain_class}}ModelFactory.create(id=1000, noverde_unique_field=unique_field)
    # fmt: off
    test_instance = (
        Noverde{{cookiecutter.domain_class}}Model.query()
        .filter(Noverde{{cookiecutter.domain_class}}Model.id == 1000)
        .one()
    )
    # fmt: on
    assert test_instance.noverde_unique_field == unique_field


def test_read_model(noverde_{{cookiecutter.domain_slug}}_model):
    """Test Read Model.

    This test show:
        1. Model generated using Factory Boy, via fixture (service_model).
        2. A simple query using SQLAlchemy.

    """
    test_instance = (
        Noverde{{cookiecutter.domain_class}}Model.query()
        .filter(Noverde{{cookiecutter.domain_class}}Model.id == noverde_{{cookiecutter.domain_slug}}_model.id)
        .one()
    )
    assert test_instance == noverde_{{cookiecutter.domain_slug}}_model


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
        .filter(Noverde{{cookiecutter.domain_class}}Model.id == new_service.id)  # noqa: E122
    .one()
    )
    # fmt: on
    assert test_service.created == arrow.get("2020-03-30 13:00:00").datetime
{% endif %}