import unittest
from functiondispatcher import *


class TestFunctionDispatcher(unittest.TestCase):

    def test_total_sum(self):
        self.assertEqual(total_sum([3, 4]), 7)
        self.assertEqual(total_sum([-1, 0, 1]), 0)
        self.assertEqual(total_sum([]), 0)

    def test_apply(self):
        self.assertEqual(apply(lambda x: x + 1, [3, 4]), [4, 5])
        self.assertEqual(apply(lambda x: x ** 2, [3, 4]), [9, 16])
        self.assertEqual(apply(lambda x: x * 2, []), [])

    def test_square(self):
        self.assertEqual(square([3, 4]), [9, 16])
        self.assertEqual(square([-1, 0, 1]), [1, 0, 1])
        self.assertEqual(square([]), [])

    def test_magnitude(self):
        self.assertEqual(magnitude([3, 4]), 5.0)
        self.assertEqual(magnitude([-1, 2]), math.sqrt(5))
        self.assertEqual(magnitude([]), 0)

    def test_FunctionDispatcher(self):
        fd = FunctionDispatcher(dispatch_table)
        self.assertEqual(fd.process_command(1, [3, 4]), 7)
        self.assertEqual(fd.process_command(2, [3, 4]), [9, 16])
        self.assertEqual(fd.process_command(3, [3, 4]), 5.0)
        self.assertRaises(KeyError, fd.process_command, 4, [3, 4])
        self.assertRaises(TypeError, fd.process_command, 2, [3, "a"])
