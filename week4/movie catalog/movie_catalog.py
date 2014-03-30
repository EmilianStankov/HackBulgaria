from actor import Actor
from movie import Movie
import os
import sqlite3
from collections import OrderedDict


class MovieCatalogProgram():
    def __init__(self):
        self.actors = []
        self.movies = OrderedDict()

        self.db_path = sqlite3.connect("movie_catalog.db")
        self.cursor = self.db_path.cursor()
        self._load_initial_state()

    def add_movie(self):
        self.movie_title = input('title >')
        self.movie_year = input('year >')
        while True:
            self.movie_rating = int(input('rating >'))
            if self.movie_rating <= 10 and self.movie_rating > 0:
                break
            else:
                print("Rating can only be a number between 1 and 10.")
        self.m = Movie(self.movie_title,
                       self.movie_year,
                       self.movie_rating)
        if(self.m.get_title() not in self.movies.keys()
           and self.m.get_year() not in self.movies.values()):
            self.movies[self.movie_title] = self.movie_year
            self.m.save()
            print('{} ({}) {}'.format(self.movie_title,
                                      self.movie_year,
                                      'was added to your catalog!'))
        else:
            print('Movie already exists!')

    def add_actor(self, *arguments):
        arguments = list(arguments)
        if len(arguments) == 1:
            self.name = input('name >')
            self.a = Actor(self.name)
            self.actors.append(self.name)
            arguments.append(len(self.actors))
            self.a.save()
        else:
            if len(self.actors) >= int(arguments[1]):
                self.a = Actor(self.actors[int(arguments[1]) - 1])
            else:
                print("There is no actor with this id! Add new actor!")
                self.name = input('name >')
                self.a = Actor(self.name)
                self.actors.append(self.name)
                self.a.save()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS relations
                               (movie_id, actor_id)""")
        query = ("INSERT INTO relations(movie_id, actor_id) VALUES (?, ?)")
        data = [int(arguments[0]), int(arguments[1])]
        self.cursor.execute(query, data)
        self.db_path.commit()

    def list_movies(self):
        i = 1
        for movie in self.movies:
            print('[{}] {} ({})'.format(str(i), movie, self.movies[movie]))
            i += 1

    def list_actors(self):
        i = 1
        for actor in self.actors:
            print('[{}] {}'.format(str(i), actor))
            i += 1

    def actor_info(self, id):
        self.__id = id
        movies_ids = []
        movies_actor_is_in = []
        lines = []
        query = ("SELECT Name FROM actors WHERE id = ?")
        data = [self.__id]
        actor = self.cursor.execute(query, data)
        for line in actor:
            actor_name = line[0]
        query = ("SELECT movie_id FROM relations WHERE actor_id = ?")
        for line in self.cursor.execute(query, data):
            movies_ids.append(line[0])
        for i in range(len(movies_ids)):
            query = ("SELECT * FROM movies WHERE id = ?")
            data = [movies_ids[i]]
            movies_actor_is_in.append(self.cursor.execute(query, data))
            for movie_actor_is_in in movies_actor_is_in:
                for line in movies_actor_is_in:
                    for data in line:
                        lines.append(data)
                        break
        print('{} stars in:'.format(actor_name))
        for line in lines:
            print('[{}] {} ({})'.format(line[0], line[1], line[2]))

    def movie_info(self, id):
        self.__id = id
        query = ("SELECT * FROM movies WHERE id = ?")
        data = [self.__id]
        movie = self.cursor.execute(query, data)
        actors_ids = []
        cast = []
        cast_names = []
        cast_names_formatted = ''
        for line in movie:
            movie_title = line[1]
            movie_year = line[2]
            movie_rating = line[3]
        query = ("SELECT actor_id FROM relations WHERE movie_id = ?")
        for line in self.cursor.execute(query, data):
            actors_ids.append(line[0])
        for i in range(len(actors_ids)):
            query = ("SELECT Name FROM actors WHERE id = ?")
            data = [actors_ids[i]]
            cast.append(self.cursor.execute(query, data))
            for actor in cast:
                for name in actor:
                    for data in name:
                        cast_names.append(data)
                        break
        print('Title: {}'.format(movie_title))
        print('Year: {}'.format(movie_year))
        for name in cast_names:
            cast_names_formatted += name + ', '
        print('Cast: ' + cast_names_formatted[:-2])
        print('Rating: {}'.format(movie_rating))

    def rate_movie(self, id):
        self.__id = id
        while True:
            rating = int(input('rating >'))
            if rating <= 10 and rating > 0:
                break
            else:
                print("Rating can only be a number between 1 and 10.")
        query = ("UPDATE movies SET rating = ? WHERE id = ?")
        data = [rating, self.__id]
        self.cursor.execute(query, data)
        self.db_path.commit()

    def find_movies(self, rating):
        self.__rating = rating
        query = ("SELECT id, Title, Year FROM movies WHERE rating = ?")
        data = [self.__rating]
        movie = self.cursor.execute(query, data)
        print('Movies rated {}:'.format(self.__rating))
        for line in movie:
            print('[{}] {} ({})'.format(str(line[0]), line[1], str(line[2])))

    def _load_initial_state(self):
        if os.path.isfile("movie_catalog.db"):
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS movies
                                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Title, Year, Rating)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS actors
                                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Name)""")
            actors_data = self.cursor.execute("""SELECT Name FROM actors""")
            for actor in actors_data:
                self.actors.append(actor[0])
            movies_data = self.cursor.execute("""SELECT Title, Year
                                                 FROM movies""")
            for movie in movies_data:
                self.movies[movie[0]] = movie[1]


def main():
    program = MovieCatalogProgram()
    while True:
        command = input(">")
        if command.startswith('add_movie'):
            program.add_movie()
        elif command.startswith('add_actor'):
            arguments = command.split()
            if len(arguments) < 3:
                program.add_actor(arguments[1])
            else:
                print(arguments[1], arguments[2])
                program.add_actor(arguments[1], arguments[2])
        elif command.startswith('list_movies'):
            program.list_movies()
        elif command.startswith('list_actors'):
            program.list_actors()
        elif command.startswith('actor_info'):
            program.actor_info(int(command.split()[1]))
        elif command.startswith('movie_info'):
            program.movie_info(int(command.split()[1]))
        elif command.startswith('rate_movie'):
            program.rate_movie(int(command.split()[1]))
        elif command.startswith('find_movies'):
            program.find_movies(int(command.split()[1]))
        elif command.startswith('exit'):
            break


if __name__ == '__main__':
    main()
