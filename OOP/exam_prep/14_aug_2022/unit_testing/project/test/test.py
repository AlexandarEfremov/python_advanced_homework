from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(100)

    def test_correct_setup(self):
        self.assertEqual(100, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_negative_book_limit_or_zero(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.books_limit = -1

        self.assertEqual("Books limit of -1 is not valid", str(ex.exception))

    def test_zero_book_limit(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_dictionary_books(self):
        self.bookstore.receive_book("Alex", 10)
        self.assertEqual(10, self.bookstore.__len__())

    def test_dict_length_multiple_books(self):
        self.bookstore.receive_book("Alex", 10)
        self.bookstore.receive_book("Ewcia", 20)

        self.assertEqual(30, self.bookstore.__len__())

    def test_if_book_capacity_is_over(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Alex", 101)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_existing_book_extra_copies(self):
        self.bookstore.receive_book("Alex", 10)
        self.bookstore.receive_book("Alex", 3)

        self.assertEqual({"Alex": 13}, self.bookstore.availability_in_store_by_book_titles)

    def test_regular_reception_of_books(self):
        self.bookstore.receive_book("Alex", 50)
        self.assertEqual({"Alex": 50}, self.bookstore.availability_in_store_by_book_titles)

    def test_display_message_after_receiving_books(self):
        ex = self.bookstore.receive_book("Alex", 50)
        self.assertEqual("50 copies of Alex are available in the bookstore.", ex)

    def test_sell_book_if_title_not_in_dict(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Alex", 10)

        self.assertEqual("Book Alex doesn't exist!", str(ex.exception))

    def test_partial_sell_leftover_expected(self):
        self.bookstore.receive_book("Alex", 10)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Alex", 15)

        self.assertEqual("Alex has not enough copies to sell. Left: 10", str(ex.exception))

    def test_successful_sell_1_3(self):
        self.bookstore.receive_book("Alex", 10)
        self.assertEqual("Sold 5 copies of Alex", self.bookstore.sell_book("Alex", 5))

    def test_successful_sell2_3(self):
        self.bookstore.receive_book("Alex", 10)
        self.bookstore.sell_book("Alex", 5)

        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles["Alex"])

    def test_successful_sell_3_3(self):
        self.bookstore.receive_book("Alex", 10)
        self.bookstore.sell_book("Alex", 7)

        self.assertEqual(7, self.bookstore.total_sold_books)

    def test_str(self):
        self.bookstore.receive_book("Alex", 100)
        self.bookstore.sell_book("Alex", 50)

        ex = ("Total sold books: 50\n"
              "Current availability: 50\n"
              " - Alex: 50 copies")
        self.assertEqual(ex, self.bookstore.__str__())


if __name__ == "__main__":
    main()