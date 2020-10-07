#!/usr/bin/python3
"""
task 7
"""
import json


def save_to_json_file(my_obj, filename):
    """jason convert object function"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
