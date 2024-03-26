from unittest import TestCase, main
from testing.projects.list import IntegerList


class TestList(TestCase):
    def setUp(self):
        self.i_list = IntegerList(5.5, 1, 2, 3, "hello")

    def test_correct_init_ignores_non_int_values(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())

    def test_correct_init_ignores_not_int_values(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_to_list(self):
        expected_list = self.i_list.get_data() + [4]

        self.i_list.add(4)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_remove_index_which_is_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_valid_index(self):
        self.i_list.remove_index(1)

        self.i_list.remove_index(1)

        self.assertEqual([1, 3], self.i_list.get_data())


if __name__ == "__main__":
    main()