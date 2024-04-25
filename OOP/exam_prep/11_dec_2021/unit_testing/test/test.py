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

    def test_adding_members_with_repeating_names(self):
        self.team.members = {"mike": 20, "john": 21}
        second_members = {"alex": 20, "john": 21}
        res = self.team.add_member(**second_members)

        ex_mes = f"Successfully added: alex"
        self.assertEqual(ex_mes, res)
        self.assertEqual({"mike": 20, "john": 21, "alex": 20}, self.team.members)


if __name__ == "__main__":
    main()