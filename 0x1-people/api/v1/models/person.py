#!/usr/bin/env python3

"""
User model for ORM mapping
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Person(Base):
    """
    Person Model
    """
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(130), unique=True, nullable=False)

    