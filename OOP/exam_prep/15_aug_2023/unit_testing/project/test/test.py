from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self):
        self.trip = Trip(1000.0, 4, True)

    def test_correct__init__(self):
        self.assertEqual(1000.0, self.trip.budget)
        self.assertEqual(4, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_traveller_number_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ex.exception))

    def test_if_is_family_with_1_person_expect_false(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertFalse(self.trip.is_family)

    def test_if_family_with_2_people_expect_true(self):
        self.trip.travelers = 2
        self.trip.is_family = True
        self.assertTrue(self.trip.is_family)

    def test_book_a_trip_for_destination_not_in_list_expect_decline(self):
        ex_res = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(ex_res, self.trip.book_a_trip("Colorado"))

    def test_required_budget_not_enough_for_all_people(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        ex_res = 'Your budget is not enough!'
        self.assertEqual(ex_res, self.trip.book_a_trip("Brazil"))

    def test_required_budget_not_enough_for_family(self):
        ex_res = 'Your budget is not enough!'
        self.assertEqual(ex_res, self.trip.book_a_trip("Brazil"))

    def test_budget_enough_for_all_people(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        ex_res = 'Successfully booked destination Bulgaria! Your budget left is 500.00'
        self.assertEqual(ex_res, self.trip.book_a_trip("Bulgaria"))

    def test_budget_for_a_family(self):
        self.trip.budget = 10_000
        ex_res = 'Successfully booked destination Bulgaria! Your budget left is 8200.00'
        self.assertEqual(ex_res, self.trip.book_a_trip("Bulgaria"))

    def test_no_bookings_made(self):
        ex_res = 'No bookings yet. Budget: 1000.00'
        self.assertEqual(ex_res, self.trip.booking_status())

    def test_booking_status(self):
        self.trip.budget = 50_000
        self.trip.book_a_trip("Bulgaria")
        self.trip.book_a_trip("New Zealand")

        ex_result = (f"Booked Destination: Bulgaria\n"
                     f"Paid Amount: 1800.00\n"
                     f"Booked Destination: New Zealand\n"
                     f"Paid Amount: 27000.00\n"
                     f"Number of Travelers: 4\n"
                     f"Budget Left: 21200.00")

        self.assertEqual(ex_result,self.trip.booking_status())


if __name__ == "__main__":
    main()

