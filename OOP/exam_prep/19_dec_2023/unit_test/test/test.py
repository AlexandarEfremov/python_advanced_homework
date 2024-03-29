from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "usb", 10, 32)

        self.robot_with_software = ClimbingRobot(
            "Mountain",
            "usb",
            10,
            32
        )

        self.robot_with_software.installed_software = [
            {"name": "Pycharm", "capacity_consumption": 50, "memory_consumption": 49},
            {"name": "Citx", "capacity_consumption": 49, "memory_consumption": 51}
        ]

    def test_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("usb", self.robot.part_type)
        self.assertEqual(10, self.robot.capacity)
        self.assertEqual(32, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_not_in_allowed(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Macho"

        self.assertEqual(f"Category should be one of "
                         f"{self.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_return_used_capacity(self):
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_capacity()

        self.assertEqual(expected_result, result)

    def test_return_available_capacity(self):
        expected_result = self.robot_with_software.capacity - self.robot_with_software.get_used_capacity()
        result = self.robot_with_software.get_available_capacity()

        self.assertEqual(expected_result, result)

    def test_return_used_memory(self):
        expect = sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_memory()

        self.assertEqual(expect, result)

    def test_return_available_memory(self):
        expect = self.robot_with_software.memory - self.robot_with_software.get_used_memory()
        result = self.robot_with_software.get_available_memory()

        self.assertEqual(expect, result)


if __name__ == "__main__":
    main()