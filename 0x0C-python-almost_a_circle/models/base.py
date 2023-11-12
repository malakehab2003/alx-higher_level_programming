#!/usr/bin/python3
"""make Base class"""
import json


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """private the id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """change a dict to string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to file"""
        list_d = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_d.append(list_objs[i].to_dictionary())
        the_list = cls.to_json_string(list_d)
        the_file = cls.__name__ + ".json"
        with open(the_file, 'w') as file:
            file.write(the_list)

    @staticmethod
    def from_json_string(json_string):
        """get from json string to dict"""
        the_list = []
        if json_string is None or not json_string:
            return the_list

        the_list = json.loads(json_string)
        return the_list

    @classmethod
    def create(cls, **dictionary):
        """write the attrs that aready set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """load from json file"""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as file:
                data = file.read()
                instances_data = cls.from_json_string(data)
                instances = [cls.create(**instance_data)
                             for instance_data in instances_data]
                return instances
        except FileNotFoundError:
            return []
