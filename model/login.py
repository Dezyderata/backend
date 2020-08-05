from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Login(Base):
    '''
    ORM/Entity storing data about user login.
    It extending person table.
    '''
    __tablename__ = 'login'
    login_id = Column(Integer, primary_key=True)
    uuid = Column(String(32), nullable=False, unique=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    salt = Column(String(16), nullable=False, unique=True)
    md5 = Column(String(32), nullable=False, unique=True)
    sha1 = Column(String(40), nullable=False, unique=True)
    sha256 = Column(String(64), nullable=False, unique=True)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship('Person', back_populates='login')
