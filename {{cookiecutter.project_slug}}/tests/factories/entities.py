"""Entities Factory.

For more info: https://github.com/FactoryBoy/factory_boy
"""
from datetime import datetime
import dataclasses

import arrow
from factory import Factory, Faker, LazyFunction
from factory.alchemy import SESSION_PERSISTENCE_FLUSH, SQLAlchemyModelFactory

from enterprise.helpers.get_uuid import get_uuid
from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model
from enterprise.rulemodels.noverde_{{cookiecutter.domain_slug}}_document import Noverde{{cookiecutter.domain_class}}Document
from interface.initializers.sql import Session


def return_now() -> datetime:
    """Return current time.

    To freeze time in Factory
    wrap them using `freeze_time` decorator

    :return: datetime object
    """
    return arrow.utcnow().datetime


class Noverde{{cookiecutter.domain_class}}ModelFactory(SQLAlchemyModelFactory):
    """{{cookiecutter.domain_class}}Model Factory.

    This is a simple example for
    Entity's Factory suitable for tests.

    More Info: https://factoryboy.readthedocs.io/en/latest/orms.html#sqlalchemy
    """

    class Meta:
        """Factory Meta Class."""

        model = Noverde{{cookiecutter.domain_class}}Model
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = SESSION_PERSISTENCE_FLUSH

    created = LazyFunction(return_now)
    rule = EnterpriseResources.noverde


class Noverde{{cookiecutter.domain_class}}DocumentFactory(Factory):
    """{{cookiecutter.domain_class}}Document Factory.

    This is a simple example for
    Entity's DynamoDB Factory suitable for tests.
    """

    class Meta:
        """Factory DynamoDB Meta Class."""

        model = Noverde{{cookiecutter.domain_class}}Document

    uuid = LazyFunction(get_uuid)
    created = LazyFunction(return_now)
    rule = EnterpriseResources.noverde
    noverde_unique_field = Faker("name")
