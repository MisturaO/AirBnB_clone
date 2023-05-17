#!/usr/bin/python3
"""
This module tests the state file
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This class contain functions that test the state atributes
    """

    def test_inheritance(self):
        """function tests if the State class inherited from basemodel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_Statebase_attributes(self):
        """function test if State inherited base attributes"""
        st = State()
        self.assertTrue(hasattr(st, 'id'))
        self.assertTrue(hasattr(st, 'created_at'))
        self.assertTrue(hasattr(st, 'updated_at'))

    def test_str_attributes(self):
        """tests if state attribute is of type str"""
        st = State()
        self.assertEqual(type(st.name), str)

    def test_required_attributes(self):
        """test that state has all the required attributes"""
        st = State()
        self.assertTrue(hasattr(st, "name"))
