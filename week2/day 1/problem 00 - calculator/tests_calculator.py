import calculator
import unittest


class CalculatorTest(unittest.TestCase):
    """Testing the very simple and trivial calculator module"""
    def test_add(self):
        self.assertEqual(5 + 6, calculator.add(5, 6))

    def test_minus(self):
        self.assertEqual(5 - 6, calculator.minus(5, 6))

    def test_multiply(self):
        self.assertEqual(5 * 5, calculator.multiply(5, 5))

    def test_float_division(self):
        self.assertEqual(5 / 2, calculator.float_division(5, 2))

    def test_integer_division(self):
        self.assertEqual(99 // 4, calculator.integer_division(99, 4))

    def test_modulo(self):
        self.assertEqual(7 % 3, calculator.modulo(7, 3))

if __name__ == '__main__':
    unittest.main()
