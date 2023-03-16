import unittest
from creatures import *


class TestCreature(unittest.TestCase):

    def test_orthrus(self):
        doggy1 = Head("Kane")
        doggy2 = Head("Wolfie")
        ort1 = Orthrus(doggy1, doggy2)

        self.assertEqual(str(ort1), "Kane Wolfie")
        self.assertTrue(ort1.search("Kane"))
        self.assertTrue(ort1.search("Wolfie"))
        self.assertFalse(ort1.search("Taker"))

    def test_cerberus(self):
        doggy1 = Head("Kane")
        doggy2 = Head("Wolfie")
        doggy3 = Head("Rugal")
        doggy4 = Head("Taker")
        ort1 = Orthrus(doggy1, doggy2)
        ort2 = Orthrus(doggy3, Head("Jeff"))
        cer = Cerberus(ort1, doggy4, ort2)

        self.assertEqual(str(cer), "Kane Wolfie Taker Rugal Jeff")
        self.assertTrue(cer.search("Kane"))
        self.assertTrue(cer.search("Wolfie"))
        self.assertTrue(cer.search("Rugal"))
        self.assertTrue(cer.search("Taker"))
        self.assertTrue(cer.search("Jeff"))
        self.assertFalse(cer.search("Drogon"))

    def test_head(self):
        doggy = Head("Kane")

        self.assertEqual(str(doggy), "Kane")
        self.assertTrue(doggy.search("Kane"))
        self.assertFalse(doggy.search("Taker"))


if __name__ == '__main__':
    unittest.main()
