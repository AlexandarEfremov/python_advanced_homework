from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Alex")

    def test_correct_init(self):
        self.assertEqual("Alex", self.team.name)
        self.assertEqual({}, self.team.members)




if __name__ == "__main__":
    main()