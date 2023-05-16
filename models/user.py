#@/usr/bin/python3
"""
This module sets the user attributes. it inherits from the BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class sets the following public attributes for the user. The attributes
    are strings.

    The FileStorage class will be updated to mange the serialization and
    deserialization of User
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
