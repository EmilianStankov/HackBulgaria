from solution import sum_of_digits
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual(43, sum_of_digits(1325132435356))
        self.assertEqual(6, sum_of_digits(123))
        self.assertEqual(6, sum_of_digits(6))
        self.assertEqual(1, sum_of_digits(-10))
        self.assertEqual(0, sum_of_digits(0))


if __name__ == '__main__':
    unittest.main()
