from solution import count_substrings
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual(2, count_substrings("This is a test string", "is"))
        self.assertEqual(2, count_substrings("babababa", "baba"))
        self.assertEqual(4, count_substrings("Python is an awesome language to program in!", "o"))
        self.assertEqual(0, count_substrings("We have nothing in common!", "really?"))
        self.assertEqual(2, count_substrings("This is this and that is this", "this"))


if __name__ == '__main__':
    unittest.main()
