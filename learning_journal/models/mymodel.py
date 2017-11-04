from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    DateTime,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    author = Column(Unicode)
    date = Column(DateTime)
    text = Column(Unicode)


Index('my_index', MyModel.title, unique=True, mysql_length=255)
