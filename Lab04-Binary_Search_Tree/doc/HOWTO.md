# Binary Search Tree(BST) 

We will be implementing three classes to represent binary search trees.

We will have abstract class `Node` and two concrete subclasses `Leaf` and `Internal`.

Consider the following binary search tree:

Binary Search Tree  

 

We say node 5 is the parent of node 3 and node 7, and we say node 3 and node 7 are the children of node 5.

Nodes are represented as both circles and boxes in this example. Circle nodes are of class `Internal`. They have children. Box nodes are of class `Leaf` and they don't have children.

(Note that this is not the only way to implement a Binary Search Tree)


## Step 1
Make a Python file called `Binary_Search_Tree.py`.

Create a class `Node`, whose constructor takes a parameter value of type `int`. Inside the constructor,
create a class variable called `node_data` to save the parameter value.

Make method `sum_node_data` in class `Node`, raising `NotImplementedError` with an error message.

Abstract method `sum_node_data` will sum the value of current node and all nodes below. For example, if we call `sum_node_data` on node 5 of the above figure, it will give us 30.

## Step 2
Make a class `Leaf` inheriting `Node`, whose constructor takes a single integer value `node_data`.
Make a class `Internal` inheriting `Node`, whose constructor takes the following values:
`node_data: int`, `left: Node`, and `right: Node`.

The `left` and `right` are the `left` and `right` children of an `Internal` node.

## Step 3
Now implement `sum_node_data` method in both `Internal` and `Leaf`.

Note that a child of an `Internal` node could be a `Leaf` node, like both children of node 7, or it could be another `Internal` node, like the right child of node 5.

You can assume that both children of `Internal` are not `None`. 

## Step 4
Add the following code to the end of your file and run your program.

```python
def main(): 
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root.sum_node_data())

if __name__ == '__main__':
    main()
 ```

## Step 5
At this point you should see the recursive nature of the `sum_node_data` method.

Now implement the `__str__` method in all three classes so that it gives us the representation of a tree or a subtree in the form of `<data, left, right>`. For example, if we add the following line to our main function:

```python
print(root)
```
Our output is:

`<5, 3, <7, 6, 9>>`

 

### Deliverable:
 

Upload your `Binary_Search_Tree.py` file to Canvas at the end of the lab.

 

