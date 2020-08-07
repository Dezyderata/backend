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
    email = Column(String(256), nullable=False) #email not unique 287 and 621
    phone = Column(String(15))
    cell = Column(String(15))
    nat = Column(String(4))

    def __init__(self, gender, email, phone, cell, nat):
        self.gender = gender
        self.email = email
        self.phone = phone
        self.cell = cell
        self.nat = nat
