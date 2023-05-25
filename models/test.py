#!/usr/bin/python3
import sys
dirctory_path = r'C:\Users\HP\Desktop\alu-AirBnB_clone'
sys.path.append(dirctory_path)  # Replace with the actual path to the project directory

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model_2"
my_model.my_number = 90
my_model.save()
print(my_model)