from sqlalchemy import (
    Column,
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

    def to_dict(self):
        """Take all model attributes and render them as a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'augthor': self.author,
            'date': self.date.strftime('%B %d, %Y'),
            'text': self.text
        }
