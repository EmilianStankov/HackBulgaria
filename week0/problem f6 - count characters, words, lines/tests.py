import solution
import unittest
import sys

class CountLinesTest(unittest.TestCase):

    def test_count_chars(self):
        sys.argv.append('chars')
        sys.argv.append('story.txt')
        self.assertEqual(1032, solution.counter())

    def test_count_lines(self):
        sys.argv[1] = 'lines'
        self.assertEqual(6, solution.counter())

    def test_count_words(self):
        sys.argv[1] = 'words'
        self.assertEqual(166, solution.counter())


if __name__ == '__main__':
    unittest.main()
