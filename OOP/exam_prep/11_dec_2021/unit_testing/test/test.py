from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Alex")

    def test_correct_init(self):
        self.assertEqual("Alex", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_with_digits(self):
        with self.assertRaises(Exception) as ex:
            self.team.name = "alex123"

        message = "Team Name can contain only letters!"
        self.assertEqual(message, str(ex.exception))


if __name__ == "__main__":
    main()