#!/usr/bin/python3

"""The module build on user """

from models.base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name  = ""


    def __init__(self, *args, **kwargs):
        """creates instance of user """
        super().__init__(*args, **kwargs)
