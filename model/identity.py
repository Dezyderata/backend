from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from base import Base

class Identity(Base):
    '''
    ORM/Entity extending person table and storing identity data like name and value.
    '''
    __tablename__ = 'identity'
    identity_id = Column(Integer, primary_key=True)
    name = Column(Integer)
    value = Column(String(20))
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship('Person', backref=backref('identity', uselist=False))
    
    def __init__(self, name, value, person):
        self.name = name
        self.value = value
        self.person = person
