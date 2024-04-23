from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Alex", 1993, 5)
        self.other = Movie("Ewcia", 1990, 6)

    def test_other_correct_init(self):
        self.assertEqual("Ewcia", self.other.name)
        self.assertEqual(1990, self.other.year)
        self.assertEqual(6, self.other.rating)
        self.assertEqual([], self.other.actors)

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

    def test_ewcia_beter_than_alex(self):
        ex_res = f'"{self.other.name}" is better than "{self.movie.name}"'
        self.assertEqual(self.movie.__gt__(self.other), ex_res)

    def test_alex_is_better_than_ewcia(self):
        self.movie.rating = 7
        ex_res = f'"{self.movie.name}" is better than "{self.other.name}"'
        self.assertEqual(self.movie.__gt__(self.other), ex_res)


if __name__ == "__main__":
    main()