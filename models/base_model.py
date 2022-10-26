#!/usr/bin/python3
"""A Base class for all models."""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import models


Base = declarative_base()


class BaseModel:
    """A base class for all models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if id not in kwargs:
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

        if "updated_at" not in kwargs:
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
        if "__class__" in kwargs:
            del kwargs['__class__']

        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the object"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Converts object into a dictionary"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """Deletes instance"""
        models.storage.delete(self)