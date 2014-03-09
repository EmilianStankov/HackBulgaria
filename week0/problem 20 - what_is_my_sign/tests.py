from solution import what_is_my_sign
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual("Leo", what_is_my_sign(5, 8))
        self.assertEqual("Aquarius", what_is_my_sign(29, 1))
        self.assertEqual("Cancer", what_is_my_sign(30, 6))
        self.assertEqual("Gemini", what_is_my_sign(31, 5))
        self.assertEqual("Aquarius", what_is_my_sign(2, 2))
        self.assertEqual("Taurus", what_is_my_sign(8, 5))
        self.assertEqual("Capricorn", what_is_my_sign(9, 1))


if __name__ == '__main__':
    unittest.main()
