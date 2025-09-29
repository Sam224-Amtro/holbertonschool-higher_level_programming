#!/usr/bin/python3
"""Module that defines the read_file function"""

def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its content to stdout"""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
