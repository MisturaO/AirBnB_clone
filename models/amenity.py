#!/usr/bin/python3
"""
This module sets the class attribute Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class inherits from the basemodel. it sets the public class
    attribute name. name is an empty string
    """
    name = ''
