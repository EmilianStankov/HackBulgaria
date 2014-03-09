from solution import is_int_palindrom
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual(True, is_int_palindrom(1234321))
        self.assertEqual(False, is_int_palindrom(1234))
        self.assertEqual(True, is_int_palindrom(1))
        self.assertEqual(False, is_int_palindrom(42))
        self.assertEqual(True, is_int_palindrom(100001))
        self.assertEqual(True, is_int_palindrom(999))
        self.assertEqual(False, is_int_palindrom(123))


if __name__ == '__main__':
    unittest.main()
