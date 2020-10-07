#!/usr/bin/python3
"""
task 3
"""


def write_file(filename="", text=""):
    """write in file function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
