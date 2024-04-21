from unittest import TestCase, main

from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(100)

    def test_correct_init(self):
        self.assertEqual(100, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_wrong_size_error(self):
        with self.assertRaises(Exception) as ex:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_not_possible(self):
        self.plantation.hire_worker("Alex")

        with self.assertRaises(Exception) as ex:
            self.plantation.hire_worker("Alex")

        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_successful_hire_and_in_list(self):
        res = self.plantation.hire_worker("Alex")
        self.assertEqual("Alex successfully hired.", res)
        self.assertEqual(["Alex"], self.plantation.workers)

    def test_len_of_plants(self):
        self.plantation.hire_worker("Alex")
        self.plantation.hire_worker("John")
        self.plantation.planting("Alex", "rose")
        self.plantation.planting("Alex", "cabbage")
        self.plantation.planting("John", "rice")
        self.assertEqual(3, self.plantation.__len__())

    def test_zero_len(self):
        self.assertEqual(0, self.plantation.__len__())

    def test_planting_if_worker_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.plantation.planting("Alex", "rose")

        self.assertEqual("Worker with name Alex is not hired!", str(ex.exception))

    def test_plantation_is_full(self):
        self.plantation.hire_worker("Alex")
        self.plantation.size = 1
        self.plantation.planting("Alex", "rose")

        with self.assertRaises(Exception) as ex:
            self.plantation.planting("Alex", "cabbage")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_if_worker_available_but_plantation_full(self):
        self.plantation.hire_worker("Alex")
        self.plantation.size = 0

        with self.assertRaises(Exception) as ex:
            self.plantation.planting("Alex", "rose")

        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_correct_plantation_and_availability_in_dict(self):
        self.plantation.hire_worker("Alex")
        res = self.plantation.planting("Alex", "rose")

        self.assertEqual("Alex planted it's first rose.", res)
        self.assertEqual({"Alex": ["rose"]}, self.plantation.plants)

        two = self.plantation.planting("Alex", "cabbage")
        self.assertEqual("Alex planted cabbage.", two)
        self.assertEqual({"Alex": ["rose", "cabbage"]}, self.plantation.plants)

    def test_correct_str(self):
        self.plantation.hire_worker("Alex")
        self.plantation.planting("Alex", "rose")
        self.plantation.planting("Alex", "cabbage")

        self.assertEqual("Plantation size: 100\nAlex\nAlex planted: rose, cabbage", self.plantation.__str__())

    def test_correct_repr(self):
        self.plantation.hire_worker("Alex")
        self.plantation.planting("Alex", "rose")
        self.plantation.planting("Alex", "cabbage")
        self.plantation.hire_worker("John")

        self.assertEqual("Size: 100\nWorkers: Alex, John", self.plantation.__repr__())


if __name__ == "__main__":
    main()