from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Ford", "hatchback", 1_000_000, 10_000.00)

    def test_correct__init__(self):
        self.assertEqual("Ford", self.car.model)
        self.assertEqual("hatchback", self.car.car_type)
        self.assertEqual(1_000_000, self.car.mileage)
        self.assertEqual(10_000.00, self.car.price)
        self.assertEqual([], self.car.repairs)

if __name__ == "__main__":
    main()