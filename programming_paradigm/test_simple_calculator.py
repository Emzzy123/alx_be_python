import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(11, 22), 33)
        
# Remember to write additional test methods for subtract, multiply, and divide.
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(12, 33), -21)
        self.assertEqual(self.calc.subtract(14, 7.5), 6.5)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-3, -6), 18)
        self.assertEqual(self.calc.multiply(9, -3), -27)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(19, 4), 4.75)
        self.assertRaises(self.calc.divide(4, 0), None)