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
        myCity = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(myCity))
        self.assertNotIn("state_id", myCity.__dict__)

    def test_name_is_public_class_attribute(self):
        myCity = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(myCity))
        self.assertNotIn("name", myCity.__dict__)

    def test_two_cities_unique_ids(self):
        myCity_1 = City()
        myCity_2 = City()
        self.assertNotEqual(myCity_1.id, myCity_2.id)

    def test_two_cities_different_created_at(self):
        myCity_1 = City()
        sleep(0.05)
        myCity_2 = City()
        self.assertLess(myCity_1.created_at, myCity_2.created_at)

    def test_two_cities_different_updated_at(self):
        myCity_1 = City()
        sleep(0.05)
        myCity_2 = City()
        self.assertLess(myCity_1.updated_at, myCity_2.updated_at)

    def test_str_representation(self):
        myDate = datetime.today()
        myDateRepr = repr(my_date)
        myCity = City()
        myCity.id = "444444"
        myCity.created_at = myCity.updated_at = myDate
        myCityStr = myCity.__str__()
        self.assertIn("[City] (444444)", myCityStr)
        self.assertIn("'id': '444444'", myCityStr)
        self.assertIn("'created_at': " + myDateRepr,  myCityStr)
        self.assertIn("'updated_at': " + myDateRepr,  myCityStr)

    def test_args_unused(self):
        myCity = City(None)
        self.assertNotIn(None, myCity.__dict__.values())

    def test_instantiation_with_kwargs(self):
        myDate = datetime.today()
        myDateIso = myDate.isoformat()
        myCity = City(id="345", created_at=myDateIso, updated_at=myDateIso)
        self.assertEqual(myCity.id, "345")
        self.assertEqual(myCity.created_at, myDate)
        self.assertEqual(myCity.updated_at, myDate)

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
        myCity = City()
        sleep(0.05)
        first_updated_at = myCity.updated_at
        myCity.save()
        self.assertLess(first_updated_at, myCity.updated_at)

    def test_two_saves(self):
        myCity = City()
        sleep(0.05)
        first_updated_at = myCity.updated_at
        myCity.save()
        second_updated_at = myCity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        myCity.save()
        self.assertLess(second_updated_at, myCity.updated_at)

    def test_save_with_arg(self):
        myCity = City()
        with self.assertRaises(TypeError):
            myCity.save(None)

    def test_save_updates_file(self):
        myCity = City()
        mycity.save()
        myCityId = "City." + myCity.id
        with open("file.json", "r") as f:
            self.assertIn(myCityId, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        myCity = City()
        self.assertIn("id", myCity.to_dict())
        self.assertIn("created_at", myCity.to_dict())
        self.assertIn("updated_at", myCity.to_dict())
        self.assertIn("__class__", myCity.to_dict())

    def test_to_dict_contains_added_attributes(self):
        myCity = City()
        myCity.middle_name = "Nwaeze"
        myCity.my_number = 444
        self.assertEqual("Nwaeze", myCity.middle_name)
        self.assertIn("my_number", myCity.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        myCity = City()
        myCityDict = myCity.to_dict()
        self.assertEqual(str, type(myCityDict["id"]))
        self.assertEqual(str, type(myCityDict["created_at"]))
        self.assertEqual(str, type(myCityDict["updated_at"]))

    def test_to_dict_output(self):
        myDate = datetime.today()
        myCity = City()
        myCity.id = "444444"
        myCity.created_at = myCity.updated_at = myDate
        to_dict = {
            'id': '444444',
            '__class__': 'City',
            'created_at': myDate.isoformat(),
            'updated_at': myDate.isoformat(),
        }
        self.assertDictEqual(myCity.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        myCity = City()
        self.assertNotEqual(myCity.to_dict(), myCity.__dict__)

    def test_to_dict_with_arg(self):
        myCity = City()
        with self.assertRaises(TypeError):
            myCity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
