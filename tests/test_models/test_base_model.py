#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import os
import unittest
from models.base_model import BaseModel



class TestBasemodel(unittest.TestCase):
    """
    Unittest for BaseModel
    """

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
    def test_init(self):
        """
        Test for init
        """
        mbm = BaseModel()

        self.assertIsNotNone(mbm.id)
        self.assertIsNotNone(mbm.created_at)
        self.assertIsNotNone(mbm.updated_at)

    def test_save(self):
        """
        Test for save method
        """
        mbm = BaseModel()

        iua = mbm.updated_at

        cua = mbm.save()

        self.assertNotEqual(iua, cua)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        mbm = BaseModel()

        mbd = mbm.to_dict()

        self.assertIsInstance(mbd, dict)

        self.assertEqual(mbd["__class__"], 'BaseModel')
        self.assertEqual(mbd['id'], mbm.id)
        self.assertEqual(mbd['created_at'], mbm.created_at.isoformat())
        self.assertEqual(mbd["updated_at"], mbm.created_at.isoformat())


    def test_str(self):
        """
        Test for string representation
        """
       mbm = BaseModel()

        self.assertTrue(str(mbm).startswith('[BaseModel]'))

        self.assertIn(mbm.id, str(mbm))

        self.assertIn(str(mbm.__dict__), str(mbm))


if __name__ == "__main__":
    unittest.main()
