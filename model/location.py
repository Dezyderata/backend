from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Location(Base):
    '''
    ORM/Entity storing data about user location details like city, state,
    country and postcode.
    It is extend by street, coordinates and timezone table.
    '''
    __tablename__ = 'location'
    location_id = Column(Integer, primary_key=True)
    city = Column(String(60), nullable=False)
    state = Column(String(40))
    country = Column(String(56), nullable=False)
    postcode = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    street = relationship('Street', uselist=False, back_populates='location')
    coordinates = relationship('Coordinates', uselist=False, back_populates='location')
    timezone = relationship('Timezone', uselist=False, back_populates='location')
