from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Person(Base):
    '''
    Main ORM/Entity for person details. It contains data gender,
    email, phon cell and nationality fields, and is extended by name,
    location, login dob, registered and identity table.
    '''
    __tablename__ = 'person'
    person_id = Column(Integer, primary_key=True)
    gender = Column(String(10))
    email = Column(String(256), nullable=False)
    phone = Column(String(15))
    cell = Column(String(15))
    nat = Column(String(4))
    name = relationship('Name', uselist=False, back_populates='person')
    location = relationship('Location', backref='person')
    login = relationship('Login', uselist=False, back_populates='person')
    dob = relationship('Dob', uselist=False, back_populates='person')
    registered = relationship('Registered', uselist=False, back_populates='person')
    identity = relationship('Identity', uselist=False, back_populates='person')
