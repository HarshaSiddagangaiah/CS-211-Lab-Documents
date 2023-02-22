# Intervals

## The concepts covered in this lab are:

An introductory lab exercise for CIS 211, related to the Agenda main project. This exercise introduces

- classes, which is how we add new types of objects to Python,
- objects, which are the values of the new types we create,
- methods, which are like functions specialized to classes, and
- "magic" methods (aka "special" methods), which are automatically invoked through some built-in functions like `str`, or through operations like `+`

## Breif summary
This lab document provides a review of Python data types and types of data, and provides a series of exercises to demonstrate the use of types in Python. The document then walks the user through the creation of a Python source file to define the `"interval"` class, beginning with a header comment, followed by a class declaration, and then a constructor method that ensures the lower bound is not greater than the upper bound. The lab then introduces the concept of a membership method that tests whether a given integer is contained within an interval, and if intervals are overlapping, and if intervals are equal to each other interval.

## Plan for the lab

1. Downloading and Installing Pycharm IDE
2. Creating a `"Interval"` class to represent intervals and writing a constructor method.
3. Implementation of the following methods for the Interval class:
    - `contains` (check if an integer is contained in an interval)
    - `overlaps` (check if two intervals overlap)
    - `__eq__` (check if two intervals are equal/same)
    - `join` (joins two intervals)

Look in doc/HOWTO.md for detailed directions.
