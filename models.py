"""
Models for CL App
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, backref
from flask.ext.login import UserMixin

#engine = sqlalchemy.create_engine('sqlite:///cl_app.db', echo=False)
engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=False)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(UserMixin, Base):
    __tablename__ = 'users'

    userid = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return '<User %r?' % (self.name)
    

Base.metadata.create_all(engine)
    

