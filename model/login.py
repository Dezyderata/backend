from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from base import Base

class Login(Base):
    '''
    ORM/Entity storing data about user login.
    It extending person table.
    '''
    __tablename__ = 'login'
    login_id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False, unique=True)
    username = Column(String(20), nullable=False) #username not unique 156
    password = Column(String(20), nullable=False)
    salt = Column(String(16), nullable=False, unique=True)
    md5 = Column(String(32), nullable=False, unique=True)
    sha1 = Column(String(40), nullable=False, unique=True)
    sha256 = Column(String(64), nullable=False, unique=True)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship('Person', backref=backref('login', uselist=False))

    def __init__(self, uuid, username, password, salt, md5, sha1, sha256, person):
        self.uuid = uuid
        self.username = username
        self.password = password
        self.salt = salt
        self.md5 = md5
        self.sha1 = sha1
        self.sha256 = sha256
        self.person = person
