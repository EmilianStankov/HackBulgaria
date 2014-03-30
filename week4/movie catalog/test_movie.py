import unittest
from movie import Movie


class TestMovieClass(unittest.TestCase):
    def setUp(self):
        self.m = Movie("Best.Movie.Ever.", 2014, 10)

    def test_get_movie_title(self):
        self.assertEqual("Best.Movie.Ever.", self.m.get_title())

    def test_get_movie_year(self):
        self.assertEqual(2014, self.m.get_year())

    def test_get_movie_rating(self):
        self.assertEqual(10, self.m.get_rating())

    @unittest.skip("This works but no point in generating extra movies.")
    def test_save_movie(self):
        self.assertTrue(self.m.save())


if __name__ == '__main__':
    unittest.main()
