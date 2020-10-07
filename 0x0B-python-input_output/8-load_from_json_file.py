#!/usr/bin/python3
"""
task 8
"""
import json


def load_from_json_file(filename):
    """jason convert object function"""
    with open(filename, encoding="utf-8") as f:
       return json.load(f)
