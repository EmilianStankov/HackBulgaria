import ext
import unittest, os


class ExtTest(unittest.TestCase):

    def test_ext(self):
        self.assertEqual(1, ext.count_files('.py', 'folder'))
        self.assertEqual(0, ext.count_files('py', 'folder'))


if __name__ == '__main__':
    unittest.main()
