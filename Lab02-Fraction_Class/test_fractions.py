import unittest
from fractions import Fraction

class TestFraction(unittest.TestCase):

    def test_constructor(self):
        with self.assertRaises(ValueError):
            f = Fraction(4, 0)
        with self.assertRaises(ValueError):
            f = Fraction(-3, 4)

    def test_str(self):
        f = Fraction(5, 8)
        self.assertEqual(str(f), "5/8")

    def test_repr(self):
        f = Fraction(4, 9)
        self.assertEqual(repr(f), "Fraction(4,9)")

    def test_mul(self):
        f1 = Fraction(1, 4)
        f2 = Fraction(3, 5)
        res = f1 * f2
        self.assertEqual(str(res), "3/20")

    def test_add(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 5)
        res = f1 + f2
        self.assertEqual(str(res), "23/20")

    def test_simplify(self):
        f = Fraction(35, 56)
        f.simplify()
        self.assertEqual(str(f), "5/8")

if __name__ == '__main__':
    unittest.main()
