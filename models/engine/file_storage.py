#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    FileStorage class for storing, serializing and deserializing data
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
         Sets an object in the __objects dictionary with a key of 
         <obj class name>.id.
        """
        ocsname = obj.__class__.__name__

        k = "{}.{}".format(ocsname, obj.id)

        FileStorage.__objects[k] = obj


    def all(self):
        """
        Returns the __objects dictionary. 
        It provides access to all the stored objects.
        """
        return  FileStorage.__objects


    def save(self):
        """
        Serializes the __objects dictionary into 
        JSON format and saves it to the file specified by __file_path.
        """
        alobjs = FileStorage.__objects

        objdict = {}

        for obj in alobjs.keys():
            objdict[obj] = alobjs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objdict, file)

    def reload(self):
        """
        This method deserializes the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    objdict = json.load(file)

                    for k, v in objdict.items():
                        cls_name, objid = k.split('.')

                        cls = eval(cls_name)

                        insta = cls(**v)

                        FileStorage.__objects[k] = insta
                except Exception:
                    pass
