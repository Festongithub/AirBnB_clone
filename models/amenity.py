#!/usr/bin/python3

"""Models the amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """creates the instance of amenity"""
        super().__init__(*args, **kwargs)
