#!/usr/bin/python3
"""
task 4
"""


def write_file(filename="", text=""):
    """append file function"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
