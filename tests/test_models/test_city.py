#!/usr/bin/python3
"""This program contains the unittest TestCase
for City
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ This class will Test for the City class
    """

    def test_instance(self):
        """This func will Test for City's Instance
        """
        city_1 = City()
        self.assertIsInstance(city_1, City)

    def test_attributes(self):
        """ This func will Test if the City has the defined attributes
        """
        city_1 = City()
        self.assertTrue(hasattr(city_1, "name"))
        self.assertTrue(hasattr(city_1, "state_id"))
        self.assertIsInstance(city_1.name, str)
        self.assertIsInstance(city_1.state_id, str)

    def test_class_name(self):
        """ This func will Check the type for City instance
        """
        city_1 = City()
        self.assertEqual(str(type(city_1)), "<class 'models.city.City'>")


if __name__ == '__main__':
    unittest.main()
