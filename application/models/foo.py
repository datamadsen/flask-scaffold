from sqlalchemy import Column, Integer, String
from application.models import Base


class Foo(Base):
    """Foo for fun."""
    __tablename__ = 'foo'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
