# Inheritance - Shape3D

### The concepts covered in this lab include:

1. Inheritance and subclassing in Python.
2. Abstract classes and methods.
3. Overriding and implementing methods in subclasses.
4. Polymorphism and using subclasses as instances of a parent class.

### Brief summary

This lab focuses on the concept of inheritance in object-oriented programming using Python. The lab requires the creation of concrete classes that inherit from an abstract class called `Shape3D`. The abstract class defines methods that are not implemented, and each concrete subclass must implement those methods with specific functionality. 
The lab covers creating concrete subclasses, defining class attributes, and implementing class methods. The lab culminates in testing the classes using a provided code snippet.

### Plan for the lab

1. Creating abstract class `Shape3D`, which has three methods: `__init__`, `volume`, and `area`.
2. Implementing a new method called `print_info` in the `Shape3D` abstract class that prints both the `volume` and `area` of the shape.
3. Creating a new class called `Cylinder` that inherits from the `Shape3D` abstract class. Implement methods to calculate the `volume` and `area` of a cylinder using the radius and height attributes.
4. Creating a new class called `Cuboid` that also inherits from the `Shape3D` abstract class. Implement methods to calculate the `volume` and `area` of a cuboid using the width, length, and height attributes.
5. Creating a new class called `Cube` that inherits from Cuboid. Since a cube is a specific type of cuboid, the `volume` and `area` calculation methods in Cube can simply use the ones already defined in Cuboid.
6. Testing the implementation by creating instances of `Cylinder`, `Cuboid`, and `Cube`, and calling the `print_info` method on each of them to verify that the calculations are correct.

Look in doc/HOWTO.md for detailed directions.
