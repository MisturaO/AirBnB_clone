#!/usr/bin/python3
"""
This module contains the base class for the Airbnb console project
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    class defines all common attributes/methods for other classes. contains

    public instance attributes
    public instance methods
    """

    def __init__(self, *args, **kwargs):
        """function initializes the public instance attributes

        params: args is not used. if a dict is passed using the kwargs
        argument, an id is assigned, and time which instance is created is
        set as a datetime object. if dict contains a key called __class__,
        it is removed.

        if a new instance that is not from dict is created,
        the instance is stored as a new object
        """

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if "created_at" in kwargs:
                    kwargs["created_at"] = datetime.now()
                if "updated_at" in kwargs:
                    kwargs["updated_at"] = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """function prints the class name, id and dict"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """function updates the updated_at with the current datetime at which
        an instance is created, and the updated time is saved in storage

        note: The save() function is in the FileStorage class, but storage is
        is a variable that calls the filestorage class. consult
        models/__init__.py
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """function returns a dictionary containing all keys/values of
        __dict__ of the instance.

        The times are converted to string in the format: year-month-day,
        Hours:Minutes:Seconds.microseconds.
        The class name is assigned to a key called __class__
        """

        my_dict = self.__dict__.copy()
        timestr1 = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        timestr2 = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        my_dict["created_at"] = timestr1
        my_dict["updated_at"] = timestr2
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
