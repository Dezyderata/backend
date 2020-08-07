from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from base import Base

class Registered(Base):
    '''
    ORM/Entity extending person table and storing data concerning registration.
    '''
    __tablename__ = 'registered'
    registered_id = Column(Integer, primary_key=True)
    date = Column(String(24), nullable=False)
    age = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship('Person', backref=backref('registered', uselist=False))

    def __init__(self, date, age, person):
        self.date = date
        self.age = age
        self.person = person
