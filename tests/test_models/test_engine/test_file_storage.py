#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
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
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
    
    def test_get_method_returns_correct_object(self):
        # Define a test object and add it to the in-memory storage
        test_object = YourObjectClass()  # Replace with the actual name of your object class
        test_object.id = 1
        key = "{}.{}".format(type(test_object).__name__, test_object.id)
        self.in_memory_storage.__objects[key] = test_object

        # Call the get method with the test object's class and id
        result = self.in_memory_storage.get(type(test_object).__name__, 1)

        # Assert that the returned object is the same as the added object
        self.assertEqual(result, test_object)

    def test_get_method_returns_none_for_nonexistent_object(self):
        # Call the get method with a non-existent class and id
        result = self.in_memory_storage.get("NonExistentClass", 1)

        # Assert that the result is None
        self.assertIsNone(result)

    def test_count_method_returns_correct_number_of_objects(self):
        # Define test objects and add them to the in-memory storage
        test_objects = [YourObjectClass() for _ in range(3)]  # Replace with the actual name of your object class
        for i, obj in enumerate(test_objects, start=1):
            obj.id = i
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.in_memory_storage.__objects[key] = obj

        # Call the count method without specifying a class
        result = self.in_memory_storage.count()

        # Assert that the result is equal to the total number of test objects
        self.assertEqual(result, len(test_objects))

    def test_count_method_returns_correct_number_of_objects_for_specific_class(self):
        # Define test objects for a specific class and add them to the in-memory storage
        test_objects = [YourObjectClass() for _ in range(2)]  # Replace with the actual name of your object class
        for i, obj in enumerate(test_objects, start=1):
            obj.id = i
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.in_memory_storage.__objects[key] = obj

        # Call the count method for the specific class
        result = self.in_memory_storage.count(cls=type(test_objects[0]))

        # Assert that the result is equal to the number of test objects for that class
        self.assertEqual(result, len(test_objects))

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))