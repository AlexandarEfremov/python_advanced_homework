from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(30.5, 100.5)

    def test_init(self):
        self.assertEqual(30.5, self.vehicle.fuel)
        self.assertEqual(100.5, self.vehicle.horse_power)

    def test_less_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ve:
            self.vehicle.drive(1000000)

        self.assertEqual("Not enough fuel", str(ve.exception))

    def test_fuel_left_after_drive(self):
        self.vehicle.drive(10)

        self.assertEqual(18, self.vehicle.fuel)

    def test_refueling_too_much(self):
        with self.assertRaises(Exception) as ve:
            self.vehicle.refuel(10000)

        self.assertEqual("Too much fuel", str(ve.exception))

    def test_correct_refueling(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(2)

        self.assertEqual(20, self.vehicle.fuel)

    def test_return_string(self):
        self.assertEqual("The vehicle has 100.5 horse power with 30.5 fuel left "
                         "and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()