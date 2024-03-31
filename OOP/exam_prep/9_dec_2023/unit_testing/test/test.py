from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.train = RailwayStation("Alex")
        self.train.arrival_trains = ["a", "b", "c"]
        self.train.departure_trains = ["x", "y", "z"]

    def test_correct__init__(self):
        self.assertEqual("Alex", self.train.name)
        self.assertEqual(["a", "b", "c"], self.train.arrival_trains)
        self.assertEqual(["x", "y", "z"], self.train.departure_trains)

    def test_name_setter_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.train = RailwayStation("Aex")
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))




if __name__ == "__main__":
    main()
