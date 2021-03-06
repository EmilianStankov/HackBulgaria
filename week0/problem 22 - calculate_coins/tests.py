from solution import calculate_coins
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual({1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0}, calculate_coins(0.53))
        self.assertEqual({1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}, calculate_coins(8.94))
        self.assertEqual({1: 1, 2: 1, 100: 16, 5: 1, 10: 0, 50: 1, 20: 0}, calculate_coins(16.58))

if __name__ == '__main__':
    unittest.main()
