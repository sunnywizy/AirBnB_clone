#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """
    class User that handle users information
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
