from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "usb", 10, 32)
        self.ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        self.robot.installed_software = []

    def test_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("usb", self.robot.part_type)
        self.assertEqual(10, self.robot.capacity)
        self.assertEqual(32, self.robot.memory)

    def test_category_not_in_allowed(self):
        with self.assertRaises(Exception) as ex:
            self.robot.category = "Macho"

        self.assertEqual(f"Category should be one of "
                         f"{self.ALLOWED_CATEGORIES}", str(ex.exception))



if __name__ == "__main__":
    main()