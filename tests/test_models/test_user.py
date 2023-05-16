#!/usr/bin/python3
"""
This module tests the user file
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This class contain functions that test the user atributes
    """

    def test_inheritance(self):
        """function tests if the user class inherited from basemodel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_Userbase_attributes(self):
        """function test if User inherited base attributes"""
        usr = User()
        self.assertTrue(hasattr(usr, 'id'))
        self.assertTrue(hasattr(usr, 'created_at'))
        self.assertTrue(hasattr(usr, 'updated_at'))

    def test_str_attributes(self):
        """tests if user attributes is of type str"""
        usr = User()
        self.assertEqual(type(usr.email), str)
        self.assertEqual(type(usr.password), str)
        self.assertEqual(type(usr.first_name), str)
        self.assertEqual(type(usr.last_name), str)

    def test_required_attributes(self):
        """test that user has all the required attributes"""
        usr = User()
        self.assertTrue(hasattr(usr, "email"))
        self.assertTrue(hasattr(usr, "password"))
        self.assertTrue(hasattr(usr, "first_name"))
        self.assertTrue(hasattr(usr, "last_name"))
