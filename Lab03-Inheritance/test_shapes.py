import unittest
import math
from shapes import Shape3D, Cylinder, Cuboid, Cube


class TestShapes(unittest.TestCase):

    def test_cylinder(self):
        c = Cylinder(3, 5)
        self.assertAlmostEqual(c.volume(), 141.3716694, places=4)
        self.assertAlmostEqual(c.area(), 150.7964474, places=4)
        self.assertEqual(c.print_info(), "Area: 150.79644737231007, Volume: 141.3716694115407")

    def test_cuboid(self):
        c = Cuboid(6, 4, 9)
        self.assertAlmostEqual(c.volume(), 216, places=4)
        self.assertAlmostEqual(c.area(), 228, places=4)
        self.assertEqual(c.print_info(), "Area: 228, Volume: 216")

    def test_cube(self):
        c = Cube(3)
        self.assertAlmostEqual(c.volume(), 27, places=4)
        self.assertAlmostEqual(c.area(), 54, places=4)
        self.assertEqual(c.print_info(), "Area: 54, Volume: 27")


if __name__ == '__main__':
    unittest.main()
