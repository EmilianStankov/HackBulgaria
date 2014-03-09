from solution import is_prime
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual(False, is_prime(1))
        self.assertEqual(True, is_prime(2))
        self.assertEqual(False, is_prime(8))
        self.assertEqual(True, is_prime(11))
        self.assertEqual(False, is_prime(-10))


if __name__ == '__main__':
    unittest.main()
