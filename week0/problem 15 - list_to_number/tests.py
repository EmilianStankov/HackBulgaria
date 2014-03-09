from solution import list_to_number
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual(123, list_to_number([1,2,3]))
        self.assertEqual(99999, list_to_number([9,9,9,9,9]))
        self.assertEqual(123023, list_to_number([1,2,3,0,2,3]))


if __name__ == '__main__':
    unittest.main()
