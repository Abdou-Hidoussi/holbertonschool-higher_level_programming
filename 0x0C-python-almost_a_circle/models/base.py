#!/usr/bin/python3
""" base """
from json import dumps, loads
import csv


class Base:
    """ classs Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return dumps(list_dictionaries)
        return dumps([])

    @staticmethod
    def from_json_string(json_string):
        if json_string:
            return loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        ls = []
        name = cls.__name__ + '.json'
        if list_objs:
            ls = [data.to_dictionary() for data in list_objs]
        with open(name, 'w', encoding='utf-8') as my_file:
            my_file.write(Base.to_json_string(ls))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(10, 10)
        elif cls.__name__ is "Square":
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        name = cls.__name__ + ".json"
        data = []
        try:
            with open(filename) as file:
                data = cls.from_json_string(file.read())
            for i, j in enumerate(data):
                data[i] = cls.create(**data[i])
        except:
            pass
        return data
