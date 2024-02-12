#!/usr/bin/python3
"""
Module for FilStorage unittest
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    Unittests for testing methods of the FileStorage class.
    """

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        mbm = BaseModel()
        mus = User()
        mst = State()
        mpl = Place()
        mcy = City()
        mam = Amenity()
        mrv = Review()
        models.storage.new(mbm)
        models.storage.new(mus)
        models.storage.new(mst)
        models.storage.new(mpl)
        models.storage.new(mcy)
        models.storage.new(mam)
        models.storage.new(mrv)
        self.assertIn("BaseModel." + mbm.id, models.storage.all().keys())
        self.assertIn(mbm, models.storage.all().values())
        self.assertIn("User." + mus.id, models.storage.all().keys())
        self.assertIn(mus, models.storage.all().values())
        self.assertIn("State." + mst.id, models.storage.all().keys())
        self.assertIn(mst, models.storage.all().values())
        self.assertIn("Place." + mpl.id, models.storage.all().keys())
        self.assertIn(mpl, models.storage.all().values())
        self.assertIn("City." + mcy.id, models.storage.all().keys())
        self.assertIn(mcy, models.storage.all().values())
        self.assertIn("Amenity." + mam.id, models.storage.all().keys())
        self.assertIn(mam, models.storage.all().values())
        self.assertIn("Review." + mrv.id, models.storage.all().keys())
        self.assertIn(mrv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        mbm = BaseModel()
        mus = User()
        mst = State()
        mpl = Place()
        mcy = City()
        mam = Amenity()
        mrv = Review()
        models.storage.new(mbm)
        models.storage.new(mus)
        models.storage.new(mst)
        models.storage.new(mpl)
        models.storage.new(mcy)
        models.storage.new(mam)
        models.storage.new(mrv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + mbm.id, save_text)
            self.assertIn("User." + mus.id, save_text)
            self.assertIn("State." + mst.id, save_text)
            self.assertIn("Place." + mpl.id, save_text)
            self.assertIn("City." + mcy.id, save_text)
            self.assertIn("Amenity." + mam.id, save_text)
            self.assertIn("Review." + mrv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        mbm = BaseModel()
        mus = User()
        mst = State()
        mpl = Place()
        mcy = City()
        mam = Amenity()
        mrv = Review()
        models.storage.new(mbm)
        models.storage.new(mus)
        models.storage.new(mst)
        models.storage.new(mpl)
        models.storage.new(mcy)
        models.storage.new(mam)
        models.storage.new(mrv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + mbm.id, objs)
        self.assertIn("User." + mus.id, objs)
        self.assertIn("State." + mst.id, objs)
        self.assertIn("Place." + mpl.id, objs)
        self.assertIn("City." + mcy.id, objs)
        self.assertIn("Amenity." + mam.id, objs)
        self.assertIn("Review." + mrv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
