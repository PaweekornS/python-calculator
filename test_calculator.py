import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -2), -3)
        self.assertEqual(self.calc.add(-5, 3), -2)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(4, -2), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 4), 24)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(-10, -5), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 8), 2)
        self.assertEqual(self.calc.modulo(-7, 5), 3)

if __name__ == '__main__':
    unittest.main()