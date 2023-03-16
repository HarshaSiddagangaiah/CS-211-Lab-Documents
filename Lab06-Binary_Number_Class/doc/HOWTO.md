# BinaryNumber Class

Everything in Python is represented as binary digits and it natively provides operators to perform bitwise operations such as and `&`,  or `|`, right-shift `>>`, and left-shift `<<`.

In this Lab, you will create your own `BinaryNumber` class to deal with unsigned, positive binary numbers. The goal of the Lab is to provide you with some practice in dealing with binary number representations and, by doing so, hopefully, get some additional insight that will prove useful when completing this week's project.

## Specifications
`BinaryNumber` only has one attribute - `bits` - which is an integer list and all of its elements are either `1` or `0`.

Here's an instance example:

```python
bn = BinaryNumber([1,0,1,0,1])
```

## Methods

Implement the following methods for the class:

- `__or__`
- `__and__`
- `left_shift`
- `right_shift`

**IMPORTANT NOTE:**  `__or__` and `__and__` produce a new BinaryNumber object. The shifting methods, however, work in-place, modifying the current object.

**IMPORTANT NOTE 2:** `__or__` and `__and__`  only work for BinaryNumber objects with the same length.

If you have any questions regarding the functionality of these methods, please refer to the the TA/LA..

When you're done you should be able to use your code to perform operations like the following:

```python
>>> bn = BinaryNumber([1,0,1,0,1])
>>> bn2 = BinaryNumber([1,1,1,0,0])
>>> print("1st binary number =",bn)
1st binary number = [1, 0, 1, 0, 1]

>>> print("2nd binary number =", bn2)
2nd binary number = [1, 1, 1, 0, 0]

>>> print("AND",bn & bn2)
AND [1, 0, 1, 0, 0]

>>> print("OR", bn | bn2)
OR [1, 1, 1, 0, 1]

>>> bn.right_shift()
>>> print("1st number right-shifted =", bn)
1st number right-shifted = [0, 1, 0, 1, 0]

>>> bn.left_shift()
>>> print("1st number left-shifted =", bn)
1st number left-shifted = [1, 0, 1, 0, 0]
```

## Extract Method
Implement an `extract` method for the `BinaryNumber` class that receives two integer indexes (start and end) and then extracts the bits in those positions and returns a new `BinaryNumber` object with those bits.


- `0 <= start < end`
- `start < end <= binary number length`
- The extracted BinaryNumber must have the length as the original.

IMPORTANT NOTE: do NOT simply use list slicing to implement the extract method. Use the `__or__`, `__and__`, and shift methods that you implemented previously. This will allow you to practice for the upcoming project.

Once you're done you should be able to use the code as follows:

```python
                       7  6  5  4  3  2  1  0
>>> bn = BinaryNumber([1, 0, 0, 1, 0, 1, 1, 1])
>>> extracted = bn.extract(2, 4)
>>> print(extracted)
[0, 0, 0, 0, 0, 1, 0, 1]
```

Submit a file named `binarynumber.py` with your code
