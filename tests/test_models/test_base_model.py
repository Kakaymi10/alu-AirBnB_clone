#!/usr/bin/python3
"""impoering modules"""
import unittest
from datetime import datetime
from unittest.mock import patch
import time

"impoting the file to test"
from ../../models/base_model import BaseModel

"""Class"""
class TestBaseModel(unittest.TestCase):

    """functions"""
    def test_init(self):
        """test"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    """functions"""
    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        # Introduce a small time delay
        time.sleep(0.1)

        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    """functions"""
    def test_to_dict(self):
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], model.id)
        self.assertEqual(obj_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], model.updated_at.isoformat())

    """functions"""
    def test_str(self):
        model = BaseModel()
        with patch('builtins.print') as mock_print:
            expected_output = f"[BaseModel] ({model.id}) {model.__dict__}"
            model.__str__()
            mock_print.assert_called_with(expected_output)

"""Run it"""
if __name__ == '__main__':
    unittest.main()
