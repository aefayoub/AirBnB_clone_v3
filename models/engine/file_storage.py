#!/usr/bin/python3
"""Contains the FileStorage class."""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from builtins import KeyError

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    Serialize instances to a JSON file and deserializes back to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects by <class name>.id.
    """

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """
        Return the dictionary __objects.

        Args:
            cls (class): The class to filter the dictionary.

        Returns:
            dict: A dictionary containing all objects of the specified class.
        """
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.

        Args:
            obj (Base): The object to add to __objects.
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except KeyError:
            pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside.

        Args:
            obj (Base): The object to delete from __objects.
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects."""
        self.reload()

    def get(self, cls, id):
        """
        Return object by class name and its ID.

        Args:
            cls (class): The class to retrieve the object from.
            id (str): The ID of the object to retrieve.

        Returns:
            Base: The object with the specified ID in the specified class.
        """
        obj_dict = {}
        obj = None
        obj_dict = FileStorage.__objects.values()
        if cls:
            for item in obj_dict:
                if item.id == id:
                    obj = item
            return obj

    def count(self, cls=None):
        """
        Return the number of objects in storage.

        Args:
            cls (class): The class to count objects for.

        Returns:
            int: The number of objects in the specified class.
        """
        if cls:
            list_obj = []
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    list_obj.append(value)
            return len(list_obj)
        else:
            list_obj = []
            for item in classes:
                list_obj.append(item)
            return len(list_obj)
