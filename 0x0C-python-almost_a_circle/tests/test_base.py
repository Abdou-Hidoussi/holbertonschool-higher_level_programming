#!/usr/bin/python3
"""unitest for base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """testing for base class"""

    def test_docstring(self):
        self.assertIsNotNone(Base.__doc__)

    def test_id_incrementation(self):
        t1 = Base()
        self.assertEqual(t1.id, 1)
        t2 = Base()
        self.assertEqual(t2.id, 2)

