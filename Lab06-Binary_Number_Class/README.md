# Binary Number Class

## The concepts covered in this lab include:
1. Working with binary numbers and performing bitwise operations and bit extraction in Python
2. Implementing built-in methods in Python classes
3. Using in-place modification of objects in Python
4. Creating and working with Python lists and performing list Slicing.

## Breif summary
This lab describes a programming exercise to create a BinaryNumber class in Python, which deals with unsigned, positive binary numbers. The class has one attribute, `"bits"`, which is an integer list with elements of either 1 or 0. This lab requires implementing various methods such as `__or__`, `__and__`, `left_shift`, `right_shift`, and an `extract` method. This lab provides instructions and specifications for implementing these methods and gives example usage code for the BinaryNumber class.

## Plan for the lab

1. Introduction to bitwise operations and binary number representation in Python
2. Creation of a custom `BinaryNumber` class to handle unsigned, positive binary numbers
3. Implementation of the class's single attribute `bits` - as an integer list with elements of either `1` or `0`
4. Implementation of the following methods for the BinaryNumber class:
   - `__or__` (bitwise or)
   - `__and__` (bitwise and)
   - `left_shift` (bitwise left shift)
   - `right_shift` (bitwise right shift)
5. In-place modification of current object for `left_shift` and `right_shift` methods
6. Implementation of an 'extract' method to extract bits in a given range and return a new BinaryNumber object with those bits

Look in doc/HOWTO.md for detailed directions.
