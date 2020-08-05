from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from base import Base

class Dob(Base):
    '''
    ORM/Entity containing data about user age and birth date.
    '''
    __tablename__ = 'dob'
    dob_id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    age = Column(Integer, nullable=False)
    day_to_birthday = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship('Person', back_populates='login')
