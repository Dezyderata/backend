from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from base import Base

class Coordinates(Base):
    '''
    ORM/Entity extending location table and storing data like latitude and longitude.
    '''
    __tablename__ = 'coordinates'
    coordinates_id = Column(Integer, primary_key=True)
    latitude = Column(String(10))
    longitude = Column(String(10))
    location_id = Column(Integer, ForeignKey('location.location_id'))
    location = relationship('Location', backref=backref('coordinates', uselist=False))

    def __init__(self, latitude, longitude, location):
        self.latitude = latitude
        self.longitude = longitude
        self.location = location
