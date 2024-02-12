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
        mpl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(mpl))
        self.assertNotIn("city_id", mpl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(mpl))
        self.assertNotIn("user_id", mpl.__dict__)

    def test_name_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(mpl))
        self.assertNotIn("name", mpl.__dict__)

    def test_description_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(mpl))
        self.assertNotIn("desctiption", mpl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(mpl))
        self.assertNotIn("number_rooms", mpl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(mpl))
        self.assertNotIn("number_bathrooms", mpl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(mpl))
        self.assertNotIn("max_guest", mpl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(mpl))
        self.assertNotIn("price_by_night", mpl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(mpl))
        self.assertNotIn("latitude", mpl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(mpl))
        self.assertNotIn("longitude", mpl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        mpl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(mpl))
        self.assertNotIn("amenity_ids", mpl.__dict__)

    def test_two_places_unique_ids(self):
        mpl1 = Place()
        mpl2 = Place()
        self.assertNotEqual(mpl1.id, mpl2.id)

    def test_two_places_different_created_at(self):
        mpl1 = Place()
        sleep(0.05)
        mpl2 = Place()
        self.assertLess(mpl1.created_at, mpl2.created_at)

    def test_two_places_different_updated_at(self):
        mpl1 = Place()
        sleep(0.05)
        mpl2 = Place()
        self.assertLess(mpl1.updated_at, mpl2.updated_at)

    def test_str_representation(self):
        mdt = datetime.today()
        mdr = repr(mdt)
        mpl = Place()
        mpl.id = "444444"
        mpl.created_at = mpl.updated_at = mdt
        mpstr = mpl.__str__()
        self.assertIn("[Place] (444444)", mpstr)
        self.assertIn("'id': '444444'", mpstr)
        self.assertIn("'created_at': " + mdr, mpstr)
        self.assertIn("'updated_at': " + mdr, myPlaceStr)

    def test_args_unused(self):
        mpl = Place(None)
        self.assertNotIn(None, mpl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        mdt = datetime.today()
        mdiso = mdt.isoformat()
        mpl = Place(id="444", created_at=mdiso, updated_at=mdiso)
        self.assertEqual(mpl.id, "444")
        self.assertEqual(mpl.created_at, mdt)
        self.assertEqual(mpl.updated_at, mdt)

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
        mpl = Place()
        sleep(0.05)
        first_updated_at = mpl.updated_at
        mpl.save()
        self.assertLess(first_updated_at, mpl.updated_at)

    def test_two_saves(self):
        mpl = Place()
        sleep(0.05)
        first_updated_at = mpl.updated_at
        mpl.save()
        second_updated_at = mpl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        mpl.save()
        self.assertLess(second_updated_at, mpl.updated_at)

    def test_save_with_arg(self):
        mpl = Place()
        with self.assertRaises(TypeError):
            mpl.save(None)

    def test_save_updates_file(self):
        mpl = Place()
        mpl.save()
        mplid = "Place." + mpl.id
        with open("file.json", "r") as f:
            self.assertIn(mplid, f.read())


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
        mpl = Place()
        self.assertIn("id", mpl.to_dict())
        self.assertIn("created_at", mpl.to_dict())
        self.assertIn("updated_at", mpl.to_dict())
        self.assertIn("__class__", mpl.to_dict())

    def test_to_dict_contains_added_attributes(self):
        mpl = Place()
        mpl.middle_name = "Nwaeze"
        mpl.my_number = 444
        self.assertEqual("Nwaeze", mpl.middle_name)
        self.assertIn("my_number", mpl.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        mpl = Place()
        mpldict = mpl.to_dict()
        self.assertEqual(str, type(mpldict["id"]))
        self.assertEqual(str, type(mpldict["created_at"]))
        self.assertEqual(str, type(mpldict["updated_at"]))

    def test_to_dict_output(self):
        mdt = datetime.today()
        mpl = Place()
        mpl.id = "777777"
        mpl.created_at = mpl.updated_at = mdt
        to_dict = {
            'id': '444444',
            '__class__': 'Place',
            'created_at': mdt.isoformat(),
            'updated_at': mdt.isoformat(),
        }
        self.assertDictEqual(mpl.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        mpl = Place()
        self.assertNotEqual(mpl.to_dict(), mpl.__dict__)

    def test_to_dict_with_arg(self):
        mpl = Place()
        with self.assertRaises(TypeError):
            mpl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
