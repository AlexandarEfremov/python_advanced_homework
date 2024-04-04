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

    def test_minimum_price_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.price = 1.0

        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

    def test_min_mileage_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',
                         str(ex.exception))

    def test_setting_promotional_offer_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.set_promotional_price(20_000.00)

        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_setting_promotional_offer_expect_success(self):
        self.assertEqual('The promotional price has been successfully set.',
                         self.car.set_promotional_price(5_000.00))

    def test_repair_if_repair_price_is_more_than_half_expect_error(self):
        self.assertEqual('Repair is impossible!', self.car.need_repair(5_001.00, "wheels"))

    def test_repair_if_price_is_less_than_half_expect_success(self):
        self.assertEqual('Price has been increased due to repair charges.',
                         self.car.need_repair(4_001.00, "wheels"))


if __name__ == "__main__":
    main()