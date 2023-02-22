# Binary_Search_Tree

## The concepts covered in this lab are:

1. Binary Search Trees (BSTs) and their properties.
2. Abstract classes, concrete subclasses, and inheritance in object-oriented programming.
3. The construction of a binary search tree using the `Node`, `Leaf`, and `Internal` classes in Python.
4. The recursive nature of the sub class methods.

## Brief Summary
This lab provides a step-by-step guide on how to implement a Binary Search Tree (BST) using Python programming language. It covers the creation of three classes - `Node`, `Leaf`, and `Internal` - to represent the BST, and the implementation of various methods such as `sum_node_data` and `str` in these classes. The document walks the user through the process of building a BST using the `Internal` and `Leaf` classes, calling the `sum_node_data` method and printing the output. The lab provides a comprehensive introduction to building and working with BSTs in Python.

## Plan for the lab
1. Creation of three classes - `Node`, `Leaf`, and `Internal` - to represent the `BST`.
2. Definition of the `Node` class with a constructor that accepts an `integer value`, and an abstract method `sum_node_data` that sums the value of current node and all nodes below.
3. Implementation of `Leaf` and `Internal` classes inheriting `Node` class and with their respective constructors.
4. Implementation of the `sum_node_data` method in both `Internal` and `Leaf` classes to calculate the sum of nodes.
5. Running the program by creating a binary search tree using the `Internal` and `Leaf` classes, calling the `sum_node_data` method and printing the output.
6. Implementation of the `str` method in all three classes to provide the representation of the tree or subtree in the form of `<data, left, right>`.
