#!/usr/bin/python3
""" Base unit testing """
import unittest
import pep8
import inspect
import json
from models import base
Base = base.Base


class TestBaseTypos(unittest.TestCase):
    """ Tests base documentation """

    @classmethod
    def setUpClass(cls):
        """ Set up for tests """
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8(self):
        """ Test that models/base.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])

    def test_module(self):
        """ Tests module """
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class(self):
        """ Tests class """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_funcions(self):
        """ Tests functions """
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBaseFunctions(unittest.TestCase):
    """ Test base class """

    def test_arguments_overflow(self):
        """ Send many arguments """
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_no_id(self):
        """ Do not send id """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        """ Send id normally """
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_no_id_after_set(self):
        """ Change id after setter """
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_nb(self):
        """ Tests objects as a private attribute """
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_json_string(self):
        """ Tests json string function """
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_empty_json_string(self):
        """ Send empty string to json function """
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_String(self):
        """ Send none to json function """
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """ Regular data to open """
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
                    {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_fjs_empty(self):
        """ Send empty string """
        self.assertEqual([], Base.from_json_string(""))

    def test_fjs_None(self):
        """ Send None """
        self.assertEqual([], Base.from_json_string(None))
