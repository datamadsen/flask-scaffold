from sqlalchemy import Column, String
from application.models import Base, MyBase


class Bar(MyBase, Base):
    bar = Column(String(length=50))
