#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_get_method_returns_correct_object(self):
        # Define a test object and add it to the database
        test_object = YourObjectClass()  # Replace with the actual name of your object class
        test_object.id = 1
        self.db_storage.add(test_object)  # Assuming there's an 'add' method to add objects to the storage

        # Call the get method with the test object's class and id
        result = self.db_storage.get(type(test_object).__name__, 1)

        # Assert that the returned object is the same as the added object
        self.assertEqual(result, test_object)

    def test_get_method_returns_none_for_nonexistent_object(self):
        # Call the get method with a non-existent class and id
        result = self.db_storage.get("NonExistentClass", 1)

        # Assert that the result is None
        self.assertIsNone(result)

    def test_count_method_returns_correct_number_of_objects(self):
        # Define test objects and add them to the database
        test_objects = [YourObjectClass() for _ in range(3)]  # Replace with the actual name of your object class
        for i, obj in enumerate(test_objects, start=1):
            obj.id = i
            self.db_storage.add(obj)  # Assuming there's an 'add' method to add objects to the storage

        # Call the count method without specifying a class
        result = self.db_storage.count()

        # Assert that the result is equal to the total number of test objects
        self.assertEqual(result, len(test_objects))

    def test_count_method_returns_correct_number_of_objects_for_specific_class(self):
        # Define test objects for a specific class and add them to the database
        test_objects = [YourObjectClass() for _ in range(2)]  # Replace with the actual name of your object class
        for i, obj in enumerate(test_objects, start=1):
            obj.id = i
            self.db_storage.add(obj)  # Assuming there's an 'add' method to add objects to the storage

        # Call the count method for the specific class
        result = self.db_storage.count(cls=type(test_objects[0]))

        # Assert that the result is equal to the number of test objects for that class
        self.assertEqual(result, len(test_objects))

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
