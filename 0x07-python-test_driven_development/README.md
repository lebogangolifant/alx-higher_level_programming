
# 0x07 Python - Test-driven development

Test-driven development; tasks solutions in Python.

## Concepts

- __Unit Testing__
- __Doc Tests__

## Function Files

| File | Description |
| ---- | ----------- |
| 0-add_integer.py | Adds two integers and returns the result. |
| 2-matrix_divided.py | Divides all elements of a matrix by a given divisor. |
| 3-say_my_name.py | Prints a formatted string with the provided first and last name. |
| 4-print_square.py | Prints a square of a specified size. |
| 5-text_indentation.py | Indents a given text based on certain conditions. |
| 6-max_integer.py | Finds the maximum integer in a given list. |


## Tests Files Folder

| File | Test Description |
| ---- | ----------------|
| 0-add_integer.txt | Test cases for the `add_integer` function using the `0-add_integer.txt` test file. |
| 2-matrix_divided.txt | Test cases for the `matrix_divided` function using the `2-matrix_divided.txt` test file. |
| 3-say_my_name.txt | Test cases for the `say_my_name` function using the `3-say_my_name.txt` test file. |
| 4-print_square.txt | Test cases for the `print_square` function using the `4-print_square.txt` test file. |
| 5-text_indentation.txt | Test cases for the `text_indentation` function using the `5-text_indentation.txt` test file. |
| 6-max_integer_test.py | Test cases for the `max_integer` function using the `6-max_integer_test.py` test file. |

## Running the tests

__To run the doc tests, use the following command:__

```
python3 -m doctest -v ./tests/filename.txt
```
or
```
python3 -m doctest -v ./tests/filename.txt | tail -2
```

__To run the unit tests, use the following command:___

```
python3 -m unittest tests.6-max_integer_test 2>&1 
```
or
```
python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
```

The commands will automatically discover and execute all the test files in the `tests` directory. The test results will be displayed, indicating whether each test passed or failed.

