# Fraction Class

In this lab session, you'll code a new Python class to represent Fraction objects.

The main topics you'll practice during this lab are:

- Defining magic and non-magic methods.
- Creating methods that generate new objects.
- Creating methods that modify the caller object (a.k.a mutators).

Read the instructions carefully and ask for clarification from your TA/LA if necessary.

**IMPORTANT**: Remember to use type hinting in your method headers specifying the argument types and the return type.

## Coding Step 1: Class definition and constructor method `__init__`
Define a new Python class named `Fraction`.

As you already know, fractions have 2 parts: the numerator and the denominator.

The class should then have 2 **integer** attributes attributes `"num"` and `"den"`.

For this particular exercise, **we won't deal with negative fractions**. Hence, **neither the numerator nor the denominator can be `< 0`**.

Also remember that division by `0` is undefined. Thus, the **denominator cannot be `<= 0`**.

When coding your constructor method, **make sure you check for these cases** and return an appropriate **error message**.

Make sure to test your code constantly. At this point, you should be able to execute code like this:

```python
>>> f1 = Fraction(6,8)
>>> f2 = Fraction(4,0)
AssertionError: Denominator cannot be 0 and Numerator cannot be negative 
>>> f3 = Fraction(-3,4)
AssertionError: Denominator cannot be 0 and Numerator cannot be negative
```

## Coding Step 2: `__str__` and `__repr__` magic methods
The `__str__` magic method is used whenever you print an object. For our Fraction objects, we want the output of the `__str__` method to be a string of the **numerator and the denominator separated by a forward slash**, like so:

```python
>>> f1 = Fraction(5,8)
>>> print(f1)
5/8
```

The `__repr__` magic method is used by the debugger and should return a string that looks like a call to the constructor of the class. For our Fraction object, it should look like this:

```python
>>> f1 = Fraction(3,9)
>>> f1
Fraction(3,9)
```

## Coding Step 3: `__mul__` and `__add__` magic methods
Fraction multiplication is pretty straight forward: multiply both numerators by each other and both denominators by each other:


The fraction `__mul__` magic method should then receive a second Fraction object as an argument and perform the multiplication operation for fractions.

IMPORTANT: This method should create a **NEW** Fraction object and **NOT** modify the original fractions:

```python
>>> f1 = Fraction(3,4)
>>> f2 = Fraction(2,5)
>>> res = f1 * f2
>>> print(res)
6/20
>>> print(f2)
2/5
```

For fraction addition, the resulting denominator is again the multiplication of both the original denominators. The resulting numerator is obtained by multiplying each numerator by its counterpart denominator and then adding them together like so:


Same as with `__mul__`, the `__add__` magic method must create a NEW Fraction object:

```python
>>> f1 = Fraction(3,4)
>>> f2 = Fraction(2,5)
>>> res = f1 + f2
>>> print(res)
23/20
>>> print(f1)
3/4
```

## Coding Step 4: The Simplify method
Finally, we'll code a `simplify` method that reduces a fraction to its simplest terms. For example:


To achieve this we simply must find the **Greatest Common Divisor (GCD)** of both the numerator and denominator in the fraction.

Here's some code that finds the gcd for two numbers:

```python
def gcd(a, b) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
```

Once you have the GCD, simplifying the fraction means dividing both the numerator and denominator by the GCD. For example:


**IMPORTANT:** the simplify method **DOES NOT** create a new object, instead it **MODIFIES the object that calls it:**

```python
>>> f1 = Fraction(35,56)
>>> print(f1)
35/56
>>> f1.simplify()
>>> print(f1)
5/8
```

## Coding Step 5: Integrate simplify into `__init__`, `__add__`, and `__mul__`
Modify the code for `__init__`, `__add__`, and `__mul__` so that only minimal fractions are returned:

```python
>>> f1 = Fraction(4,6)
>>> print(f1)
2/3
>>> f2 = Fraction(15,20)
>>> print(f2)
3/4
>>> print(f1 * f2)
1/2
```

## Upload your code
When you finish, upload a file named `fractions.py` with your code to Canvas.

Remember, it's ok if you do not finish the full exercise. Simply upload whatever you managed to complete with your group.
