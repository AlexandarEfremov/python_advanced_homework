from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Alex", 1993, 5)

    def test_correct_init(self):
        self.assertEqual("Alex", self.movie.name)
        self.assertEqual(1993, self.movie.year)
        self.assertEqual(5, self.movie.rating)
        self.assertEqual([], self.movie.actors)




if __name__ == "__main__":
    main()