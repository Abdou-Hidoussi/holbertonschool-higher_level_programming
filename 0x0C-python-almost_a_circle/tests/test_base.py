#!/usr/bin/python3
"""unitest for base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """testing for base class"""

    def test_doc_Base(self):
        self.assertIsNotNone(Base.__doc__)

    def test_id_inc_base(self):
        t1 = Base()
        self.assertEqual(t1.id, 1)
        t2 = Base()
        self.assertEqual(t2.id, 2)

    def test_doc_Rectangle(self):
        self.assertIsNotNone(Rectangle.__doc__)

    def test_id_inc_rect(self):
        t1 = Rectangle(5, 5)
        self.assertEqual(t1.id, 3)
        t2 = Rectangle(6, 6)
        self.assertEqual(t2.id, 4)