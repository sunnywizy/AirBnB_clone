#!/usr/bin/python3
"""
Module for the BaseModel class.
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        mtfm = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs: 
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated-at":
                    setattr(self, k, datetime.strptime(v, mtfm)
                else:
                    setattr(self, k, v)
            models.storage.new(self)
    
    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()
    
    def to_dict(self):
        rcdist = self.__dict__.copy()
        rcdist["__class__"] = self.__class__.__name__
        rcdist["created_at"] = self.created_at.isoformat()
        rcdist["updated_at"] = self.updated_at.isoformat()

        return rcdist
    
    def __str__(self):
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)




my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
