#!/usr/bin/python3

import uuid
from datetime import datetime
import models
"""This module build the BaseModel"""


class BaseModel:
    """Public instance attributes"""

    def __init__(self,  *args, **kwargs):
        """
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current
        datetime when an instance is created
        updated_at: datetime - assign with the current datetime
        when an instance is created and it will be
        updated every time you change your object
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            time_f = "%Y-%m-%dT%H:%M:%S.%f"
            for (key,value) in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, time_f)
                else:
                    self.__dict__[key] = value

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""

        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] =  self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr

    def __str__(self):
        """Prints class name and id"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
