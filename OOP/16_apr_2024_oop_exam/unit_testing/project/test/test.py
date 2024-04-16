from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Alex", 10)

    def test_correct_init(self):
        self.assertEqual("Alex", self.restaurant.name)
        self.assertEqual(10, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_whitespace_name_expect_value_error(self):
        with self.assertRaises(Exception) as ex:
            self.restaurant.name = "   "
        self.assertEqual("Invalid name!", str(ex.exception))

    def test_with_no_text_expect_value_error(self):
        with self.assertRaises(Exception) as ex:
            self.restaurant.name = ""
        self.assertEqual("Invalid name!", str(ex.exception))

    def test_capacity_less_than_zero_expect_value_error(self):
        with self.assertRaises(Exception) as ex:
            self.restaurant.capacity = -1
        self.assertEqual("Invalid capacity!", str(ex.exception))

    def test_adding_waiters_no_more_capacity(self):
        self.restaurant.add_waiter("Bill")
        self.restaurant.add_waiter("George")
        self.restaurant.capacity = 2

        ex_result = self.restaurant.add_waiter("Mike")
        self.assertEqual("No more places!", ex_result)

    def test_get_waiters_no_filters(self):
        self.restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 70}
        ]

        waiters = self.restaurant.get_waiters()
        self.assertEqual(len(waiters), 2)

    def test_waiters_with_min_earnings(self):
        self.restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 70}
        ]

        waiters = self.restaurant.get_waiters(min_earnings=60)
        self.assertEqual(len(waiters), 2)
        self.assertIn({'name': 'John', 'total_earnings': 100}, waiters)
        self.assertIn({'name': 'Alice', 'total_earnings': 70}, waiters)

    def test_waiters_with_max_earnings(self):
        self.restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 70},
            {'name': 'Bob', 'total_earnings': 50},
            {'name': 'Eve', 'total_earnings': 30}
        ]

        waiters = self.restaurant.get_waiters(max_earnings=40)
        self.assertEqual(len(waiters), 1)
        self.assertIn({'name': 'Eve', 'total_earnings': 30}, waiters)

    def test_waiters_with_min_and_max(self):
        self.restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 70},
            {'name': 'Bob', 'total_earnings': 50},
            {'name': 'Eve', 'total_earnings': 30}
        ]

        waiters = self.restaurant.get_waiters(min_earnings=40, max_earnings=80)
        self.assertEqual(len(waiters), 2)
        self.assertIn({'name': 'Alice', 'total_earnings': 70}, waiters)
        self.assertIn({'name': 'Bob', 'total_earnings': 50}, waiters)

    def test_if_waiter_name_has_already_been_added(self):
        self.restaurant.add_waiter("Bill")
        ex_result = self.restaurant.add_waiter("Bill")
        self.assertEqual("The waiter Bill already exists!", ex_result)

    def test_correct_waiter_addition(self):
        ex_res = self.restaurant.add_waiter("Bill")
        self.assertEqual("The waiter Bill has been added.", ex_res)

    def test_correct_list_repr(self):
        self.restaurant.add_waiter("Bill")
        self.assertEqual([{'name': 'Bill'}], self.restaurant.waiters)

    def test_removing_invalid_waiter(self):
        self.restaurant.add_waiter("Bill")
        ex_res = self.restaurant.remove_waiter("Joey")

        self.assertEqual("No waiter found with the name Joey.", ex_res)

    def test_successful_remove(self):
        self.restaurant.add_waiter("Bill")
        ex_res = self.restaurant.remove_waiter("Bill")

        self.assertEqual("The waiter Bill has been removed.", ex_res)

    def test_empty_list_after_removal(self):
        self.restaurant.add_waiter("Bill")
        self.restaurant.remove_waiter("Bill")

        self.assertEqual([], self.restaurant.waiters)

    def test_removed_one_left_another(self):
        self.restaurant.add_waiter("Bill")
        self.restaurant.add_waiter("George")
        self.restaurant.remove_waiter("Bill")

        self.assertEqual([{'name': 'George'}], self.restaurant.waiters)

    def test_total_earnings(self):
        self.restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Alice', 'total_earnings': 70},
            {'name': 'Bob', 'total_earnings': 50},
            {'name': 'Eve', 'total_earnings': 30}
        ]

        ex_res = self.restaurant.get_total_earnings()
        self.assertEqual(250, ex_res)

if __name__ == "__main__":
    main()
