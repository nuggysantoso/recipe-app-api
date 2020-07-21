from django.test import TestCase
from app.calc import add

class CalcTests(TestCase):

    def test_add_number(self):
        """Test That Two Number Are Added Togehter"""
        self.assertEqual(add(3, 8), 11)
