from solution import prepare_meal
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual("eggs", prepare_meal(5))
        self.assertEqual("spam", prepare_meal(3))
        self.assertEqual("spam spam spam", prepare_meal(27))
        self.assertEqual("spam and eggs", prepare_meal(15))
        self.assertEqual("spam spam and eggs", prepare_meal(45))
        self.assertEqual("", prepare_meal(7))


if __name__ == '__main__':
    unittest.main()
