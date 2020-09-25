#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
class testlist(unittest.TestCase):
    def test_max(self):
        with self.assertRaises(TypeError):
            max_integer(["testing string", 1, 2])
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer("max"), "x")
        self.assertEqual(max_integer([5, 10, 88]), 88)
        self.assertEqual(max_integer([7, -1, 1]), 7)
        self.assertEqual(max_integer([5, 140, 20]), 140)
        self.assertEqual(max_integer([[200, 1200], [500, 20]]), [500, 20])
        self.assertEqual(max_integer([1]), 1)
