
# 0x0C. Python - Almost a circle
This project provides a set of classes for creating and manipulating geometric shapes in Python.

#### __Background Context__
The AirBnB project pre-plan. This project will help you be ready for it.

In this project will review Python programming concepts to use and start building the project:

- Import, __Exceptions__, Class, __Private attribute__
- __Getter/Setter__, Class method, __Static method__
- Inheritance, __Unittest__, Read/Write file

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Base Class](#base-class)
  - [Rectangle Class](#rectangle-class)
  - [Square Class](#square-class)
- [Testing](#testing)

## Installation

To use this project, you need to have Python installed on your system. You can download and install Python from the official Python website at [python.org](https://www.python.org/).

## Usage

The project consists of several modules located in the `models` directory. Here's a brief overview of each class and their associated tasks:

### Base Class

The `Base` class serves as the base class for other shape classes. It provides common functionality and attributes shared by all shapes.

| Task     | Description                                                                                   |
|----------|-----------------------------------------------------------------------------------------------|
| Task 1   | Implement the `Base` class with attributes and methods required by other shape classes.       |
| Task 14  | Add a static method `to_json_string` that returns the JSON string representation of a list of dictionaries. |
| Task 15  | Add a class method `save_to_file` that writes the JSON string representation of a list of instances to a file. |
| Task 16  | Add a static method `from_json_string` that returns a list of instances from a JSON string representation. |
| Task 17  | Add a class method `create` that returns an instance with all attributes already set.           |
| Task 18  | Add a class method `load_from_file` that returns a list of instances from a file.                |

### Rectangle Class

The `Rectangle` class represents a rectangle shape with width, height, and position attributes.

| Task     | Description                                                                                   |
|----------|-----------------------------------------------------------------------------------------------|
| Task 2   | Implement the `Rectangle` class with attributes and methods specific to rectangles.           |
| Task 3   | Override the `__str__` method to customize the string representation of a rectangle instance. |
| Task 4   | Add a method `display` that prints the rectangle using the `#` character.                      |
| Task 5   | Add a method `area` that returns the area of the rectangle.                                    |
| Task 6   | Update the `display` method to take into account the position (x, y) of the rectangle.         |
| Task 7   | Add a method `update` that assigns attributes to the rectangle instance.                       |
| Task 8   | Override the `__str__` method to customize the string representation of a rectangle instance. |
| Task 9   | Add a method `to_dictionary` that returns the dictionary representation of a rectangle.        |
| Task 12  | Add a static method `save_to_file` that writes the JSON string representation of a list of rectangle instances to a file. |
| Task 14  | Add a class method `load_from_file` that returns a list of rectangle instances from a file.    |

### Square Class

The `Square` class represents a square shape, which is a special case of a rectangle with equal width and height.

| Task     | Description                                                                                   |
|----------|-----------------------------------------------------------------------------------------------|
| Task 10  | Add a method `size` getter and setter to manipulate the size attribute of a square.           |
| Task 11  | Update the `update` method to assign attributes to the square instance.                        |
| Task 13  | Add a method `to_dictionary` that returns the dictionary representation of a square.           |

## Testing

This project includes a set of unit tests to ensure the correctness of the implemented classes and methods. The tests are located in the `tests/test_models` directory and can be run using the following command:

```bash
python3 -m unittest discover tests
```




