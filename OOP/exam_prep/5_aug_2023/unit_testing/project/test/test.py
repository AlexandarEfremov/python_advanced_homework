from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Ford", "hatchback", 1_000_000, 10_000.00)
        self.other = SecondHandCar("Volvo", "combi", 500_000, 20_000.00)
        self.other_hatchback = SecondHandCar("Seat", "hatchback", 400_000, 8_000.00)

    def test_correct__init__(self):
        self.assertEqual("Ford", self.car.model)
        self.assertEqual("hatchback", self.car.car_type)
        self.assertEqual(1_000_000, self.car.mileage)
        self.assertEqual(10_000.00, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_correct__init__other(self):
        self.assertEqual("Volvo", self.other.model)
        self.assertEqual("combi", self.other.car_type)
        self.assertEqual(500_000, self.other.mileage)
        self.assertEqual(20_000.00, self.other.price)
        self.assertEqual([], self.other.repairs)

    def test_correct__init__other_hatchback(self):
        self.assertEqual("Seat", self.other_hatchback.model)
        self.assertEqual("hatchback", self.other_hatchback.car_type)
        self.assertEqual(400_000, self.other_hatchback.mileage)
        self.assertEqual(8000.00, self.other_hatchback.price)
        self.assertEqual([], self.other_hatchback.repairs)

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

    def test_changed_promotional_price(self):
        self.car.set_promotional_price(5_000.00)
        self.assertEqual(5_000.00, self.car.price)

    def test_repair_if_repair_price_is_more_than_half_expect_error(self):
        self.assertEqual('Repair is impossible!', self.car.need_repair(5_001.00, "wheels"))

    def test_repair_if_price_is_less_than_half_expect_success(self):
        self.assertEqual('Price has been increased due to repair charges.',
                         self.car.need_repair(4_001.00, "wheels"))

    def test_price_after_repairs_expect_increase(self):
        self.car.need_repair(5_000.00, "wheels")
        self.assertEqual(15_000.00, self.car.price)

    def test_repair_parts_in_list_after_repair(self):
        self.car.need_repair(5_000.00, "wheels")
        self.assertEqual(["wheels"], self.car.repairs)

    def test__gt__expect_negative(self):
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car > self.other)

    def test__gt__expect_positive(self):
        self.assertTrue(self.car > self.other_hatchback)

    def test_str_representation(self):
        expect = "Model Ford | Type hatchback | Milage 1000000km\nCurrent price: 10000.00 | Number of Repairs: 0"

        self.assertEqual(expect, self.car.__str__())


if __name__ == "__main__":
    main()