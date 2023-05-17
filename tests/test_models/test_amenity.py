#!/usr/bin/python3
"""
This module tests the amenity file
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This class contain functions that test the amenity atributes
    """

    def test_inheritance(self):
        """function tests if the Amenity class inherited from basemodel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_Amenitybase_attributes(self):
        """function test if Amenity inherited base attributes"""
        amty = Amenity()
        self.assertTrue(hasattr(amty, 'id'))
        self.assertTrue(hasattr(amty, 'created_at'))
        self.assertTrue(hasattr(amty, 'updated_at'))

    def test_str_attributes(self):
        """tests if amenity attribute is of type str"""
        amty = Amenity()
        self.assertEqual(type(amty.name), str)

    def test_required_attributes(self):
        """test that amenity has all the required attributes"""
        amty = Amenity()
        self.assertTrue(hasattr(amty, "name"))
