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

    def test_append_new_train(self):
        self.train.arrival_trains.append("d")
        self.assertEqual(["a", "b", "c", "d"], self.train.arrival_trains)

    def test_other_trains_before_info(self):
        train_info = "c"
        self.assertEqual(f"There are other trains to arrive before {train_info}.",
                         self.train.train_has_arrived(train_info))

    def test_info_train_is_next(self):
        train_info = "a"
        self.assertEqual(f"{train_info} is on the platform and will leave in 5 minutes.",
                         self.train.train_has_arrived(train_info))

if __name__ == "__main__":
    main()
