from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, ENUM

from enterprise.helpers.get_uuid import get_uuid
from enterprise.types.enterprise_resources import EnterpriseResources
from interface.initializers.sql import Base, Session


class {{cookiecutter.domain_class}}Model(Base):
    __tablename__ = "{{cookiecutter.domain_slug}}_model"

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(UUID, nullable=False, unique=True, default=get_uuid)
    created = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    rule = sa.Column(ENUM(EnterpriseResources), nullable=False)

    def __str__(self):
        return (
            f"<{{cookiecutter.domain_class}}Model(id={self.id}, "
            f"uuid={self.uuid}, "
            f"rule={self.rule}, "
            f"created={self.created.isoformat()})>, "
            f"id={id(self)})>"
        )
