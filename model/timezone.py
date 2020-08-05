from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Timezone(Base):
    '''
    ORM/Entity extending location table and storing data concerning timezone.
    '''
    __tablename__ = 'timezone'
    timezone_id = Column(Integer, primary_key=True)
    offset = Column(String(8))
    description = Column(String(100))
    location_id = Column(Integer, ForeignKey('location.location_id'))
    location = relationship('Location', back_populates='timezone')
