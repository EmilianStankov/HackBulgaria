import solution
import unittest
import sys

class SumTest(unittest.TestCase):

    def setUp(self):
        sys.argv.append('numbers.txt')

    def test_sum(self):
        self.assertEqual(48462, solution.sum_numbers())


if __name__ == '__main__':
    unittest.main()
