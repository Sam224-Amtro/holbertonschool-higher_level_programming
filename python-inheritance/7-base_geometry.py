#!/usr/bin/python3
"""Module for base_geometry class."""



class BaseGeometry:
    """A class for basic geometric operations."""

    def area(self):
        """Raises an exception indicating that the method is not
        implemented."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Validates that the value is an integer and greater than 0.

        Args:
            name (str): The name of the value (used in the exception
            message.)

            value (int): The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
