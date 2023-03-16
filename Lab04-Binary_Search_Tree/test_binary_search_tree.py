import unittest
from binary_search_tree import Node, Leaf, Internal


class TestNode(unittest.TestCase):

    def test_sum_node_data_not_implemented(self):
        node = Node(5)
        with self.assertRaises(NotImplementedError):
            node.sum_node_data()

    def test_str_not_implemented(self):
        node = Node(5)
        with self.assertRaises(NotImplementedError):
            str(node)


class TestLeaf(unittest.TestCase):

    def test_sum_node_data(self):
        leaf = Leaf(5)
        self.assertEqual(leaf.sum_node_data(), 5)

    def test_str(self):
        leaf = Leaf(5)
        self.assertEqual(str(leaf), "5")


class TestInternal(unittest.TestCase):

    def setUp(self):
        self.l1 = Leaf(3)
        self.l2 = Leaf(6)
        self.l3 = Leaf(9)
        self.i = Internal(7, self.l2, self.l3)
        self.root = Internal(5, self.l1, self.i)

    def test_sum_node_data(self):
        self.assertEqual(self.root.sum_node_data(), 30)

    def test_str(self):
        self.assertEqual(str(self.root), "< 5 , 3 , < 7 , 6 , 9 > >")


if __name__ == '__main__':
    unittest.main()
