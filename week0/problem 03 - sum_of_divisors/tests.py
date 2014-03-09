from solution import sum_of_divisors
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual(15, sum_of_divisors(8))
        self.assertEqual(8, sum_of_divisors(7))
        self.assertEqual(1, sum_of_divisors(1))
        self.assertEqual(2340, sum_of_divisors(1000))


if __name__ == '__main__':
    unittest.main()
