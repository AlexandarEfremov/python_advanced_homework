from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self):
        self.robot = Robot("R2D2", "Military", 10, 100.00)

    def test_correct_init_(self):
        self.assertEqual("R2D2", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(100.00, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_wrong_category_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.robot.category = "Alex"

        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ex.exception))

    def test_negative_price_value_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.robot.price = -22

        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_upgrade_if_component_in_hardware_list(self):
        self.robot.hardware_upgrades.append("usb")
        result = self.robot.upgrade("usb", 100)

        self.assertEqual(f"Robot R2D2 was not upgraded.", result)

    def test_new_hardware_if_present_in_list(self):
        hardware_component = "light"
        self.robot.upgrade(hardware_component, 100)

        self.assertEqual(["light"], self.robot.hardware_upgrades)

    def test_price_after_hardware_upgrade(self):
        hardware_component = "light"
        self.robot.upgrade(hardware_component, 100)

        self.assertEqual(250.0, self.robot.price)

if __name__ == "__main__":
    main()