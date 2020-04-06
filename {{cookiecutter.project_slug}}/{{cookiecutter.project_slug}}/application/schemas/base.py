from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from interface.initializers.sql import Session


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = Session
