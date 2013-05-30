from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def get_session_and_Base(app):
    """ Get sqlalchemy scoped_session and Base. """
    if not isinstance(app, Flask):
        raise TypeError('app must be a Flask app')

    if not 'DB_URL' in app.config:
        raise KeyError("DB_URL key not found app.config")

    engine = create_engine(app.config['DB_URL'], convert_unicode=True)
    db_session = scoped_session(sessionmaker(
        autocommit=False, autoflush=False, bind=engine))

    Base = declarative_base()
    Base.query = db_session.query_property()

    return db_session, Base
