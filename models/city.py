#!/usr/bin/python3
"""
This module sets the class attribute city and state id
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class inherits from the basemodel. it sets the public class
    attribute name and state id. both are empty string
    """
    name = ''
    state_id = ''
