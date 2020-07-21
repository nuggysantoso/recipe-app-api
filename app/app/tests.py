from django.test import TestCase
from app.calc import add, substract


class CalcTests(TestCase):

    def test_add_number(self):
        """Test That Two Number Are Added Togehter"""
        self.assertEqual(add(3, 8), 11)

    def test_substract_number(self):
        """Test That Values Are Substracted and Returned"""
        self.assertEqual(substract(5, 11), 6)
