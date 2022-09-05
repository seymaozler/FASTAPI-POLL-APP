from cgitb import text
import email
from email.policy import default
from enum import unique
import imp
from turtle import title
from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import null
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP



class Poll(Base):
    __tablename__ = 'poll'

    id = Column(Integer, primary_key = True, nullable=False)
    title = Column(String, nullable= True)
    content = Column(String, nullable = True)
    


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True, nullable = False)
    email = Column(String, nullable = True)
    password = Column(String, nullable = True)
