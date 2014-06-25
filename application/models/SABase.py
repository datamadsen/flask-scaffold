from application import app
from application.helpers import database_helper
from sqlalchemy import Column, Integer, DateTime

session, Base = database_helper.get_session_and_Base(app)


class SABase(object):
    id = Column(Integer)

    def read(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

