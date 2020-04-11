{%- if cookiecutter.database == "RDS" or cookiecutter.database == "Both" -%}
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import event
from sqlalchemy.dialects.postgresql import UUID, ENUM

from enterprise.helpers.get_uuid import get_uuid
from enterprise.types.enterprise_resources import EnterpriseResources
from interface.initializers.sql import Base


class {{cookiecutter.domain_class}}Model(Base):
    __tablename__ = "{{cookiecutter.domain_slug}}_model"

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(UUID, nullable=False, unique=True, default=get_uuid)
    created = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    rule = sa.Column(ENUM(EnterpriseResources), nullable=False)
    __mapper_args__ = {"polymorphic_on": rule}

    def __str__(self):
        return (
            f"<{{cookiecutter.domain_class}}Model(id={self.id}, "
            f"uuid={self.uuid}, "
            f"rule={self.rule}, "
            f"created={self.created.isoformat() if self.created else ''})>, "
            f"id={id(self)})>"
        )


# fmt: off
@event.listens_for({{cookiecutter.domain_class}}Model, 'before_insert')
@event.listens_for({{cookiecutter.domain_class}}Model, 'before_update')
def validate(mapper, connection, target):
    """Validate record before save.

    Always run validate(), even
    if we insert/modify record
    direct using session.commit()
    instead instance.save()
    """
    return target.validate()
# fmt: on
{% endif %}