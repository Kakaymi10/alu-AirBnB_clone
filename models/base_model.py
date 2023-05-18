#!/usr/bin/python3
"""Importing the UUID module"""
import uuid
"""Importing the datetime module"""
from datetime import datetime



"""
Write a class BaseModel that defines all
common attributes/methods for other classes
"""
class BaseModel:
    """Public instance attributes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    """Str method"""
    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
    
    """public instance save:
    updates the public instance attribute updated_at with the current datetime"""
    def save(self):
        self.updated_at = datetime.now()
    
    """to_dict(self): returns a dictionary containing all keys/values 
    of __dict__ of the instance:"""
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to ISO format strings
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

