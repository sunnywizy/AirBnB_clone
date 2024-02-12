#!/usr/bin/python3
"""
Module for testing Review
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Review class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_text_is_public_class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_two_reviews_unique_ids(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_two_reviews_different_created_at(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_two_reviews_different_updated_at(self):
       rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    def test_str_representation(self):
        mdt = datetime.today()
        mdr = repr(mdt)
        rev = Review()
        rev.id = "444444"
        rev.created_at = rev.updated_at = mdt
        rev_str = rev.__str__()
        self.assertIn("[Review] (444444)", rev_str)
        self.assertIn("'id': '44444'", rev_str)
        self.assertIn("'created_at': " + mdr, rev_str)
        self.assertIn("'updated_at': " + mdr, rev_str)

    def test_args_unused(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_instantiation_with_kwargs(self):
        mdt = datetime.today()
        mdiso = mdt.isoformat()
        rev = Review(id="444", created_at=mdiso, updated_at=mdiso)
        self.assertEqual(rev.id, "444")
        self.assertEqual(rev.created_at, mdt)
        self.assertEqual(rev.updated_at, mdt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """
    Unittests for testing save method of the Review class.
    """

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
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        self.assertLess(first_updated_at, rev.updated_at)

    def test_two_saves(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        second_updated_at = rev.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rev.save()
        self.assertLess(second_updated_at, rev.updated_at)

    def test_save_with_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_save_updates_file(self):
        rev = Review()
        rev.save()
        revId = "Review." + rev.id
        with open("file.json", "r") as f:
            self.assertIn(revId, f.read())


class TestReview_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Review class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_to_dict_contains_added_attributes(self):
        rev = Review()
        rev.middle_name = "Nwaeze"
        rev.my_number = 444
        self.assertEqual("Nwaeze", rev.middle_name)
        self.assertIn("my_number", rev.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        rev = Review()
        revDict = rev.to_dict()
        self.assertEqual(str, type(revDict["id"]))
        self.assertEqual(str, type(revDict["created_at"]))
        self.assertEqual(str, type(revDict["updated_at"]))

    def test_to_dict_output(self):
        mdt = datetime.today()
        rev = Review()
        rev.id = "444444"
        rev.created_at = rev.updated_at = mdt
        to_dict = {
            'id': '444444',
            '__class__': 'Review',
            'created_at': mdt.isoformat(),
            'updated_at': mdt.isoformat(),
        }
        self.assertDictEqual(rev.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        rev= Review()
        self.assertNotEqual(rev.to_dict(), rev.__dict__)

    def test_to_dict_with_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)


if __name__ == "__main__":
    unittest.main()
