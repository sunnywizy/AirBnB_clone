#!/usr/bin/python3
"""
Module for Place class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Place class.
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
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(myPlace))
        self.assertNotIn("city_id", myPlace.__dict__)

    def test_user_id_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(myPlace))
        self.assertNotIn("user_id", myPlace.__dict__)

    def test_name_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(myPlace))
        self.assertNotIn("name", myPlace.__dict__)

    def test_description_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(myPlace))
        self.assertNotIn("desctiption", myPlace.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(myPlace))
        self.assertNotIn("number_rooms", myPlace.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(myPlace))
        self.assertNotIn("number_bathrooms", myPlace.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(myPlace))
        self.assertNotIn("max_guest", myPlace.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(myPlace))
        self.assertNotIn("price_by_night", myPlace.__dict__)

    def test_latitude_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(myPlace))
        self.assertNotIn("latitude", myPlace.__dict__)

    def test_longitude_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(myPlace))
        self.assertNotIn("longitude", myPlace.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        myPlace = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(myPlace))
        self.assertNotIn("amenity_ids", myPlace.__dict__)

    def test_two_places_unique_ids(self):
        myPlace_1 = Place()
        myPlace_2 = Place()
        self.assertNotEqual(myPlace_1.id, myPlace_2.id)

    def test_two_places_different_created_at(self):
        myPlace_1 = Place()
        sleep(0.05)
        myPlace_2 = Place()
        self.assertLess(myPlace_1.created_at, myPlace_2.created_at)

    def test_two_places_different_updated_at(self):
        myPlace_1 = Place()
        sleep(0.05)
        myPlace_2 = Place()
        self.assertLess(myPlace_1.updated_at, myPlace_2.updated_at)

    def test_str_representation(self):
        myDate = datetime.today()
        myDateRepr = repr(myDate)
        myPlace = Place()
        myPlace.id = "444444"
        myPlace.created_at = myPlace.updated_at = myDate
        myPlaceStr = myPlace.__str__()
        self.assertIn("[Place] (444444)", myPlaceStr)
        self.assertIn("'id': '444444'", myPlaceStr)
        self.assertIn("'created_at': " + myDateRepr, myPlaceStr)
        self.assertIn("'updated_at': " + myDateRepr, myPlaceStr)

    def test_args_unused(self):
        myPlace = Place(None)
        self.assertNotIn(None, myPlace.__dict__.values())

    def test_instantiation_with_kwargs(self):
        myDate = datetime.today()
        myDateIso = myDate.isoformat()
        myPlace = Place(id="444", created_at=myDateIso, updated_at=myDateIsoo)
        self.assertEqual(myPlace.id, "777")
        self.assertEqual(myPlace.created_at, myDate)
        self.assertEqual(myPlace.updated_at, myDate)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """
    Unittests for testing save method of the Place class.
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
        myPlace = Place()
        sleep(0.05)
        first_updated_at = myPlace.updated_at
        my_place.save()
        self.assertLess(first_updated_at, myPlace.updated_at)

    def test_two_saves(self):
        myPlace = Place()
        sleep(0.05)
        first_updated_at = myPlace.updated_at
        myPlace.save()
        second_updated_at = myPlace.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        myPlace.save()
        self.assertLess(second_updated_at, myPlace.updated_at)

    def test_save_with_arg(self):
        myPlace = Place()
        with self.assertRaises(TypeError):
            myPlace.save(None)

    def test_save_updates_file(self):
        myPlace = Place()
        myPlace.save()
        myPlaceId = "Place." + myPlace.id
        with open("file.json", "r") as f:
            self.assertIn(myPlaceId, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Place class.
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
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        myPlace = Place()
        self.assertIn("id", myPlace.to_dict())
        self.assertIn("created_at", myPlace.to_dict())
        self.assertIn("updated_at", myPlace.to_dict())
        self.assertIn("__class__", myPlace.to_dict())

    def test_to_dict_contains_added_attributes(self):
        myPlace = Place()
        myPlace.middle_name = "Nwaeze"
        myPlace.my_number = 444
        self.assertEqual("Nwaeze", myPlace.middle_name)
        self.assertIn("my_number", myPlace.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        myPlace = Place()
        myPlaceDict = myPlace.to_dict()
        self.assertEqual(str, type(myPlaceDict["id"]))
        self.assertEqual(str, type(myPlaceDict["created_at"]))
        self.assertEqual(str, type(myPlaceDict["updated_at"]))

    def test_to_dict_output(self):
        myDate = datetime.today()
        myPlace = Place()
        myPlace.id = "777777"
        myPlace.created_at = myPlace.updated_at = myDate
        to_dict = {
            'id': '444444',
            '__class__': 'Place',
            'created_at': myDate.isoformat(),
            'updated_at': myDate.isoformat(),
        }
        self.assertDictEqual(myPlace.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        myPlace = Place()
        self.assertNotEqual(myPlace.to_dict(), myPlace.__dict__)

    def test_to_dict_with_arg(self):
        myPlace = Place()
        with self.assertRaises(TypeError):
            myPlace.to_dict(None)


if __name__ == "__main__":
    unittest.main()
