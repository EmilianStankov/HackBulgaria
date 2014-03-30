import create_company
import unittest
import sqlite3


class TestCreateCompany(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("test.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS company
        (id, name, monthly_salary, yearly_bonus, position)""")
        self.conn.commit()
        self.cursor.execute("""INSERT INTO company
            (id, name, monthly_salary, yearly_bonus, position) VALUES
            (1, 'Ivan Ivanov', 5000, 10000, 'Software Developer')""")
        self.conn.commit()
        self.cursor.execute("""INSERT INTO company
            (id, name, monthly_salary, yearly_bonus, position) VALUES
            (2, 'Rado Rado', 500, 0, 'Technical Support Intern')""")
        self.conn.commit()
        self.cursor.execute("""INSERT INTO company
            (id, name, monthly_salary, yearly_bonus, position) VALUES
            (3, 'Ivo Ivo', 10000, 100000, 'CEO')""")
        self.conn.commit()
        self.cursor.execute("""INSERT INTO company
            (id, name, monthly_salary, yearly_bonus, position) VALUES
            (4, 'Petar Petrov', 3000, 1000, 'Marketing Manager')""")
        self.conn.commit()
        self.cursor.execute("""INSERT INTO company
            (id, name, monthly_salary, yearly_bonus, position) VALUES
            (5, 'Maria Georgieva', 8000, 10000, 'COO')""")
        self.conn.commit()

    def test_yearly_spending(self):
        self.assertEqual(439000, create_company.yearly_spending())

    def test_monthly_spending(self):
        self.assertEqual(26500, create_company.monthly_spending())

    #def test_list(self):

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
