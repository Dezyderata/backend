from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from base import Base

class Street(Base):
    '''
    ORM/Entity extending location table and storing street name and number.
    '''
    __tablename__ = 'street'
    street_id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(String(50))
    location_id = Column(Integer, ForeignKey('location.location_id'))
    location = relationship('Location', backref=backref('street', uselist=False))

    def __init__(self, number, name, location):
        self.number = number
        self.name = name
        self.location = location
