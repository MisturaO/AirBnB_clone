#!/usr/bin/python3
"""
This module sets the place attribute
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class sets public attributes that capture a place description
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
