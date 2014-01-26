from sqlalchemy import Column, Integer, String, DateTime
from application.models import Base


class Foo(Base):
    """Foo for fun."""
    __tablename__ = 'foo'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    created = Column(DateTime(timezone=True))
