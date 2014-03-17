import solution
import unittest
import sys

class Cat2Test(unittest.TestCase):

    def setUp(self):
        sys.argv.append('file.txt')
        sys.argv.append('file2.txt')
        self.content = []
        self.filename1 = sys.argv[1]
        self.filename2 = sys.argv[2]
        self.f = open(self.filename1, 'r')
        self.f2 = open(self.filename2, 'r')
        self.file_content = self.f.read()
        self.content.append(self.file_content)
        self.file_content = self.f2.read()
        self.content.append(self.file_content)

    def test_cat(self):
        self.assertEqual('\n\n'.join(self.content), solution.cat2())

    def tearDown(self):
        self.f.close()
        self.f2.close()


if __name__ == '__main__':
    unittest.main()
