#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
     """
    Interacts with the MySQL database.

    Attributes:
        __engine (sqlalchemy.engine.Engine): The database engine.
        __session (sqlalchemy.orm.Session): The database session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
         """
        Query on the current database session.

        Args:
            cls (class): The class to filter the query.

        Returns:
            dict: A dictionary containing all objects of the specified class.
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
        Add the object to the current database session.

        Args:
            obj (Base): The object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session if obj is not None.

        Args:
            obj (Base): The object to delete from the session.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Retrieve the first record in class by id.

        Args:
            cls (class): The class to retrieve the record from.
            id (str): The id of the record to retrieve.

        Returns:
            Base: The object with the specified id in the specified class.
        """
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss])
                for obj in objs:
                    if obj.id == id:
                        return obj
        return (None)

    def count(self, cls=None):
        """
        Return the number of objects in storage.

        Args:
            cls (class): The class to count objects for.

        Returns:
            int: The number of objects in the specified class.
        """
        nobjects = 0
        if cls:
            for clss in classes:
                if cls is classes[clss] or cls is clss:
                    nobjects += len(self.__session.query(classes[clss]).all())
            return nobjects
        else:
            for clss in classes:
                nobjects += len(self.__session.query(classes[clss]).all())
            return nobjects
