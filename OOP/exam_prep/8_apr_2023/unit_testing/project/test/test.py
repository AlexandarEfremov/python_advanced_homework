from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Alex", 31, 400)
        self.other_player = TennisPlayer("Ewcia", 33, 500)

    def test_correct_other_init(self):
        self.assertEqual("Ewcia", self.other_player.name)
        self.assertEqual(33, self.other_player.age)
        self.assertEqual(500, self.other_player.points)
        self.assertEqual([], self.other_player.wins)

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

    def test_tournament_in_tournament_list_bad(self):
        self.player.add_new_win("Wimbeldon")
        result = self.player.add_new_win("Wimbeldon")

        self.assertEqual("Wimbeldon has been already added to the list of wins!", result)

    def test_tournament_not_in_tournament_list_good(self):
        self.player.add_new_win("Wimbeldon")
        self.assertEqual(["Wimbeldon"], self.player.wins)

    def test_if_im_better_expect_yes(self):
        self.player.points = 600
        result = 'Alex is a better player than Ewcia'

        self.assertEqual(self.player.__lt__(self.other_player), result)

    def test_if_im_better_expect_no(self):
        result = 'Ewcia is a top seeded player and he/she is better than Alex'
        self.assertEqual(self.player.__lt__(self.other_player), result)

    def test_return_correct_string(self):
        self.player.add_new_win("Wimbeldon")
        self.player.add_new_win("Australian Open")

        result = f"Tennis Player: Alex\n" \
                 f"Age: 31\n" \
                 f"Points: 400.0\n" \
                 f"Tournaments won: Wimbeldon, Australian Open"
        self.assertEqual(self.player.__str__(), result)

    def test_return_string_with_no_tournaments(self):
        result = f"Tennis Player: Alex\n" \
                 f"Age: 31\n" \
                 f"Points: 400.0\n" \
                 f"Tournaments won: "

        self.assertEqual(self.player.__str__(), result)


if __name__ == "__main__":
    main()