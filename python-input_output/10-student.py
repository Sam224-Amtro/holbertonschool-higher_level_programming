#!/usr/bin/python3
"""Defines a class Student"""

class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes contained in this list
        are retrieved. Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__
