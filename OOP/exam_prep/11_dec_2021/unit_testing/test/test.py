from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Alex")
        self.other = Team("Ewcia")

    def test_correct_init(self):
        self.assertEqual("Alex", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_with_digits(self):
        with self.assertRaises(Exception) as ex:
            self.team.name = "alex123"

        message = "Team Name can contain only letters!"
        self.assertEqual(message, str(ex.exception))

    def test_invalid_team_name(self):
        with self.assertRaises(ValueError) as ex:
            Team("123Team")

        message = "Team Name can contain only letters!"
        self.assertEqual(message, str(ex.exception))

    def test_adding_multiple_members(self):
        members_to_add = {"john": 21, "mike": 20, "peter": 25}
        res = self.team.add_member(**members_to_add)

        expected_message = "Successfully added: john, mike, peter"
        self.assertEqual(expected_message, res)
        self.assertEqual(members_to_add, self.team.members)

    def test_adding_members_with_repeating_names(self):
        self.team.members = {"mike": 20, "john": 21}
        second_members = {"alex": 20, "john": 21}
        res = self.team.add_member(**second_members)

        ex_mes = f"Successfully added: alex"
        self.assertEqual(ex_mes, res)
        self.assertEqual({"mike": 20, "john": 21, "alex": 20}, self.team.members)

    def test_deleting_member_in_dict(self):
        self.team.members = {"mike": 20, "john": 21}
        res = self.team.remove_member("mike")

        self.assertEqual("Member mike removed", res)
        self.assertEqual({"john": 21}, self.team.members)

    def test_greater_than(self):
        self.team.members = {"mike": 20, "john": 21}
        self.other.members = {"mike": 20, "john": 21, "peter": 33}

        self.assertFalse(self.team.__gt__(self.other))
        self.assertTrue(self.other.__gt__(self.team))

    def test_len(self):
        self.team.members = {"mike": 20, "john": 21}
        self.assertEqual(2, self.team.__len__())

    def test_creating_a_new_team(self):
        self.team.members = {"mike": 20, "john": 21}
        self.other.members = {"mike": 20, "john": 21, "peter": 33}

        new_team = self.team.__add__(self.other)

        self.assertEqual("AlexEwcia", new_team.name)
        self.assertEqual({"mike": 20, "john": 21, "peter": 33}, new_team.members)

    def test_correct_str(self):
        self.team.members = {"mike": 20, "john": 21}
        res = "Team name: Alex\nMember: john - 21-years old\nMember: mike - 20-years old"
        self.assertEqual(res, self.team.__str__())

    def test_correct_str_two(self):
        res = "Team name: Alex"
        self.assertEqual(res, self.team.__str__())


if __name__ == "__main__":
    main()