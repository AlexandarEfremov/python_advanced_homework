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


if __name__ == "__main__":
    main()

