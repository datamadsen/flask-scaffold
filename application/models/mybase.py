from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer


class MyBase(object):
    """Docstring for MyBase """

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

    def create(self):
        pass

    def read():
        pass

    def update(self):
        pass

    def delete(self):
        pass
