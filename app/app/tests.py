"""
Example Tests
"""

from django.test import SimpleTestCase
from app.calc import add, subtract


class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_number(self):
        """adding here"""
        res = add(5, 9)

        self.assertEqual(res, 14)

    def test_subtract_number(self):
        """subtract here"""
        res = subtract(10, 5)

        self.assertEqual(res, 5)
