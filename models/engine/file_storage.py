#!/usr/bin/python3
"""
This module converts dictionary representation to a JSON string, which is a
standard representation of a data structure
"""

import json
from models.base_model import BaseModel
import sys


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

        remember that value is a dictionary.
        since sys.module contains all modules in our program, we call it on
        our file's module, and then extract the names of classes in our
        value dict

        These names are passed as **kwargs to the new() function which
        recreates or forms our __objects dict
        """
        try:
            objts = {}
            with open(self.__file_path, 'r') as f:
                objts = json.load(f)

            for key, value in objts.items():
                theClass = value.pop("__class__")
                objtsAttr = getattr(sys.modules[__name__], theClass)
                self.new(objtsAttr(**value))
        except FileNotFoundError:
            return
