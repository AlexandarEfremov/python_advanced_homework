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

    def test_add_book_author_not_in_list_and_book_not_with_author(self):
        self.library.add_book("Ewcia", "Poland")
        self.assertEqual({"Ewcia": ["Poland"]}, self.library.books_by_authors)

    def test_add_book_author_in_list_book_not_in_author(self):
        self.library.add_book("Ewcia", "Poland")
        self.library.add_book("Ewcia", "Bulgaria")

        self.assertEqual({"Ewcia": ["Poland", "Bulgaria"]}, self.library.books_by_authors)

if __name__ == "__main__":
    main()
