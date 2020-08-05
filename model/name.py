from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Name(Base):
    '''
    ORM/Entity extending person table and storing data like title first and last name.
    '''
    __tablename__ = 'name'
    name_id = Column(Integer, primary_key=True)
    title = Column(String(10))
    first = Column(String(32), nullable=False)
    last = Column(String(32), nullable=False)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship('Person', back_populates='name')
