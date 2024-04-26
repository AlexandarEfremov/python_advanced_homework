from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Alex")

    def test_correct_init(self):
        self.assertEqual("Alex", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_wrong_name_setter(self):
        with self.assertRaises(Exception) as ex:
            self.library.name = ""
        ex_res = "Name cannot be empty string!"
        self.assertEqual(ex_res, str(ex.exception))


if __name__ == "__main__":
    main()
