# Recursion Review

The purpose of this lab exercise is to provide you with more practice on doing recursion in OOP.

You will build a tree-like data structure using three concrete subclasses of one abstract class.

The abstract class is defined as follows:

```python
class Creature(object):

    def __init__(self):
        raise NotImplementedError("Abstract classes should not be instanciated")

    def __str__(self) -> str:
        raise NotImplementedError("Abstract class methods should not be called")

    def search(self, value: str) -> bool:
        raise NotImplementedError("Abstract class methods should not be called")
```

The 3 concrete classes are named: Orthrus[Links to an external site]([url](https://en.wikipedia.org/wiki/Orthrus))., CerberusLinks to an external site., and Head. 

All three should have the following methods:

- `__str__(self) -> str`
  - to provide a string representation for the class
- `search(self, name: str) -> bool`
- - a method that searches through the data structure for a specific name

The attributes for each class should be as follows:

- `Orthrus`
  - `left: Creature`
  - `right: Creature`
- `Cerberus`
  - `left: Creature`
  - `middle: Creature`
  - `right: Creature`
- `Head`
  - `name: str`

When you are done coding the classes you should be able to execute code like the following:

```python
>>> doggy1 = Head("Kane")
>>> doggy2 = Head("Wolfie")
>>> doggy3 = Head("Rugal")
>>> doggy4 = Head("Taker")
>>> ort1 = Orthrus(doggy1, doggy2)
>>> ort2 = Orthrus(doggy3, Head("Jeff"))
>>> cer = Cerberus(ort1, doggy4, ort2)

>>> print(cer)
Kane Wolfie Taker Rugal Jeff

>>> cer.search("Drogon")
False

>>> cer.search("Rugal")
True
```

Submit a file named `"Creatures.py"` with your code.
