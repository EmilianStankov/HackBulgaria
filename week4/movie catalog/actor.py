import sqlite3


class Actor():
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def save(self):
        self.db_path = sqlite3.connect('movie_catalog.db')
        self.cursor = self.db_path.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS actors
                               (id INTEGER PRIMARY KEY AUTOINCREMENT, Name)""")
        query = ("INSERT INTO actors(Name) VALUES (?)")
        data = [self.get_name()]
        self.cursor.execute(query, data)
        self.db_path.commit()
        self.db_path.close()
        return True
