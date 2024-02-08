#!/usr/bin/python3
"""This program  contains the unittest TestCase
for Amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ This class Tests for the Amenity class
    """

    def test_instance(self):
        """ This method Tests for Amenity's Instance
        """
        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1, Amenity)

    def test_attributes(self):
        """ This Tests if Amenity has the defined attributes
        """
        amenity_1 = Amenity()
        self.assertTrue(hasattr(amenity_1, "name"))
        self.assertIsInstance(amenity_1.name, str)

    def test_class_name(self):
        """ This Checks the type for State instance
        """
        amenity_1 = Amenity()
        self.assertEqual(str(type(amenity_1)),
                         "<class 'models.amenity.Amenity'>")


if __name__ == '__main__':
    unittest.main()
