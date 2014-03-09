from solution import count_words
import unittest


class Test(unittest.TestCase):

    def test_problem_statement_cases(self):
        self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, count_words(["apple", "banana", "apple", "pie"]))
        self.assertEqual({'ruby': 1, 'python': 3}, count_words(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    unittest.main()
