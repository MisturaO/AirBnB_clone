#!/usr/bin/python3
"""
This module tests the review file
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This class contain functions that test the Review atributes
    """

    def test_inheritance(self):
        """function tests if the Review class inherited from basemodel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_Reviewbase_attributes(self):
        """function test if review inherited base attributes"""
        rv = Review()
        self.assertTrue(hasattr(rv, 'id'))
        self.assertTrue(hasattr(rv, 'created_at'))
        self.assertTrue(hasattr(rv, 'updated_at'))

    def test_str_attributes(self):
        """tests if Review attribute is of type str"""
        rv = Review()
        self.assertEqual(type(rv.place_id), str)
        self.assertEqual(type(rv.user_id), str)
        self.assertEqual(type(rv.text), str)

    def test_required_attributes(self):
        """test that review has all the required attributes"""
        rv = Review()
        self.assertTrue(hasattr(rv, "place_id"))
        self.assertTrue(hasattr(rv, "user_id"))
        self.assertTrue(hasattr(rv, "text"))
