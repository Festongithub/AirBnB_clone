#!/usr/bin/python3

"""This module models the state"""

from models.base_model import BaseModel


class State(BaseModel):
    """Create state class
    name: string - empty string """

    name = ""

    def __init__(self, *args, **kwargs):
        """creates instance of the state"""
        super().__init__(*args, **kwargs)

