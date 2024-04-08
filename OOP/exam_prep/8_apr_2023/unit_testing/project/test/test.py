from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Alex", 31, 400)

    def test_correct_init(self):
        self.assertEqual("Alex", self.player.name)
        self.assertEqual(31, self.player.age)
        self.assertEqual(400, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.player.name = "Al"

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_age_setter_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))


if __name__ == "__main__":
    main()