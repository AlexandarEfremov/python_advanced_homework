from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self):
        self.toy = ToyStore()

    def test_shelves_attribute(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)

    def test_add_toy_to_non_exist_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("Z", "mecho")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_which_exists(self):
        self.toy.add_toy("A", "mecho")
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "mecho")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_a_taken_shelf(self):
        self.toy.add_toy("A", "mecho")
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "zayo")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_success(self):
        ex = "Toy:Mecho placed successfully!"

        self.assertEqual(ex, self.toy.add_toy("A", "Mecho"))

    def test_find_toy_on_shelf(self):
        self.toy.add_toy("A", "mecho")
        self.assertEqual("mecho", self.toy.toy_shelf["A"])

    def test_removing_a_toy_from_a_non_exist_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("Z", "mecho")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_which_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("A", "mecho")

            self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_successful_remove(self):
        self.toy.add_toy("A", "mecho")
        self.assertEqual("Remove toy:mecho successfully!",
                         self.toy.remove_toy("A", "mecho"))

    def test_shelf_is_again_none(self):
        self.toy.add_toy("A", "mecho")
        self.toy.remove_toy("A", "mecho")
        self.assertEqual(None, self.toy.toy_shelf["A"])

if __name__ == "__main__":
    main()