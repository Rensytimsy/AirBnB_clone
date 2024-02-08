#!/usr/bin/python3
"""This program contains the unittest TestCase
for State
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """This class Tests for the State class
    """

    def test_instance(self):
        """ This funcTests for State's Instance
        """
        state_1 = State()
        self.assertIsInstance(state_1, State)

    def test_attributes(self):
        """ This func Tests if State has the defined attributes
        """
        state_1 = State()
        self.assertTrue(hasattr(state_1, "name"))
        self.assertIsInstance(state_1.name, str)

    def test_class_name(self):
        """ This func Checks the type for State instance
        """
        state_1 = State()
        self.assertEqual(str(type(state_1)), "<class 'models.state.State'>")


if __name__ == '__main__':
    unittest.main()
