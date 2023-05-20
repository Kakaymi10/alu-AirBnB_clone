#!/usr/bin/python3
"""impoering modules"""
import unittest
from datetime import datetime
from unittest.mock import patch
import time
import sys
dirctory_path = r'C:\Users\HP\Desktop\alu-AirBnB_clone'
sys.path.append(dirctory_path)  # Replace with the actual path to the project directory

from models.base_model import BaseModel



 # Import the module containing the BaseModel class

class BaseModelTestCase(unittest.TestCase):

    def setUp(self):
        # Create a BaseModel instance with some initial values for testing
        self.base_model = BaseModel(id='123', created_at='2023-01-01T12:00:00.000', updated_at='2023-01-01T12:00:00.000')

    def test_init(self):
        # Check if the instance attributes are set correctly during initialization
        self.assertEqual(self.base_model.id, '123')
        self.assertEqual(self.base_model.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(self.base_model.updated_at, datetime(2023, 1, 1, 12, 0, 0))

    def test_save(self):
        # Check if the save method updates the updated_at attribute with the current datetime
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, datetime(2023, 1, 1, 12, 0, 0))

    def test_to_dict(self):
        # Check if the to_dict method returns a dictionary with the expected keys and values
        expected_dict = {
            'id': '123',
            'created_at': '2023-01-01T12:00:00',
            'updated_at': '2023-01-01T12:00:00',
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    def test_str(self):
        # Check if the str method returns the expected string representation
        expected_str = "[BaseModel] (123) {'id': '123', 'created_at': datetime.datetime(2023, 1, 1, 12, 0), 'updated_at': datetime.datetime(2023, 1, 1, 12, 0)}"
        self.assertEqual(str(self.base_model), expected_str)

if __name__ == '__main__':
    unittest.main()
