#!/usr/bin/python3
"""
This module converts dictionary representation to a JSON string, which is a
standard representation of a data structure
"""

import json
from models.base_model import BaseModel
from models.user import User
import sys

AppModels = {'BaseModel': BaseModel, 'User': User}


class FileStorage():
    """
    class serializes instances to a JSON file and deserializes JSON file
    to instances

    params: file_path and objects are private class attributes.
    __objects will store all objects by format <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """function returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """function appends in the dict all objects and their id"""

        objName = obj.__class__.__name__
        key = "{}.{}".format(objName, obj.id)
        self.__objects[key] = obj

    def save(self):
        """function serializes __object items to JSON file

        add __object items to existing dictionary using the to_dict() function
        in BaseModel, then make a json file
        """
        objdict = {key: value.to_dict() for key, value in
                   self.__objects.items()}
        with open(self.__file_path, 'w') as jsonfile:
            json.dump(objdict, jsonfile)

    def reload(self):
        """if the json file exists, function deserializes it to __objects
        if file does not exist, nothing should be done, no exception is raised

        When file is loaded, the class of the key is extracted, and if its
        say BaseModel, arguments in the key are passed to this model using
        the **kwargs and this reconstructs our self.__objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                objts = json.load(f)

            for key in objts:
                self.__objects[key] = AppModels[objts[key]['__class__']
                                                ](**objts[key])
        except FileNotFoundError:
            return
