#!/usr/bin/python3
"""Module that manages the id attribute for all other classes in the project"""
import json
import csv
import pygame


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

    @staticmethod
    def draw(list_rectangles, list_squares):
        pygame.init()

        width = 800
        height = 600
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Drawing Rectangles and Squares")

        white = (255, 255, 255)
        black = (0, 0, 0)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            window.fill(white)

            for rect in list_rectangles:
                pygame.draw.rect(window, black, pygame.Rect(rect.x, rect.y,
                                 rect.width, rect.height))

            for square in list_squares:
                pygame.draw.rect(window, black, pygame.Rect(square.x, square.y,
                                                            square.size,
                                                            square.size))
            pygame.display.flip()

        pygame.quit()
