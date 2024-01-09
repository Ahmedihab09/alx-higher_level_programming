#!/usr/bin/python3

'''Student module'''


class Student:
    """
    Defines a student with first name, last name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those in the json dictionary.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
