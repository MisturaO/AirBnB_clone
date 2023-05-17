#!/usr/bin/python3
"""
This module tests the city file
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This class contain functions that test the city atributes
    """

    def test_inheritance(self):
        """function tests if the City class inherited from basemodel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_Statebase_attributes(self):
        """function test if City inherited base attributes"""
        cty = City()
        self.assertTrue(hasattr(cty, 'id'))
        self.assertTrue(hasattr(cty, 'created_at'))
        self.assertTrue(hasattr(cty, 'updated_at'))

    def test_str_attributes(self):
        """tests if city attribute is of type str"""
        cty = City()
        self.assertEqual(type(cty.name), str)
        self.assertEqual(type(cty.state_id), str)

    def test_required_attributes(self):
        """test that cty has all the required attributes"""
        cty = City()
        self.assertTrue(hasattr(cty, "name"))
        self.assertTrue(hasattr(cty, "state_id"))
