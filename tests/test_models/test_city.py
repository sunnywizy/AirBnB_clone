#!/usr/bin/python3
"""
Module for City unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """
    Unittests for instantiation of the City class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        mcy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(mcy))
        self.assertNotIn("state_id", mcy.__dict__)

    def test_name_is_public_class_attribute(self):
        mcy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(mcy))
        self.assertNotIn("name", mcy.__dict__)

    def test_two_cities_unique_ids(self):
        mcy1 = City()
        mcy2 = City()
        self.assertNotEqual(mcy1.id, mcy2.id)

    def test_two_cities_different_created_at(self):
        mcy1 = City()
        sleep(0.05)
        mcy2 = City()
        self.assertLess(mcy1.created_at, mcy2.created_at)

    def test_two_cities_different_updated_at(self):
        mcy1 = City()
        sleep(0.05)
        mcy2 = City()
        self.assertLess(mcy1.updated_at, mcy2.updated_at)

    def test_str_representation(self):
        mdt = datetime.today()
        mdr = repr(mdt)
        mcy = City()
        mcy.id = "444444"
        myCity.created_at = mcy.updated_at = mdt
        mcystr = mcy.__str__()
        self.assertIn("[City] (444444)", mcystr)
        self.assertIn("'id': '444444'", mcystr)
        self.assertIn("'created_at': " + mdr,  mcystr)
        self.assertIn("'updated_at': " + mdr,  mcystr)

    def test_args_unused(self):
        mcy = City(None)
        self.assertNotIn(None, mcy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        mdt = datetime.today()
        mdiso = mdt.isoformat()
        mcy = City(id="345", created_at=mdiso, updated_at=mdiso)
        self.assertEqual(mcy.id, "345")
        self.assertEqual(mcycreated_at, mdt)
        self.assertEqual(mcy.updated_at, mdt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
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

    def test_one_save(self):
        mcy = City()
        sleep(0.05)
        first_updated_at = mcy.updated_at
        mcy.save()
        self.assertLess(first_updated_at, mcy.updated_at)

    def test_two_saves(self):
        mcy = City()
        sleep(0.05)
        first_updated_at = mcy.updated_at
        mcy.save()
        second_updated_at = mcy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        mcy.save()
        self.assertLess(second_updated_at, mcy.updated_at)

    def test_save_with_arg(self):
        mcy = City()
        with self.assertRaises(TypeError):
            mcy.save(None)

    def test_save_updates_file(self):
        mcy = City()
        mcy.save()
        mcyid = "City." + mcy.id
        with open("file.json", "r") as f:
            self.assertIn(mcyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        mcy = City()
        self.assertIn("id", mcy.to_dict())
        self.assertIn("created_at", mcy.to_dict())
        self.assertIn("updated_at", mcy.to_dict())
        self.assertIn("__class__", mcy.to_dict())

    def test_to_dict_contains_added_attributes(self):
        mcy = City()
        mcy.middle_name = "Nwaeze"
        mcy.my_number = 444
        self.assertEqual("Nwaeze", mcy.middle_name)
        self.assertIn("my_number", mcy.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        mcy = City()
        mcydict = mcy.to_dict()
        self.assertEqual(str, type(mcydict["id"]))
        self.assertEqual(str, type(mcydict["created_at"]))
        self.assertEqual(str, type(mcydict["updated_at"]))

    def test_to_dict_output(self):
        mdt = datetime.today()
        mcy = City()
        mcy.id = "444444"
        mcy.created_at = mcy.updated_at = mdt
        to_dict = {
            'id': '444444',
            '__class__': 'City',
            'created_at': mdt.isoformat(),
            'updated_at': mdt.isoformat(),
        }
        self.assertDictEqual(mcy.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        mcy = City()
        self.assertNotEqual(mcy.to_dict(), mcy.__dict__)

    def test_to_dict_with_arg(self):
        mcy = City()
        with self.assertRaises(TypeError):
            mcy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
