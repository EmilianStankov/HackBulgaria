import solution
import unittest
import sys

class CatTest(unittest.TestCase):

    def setUp(self):
        sys.argv.append('file.txt')
        self.filename = sys.argv[1]
        self.f = open(self.filename, 'r')
        self.content = self.f.read()

    def test_cat(self):
        self.assertEqual(self.content, solution.cat())

    def tearDown(self):
        self.f.close()


if __name__ == '__main__':
    unittest.main()
