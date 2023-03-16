# Inheritance - Shape3D

In this lab, we will create concrete classes that inherit from an abstract class.

The abstract class from which the concrete classes will inherit is called `Shape3D`.

```python
class Shape3D:

    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")

    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")
```

The **volume** and **area** methods are not implemented in the abstract class leaving the specific implementation to each concrete subclass.

## Coding step 1
Add a method called `print_info` to the abstract class. This method, unlike the volume and area, **should** be implemented. The **print_info** method must print a string with both the volume and the area of the shape like so:

`Area: XXXXX`  `Volume: XXXXX`

where the `XXXXX` stands for the actual results from the area and volume calculations.

## Coding step 2
Add a concrete subclass `Cylinder` that inherits from `Shape3D`.

A Cylinder has 2 attributes: `radius` and `height`. Both should be of the `float` type.

The formula for the `volume of a Cylinder` is as follows:  $\pi * radius^2 * height$


The formula for the `area of a Cylinder` is as follows: $2 * \pi * radius^2 + 2 * \pi * radius * height$


## Coding step 3
Add a concrete subclass `Cuboid` that inherits from `Shape3D`.

A Cuboid has 3 attributes: `width`, `length`, and `height`. All should have `float` type.

The formula for the `volume of a Cuboid` is as follows:


The formula for the `area of a Cylinder` is as follows:


## Coding step 4
Add a concrete subclass `Cube` that inherits from `Cuboid`.

A Cube only has one attribute: `width`. It should have `float` type.

You **do NOT** need to implement the volume and area methods for the `Cube` class since they work exactly the same as the ones of its super class.

## Coding step 5
Once you're done coding the subclasses you should be able to run the following code:

```python
>>> cyl = Cylinder(3,5)
>>> cuboid = Cuboid(6,4,9)
>>> lst = [ Cube(3), cyl, cuboid ]
>>> for shape in lst:
        print(shape.print_info())
Area: 54  Volume: 27
Area: 150.79644737231007  Volume: 141.3716694115407
Area: 228  Volume: 216
```

Submit a file named `Shape3D.py` with your code to Canvas.
