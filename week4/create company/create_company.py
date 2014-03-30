import sqlite3
import os.path

if os.path.isfile("company.db"):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
else:
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS company
        (id, name, monthly_salary, yearly_bonus, position)""")
    conn.commit()
    cursor.execute("""INSERT INTO company
        (id, name, monthly_salary, yearly_bonus, position) VALUES
        (1, 'Ivan Ivanov', 5000, 10000, 'Software Developer')""")
    conn.commit()
    cursor.execute("""INSERT INTO company
        (id, name, monthly_salary, yearly_bonus, position) VALUES
        (2, 'Rado Rado', 500, 0, 'Technical Support Intern')""")
    conn.commit()
    cursor.execute("""INSERT INTO company
        (id, name, monthly_salary, yearly_bonus, position) VALUES
        (3, 'Ivo Ivo', 10000, 100000, 'CEO')""")
    conn.commit()
    cursor.execute("""INSERT INTO company
        (id, name, monthly_salary, yearly_bonus, position) VALUES
        (4, 'Petar Petrov', 3000, 1000, 'Marketing Manager')""")
    conn.commit()
    cursor.execute("""INSERT INTO company
        (id, name, monthly_salary, yearly_bonus, position) VALUES
        (5, 'Maria Georgieva', 8000, 10000, 'COO')""")
    conn.commit()


def list():
    result = cursor.execute("SELECT id, name, position FROM company")
    for row in result:
        print(str(row[0]) + ' - ' + row[1] + ' - ' + row[2])


def monthly_spending():
    sum = 0
    result = cursor.execute("SELECT monthly_salary FROM company")
    for row in result:
        sum += row[0]
    return sum


def yearly_spending():
    sum = 0
    result = cursor.execute("SELECT monthly_salary, yearly_bonus FROM company")
    for row in result:
        sum += row[0] * 12 + row[1]
    return sum


def add_employee():
    result = cursor.execute("SELECT id FROM company")
    id = 0
    for row in result:
        id = row[0]
    new_id = id + 1
    name = input('name >')
    monthly_salary = input('monthly_salary >')
    yearly_bonus = input('yearly_bonus >')
    position = input('position >')
    query = """
     INSERT INTO company
         (id, name, monthly_salary, yearly_bonus, position)
     VALUES
          (?, ?, ?, ?, ?)
        """
    data = [int(new_id),
            name,
            int(monthly_salary),
            int(yearly_bonus),
            position]
    cursor.execute(query, data)


def delete_employee():
    employee_id = [int(command.split()[1])]
    query = ("DELETE FROM company WHERE id = ?")
    cursor.execute(query, employee_id)


def update_employee():
    employee_id = [int(command.split()[1])]
    name = input('name >')
    monthly_salary = input('monthly_salary >')
    yearly_bonus = input('yearly_bonus >')
    position = input('position >')
    query = """
     UPDATE company SET
        id = ?, name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
        WHERE id = ?
    """
    data = [int(employee_id[0]),
            name,
            int(monthly_salary),
            int(yearly_bonus),
            position,
            int(employee_id[0])]
    cursor.execute(query, data)


while True:
    command = input('>>>')
    if command == 'list':
        list()
    elif command == 'monthly_spending':
        print('The company spends $' + str(monthly_spending()) + ' a month.')
    elif command == 'yearly_spending':
        print('The company spends $' + str(yearly_spending()) + ' a year.')
    elif command == 'add_employee':
        add_employee()
        conn.commit()
    elif command.startswith('delete_employee'):
        delete_employee()
        conn.commit()
    elif command.startswith('update_employee'):
        update_employee()
        conn.commit()
    elif command == 'exit':
        conn.commit()
        conn.close()
        break
