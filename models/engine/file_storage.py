#!/usr/bin/python3

import json
import os

"""This module serializes data in json format"""


class FileStorage():
    """instance  of  a class"""
    def __init__(self):
        pass

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        item = obj.__class__.__name__ + "." + obj.id
        self.__objects[item] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        my_dict = {}

        #for key, value in FileStrorage.__objects.items():
            #my_dict[item] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as myFile:
            json.dump(my_dict, myFile)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing
        If the file doesn’t exist, no exception should be raised
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as myFile:
                json_file = myFile.read()
        except Exception:
            return
        objects = eval(json_file)
        for (key, value) in objects.items():
            objects[key] = eval(key.split('.')[0] + '(**value)')
        self.__objects = objects
