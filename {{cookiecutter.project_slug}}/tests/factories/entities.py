"""Entities Factory.

For more info: https://github.com/FactoryBoy/factory_boy
"""
from datetime import datetime

import arrow
import factory
from factory.alchemy import SESSION_PERSISTENCE_FLUSH, SQLAlchemyModelFactory

from enterprise.types.enterprise_resources import EnterpriseResources
from enterprise.models.noverde_{{cookiecutter.domain_slug}}_model import Noverde{{cookiecutter.domain_class}}Model
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

    created = factory.LazyFunction(return_now)
    rule = EnterpriseResources.noverde
