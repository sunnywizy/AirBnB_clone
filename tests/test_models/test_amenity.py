#!/usr/bin/python3
"""
Module for Amenity class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Amenity class.
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

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        mam1 = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", mam1.__dict__)

    def test_two_amenities_unique_ids(self):
        mam1 = Amenity()
        mam2 = Amenity()
        self.assertNotEqual(mam1.id, mam2.id)

    def test_two_amenities_different_created_at(self):
        mam1 = Amenity()
        sleep(0.05)
        mam2 = Amenity()
        self.assertLess(mam1.created_at, mam2.created_at)

    def test_two_amenities_different_updated_at(self):
        mam1 = Amenity()
        sleep(0.05)
        mam2 = Amenity()
        self.assertLess(mam1.updated_at, mam2.updated_at)

    def test_str_representation(self):
        mdt = datetime.today()
        mdr = repr(mdt)
        mam1 = Amenity()
        mam1.id = "444444"
        mam1.created_at = mam1.updated_at = mdt
        mamstr = mam1.__str__()
        self.assertIn("[Amenity] (444444)", mamstr)
        self.assertIn("'id': '444444'", mamstr)
        self.assertIn("'created_at': " + mdr, mamstr)
        self.assertIn("'updated_at': " + mdr, mamstr)

    def test_args_unused(self):
        mam1 = Amenity(None)
        self.assertNotIn(None, mam1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        instantiation with kwargs test method
        """
        mdt = datetime.today()
        mdiso = mdt.isoformat()
        mam1 = Amenity(id="444", created_at=mdiso, updated_at=mdiso)
        self.assertEqual(mam1.id, "444")
        self.assertEqual(mam1.created_at, mdt)
        self.assertEqual(mam1.updated_at, mdt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

class TestAmenity_save(unittest.TestCase):
    """
    Unittests for save method of the Amenity class.
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

    def test_one_save(self):
        mam1 = Amenity()
        sleep(0.05)
        first_updated_at = mam1.updated_at
        mam1.save()
        self.assertLess(first_updated_at, mam1.updated_at)

    def test_two_saves(self):
        mam1 = Amenity()
        sleep(0.05)
        first_updated_at = mam1.updated_at
        mam1.save()
        second_updated_at = mam1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        mam1.save()
        self.assertLess(second_updated_at, mam1.updated_at)

    def test_save_with_arg(self):
        mam1 = Amenity()
        with self.assertRaises(TypeError):
            mam1.save(None)

    def test_save_updates_file(self):
        mam1 = Amenity()
        mam1.save()
        mamId = "Amenity." + mam1.id
        with open("file.json", "r") as f:
            self.assertIn(amenityId, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """
    Unittests for to_dict method of the Amenity class.
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

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        mam1 = Amenity()
        self.assertIn("id", mam1.to_dict())
        self.assertIn("created_at", mam1.to_dict())
        self.assertIn("updated_at", mam1.to_dict())
        self.assertIn("__class__", mam1.to_dict())

    def test_to_dict_contains_added_attributes(self):
        mam1 = Amenity()
        mam1.middle_name = "Nwaeze"
        mam1.my_number = 444
        self.assertEqual("Nwaeze", mam1.middle_name)
        self.assertIn("my_number", mam1.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        mam1 = Amenity()
        mamdict = mam1.to_dict()
        self.assertEqual(str, type(mamdict["id"]))
        self.assertEqual(str, type(mamdict["created_at"]))
        self.assertEqual(str, type(mamdict["updated_at"]))

    def test_to_dict_output(self):
        mdt = datetime.today()
        mam1 = Amenity()
        mam1.id = "444444"
        mam1.created_at = mam1.updated_at = mdt
        to_dict = {
            'id': '4444',
            '__class__': 'Amenity',
            'created_at': mdt.isoformat(),
            'updated_at': mdt.isoformat(),
        }
        self.assertDictEqual(mam1.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        mam1 = Amenity()
        self.assertNotEqual(mam1.to_dict(), mam1.__dict__)

    def test_to_dict_with_arg(self):
        mam1 = Amenity()
        with self.assertRaises(TypeError):
            mam1.to_dict(None)


if __name__ == "__main__":
    unittest.main()
