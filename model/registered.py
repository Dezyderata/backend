from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from base import Base

class Registered(Base):
    '''
    ORM/Entity extending person table and storing data concerning registration.
    '''
    __tablename__ = 'registered'
    registered_id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    age = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship('Person', back_populates='registered')
