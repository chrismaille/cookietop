"""Initialize Database Session.

As per SQLAlchemy API.
Database URL must have this format: postgres://<user>:<password>@<host>:<port>/<name>

You can define the settings "database.sql.url" or
the DATABASE_SQL_URL environment variable.

"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from stela import settings

engine = create_engine(settings["database.sql.url"], echo=settings['database.sql.echo'])
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine, autoflush=True))

db_session = Session()
