import string_utils
import unittest


class StringUtilsTest(unittest.TestCase):
    def test_lines(self):
        self.assertEqual(['it', 'works'], string_utils.lines('it\nworks'))
        self.assertEqual(['this', 'works', 'too'],
            string_utils.lines('this\nworks\ntoo'))

    def test_unlines(self):
        self.assertEqual('it\nworks', string_utils.unlines(['it', 'works']))
        self.assertEqual('this\nworks\ntoo',
            string_utils.unlines(['this', 'works', 'too']))

    def test_words(self):
        self.assertEqual(['it', 'works'], string_utils.words('it works'))
        self.assertEqual(['this', 'works', 'too'],
            string_utils.words('this works too'))

    def test_unwords(self):
        self.assertEqual('it works', string_utils.unwords(['it', 'works']))
        self.assertEqual('this works too',
            string_utils.unwords(['this', 'works', 'too']))

    def test_tabs_to_spaces(self):
        self.assertEqual('it    works',
            string_utils.tabs_to_spaces('it\tworks'))
        self.assertEqual('this    works    too',
            string_utils.tabs_to_spaces('this\tworks\ttoo'))

if __name__ == '__main__':
    unittest.main()
