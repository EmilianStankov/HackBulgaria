from solution import number_to_list
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual([1, 2, 3], number_to_list(123))
        self.assertEqual([9, 9, 9, 9, 9], number_to_list(99999))
        self.assertEqual([1, 2, 3, 0, 2, 3], number_to_list(123023))


if __name__ == '__main__':
    unittest.main()
