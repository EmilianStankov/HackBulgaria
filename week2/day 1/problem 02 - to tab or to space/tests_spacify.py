import unittest
import spacify
import string_utils


class SpacifyTest(unittest.TestCase):

    def setUp(self):
        self.f = open("file.txt", 'w')

    def test_spacify(self):
        f = open("file.txt", 'r')
        content = f.read()
        f.close()
        self.f.write(string_utils.tabs_to_spaces(content, 4))
        self.f.close()
        self.assertEqual(content.replace('\t', " " * 4),
            string_utils.tabs_to_spaces(content, 4))

    def tearDown(self):
        self.f.close()


if __name__ == '__main__':
    unittest.main()
