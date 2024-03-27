from unittest import TestCase, main
# from testing.projects.car import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Ford", "Focus", 10, 30)

    def test_correct_init(self):
        self.assertEqual("Ford", self.car.make)
        self.assertEqual("Focus", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(30, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_make_string(self):
        with self.assertRaises(Exception) as ve:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ve.exception))

    def test_empty_model_string(self):
        with self.assertRaises(Exception) as ve:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ve.exception))

    def test_zero_or_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ve:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ve.exception))

    def test_zero_or_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as ve:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ve.exception))

    def test_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ve:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ve.exception))

    def test_refuel_with_negative_amount(self):
        with self.assertRaises(Exception) as ve:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ve.exception))

    def test_drive_more_than_available(self):
        with self.assertRaises(Exception) as ve:
            self.car.drive(10000000)

        self.assertEqual("You don't have enough fuel to drive!", str(ve.exception))

    def test_drive_with_enough_fuel_decreases_fuel(self):
        self.car.refuel(1000)
        self.car.drive(10)
        self.assertEqual(29.0, self.car.fuel_amount)


if __name__ == "__main__":
    main()