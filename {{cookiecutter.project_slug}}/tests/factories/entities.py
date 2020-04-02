"""Entities Factory.

For more info: https://github.com/FactoryBoy/factory_boy
"""
from datetime import datetime

import arrow
import factory
from factory.alchemy import SESSION_PERSISTENCE_FLUSH, SQLAlchemyModelFactory

from entities import Service
from initializers.sql import Session


def return_now() -> datetime:
    """Return current time.

    To freeze time in Factory
    wrap them using `freeze_time` decorator

    :return: datetime object
    """
    return arrow.utcnow().datetime


class ServiceFactory(SQLAlchemyModelFactory):
    """Service Factory.

    This is a simple example for
    Entity's Factory suitable for tests.

    More Info: https://factoryboy.readthedocs.io/en/latest/orms.html#sqlalchemy
    """

    class Meta:
        """Factory Meta Class."""

        model = Service
        sqlalchemy_session = Session
        sqlalchemy_session_persistence = SESSION_PERSISTENCE_FLUSH

    name = factory.Faker("first_name")
    description = factory.Faker("sentence")
    created = factory.LazyFunction(return_now)
