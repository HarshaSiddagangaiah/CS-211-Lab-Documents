import unittest
from binarynumber import BinaryNumber


class TestBinaryNumber(unittest.TestCase):

    def test_init(self):
        bn = BinaryNumber([1, 0, 1, 0, 1])
        self.assertEqual(str(bn), "[1, 0, 1, 0, 1]")

    def test_or(self):
        bn1 = BinaryNumber([1, 0, 1, 0, 1])
        bn2 = BinaryNumber([1, 1, 1, 0, 0])
        result = bn1 | bn2
        self.assertEqual(str(result), "[1, 1, 1, 0, 1]")

    def test_and(self):
        bn1 = BinaryNumber([1, 0, 1, 0, 1])
        bn2 = BinaryNumber([1, 1, 1, 0, 0])
        result = bn1 & bn2
        self.assertEqual(str(result), "[1, 0, 1, 0, 0]")

    def test_left_shift(self):
        bn = BinaryNumber([1, 0, 1, 0, 1])
        bn.left_shift()
        self.assertEqual(str(bn), "[0, 1, 0, 1, 0]")

    def test_right_shift(self):
        bn = BinaryNumber([1, 0, 1, 0, 1])
        bn.right_shift()
        self.assertEqual(str(bn), "[0, 1, 0, 1, 0]")

    def test_extract(self):
        bn = BinaryNumber([1, 0, 0, 1, 0, 1, 1, 1])
        result = bn.extract(2, 4)
        self.assertEqual(str(result), "[0, 0, 0, 0, 0, 1, 0, 1]")


if __name__ == '__main__':
    unittest.main()
