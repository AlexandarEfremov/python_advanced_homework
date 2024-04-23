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

    def test_name_setter_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_setter_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.movie.year = 1500
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_in_list_expect_error(self):
        self.movie.add_actor("John")
        res = self.movie.add_actor("John")

        self.assertEqual("John is already added in the list of actors!", res)

    def test_add_actor_not_in_list(self):
        self.movie.add_actor("John")
        self.assertEqual(["John"], self.movie.actors)

if __name__ == "__main__":
    main()