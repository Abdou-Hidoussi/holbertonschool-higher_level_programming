#!/usr/bin/python3
"""
Task 4
"""


def inherits_from(obj, a_class):
    """
    obj: Object
    a_class: Class
    return: Bool
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
