#!/usr/bin/python3
"""Module that manages the id attribute for all other classes in the project"""
import json
import csv
import turtle


class Base:
    """Base class for managing id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of objects represented by the JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the Turtle graphics module """
        screen = turtle.Screen()
        screen.bgcolor("#b7312c")
        turt = turtle.Turtle()
        turt.pensize(3)
        turt.shape("turtle")

    def draw_rectangle(rect):
        turt.up()
        turt.goto(rect.x, rect.y)
        turt.down()
        turt.color("#ffffff")
        for _ in range(2):
            turt.forward(rect.width)
            turt.left(90)
            turt.forward(rect.height)
            turt.left(90)

    def draw_square(sq):
        turt.up()
        turt.goto(sq.x, sq.y)
        turt.down()
        turt.color("#b5e3d8")
        for _ in range(4):
            turt.forward(sq.side_length)
            turt.left(90)

    for rect in list_rectangles:
        draw_rectangle(rect)

    for sq in list_squares:
        draw_square(sq)

    turtle.done()

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                instances = [cls.create(**d) for d in data]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to CSV format and save to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file and return as a list"""
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    instance = cls.create_from_csv_row(row)
                    instances.append(instance)
        except FileNotFoundError:
            pass
        return instances

    def to_dictionary(self):
        """Return the dictionary representation of an instance"""
        return self.__dict__.copy()

    @classmethod
    def create_from_csv_row(cls, row):
        """Create an instance from a CSV row"""
        raise NotImplementedError

    def to_csv_row(self):
        """Return the CSV row representation of an instance"""
        raise NotImplementedError
