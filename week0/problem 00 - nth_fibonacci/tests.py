from solution import nth_fibonacci
import unittest


class Test(unittest.TestCase):
    """Testing the 250 problem from TC 608 SRM Div 250"""

    def test_problem_statement_cases(self):
        self.assertEqual(1, nth_fibonacci(1))
        self.assertEqual(1, nth_fibonacci(2))
        self.assertEqual(2, nth_fibonacci(3))
        self.assertEqual(3, nth_fibonacci(4))
        self.assertEqual(5, nth_fibonacci(5))
        self.assertEqual(8, nth_fibonacci(6))
        self.assertEqual(13, nth_fibonacci(7))
        self.assertEqual(21, nth_fibonacci(8))
        self.assertEqual(34, nth_fibonacci(9))
        self.assertEqual(55,nth_fibonacci(10))
        self.assertEqual(89, nth_fibonacci(11))
        self.assertEqual(144, nth_fibonacci(12))
        self.assertEqual(233, nth_fibonacci(13))
        self.assertEqual(377, nth_fibonacci(14))
        self.assertEqual(610, nth_fibonacci(15))
        self.assertEqual(987, nth_fibonacci(16))
        self.assertEqual(1597, nth_fibonacci(17))
        self.assertEqual(2584, nth_fibonacci(18))
        self.assertEqual(4181, nth_fibonacci(19))
        self.assertEqual(6765, nth_fibonacci(20))


if __name__ == '__main__':
    unittest.main()
