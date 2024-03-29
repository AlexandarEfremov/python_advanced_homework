from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "usb", 100, 320)

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
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(320, self.robot.memory)
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

    def test_successful_installation(self):
        result = self.robot.install_software(
            {"name": "Pycharm", "capacity_consumption": 50, "memory_consumption": 49}
        )

        self.assertEqual("Software 'Pycharm' successfully installed on Mountain part.",
                         result
                         )

        self.assertEqual(
            self.robot.installed_software, [{"name": "Pycharm", "capacity_consumption": 50, "memory_consumption": 49}]
        )

    def test_installation_with_double_max_values_expect_success(self):
        result = self.robot.install_software(
            {"name": "Pycharm", "capacity_consumption": 100, "memory_consumption": 320}
        )

        self.assertEqual("Software 'Pycharm' successfully installed on Mountain part.",
                         result
                         )

        self.assertEqual(
            self.robot.installed_software, [{"name": "Pycharm", "capacity_consumption": 100, "memory_consumption": 320}]
        )
    def test_installation_with_not_enough_capacity_expect_fail(self):
        result = self.robot.install_software(
            {"name": "Pycharm", "capacity_consumption": 101, "memory_consumption": 49}
        )

        self.assertEqual("Software 'Pycharm' cannot be installed on Mountain part.", result)

        self.assertEqual(
            self.robot.installed_software,
            []
        )

    def test_installation_with_not_enough_memory_expect_fail(self):
        result = self.robot.install_software(
            {"name": "Pycharm", "capacity_consumption": 10, "memory_consumption": 490}
        )

        self.assertEqual("Software 'Pycharm' cannot be installed on Mountain part.", result)

        self.assertEqual(
            self.robot.installed_software,
            []
        )

if __name__ == "__main__":
    main()