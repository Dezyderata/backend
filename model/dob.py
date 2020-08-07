from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from base import Base

class Dob(Base):
    '''
    ORM/Entity containing data about user age and birth date.
    '''
    __tablename__ = 'dob'
    dob_id = Column(Integer, primary_key=True)
    date = Column(String(24), nullable=False)
    age = Column(Integer, nullable=False)
    days_to_birthday = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship('Person', backref=backref('dob', uselist=False))

    def __init__(self, date, age, days_to_birthday, person):
        self.date = date
        self.age = age
        self.days_to_birthday = days_to_birthday
        self.person = person
