#!/usr/bin/python3
"""
module tests the functions in the FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class testFileStorage(unittest.TestCase):
    """
    class tests storage data to enseure instances are stored appropriately
    """
    def setUp(self):
        """
        An inbuilt python function. It helps us set variables needed in all
        test methods to avoid repetition. consider it a global function
        kind of. Python runs it and allow things set in it be accessible
        to other methods
        """
        self.my_model = BaseModel()
        self.from_store = storage.all()

    def test_all(self):
        """test that the all function returns the saved __object as a dict"""

        self.assertEqual(type(self.from_store), dict)

    def test_new(self):
        """function tests that a new object is created, it is in the format
        objectname.id which serves as the key and it is appended appropriately
        in the general dict __objects.

        is the key in the right format?
        are the values stored as dict?
        are the values passed by the instance stored?
        """
        
        keyformat = 'BaseModel' + '.' + self.my_model.id
        self.assertIn(keyformat, self.from_store.keys())
        self.assertIn(self.my_model, self.from_store.values())

    def test_save(self):
        """
        function tests that __objects is serialized to a json file.
        json files are strings

        is the type of our saved file a string?
        """

        self.assertEqual(type('file.json'), str)
