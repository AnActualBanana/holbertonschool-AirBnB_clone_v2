#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """Contains amenities class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)