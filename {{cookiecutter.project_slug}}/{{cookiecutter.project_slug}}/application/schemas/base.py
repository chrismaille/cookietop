from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


from interface.initializers.sql import Session


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = Session
        include_relationships = True
        load_instance = True
