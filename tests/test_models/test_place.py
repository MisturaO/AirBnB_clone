#!/usr/bin/python3
"""
This module tests the place file
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    This class contain functions that test the place atributes
    """

    def test_inheritance(self):
        """function tests if the Place class inherited from basemodel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_Placebase_attributes(self):
        """function test if place inherited base attributes"""
        pl = Place()
        self.assertTrue(hasattr(pl, 'id'))
        self.assertTrue(hasattr(pl, 'created_at'))
        self.assertTrue(hasattr(pl, 'updated_at'))

    def test_place_str_attributes(self):
        """tests for the required str attributes"""
        pl = Place()
        self.assertEqual(type(pl.city_id), str)
        self.assertEqual(type(pl.user_id), str)
        self.assertEqual(type(pl.name), str)
        self.assertEqual(type(pl.description), str)

    def test_place_integer_attributes(self):
        """tests for the required integer attributes"""
        pl = Place()
        self.assertEqual(type(pl.number_rooms), int)
        self.assertEqual(type(pl.number_bathrooms), int)
        self.assertEqual(type(pl.max_guest), int)
        self.assertEqual(type(pl.price_by_night), int)

    def test_float_list_attributes(self):
        """tests for the required float and list attributes"""
        pl = Place()
        self.assertEqual(type(pl.latitude), float)
        self.assertEqual(type(pl.longitude), float)
        self.assertEqual(type(pl.amenity_ids), list)

    def test_required_attributes(self):
        """test that place has all the required attributes"""
        pl = Place()
        self.assertTrue(hasattr(pl, "city_id"))
        self.assertTrue(hasattr(pl, "user_id"))
        self.assertTrue(hasattr(pl, "name"))
        self.assertTrue(hasattr(pl, "description"))
        self.assertTrue(hasattr(pl, "number_rooms"))
        self.assertTrue(hasattr(pl, "number_bathrooms"))
        self.assertTrue(hasattr(pl, "max_guest"))
        self.assertTrue(hasattr(pl, "price_by_night"))
        self.assertTrue(hasattr(pl, "latitude"))
        self.assertTrue(hasattr(pl, "longitude"))
        self.assertTrue(hasattr(pl, "amenity_ids"))
