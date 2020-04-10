from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema

from interface.initializers.sql import Session


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = Session


class BaseDocumentSchema(Schema):
    pass