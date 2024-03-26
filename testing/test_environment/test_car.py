from unittest import TestCase, main
from testing.projects.car import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Ford", "Focus", 10, 30)

    def test_correct_init(self):
        self.assertEqual("Ford", self.car.make)
        self.assertEqual("Focus", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(30, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_model_string(self):
        with self.assertRaises(Exception) as ve:

if __name__ == "__main__":
    main()