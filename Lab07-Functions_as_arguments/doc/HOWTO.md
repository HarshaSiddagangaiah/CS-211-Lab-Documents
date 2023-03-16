# Functions as arguments

When a function is defined in Python, the name of the function is a pointer to the location in memory where the function is stored, just as with any other object.

```python
>>> def plus_one(x:int) -> int:
...     return x + 1

>>> plus_one
<function plus_one at 0x7f886d915b00>

>>> def minus_one(x:int) -> int:
... return x - 1

>>> minus_one
<function minus_one at 0x7f886d915b90>
```

We already know that we can pass any type of object as the argument for a method or function. This means that there's nothing stopping us from using functions as arguments for other functions or methods:

```python
>>> def composite_double_function(function: Callable, argument: int) -> int:
...     return function(argument) * 2

>>> composite_double_function(plus_one, 3)
8

>>> composite_double_function(minus_one, 3)
4
```

Notice that the type hint for functions is `Callable`. You need to import the type from typing as you have been doing for lists or tuples.

```python
>>> from typing import Callable
```

## Lambda functions
Lambda functions are small functions with no name. They're most useful when used as arguments for other functions.

For example, instead of defining the `plus_one` function as we did previously, we can simply use an equivalent lambda function and use it as an argument:

```python
>>> composite_double_function(lambda x: x + 1, 3)
8
```

The syntax of lambda functions is as follows:

```python
lambda arguments : expression
```

## Function aliasing
Similarly, as with any other object, we can create aliases for functions, and then use these aliases to call them:

```python
>>> f = plus_one
>>> f
<function plus_one at 0x7f886d915b00>
>>> f(4)
5
```

This means, for example, that we can create a list where the elements are pointers to functions.

```python
>>> function_list = [plus_one, minus_one]
```

Of course, we could also create the list using lambda functions, or a combination of the two:

```python
>>> function_list = [plus_one, lambda x : x - 1]
```

And this allows us to write code like this:

```python
>>> for function in function_list:
...     print(function(4))
5
3
```

That is, we only need to refer to a specific element in the list to use whichever function we desire:

```python
>>> function_list[1](11)
10
```

This a way to implement caller dispatch, where we use the value of a variable (in this case the index of the list) to connect to a function.

This can be useful for example in a network environment where some process sends you command codes, then by creating a dispatcher, you can translate the codes into executable code.

Another, very relevant example, is to execute the instructions in a CPU where, depending on the Opcode of the instruction, different actions are taken.

## FunctionDispatcher Class
In this exercise, you will get some practice using functions as arguments and taking advantage of function aliasing to create a dispatcher.

### Step 1
Define the following functions:

- A function called `total_sum` that receives a list of integers as its sole argument and returns the sum of its elements. 
- A function called `apply` that receives a function as its first argument, and a list of integers as a second argument. This function should return a list created by applying the argument function to every element in the original list.
- Create a function called `square` that receives a list of integers as its sole argument and returns a list of the same length where every element of the original list has been squared. Use the `apply` function and a lambda function to create this function easily.
- Create a function called `magnitude` that receives a list of integers called `vector` as its sole argument and returns the magnitude of the vector. The magnitude of a vector is defined mathematically as the square root of the sum of its squared elements. For example, for a two-element vector: 
 . For a three-element vector, $|[x, y]| = \sqrt{x^2 + y^2}$
 , and so on. $|[x, y, z]| = \sqrt{x^2 + y^2 + z^2}$

### Step 2
Store references to the `total_sum`, `square`, and `magnitude` functions in a Python dictionary called `dispatch_table`. 

In the example found at the bottom of these instructions, I'm using integers as keys: 1 for total_sum, 2 for square, and 3 for magnitude. However, you can use strings or whatever you'd like.

### Step 3
Create a Python class called `FunctionDispatcher`.

The init method should receive a dictionary of functions like the one you created in Step 2.

Its only method is called `process_command` and receives two arguments:

- A key indicating the command to execute
- A list of integers
The `process_command` method should then just use the key to call the appropriate function on the array of integers and return the result.

Once done, you should be able to run code like the following: 

```python
>>> fd = FunctionDispatcher(dispatch_table)
>>> fd.process_command(1, [3,4])
7
>>> fd.process_command(2, [3,4])
[9, 16]
>>> fd.process_command(3, [3,4])
5.0
```
Submit your code to Canvas in a file named `functionDispatcher.py` when you're done.
