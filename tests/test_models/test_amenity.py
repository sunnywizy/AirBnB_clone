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
        amenity_1 = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity_1.__dict__)

    def test_two_amenities_unique_ids(self):
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_two_amenities_different_created_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.created_at, amenity_2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity_1 = Amenity()
        sleep(0.05)
        amenity_2 = Amenity()
        self.assertLess(amenity_1.updated_at, amenity_2.updated_at)

    def test_str_representation(self):
        myDate = datetime.today()
        myDateRepr = repr(my_date)
        amenity_1 = Amenity()
        amenity_1.id = "777777"
        amenity_1.created_at = amenity_1.updated_at = myDate
        amenityStr = amenity_1.__str__()
        self.assertIn("[Amenity] (777777)", amenityStr)
        self.assertIn("'id': '777777'", amenityStr)
        self.assertIn("'created_at': " + myDateRepr, amenityStr)
        self.assertIn("'updated_at': " + myDateRepr, amenityStr)

    def test_args_unused(self):
        amenity_1 = Amenity(None)
        self.assertNotIn(None, amenity_1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        instantiation with kwargs test method
        """
        myDate = datetime.today()
        myDateIso = my_date.isoformat()
        amenity_1 = Amenity(id="777", created_at=myDateIso, updated_at=myDateIso)
        self.assertEqual(amenity_1.id, "777")
        self.assertEqual(amenity_1.created_at, myDate)
        self.assertEqual(amenity_1.updated_at, myDate)

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
        amenity_1 = Amenity()
        sleep(0.05)
        first_updated_at = amenity_1.updated_at
        amenity_1.save()
        self.assertLess(first_updated_at, amenity_1.updated_at)

    def test_two_saves(self):
        amenity-1 = Amenity()
        sleep(0.05)
        first_updated_at = amenity_1.updated_at
        amenity_1.save()
        second_updated_at = amenity_1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity_1.save()
        self.assertLess(second_updated_at, amenity_1.updated_at)

    def test_save_with_arg(self):
        amenity_1 = Amenity()
        with self.assertRaises(TypeError):
            amenity_1.save(None)

    def test_save_updates_file(self):
        amenity_1 = Amenity()
        amenity_1.save()
        amenityId = "Amenity." + amenity_1.id
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
        amenity_1 = Amenity()
        self.assertIn("id", amenity_1.to_dict())
        self.assertIn("created_at", amenity_1.to_dict())
        self.assertIn("updated_at", amenity_1.to_dict())
        self.assertIn("__class__", amenity_1.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amenity_1 = Amenity()
        amenity_1.middle_name = "Nwaeze"
        amenity_1.my_number = 444
        self.assertEqual("Nwaeze", amenity_1.middle_name)
        self.assertIn("my_number", amenity_1.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenity_1 = Amenity()
        amenityDict = amenity_1.to_dict()
        self.assertEqual(str, type(amenityDict["id"]))
        self.assertEqual(str, type(amenityDict["created_at"]))
        self.assertEqual(str, type(amenityDict["updated_at"]))

    def test_to_dict_output(self):
        myDate = datetime.today()
        amenity_1 = Amenity()
        amenity_1.id = "444444"
        amenity_1.created_at = amenity_1.updated_at = myDate
        to_dict = {
            'id': '4444',
            '__class__': 'Amenity',
            'created_at': myDate.isoformat(),
            'updated_at': myDate.isoformat(),
        }
        self.assertDictEqual(amenity_1.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        amenity_1 = Amenity()
        self.assertNotEqual(amenity_1.to_dict(), amenity_1.__dict__)

    def test_to_dict_with_arg(self):
        amenity_1 = Amenity()
        with self.assertRaises(TypeError):
            amenity_1.to_dict(None)


if __name__ == "__main__":
    unittest.main()
