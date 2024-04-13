from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Alex", 10.0)

    def test_correct_init(self):
        self.assertEqual("Alex", self.driver.name)
        self.assertEqual(10.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_if_bankrupt(self):
        with self.assertRaises(Exception) as ex:
            self.driver.earned_money = -1

        self.assertEqual("Alex went bankrupt.", str(ex.exception))

    def test_cargo_location_already_added_expect_error(self):
        self.driver.add_cargo_offer("Sofia", 100)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 100)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_cargo_correctly_added(self):
        result = self.driver.add_cargo_offer("Sofia", 100)
        ex_result = "Cargo for 100 to Sofia was added as an offer."
        self.assertEqual(ex_result, result)

    def test_visible_cargo_dict(self):
        self.driver.add_cargo_offer("Sofia", 100)
        self.assertEqual({"Sofia": 100}, self.driver.available_cargos)

    def test_try_getting_max_location_expect_error(self):
        self.assertEqual("There are no offers available.", self.driver.drive_best_cargo_offer())

    def test_drive_best_offer_expect_success(self):
        self.driver.add_cargo_offer("Sofia", 100)
        self.driver.add_cargo_offer("Burgas", 300)
        self.driver.add_cargo_offer("Varna", 150)

        ex_result = "Alex is driving 300 to Burgas."
        self.assertEqual(ex_result, self.driver.drive_best_cargo_offer())

    def test_money_made_after_best_offer(self):
        self.driver.add_cargo_offer("Burgas", 300)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(2980.0, self.driver.earned_money)

    def test_miles_done_after_order(self):
        self.driver.add_cargo_offer("Burgas", 300)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(300, self.driver.miles)

    def test_activity_checker_eat(self):
        self.driver.add_cargo_offer("Burgas", 600)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(5960.0, self.driver.earned_money)

    def test_activity_checker_sleep(self):
        self.driver.add_cargo_offer("Burgas", 1000)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(9875.0, self.driver.earned_money)

    def test_activity_checker_gas(self):
        self.driver.add_cargo_offer("Burgas", 1500)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(14335.0, self.driver.earned_money)

    def test_activity_checker_repair(self):
        self.driver.add_cargo_offer("Burgas", 10000)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(88250.0, self.driver.earned_money)

    def test_correct_repr_zero(self):
        ex_result = "Alex has 0 miles behind his back."
        self.assertEqual(ex_result, self.driver.__repr__())

    def test_correct_repr_more(self):
        self.driver.miles = 10_000
        ex_result = "Alex has 10000 miles behind his back."
        self.assertEqual(ex_result, self.driver.__repr__())