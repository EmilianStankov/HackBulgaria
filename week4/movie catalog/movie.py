import sqlite3


class Movie():
    def __init__(self, title, year, rating):
        self.__title = title
        self.__year = year
        self.rating = rating

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_rating(self):
        return self.rating

    def save(self):
        self.db_path = sqlite3.connect("movie_catalog.db")
        self.cursor = self.db_path.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS movies
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             Title, Year, Rating)""")
        query = ("""INSERT INTO movies(Title, Year, Rating)
                    VALUES(?, ?, ?)""")
        data = [self.get_title(), self.get_year(), self.get_rating()]
        self.cursor.execute(query, data)
        self.db_path.commit()
        self.db_path.close()
        return True
