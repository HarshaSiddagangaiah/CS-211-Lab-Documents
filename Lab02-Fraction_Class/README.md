# Fraction_Class

### The concepts covered in this lab are:

1. Object-Oriented Programming (OOP) concepts in Python
2. Defining and implementing classes and objects in Python
3. Magic and non-magic methods in Python
4. Type hinting and Error handling in Python

### Brief Summary
In this lab, you will code a Python class to represent `fraction` objects. The lab is divided into several coding steps, and in each step, you will learn and practice a different aspect of object-oriented programming, such as defining magic and non-magic methods, creating methods that generate new objects and modify the caller object, and type hinting.

You will begin by defining the Fraction class and its constructor method, where you will check for invalid input cases such as negative numerator or denominator and division by zero. Then, you will define the str and repr magic methods to control how the fraction objects are printed and displayed in the debugger.

In the next step, you will define the multiplication and addition magic methods to perform arithmetic operations on fractions. You will also learn how to create new Fraction objects from these operations without modifying the original fractions.

Finally, you will define a method to `simplify` fractions and integrate it into the constructor, `multiplication`, and `addition` methods.

### Plan for the lab

1. Class definition and constructor method init.
2. Implementing `str` and `repr` magic methods.
3. Implementing `mul` and `add` magic methods.
4. Implementing a `simplify` method that reduces a fraction to its simplest terms.
5. Integrating `simplify` into `init`, `add`, and `mul`.

Look in doc/HOWTO.md for detailed directions.
