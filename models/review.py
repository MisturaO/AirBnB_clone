#!/usr/bin/python3
"""
This module sets the Review attribute
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class sets the attribtes for reviews
    """
    place_id = ''
    user_id = ''
    text = ''
