import ext
import unittest, os


class ExtTest(unittest.TestCase):

    def test_ext(self):
        self.assertEqual(2, ext.count_files('.py'))
        self.assertEqual(0, ext.count_files('py'))


if __name__ == '__main__':
    unittest.main()
