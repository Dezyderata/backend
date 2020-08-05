from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Id(Base):
    '''
    ORM/Entity extending person table and storing data like name and value.
    '''
    __tablename__ = 'id'
    id_id = Column(Integer, primary_key=True)
    name = Column(Integer)
    value = Column(String(20))
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship('Person', back_populates='id')
