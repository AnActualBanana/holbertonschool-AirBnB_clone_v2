#!/usr/bin/python3
"""Module for file storage management"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Manages file storage for HBNB"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates into storage"""
        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'
                                      .format(dialect, driver, user, passwd,
                                              host, db), pool_pre_ping=True)
        env = os.getenv("HBNB_ENV")
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query for all objects in current session"""

        classes = {City, State, User, Place, Amenity, Review}

        dictionary = {}
        if cls in classes:
            dict = self.__session.query(cls).all()
            for element in dict:
                key = element.__class__.__name__ + '.' + element.id
                dictionary[key] = element
        elif cls is None:
            dict = []
            for cls in classes:
                dict += self.__session.query(cls).all()
            for element in dict:
                key = element.__class__.__name__ + '.' + element.id
                dictionary[key] = element

        return dictionary

    def new(self, obj):
        """adds new object to database"""
        self.__session.add(obj)

    def save(self):
        """saves changes to session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes specified object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))

    def close(self):
        """closes session"""
        self.__session.remove()